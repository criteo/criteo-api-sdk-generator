# criteo_api_api_experimental.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_inheritance**](AnalyticsApi.md#post_inheritance) | **POST** /experimental/sample/testing/inheritance | /experimental/sample/testing/inheritance
[**post_polymorphic_list**](AnalyticsApi.md#post_polymorphic_list) | **POST** /experimental/sample/testing/polymorphic-list | /experimental/sample/testing/polymorphic-list
[**post_polymorphism**](AnalyticsApi.md#post_polymorphism) | **POST** /experimental/sample/testing/polymorphism | /experimental/sample/testing/polymorphism


# **post_inheritance**
> DerivedTypeOneResponse post_inheritance()

/experimental/sample/testing/inheritance

Echoes a concrete derived type (plain inheritance / allOf).

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_api_experimental
from criteo_api_api_experimental.api import analytics_api
from criteo_api_api_experimental.model.derived_type_one_request import DerivedTypeOneRequest
from criteo_api_api_experimental.model.derived_type_one_response import DerivedTypeOneResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_api_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    derived_type_one_request = DerivedTypeOneRequest(
        data=DerivedTypeOneResource(
            attributes=DerivedTypeOne(
                type_one_value="type_one_value_example",
            ),
            type="type_example",
        ),
    ) # DerivedTypeOneRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/sample/testing/inheritance
        api_response = api_instance.post_inheritance(derived_type_one_request=derived_type_one_request)
        pprint(api_response)
    except criteo_api_api_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->post_inheritance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **derived_type_one_request** | [**DerivedTypeOneRequest**](DerivedTypeOneRequest.md)|  | [optional]

### Return type

[**DerivedTypeOneResponse**](DerivedTypeOneResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_polymorphic_list**
> BaseTypeListResponse post_polymorphic_list()

/experimental/sample/testing/polymorphic-list

Echoes a list of the polymorphic types.

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_api_experimental
from criteo_api_api_experimental.api import analytics_api
from criteo_api_api_experimental.model.base_type_list_response import BaseTypeListResponse
from criteo_api_api_experimental.model.base_type_list_request import BaseTypeListRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_api_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    base_type_list_request = BaseTypeListRequest(
        data=[
            BaseTypeResource(
                attributes=BaseType(
                    common_data='YQ==',
                    type_discriminator="type_discriminator_example",
                ),
                type="type_example",
            ),
        ],
    ) # BaseTypeListRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/sample/testing/polymorphic-list
        api_response = api_instance.post_polymorphic_list(base_type_list_request=base_type_list_request)
        pprint(api_response)
    except criteo_api_api_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->post_polymorphic_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_type_list_request** | [**BaseTypeListRequest**](BaseTypeListRequest.md)|  | [optional]

### Return type

[**BaseTypeListResponse**](BaseTypeListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_polymorphism**
> BaseTypeResponse post_polymorphism()

/experimental/sample/testing/polymorphism

Echoes a polymorphic type (allOf + discriminator).

### Example

* OAuth Authentication (oauth):
* OAuth Authentication (oauth):

```python
import time
import criteo_api_api_experimental
from criteo_api_api_experimental.api import analytics_api
from criteo_api_api_experimental.model.base_type_response import BaseTypeResponse
from criteo_api_api_experimental.model.base_type_request import BaseTypeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.criteo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: oauth
configuration = criteo_api_api_experimental.Configuration(
    host = "https://api.criteo.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with criteo_api_api_experimental.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    base_type_request = BaseTypeRequest(
        data=BaseTypeResource(
            attributes=BaseType(
                common_data='YQ==',
                type_discriminator="type_discriminator_example",
            ),
            type="type_example",
        ),
    ) # BaseTypeRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # /experimental/sample/testing/polymorphism
        api_response = api_instance.post_polymorphism(base_type_request=base_type_request)
        pprint(api_response)
    except criteo_api_api_experimental.ApiException as e:
        print("Exception when calling AnalyticsApi->post_polymorphism: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_type_request** | [**BaseTypeRequest**](BaseTypeRequest.md)|  | [optional]

### Return type

[**BaseTypeResponse**](BaseTypeResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

