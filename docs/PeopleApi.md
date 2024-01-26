# openalex_api_pydantic_v1.PeopleApi

All URIs are relative to *https://api.openalex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_person**](PeopleApi.md#get_person) | **GET** /people/{id} | /people/{id}


# **get_person**
> PersonResponseSchema get_person(id, select=select, user_agent=user_agent, mailto=mailto)

/people/{id}



### Example

```python
import time
import os
import openalex_api_pydantic_v1
from openalex_api_pydantic_v1.models.person_response_schema import PersonResponseSchema
from openalex_api_pydantic_v1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openalex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = openalex_api_pydantic_v1.Configuration(
    host = "https://api.openalex.org"
)


# Enter a context with an instance of the API client
with openalex_api_pydantic_v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openalex_api_pydantic_v1.PeopleApi(api_client)
    id = None # object | 
    select = 'select_example' # str |  (optional)
    user_agent = None # object | [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) (optional)
    mailto = None # object | The API is the primary way to get OpenAlex data. It's free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like `mailto:example@domain.com`, or in the User-Agent request header, like `User-Agent: my-app (mailto:example@domain.com)`. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). (optional)

    try:
        # /people/{id}
        api_response = api_instance.get_person(id, select=select, user_agent=user_agent, mailto=mailto)
        print("The response of PeopleApi->get_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **select** | **str**|  | [optional] 
 **user_agent** | [**object**](.md)| [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool) | [optional] 
 **mailto** | [**object**](.md)| The API is the primary way to get OpenAlex data. It&#39;s free and requires no authentication. The daily limit for API calls is 100,000 requests per user per day. For best performance, add your email to all API requests The email can be either in the query string, like &#x60;mailto:example@domain.com&#x60;, or in the User-Agent request header, like &#x60;User-Agent: my-app (mailto:example@domain.com)&#x60;. Read more about the polite pool at [docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication](https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication#the-polite-pool). | [optional] 

### Return type

[**PersonResponseSchema**](PersonResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

