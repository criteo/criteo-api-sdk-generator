# CatalogApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteStoreInventoryPerMerchantId**](CatalogApi.md#deleteStoreInventoryPerMerchantId) | **POST** /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/delete | /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/delete |
| [**upsertStoreInventoryPerMerchantId**](CatalogApi.md#upsertStoreInventoryPerMerchantId) | **POST** /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert | /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert |



## deleteStoreInventoryPerMerchantId

> deleteStoreInventoryPerMerchantId(merchantId, batchStoreInventoryDeleteRequest)

/2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/delete

Used to publish a batch of store inventories to delete. The batch is processed asynchronously.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.CatalogApi;

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

        CatalogApi apiInstance = new CatalogApi(defaultClient);
        String merchantId = "merchantId_example"; // String | Identifies the merchant, can also be called partnerId
        BatchStoreInventoryDeleteRequest batchStoreInventoryDeleteRequest = new BatchStoreInventoryDeleteRequest(); // BatchStoreInventoryDeleteRequest | 
        try {
            apiInstance.deleteStoreInventoryPerMerchantId(merchantId, batchStoreInventoryDeleteRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling CatalogApi#deleteStoreInventoryPerMerchantId");
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
| **merchantId** | **String**| Identifies the merchant, can also be called partnerId | |
| **batchStoreInventoryDeleteRequest** | [**BatchStoreInventoryDeleteRequest**](BatchStoreInventoryDeleteRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Batch accepted. |  -  |


## upsertStoreInventoryPerMerchantId

> upsertStoreInventoryPerMerchantId(merchantId, batchStoreInventoryRequest)

/2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert

Used to publish a batch of store inventories to upsert. The batch is processed asynchronously.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.CatalogApi;

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

        CatalogApi apiInstance = new CatalogApi(defaultClient);
        String merchantId = "merchantId_example"; // String | Identifies the merchant, can also be called partnerId
        BatchStoreInventoryRequest batchStoreInventoryRequest = new BatchStoreInventoryRequest(); // BatchStoreInventoryRequest | 
        try {
            apiInstance.upsertStoreInventoryPerMerchantId(merchantId, batchStoreInventoryRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling CatalogApi#upsertStoreInventoryPerMerchantId");
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
| **merchantId** | **String**| Identifies the merchant, can also be called partnerId | |
| **batchStoreInventoryRequest** | [**BatchStoreInventoryRequest**](BatchStoreInventoryRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Batch accepted. |  -  |

