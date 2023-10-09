# (C) 2023 GoodData Corporation
import logging
import os
import sys
from argparse import Namespace
from pathlib import Path
from time import time
from typing import List, Optional

import tabulate
import yaml
from gooddata_dbt.args import parse_arguments
from gooddata_dbt.dbt.cloud import DbtConnection, DbtCredentials, DbtExecution
from gooddata_dbt.dbt.profiles import DbtOutput, DbtProfiles
from gooddata_dbt.dbt.tables import DbtModelTables
from gooddata_dbt.gooddata.config import GoodDataConfig, GoodDataConfigProduct
from gooddata_dbt.logger import get_logger
from gooddata_dbt.sdk_wrapper import GoodDataSdkWrapper
from gooddata_dbt.utils import report_message_to_merge_request

from gooddata_sdk import (
    CatalogDeclarativeModel,
    CatalogDeclarativeTables,
    CatalogScanModelRequest,
    CatalogWorkspace,
    GoodDataSdk,
)

GOODDATA_LAYOUTS_DIR = Path("gooddata_layouts")

# TODO
#   Tests, ...


def layout_model_path(data_product: GoodDataConfigProduct) -> Path:
    return GOODDATA_LAYOUTS_DIR / data_product.id


def generate_and_put_pdm(
    logger: logging.Logger, sdk: GoodDataSdk, data_source_id: str, dbt_tables: DbtModelTables
) -> None:
    # Construct GoodData PDM from dbt models and put it to the server
    # GoodData caches the metadata to reduce querying them (costly) in runtime.
    scan_request = CatalogScanModelRequest(scan_tables=True, scan_views=True)
    logger.info(f"Scan data source {data_source_id=}")
    scan_pdm = sdk.catalog_data_source.scan_data_source(data_source_id, scan_request, report_warnings=True).pdm

    logger.info(f"Generate and put PDM {data_source_id=}")
    pdm = dbt_tables.make_pdm(scan_pdm)
    declarative_tables = CatalogDeclarativeTables.from_dict(pdm, camel_case=False)
    sdk.catalog_data_source.put_declarative_pdm(data_source_id, declarative_tables)


def generate_and_put_ldm(
    sdk: GoodDataSdk, data_source_id: str, workspace_id: str, dbt_tables: DbtModelTables, model_ids: Optional[List[str]]
) -> None:
    # Construct GoodData LDM from dbt models
    declarative_datasets = dbt_tables.make_declarative_datasets(data_source_id, model_ids)
    ldm = CatalogDeclarativeModel.from_dict({"ldm": declarative_datasets}, camel_case=False)

    # Deploy logical into target workspace
    sdk.catalog_workspace_content.put_declarative_ldm(workspace_id, ldm)


def register_data_source(
    logger: logging.Logger, sdk: GoodDataSdk, data_source_id: str, dbt_target: DbtOutput, dbt_tables: DbtModelTables
) -> None:
    logger.info(f"Register data source {data_source_id=} schema={dbt_tables.schema_name}")
    data_source = dbt_target.to_gooddata(data_source_id, dbt_tables.schema_name)
    sdk.catalog_data_source.create_or_update_data_source(data_source)

    logger.info("Generate and put PDM")
    generate_and_put_pdm(logger, sdk, data_source_id, dbt_tables)


def create_workspace(logger: logging.Logger, sdk: GoodDataSdk, workspace_id: str, workspace_title: str) -> None:
    logger.info(f"Create workspace {workspace_id=} {workspace_title=}")
    # Create workspaces, if they do not exist yet, otherwise update them
    workspace = CatalogWorkspace(workspace_id=workspace_id, name=workspace_title)
    sdk.catalog_workspace.create_or_update(workspace=workspace)


def deploy_ldm(
    logger: logging.Logger,
    sdk: GoodDataSdk,
    args: Namespace,
    data_source_id: str,
    dbt_tables: DbtModelTables,
    model_ids: Optional[List[str]],
    workspace_id: str,
) -> None:
    logger.info("Generate and put LDM")
    generate_and_put_ldm(sdk, data_source_id, workspace_id, dbt_tables, model_ids)
    workspace_url = f"{args.gooddata_host}/modeler/#/{workspace_id}"
    logger.info(f"LDM successfully loaded, verify here: {workspace_url}")


def upload_notification(logger: logging.Logger, sdk: GoodDataSdk, data_source_id: str) -> None:
    logger.info(f"Upload notification {data_source_id=}")
    sdk.catalog_data_source.register_upload_notification(data_source_id)


def deploy_analytics(
    logger: logging.Logger, sdk: GoodDataSdk, args: Namespace, workspace_id: str, data_product: GoodDataConfigProduct
) -> None:
    logger.info(f"Deploy analytics {workspace_id=}")

    logger.info("Read analytics model from disk")
    adm = sdk.catalog_workspace_content.load_analytics_model_from_disk(layout_model_path(data_product))

    # Deploy analytics model into target workspace
    logger.info("Load analytics model into GoodData")
    sdk.catalog_workspace_content.put_declarative_analytics_model(workspace_id, adm)

    workspace_url = f"{args.gooddata_host}/dashboards/#/workspace/{workspace_id}"
    logger.info(f"Analytics successfully loaded, verify here: {workspace_url}")


