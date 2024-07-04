# coding: utf-8

"""
    OpenAlex

    ![](https://raw.githubusercontent.com/ourresearch/openalex-docs/main/.gitbook/assets/OpenAlex-logo-5.png)  **OpenAlex** is a fully open catalog of the global research system.  It's named after the [ancient Library of Alexandria](https://en.wikipedia.org/wiki/Library_of_Alexandria) and made by the nonprofit [OurResearch](https://ourresearch.org/).  ## OpenAPI Specification  [Mearman/openalex-api-spec](https://github.com/Mearman/openalex-api-spec)  This OpenAPI specification is reverse-engineered and derived from spec generated by [openapi-devtools](https://github.com/AndrewWalsh/openapi-devtools).  The specification document itself is OpenAPI version 3.1 and is generated from TypeScript source code.  [![Open in](https://img.shields.io/badge/Open%20in-Swagger%20UI-85EA2D?style=for-the-badge&logo=Swagger&link=https://mearman.github.io/openalex-swagger-ui-react/)](https://mearman.github.io/openalex-swagger-ui-react/)  **[Releases](https://github.com/Mearman/openalex-api-spec/releases)**  ## Clients  [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript)](https://github.com/Mearman/openalex-typescript)  [![TypeScript Fetch](https://img.shields.io/badge/TypeScript%20Fetch-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white&link=https://github.com/Mearman/openalex-typescript-fetch)](https://github.com/Mearman/openalex-typescript-fetch)  [![TypeScript Node](https://img.shields.io/badge/TypeScript%20Node-339933?style=for-the-badge&logo=Node.js&logoColor=white&link=https://github.com/Mearman/openalex-typescript-node)](https://github.com/Mearman/openalex-typescript-node)  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&link=https://github.com/Mearman/openalex-python)](https://github.com/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-CodeSpaces-181717?style=for-the-badge&logo=GitHub&link=https://codespaces.new/Mearman/openalex-python)](https://codespaces.new/Mearman/openalex-python) [![Open in](https://img.shields.io/badge/Open%20in-Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&link=https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)](https://colab.research.google.com/github/Mearman/openalex-python/blob/main/README.ipynb)  ---

    The version of the OpenAPI document: 0.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr, constr, validator

from typing import Optional

from openalex_api.models.subfield import Subfield
from openalex_api.models.topic import Topic
from openalex_api.models.topics import Topics

from openalex_api.api_client import ApiClient
from openalex_api.api_response import ApiResponse
from openalex_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TopicsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_subfield_by_id(self, id : StrictStr, per_page : Optional[StrictInt] = None, user_agent : Annotated[Optional[constr(strict=True)], Field(description="[docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)")] = None, mailto : Annotated[Optional[constr(strict=True)], Field(description="The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).")] = None, **kwargs) -> Subfield:  # noqa: E501
        """/subfields/{id}  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_subfield_by_id(id, per_page, user_agent, mailto, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param per_page:
        :type per_page: int
        :param user_agent: [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)
        :type user_agent: str
        :param mailto: The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).
        :type mailto: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Subfield
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_subfield_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_subfield_by_id_with_http_info(id, per_page, user_agent, mailto, **kwargs)  # noqa: E501

    @validate_arguments
    def get_subfield_by_id_with_http_info(self, id : StrictStr, per_page : Optional[StrictInt] = None, user_agent : Annotated[Optional[constr(strict=True)], Field(description="[docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)")] = None, mailto : Annotated[Optional[constr(strict=True)], Field(description="The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/subfields/{id}  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_subfield_by_id_with_http_info(id, per_page, user_agent, mailto, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param per_page:
        :type per_page: int
        :param user_agent: [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)
        :type user_agent: str
        :param mailto: The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).
        :type mailto: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Subfield, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'per_page',
            'user_agent',
            'mailto'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subfield_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('per_page') is not None:  # noqa: E501
            _query_params.append(('per_page', _params['per_page']))

        if _params.get('mailto') is not None:  # noqa: E501
            _query_params.append(('mailto', _params['mailto']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['user_agent'] is not None:
            _header_params['User-Agent'] = _params['user_agent']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Subfield",
            '403': "ErrorMessage",
        }

        return self.api_client.call_api(
            '/subfields/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_topic_by_id(self, id : StrictStr, per_page : Optional[StrictInt] = None, user_agent : Annotated[Optional[constr(strict=True)], Field(description="[docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)")] = None, mailto : Annotated[Optional[constr(strict=True)], Field(description="The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).")] = None, **kwargs) -> Topic:  # noqa: E501
        """/topics/{id}  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_topic_by_id(id, per_page, user_agent, mailto, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param per_page:
        :type per_page: int
        :param user_agent: [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)
        :type user_agent: str
        :param mailto: The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).
        :type mailto: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Topic
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_topic_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_topic_by_id_with_http_info(id, per_page, user_agent, mailto, **kwargs)  # noqa: E501

    @validate_arguments
    def get_topic_by_id_with_http_info(self, id : StrictStr, per_page : Optional[StrictInt] = None, user_agent : Annotated[Optional[constr(strict=True)], Field(description="[docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)")] = None, mailto : Annotated[Optional[constr(strict=True)], Field(description="The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/topics/{id}  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_topic_by_id_with_http_info(id, per_page, user_agent, mailto, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param per_page:
        :type per_page: int
        :param user_agent: [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)
        :type user_agent: str
        :param mailto: The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).
        :type mailto: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Topic, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'per_page',
            'user_agent',
            'mailto'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topic_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('per_page') is not None:  # noqa: E501
            _query_params.append(('per_page', _params['per_page']))

        if _params.get('mailto') is not None:  # noqa: E501
            _query_params.append(('mailto', _params['mailto']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['user_agent'] is not None:
            _header_params['User-Agent'] = _params['user_agent']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Topic",
            '403': "ErrorMessage",
        }

        return self.api_client.call_api(
            '/topics/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_topics(self, sort : Optional[StrictStr] = None, per_page : Optional[StrictInt] = None, page : Optional[StrictStr] = None, sample : Optional[StrictStr] = None, select : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, search : Optional[StrictStr] = None, group_by : Optional[StrictStr] = None, user_agent : Annotated[Optional[constr(strict=True)], Field(description="[docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)")] = None, mailto : Annotated[Optional[constr(strict=True)], Field(description="The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).")] = None, **kwargs) -> Topics:  # noqa: E501
        """/topics  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_topics(sort, per_page, page, sample, select, filter, search, group_by, user_agent, mailto, async_req=True)
        >>> result = thread.get()

        :param sort:
        :type sort: str
        :param per_page:
        :type per_page: int
        :param page:
        :type page: str
        :param sample:
        :type sample: str
        :param select:
        :type select: str
        :param filter:
        :type filter: str
        :param search:
        :type search: str
        :param group_by:
        :type group_by: str
        :param user_agent: [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)
        :type user_agent: str
        :param mailto: The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).
        :type mailto: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Topics
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_topics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_topics_with_http_info(sort, per_page, page, sample, select, filter, search, group_by, user_agent, mailto, **kwargs)  # noqa: E501

    @validate_arguments
    def get_topics_with_http_info(self, sort : Optional[StrictStr] = None, per_page : Optional[StrictInt] = None, page : Optional[StrictStr] = None, sample : Optional[StrictStr] = None, select : Optional[StrictStr] = None, filter : Optional[StrictStr] = None, search : Optional[StrictStr] = None, group_by : Optional[StrictStr] = None, user_agent : Annotated[Optional[constr(strict=True)], Field(description="[docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)")] = None, mailto : Annotated[Optional[constr(strict=True)], Field(description="The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """/topics  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_topics_with_http_info(sort, per_page, page, sample, select, filter, search, group_by, user_agent, mailto, async_req=True)
        >>> result = thread.get()

        :param sort:
        :type sort: str
        :param per_page:
        :type per_page: int
        :param page:
        :type page: str
        :param sample:
        :type sample: str
        :param select:
        :type select: str
        :param filter:
        :type filter: str
        :param search:
        :type search: str
        :param group_by:
        :type group_by: str
        :param user_agent: [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool)
        :type user_agent: str
        :param mailto: The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool).
        :type mailto: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Topics, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'sort',
            'per_page',
            'page',
            'sample',
            'select',
            'filter',
            'search',
            'group_by',
            'user_agent',
            'mailto'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        if _params.get('per_page') is not None:  # noqa: E501
            _query_params.append(('per_page', _params['per_page']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('sample') is not None:  # noqa: E501
            _query_params.append(('sample', _params['sample']))

        if _params.get('select') is not None:  # noqa: E501
            _query_params.append(('select', _params['select']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('group_by') is not None:  # noqa: E501
            _query_params.append(('group_by', _params['group_by']))

        if _params.get('mailto') is not None:  # noqa: E501
            _query_params.append(('mailto', _params['mailto']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['user_agent'] is not None:
            _header_params['User-Agent'] = _params['user_agent']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "Topics",
            '403': "ErrorMessage",
        }

        return self.api_client.call_api(
            '/topics', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
