# AnalyticsApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postInheritance**](AnalyticsApi.md#postInheritance) | **POST** /experimental/sample/testing/inheritance | /experimental/sample/testing/inheritance |
| [**postPolymorphicList**](AnalyticsApi.md#postPolymorphicList) | **POST** /experimental/sample/testing/polymorphic-list | /experimental/sample/testing/polymorphic-list |
| [**postPolymorphism**](AnalyticsApi.md#postPolymorphism) | **POST** /experimental/sample/testing/polymorphism | /experimental/sample/testing/polymorphism |



## postInheritance

> DerivedTypeOneResponse postInheritance(derivedTypeOneRequest)

/experimental/sample/testing/inheritance

Echoes a concrete derived type (plain inheritance / allOf).

### Example

```java
package com.criteo.api.api.experimental;

import com.criteo.api.api.experimental.ApiClient;
import com.criteo.api.api.experimental.ApiClientBuilder;
import com.criteo.api.api.experimental.ApiException;
import com.criteo.api.api.experimental.Configuration;
import com.criteo.api.api.experimental.auth.*;
import com.criteo.api.api.experimental.model.*;
import com.criteo.api.api.experimental.api.AnalyticsApi;

public class Example {
    public static void main(String[] args) {

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
        DerivedTypeOneRequest derivedTypeOneRequest = new DerivedTypeOneRequest(); // DerivedTypeOneRequest | 
        try {
            DerivedTypeOneResponse result = apiInstance.postInheritance(derivedTypeOneRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#postInheritance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **derivedTypeOneRequest** | [**DerivedTypeOneRequest**](DerivedTypeOneRequest.md)|  | [optional] |

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
| **200** | Success |  -  |


## postPolymorphicList

> BaseTypeListResponse postPolymorphicList(baseTypeListRequest)

/experimental/sample/testing/polymorphic-list

Echoes a list of the polymorphic types.

### Example

```java
package com.criteo.api.api.experimental;

import com.criteo.api.api.experimental.ApiClient;
import com.criteo.api.api.experimental.ApiClientBuilder;
import com.criteo.api.api.experimental.ApiException;
import com.criteo.api.api.experimental.Configuration;
import com.criteo.api.api.experimental.auth.*;
import com.criteo.api.api.experimental.model.*;
import com.criteo.api.api.experimental.api.AnalyticsApi;

public class Example {
    public static void main(String[] args) {

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
        BaseTypeListRequest baseTypeListRequest = new BaseTypeListRequest(); // BaseTypeListRequest | 
        try {
            BaseTypeListResponse result = apiInstance.postPolymorphicList(baseTypeListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#postPolymorphicList");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **baseTypeListRequest** | [**BaseTypeListRequest**](BaseTypeListRequest.md)|  | [optional] |

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
| **200** | Success |  -  |


## postPolymorphism

> BaseTypeResponse postPolymorphism(baseTypeRequest)

/experimental/sample/testing/polymorphism

Echoes a polymorphic type (allOf + discriminator).

### Example

```java
package com.criteo.api.api.experimental;

import com.criteo.api.api.experimental.ApiClient;
import com.criteo.api.api.experimental.ApiClientBuilder;
import com.criteo.api.api.experimental.ApiException;
import com.criteo.api.api.experimental.Configuration;
import com.criteo.api.api.experimental.auth.*;
import com.criteo.api.api.experimental.model.*;
import com.criteo.api.api.experimental.api.AnalyticsApi;

public class Example {
    public static void main(String[] args) {

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
        BaseTypeRequest baseTypeRequest = new BaseTypeRequest(); // BaseTypeRequest | 
        try {
            BaseTypeResponse result = apiInstance.postPolymorphism(baseTypeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#postPolymorphism");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **baseTypeRequest** | [**BaseTypeRequest**](BaseTypeRequest.md)|  | [optional] |

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
| **200** | Success |  -  |

