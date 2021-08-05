"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_afm_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_afm_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_afm_client.model.afm_execution import AfmExecution


class AfmExplainControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __explain_afm(
            self,
            workspace_id,
            afm_execution,
            **kwargs
        ):
            """AFM explain resource.  # noqa: E501

            The resource provides static structures needed for investigation of a problem with given AFM. The structures are MAQL (internal form of AFM), and logical and physical models (LDM and PDM) of corresponding workspace.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.explain_afm(workspace_id, afm_execution, async_req=True)
            >>> result = thread.get()

            Args:
                workspace_id (str): Workspace identifier
                afm_execution (AfmExecution):

            Keyword Args:
                explain_type (str): Requested explain type (LDM, PDM or MAQL). If not specified all types are bundled in a ZIP archive.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                file_type
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workspace_id'] = \
                workspace_id
            kwargs['afm_execution'] = \
                afm_execution
            return self.call_with_http_info(**kwargs)

        self.explain_afm = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/afm/explain',
                'operation_id': 'explain_afm',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'afm_execution',
                    'explain_type',
                ],
                'required': [
                    'workspace_id',
                    'afm_execution',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'workspace_id',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'afm_execution':
                        (AfmExecution,),
                    'explain_type':
                        (str,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'explain_type': 'explainType',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'afm_execution': 'body',
                    'explain_type': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/zip'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__explain_afm
        )
