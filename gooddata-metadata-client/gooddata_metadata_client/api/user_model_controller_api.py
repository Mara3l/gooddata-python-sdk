"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_metadata_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_metadata_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_metadata_client.model.json_api_api_token_in_document import JsonApiApiTokenInDocument
from gooddata_metadata_client.model.json_api_api_token_out_document import JsonApiApiTokenOutDocument
from gooddata_metadata_client.model.json_api_api_token_out_list import JsonApiApiTokenOutList


class UserModelControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_entity_api_tokens(
            self,
            user_id,
            json_api_api_token_in_document,
            **kwargs
        ):
            """create_entity_api_tokens  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_entity_api_tokens(user_id, json_api_api_token_in_document, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                json_api_api_token_in_document (JsonApiApiTokenInDocument):

            Keyword Args:
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
                JsonApiApiTokenOutDocument
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
            kwargs['user_id'] = \
                user_id
            kwargs['json_api_api_token_in_document'] = \
                json_api_api_token_in_document
            return self.call_with_http_info(**kwargs)

        self.create_entity_api_tokens = _Endpoint(
            settings={
                'response_type': (JsonApiApiTokenOutDocument,),
                'auth': [],
                'endpoint_path': '/api/entities/users/{userId}/apiTokens',
                'operation_id': 'create_entity_api_tokens',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'json_api_api_token_in_document',
                ],
                'required': [
                    'user_id',
                    'json_api_api_token_in_document',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'json_api_api_token_in_document':
                        (JsonApiApiTokenInDocument,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                },
                'location_map': {
                    'user_id': 'path',
                    'json_api_api_token_in_document': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [
                    'application/vnd.gooddata.api+json'
                ]
            },
            api_client=api_client,
            callable=__create_entity_api_tokens
        )

        def __delete_entity_api_tokens(
            self,
            user_id,
            id,
            **kwargs
        ):
            """delete_entity_api_tokens  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_entity_api_tokens(user_id, id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                id (str):

            Keyword Args:
                predicate ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Composed query parameters used for filtering. 'id' parameter can be used for all objects. Other parameters are present according to object type (title, description,...). You can specify any object parameter and parameter of related entity up to 2nd level (for example name=John&language=english,czech&address.city=London&father.id=123).. [optional]
                filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser.You can specify any object parameter and parameter of related entity up to 2nd level (for example title=='Some Title';description=='desc'). [optional]
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
                None
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
            kwargs['user_id'] = \
                user_id
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.delete_entity_api_tokens = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/api/entities/users/{userId}/apiTokens/{id}',
                'operation_id': 'delete_entity_api_tokens',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'id',
                    'predicate',
                    'filter',
                ],
                'required': [
                    'user_id',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'id':
                        (str,),
                    'predicate':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                    'filter':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'id': 'id',
                    'predicate': 'predicate',
                    'filter': 'filter',
                },
                'location_map': {
                    'user_id': 'path',
                    'id': 'path',
                    'predicate': 'query',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_entity_api_tokens
        )

        def __get_all_entities_api_tokens(
            self,
            user_id,
            **kwargs
        ):
            """get_all_entities_api_tokens  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_all_entities_api_tokens(user_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):

            Keyword Args:
                predicate ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Composed query parameters used for filtering. 'id' parameter can be used for all objects. Other parameters are present according to object type (title, description,...). You can specify any object parameter and parameter of related entity up to 2nd level (for example name=John&language=english,czech&address.city=London&father.id=123).. [optional]
                filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser.You can specify any object parameter and parameter of related entity up to 2nd level (for example title=='Some Title';description=='desc'). [optional]
                page (int): Zero-based page index (0..N). [optional] if omitted the server will use the default value of 0
                size (int): The size of the page to be returned. [optional] if omitted the server will use the default value of 20
                sort ([str]): Sorting criteria in the format: property(,asc|desc). Default sort order is ascending. Multiple sort criteria are supported.. [optional]
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
                JsonApiApiTokenOutList
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
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.get_all_entities_api_tokens = _Endpoint(
            settings={
                'response_type': (JsonApiApiTokenOutList,),
                'auth': [],
                'endpoint_path': '/api/entities/users/{userId}/apiTokens',
                'operation_id': 'get_all_entities_api_tokens',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'predicate',
                    'filter',
                    'page',
                    'size',
                    'sort',
                ],
                'required': [
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'predicate':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                    'filter':
                        (str,),
                    'page':
                        (int,),
                    'size':
                        (int,),
                    'sort':
                        ([str],),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'predicate': 'predicate',
                    'filter': 'filter',
                    'page': 'page',
                    'size': 'size',
                    'sort': 'sort',
                },
                'location_map': {
                    'user_id': 'path',
                    'predicate': 'query',
                    'filter': 'query',
                    'page': 'query',
                    'size': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                    'sort': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_all_entities_api_tokens
        )

        def __get_entity_api_tokens(
            self,
            user_id,
            id,
            **kwargs
        ):
            """get_entity_api_tokens  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_entity_api_tokens(user_id, id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str):
                id (str):

            Keyword Args:
                predicate ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Composed query parameters used for filtering. 'id' parameter can be used for all objects. Other parameters are present according to object type (title, description,...). You can specify any object parameter and parameter of related entity up to 2nd level (for example name=John&language=english,czech&address.city=London&father.id=123).. [optional]
                filter (str): Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser.You can specify any object parameter and parameter of related entity up to 2nd level (for example title=='Some Title';description=='desc'). [optional]
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
                JsonApiApiTokenOutDocument
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
            kwargs['user_id'] = \
                user_id
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_entity_api_tokens = _Endpoint(
            settings={
                'response_type': (JsonApiApiTokenOutDocument,),
                'auth': [],
                'endpoint_path': '/api/entities/users/{userId}/apiTokens/{id}',
                'operation_id': 'get_entity_api_tokens',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'id',
                    'predicate',
                    'filter',
                ],
                'required': [
                    'user_id',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'id',
                ]
            },
            root_map={
                'validations': {
                    ('id',): {

                        'regex': {
                            'pattern': r'^[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'id':
                        (str,),
                    'predicate':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                    'filter':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'id': 'id',
                    'predicate': 'predicate',
                    'filter': 'filter',
                },
                'location_map': {
                    'user_id': 'path',
                    'id': 'path',
                    'predicate': 'query',
                    'filter': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.gooddata.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_entity_api_tokens
        )