def store_analytics(
    logger: logging.Logger, sdk: GoodDataSdk, workspace_id: str, data_product: GoodDataConfigProduct
) -> None:
    logger.info("Store analytics model to disk")
    sdk.catalog_workspace_content.store_analytics_model_to_disk(
        workspace_id,
        layout_model_path(data_product),
        # Exclude attributes related to activities of users, e.g. createdBy
        # When delivering programmatically,
        #   we don't want to transfer info about users and their activities into another environments
        exclude=["ACTIVITY_INFO"],
    )


def test_insights(logger: logging.Logger, sdk: GoodDataSdk, workspace_id: str) -> None:
    logger.info(f"Test insights {workspace_id=}")
    insights = sdk.insights.get_insights(workspace_id)

    for insight in insights:
        try:
            start = time()
            sdk.tables.for_insight(workspace_id, insight)
            duration = int((time() - start) * 1000)
            logger.info(f'Test successful insight="{insight.title}" duration={duration}(ms) ...')
        except RuntimeError:
            sys.exit()


def create_localized_workspaces(data_product: GoodDataConfigProduct, sdk: GoodDataSdk, workspace_id: str) -> None:
    if data_product.localization is None:
        return
    for to in data_product.localization.to:
        from deep_translator import GoogleTranslator

        translator_func = GoogleTranslator(
            source=data_product.localization.from_language, target=to.language
        ).translate_batch
        logging.info(f"create_localized_workspaces layout_root_path={GOODDATA_LAYOUTS_DIR / data_product.id}")
        sdk.catalog_workspace.generate_localized_workspaces(
            workspace_id,
            to_lang=to.language,
            to_locale=to.locale,
            from_lang=data_product.localization.from_language,
            translator_func=translator_func,
            provision_workspace=True,
            store_layouts=False,
            layout_root_path=GOODDATA_LAYOUTS_DIR / data_product.id,
        )


def deploy_models(
    gooddata_upper_case: bool,
    gooddata_environment_id: str,
    logger: logging.Logger,
    dbt_target: DbtOutput,
    gd_config: GoodDataConfig,
    sdk: GoodDataSdk,
    args: Namespace,
    data_source_id: str,
) -> None:
    dbt_tables = DbtModelTables.from_local(gooddata_upper_case, gd_config.all_model_ids)
    if gooddata_upper_case:
        dbt_target.schema = dbt_target.schema.upper()
        dbt_target.database = dbt_target.database.upper()
    register_data_source(logger, sdk, data_source_id, dbt_target, dbt_tables)
    for data_product in gd_config.data_products:
        logger.info(f"Process product name={data_product.name}")
        environments = gd_config.get_environment_workspaces(data_product.environment_setup_id)
        for environment in environments:
            if environment.id == gooddata_environment_id:
                workspace_id = f"{data_product.id}_{environment.id}"
                workspace_title = f"{data_product.name} ({environment.name})"
                create_workspace(logger, sdk, workspace_id, workspace_title)
                deploy_ldm(logger, sdk, args, data_source_id, dbt_tables, data_product.model_ids, workspace_id)
                if data_product.localization:
                    create_localized_workspaces(data_product, sdk, workspace_id)


def get_table(data: List[list], headers: List[str], fmt: str) -> str:
    return tabulate.tabulate(data, headers=headers, tablefmt=fmt)


def dbt_cloud_stats_degradations(
    args: Namespace,
    logger: logging.Logger,
    environment_id: str,
    model_executions: List[DbtExecution],
    dbt_conn: DbtConnection,
) -> None:
    logger.info("Get stats for historical executions...")
    models_history_avg_execution_times = dbt_conn.get_average_times(logger, model_executions, environment_id, 5)
    differences = []
    degradations = 0
    for execution in model_executions:
        for model_id, avg_time in models_history_avg_execution_times.items():
            last_execution = execution.execution_info.execution_time
            difference = float(last_execution - avg_time) / avg_time * 100
            degradation = difference > args.allowed_degradation
            if model_id == execution.unique_id:
                differences.append(
                    [
                        model_id,
                        round(last_execution, 2),
                        round(avg_time, 2),
                        round(difference, 2),
                        str(degradation),
                    ]
                )
                if degradation:
                    degradations += 1
    headers = ["Model ID", "Last duration(s)", "Average duration(s)", "Difference(%)", "Degradation"]
    pretty_table = get_table(differences, headers, "outline")
    if degradations > 0:
        logger.warning(
            "Stats for historical executions contain degradations! "
            + f"Threshold={args.allowed_degradation}%\n{pretty_table}"
        )
    else:
        logger.info(f"Stats for historical executions:\n{pretty_table}")

    gitlab_token = os.getenv("GITLAB_TOKEN")
    if os.getenv("CI_MERGE_REQUEST_IID") and gitlab_token:
        # Running in Gitlab CI pipeline, report performance of executions to the merge request to notify code reviewer
        git_table = get_table(differences, headers, "github")
        logger.info("Sending report to related Gitlab merge request as comment")
        if degradations > 0:
            message = (
                "WARNING: some executions of dbt models in this merge request are slower than average!"
                + f"Threshold={args.allowed_degradation}%\n\n{git_table}"
            )
            report_message_to_merge_request(gitlab_token, message)
        else:
            message = f"INFO: performance of all executions of dbt models is OK!\n\n{git_table}"
            report_message_to_merge_request(gitlab_token, message)


