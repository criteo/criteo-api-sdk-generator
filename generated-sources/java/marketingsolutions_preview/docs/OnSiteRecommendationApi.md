# OnSiteRecommendationApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchRecommendedProducts**](OnSiteRecommendationApi.md#searchRecommendedProducts) | **POST** /preview/recommendation/search | /preview/recommendation/search |
| [**searchRecommendedProductsConversational**](OnSiteRecommendationApi.md#searchRecommendedProductsConversational) | **POST** /preview/recommendation/search-conversational | /preview/recommendation/search-conversational |



## searchRecommendedProducts

> OnSiteRecoResponse searchRecommendedProducts(onSiteRecoRequest)

/preview/recommendation/search

Retrieves a list of products recommended for the given user. This end point can either rely on a Criteo UserId, or a list of user events to perform the recommendation

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.OnSiteRecommendationApi;

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

        OnSiteRecommendationApi apiInstance = new OnSiteRecommendationApi(defaultClient);
        OnSiteRecoRequest onSiteRecoRequest = new OnSiteRecoRequest(); // OnSiteRecoRequest | 
        try {
            OnSiteRecoResponse result = apiInstance.searchRecommendedProducts(onSiteRecoRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling OnSiteRecommendationApi#searchRecommendedProducts");
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
| **onSiteRecoRequest** | [**OnSiteRecoRequest**](OnSiteRecoRequest.md)|  | [optional] |

### Return type

[**OnSiteRecoResponse**](OnSiteRecoResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchRecommendedProductsConversational

> OnSiteRecoResponse searchRecommendedProductsConversational(onSiteRecoRequestConversational)

/preview/recommendation/search-conversational

Retrieves a list of products recommended for the given user based on a conversation between a user and a partner&#39;s agent

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.OnSiteRecommendationApi;

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

        OnSiteRecommendationApi apiInstance = new OnSiteRecommendationApi(defaultClient);
        OnSiteRecoRequestConversational onSiteRecoRequestConversational = new OnSiteRecoRequestConversational(); // OnSiteRecoRequestConversational | 
        try {
            OnSiteRecoResponse result = apiInstance.searchRecommendedProductsConversational(onSiteRecoRequestConversational);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling OnSiteRecommendationApi#searchRecommendedProductsConversational");
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
| **onSiteRecoRequestConversational** | [**OnSiteRecoRequestConversational**](OnSiteRecoRequestConversational.md)|  | [optional] |

### Return type

[**OnSiteRecoResponse**](OnSiteRecoResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

