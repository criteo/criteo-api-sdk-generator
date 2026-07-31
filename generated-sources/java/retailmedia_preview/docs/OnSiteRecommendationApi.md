# OnSiteRecommendationApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chatbotProductRecommendations**](OnSiteRecommendationApi.md#chatbotProductRecommendations) | **POST** /preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations | /preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations |



## chatbotProductRecommendations

> MessageBodyModel chatbotProductRecommendations(catalogid, inbotDiscussionBodyModel)

/preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations

Ask a chatbot for a product recommendation

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.OnSiteRecommendationApi;

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
        String catalogid = "catalogid_example"; // String | the identifier of the catalog to query
        InbotDiscussionBodyModel inbotDiscussionBodyModel = new InbotDiscussionBodyModel(); // InbotDiscussionBodyModel | 
        try {
            MessageBodyModel result = apiInstance.chatbotProductRecommendations(catalogid, inbotDiscussionBodyModel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling OnSiteRecommendationApi#chatbotProductRecommendations");
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
| **catalogid** | **String**| the identifier of the catalog to query | |
| **inbotDiscussionBodyModel** | [**InbotDiscussionBodyModel**](InbotDiscussionBodyModel.md)|  | |

### Return type

[**MessageBodyModel**](MessageBodyModel.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