def dbt_cloud_stats(
    args: Namespace,
    logger: logging.Logger,
    all_model_ids: List[str],
    environment_id: str,
) -> None:
    logger.info("Get stats for last execution...")
    dbt_conn = DbtConnection(credentials=DbtCredentials(account_id=args.account_id, token=args.token))
    dbt_tables = DbtModelTables.from_local(args.gooddata_upper_case, all_model_ids)
    model_executions = dbt_conn.get_last_execution(environment_id, len(dbt_tables.tables))
    exec_list = []
    for execution in model_executions:
        exec_list.append([execution.unique_id, round(execution.execution_info.execution_time, 2)])

    headers = ["Model ID", "Duration(s)"]
    pretty_table = get_table(exec_list, headers, "outline")
    logger.info(f"Stats for last execution:\n{pretty_table}")

    dbt_cloud_stats_degradations(args, logger, environment_id, model_executions, dbt_conn)


def dbt_cloud_run(args: Namespace, logger: logging.Logger, all_model_ids: List[str]) -> None:
    dbt_conn = DbtConnection(credentials=DbtCredentials(account_id=args.account_id, token=args.token))
    logger.info("#" * 80)
    logger.info(f"Starting job in dbt cloud with job_id={args.job_id}")
    logger.info("#" * 80)

    run_id, run_href = dbt_conn.run_job(logger, args.job_id)
    logger.info(f"Job with {run_id=} successfully initiated. Link to job run {run_href=}")

    dbt_conn.fetch_run_result(run_id)
    dbt_conn.download_manifest(run_id)
    logger.info("Manifest downloaded successfully")

    environment_id = dbt_conn.get_environment_id(args.job_id)
    logger.info(f"Found environment with {environment_id=} for job_id={args.job_id}")

    environment = dbt_conn.read_environment(environment_id, args.project_id, args.job_id)
    dbt_conn.make_profiles(environment, path_to_profiles=Path(args.profiles_dir))
    logger.info(f"Profile file stored to {args.profiles_dir}")

    dbt_cloud_stats(args, logger, all_model_ids, environment_id)


def main() -> None:
    args = parse_arguments("gooddata-dbt plugin for models management and invalidating caches(upload notification)")
    logger = get_logger("gooddata-dbt", args.debug)
    logger.info("Start")
    sdk = GoodDataSdkWrapper(args, logger).sdk
    with open(args.gooddata_config) as fp:
        gd_config = GoodDataConfig.from_dict(yaml.safe_load(fp))

    if args.method == "dbt_cloud_run":
        dbt_cloud_run(args, logger, gd_config.all_model_ids)
    elif args.method == "dbt_cloud_stats":
        dbt_cloud_stats(args, logger, gd_config.all_model_ids, args.environment_id)
    elif args.method in ["upload_notification", "deploy_models"]:
        dbt_target = DbtProfiles(args).target
        data_source_id = f"{args.profile}-{dbt_target.name}"
        if args.method == "upload_notification":
            # Caches are invalidated only per data source, not per data product
            upload_notification(logger, sdk, data_source_id)
        else:
            deploy_models(
                args.gooddata_upper_case,
                args.gooddata_environment_id,
                logger,
                dbt_target,
                gd_config,
                sdk,
                args,
                data_source_id,
            )
    else:
        for data_product in gd_config.data_products:
            logger.info(f"Process product name={data_product.name}")
            environments = gd_config.get_environment_workspaces(data_product.environment_setup_id)
            for environment in environments:
                if environment.id == args.gooddata_environment_id:
                    workspace_id = f"{data_product.id}_{environment.id}"
                    if args.method == "store_analytics":
                        store_analytics(logger, sdk, workspace_id, data_product)
                    elif args.method == "deploy_analytics":
                        deploy_analytics(logger, sdk, args, workspace_id, data_product)
                    elif args.method == "test_insights":
                        test_insights(logger, sdk, workspace_id)
                    else:
                        raise Exception(f"Unsupported method requested in args: {args.method}")

    logger.info("End")
