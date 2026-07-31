# AccountsApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPrivateMarketChildAccountsByAccountId**](AccountsApi.md#getPrivateMarketChildAccountsByAccountId) | **GET** /experimental/retail-media/account-management/accounts/{accountId}/private-market-child-accounts | /experimental/retail-media/account-management/accounts/{accountId}/private-market-child-accounts |
| [**searchBrands**](AccountsApi.md#searchBrands) | **POST** /experimental/retail-media/brands/search | /experimental/retail-media/brands/search |



## getPrivateMarketChildAccountsByAccountId

> EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata getPrivateMarketChildAccountsByAccountId(accountId, limit, offset)

/experimental/retail-media/account-management/accounts/{accountId}/private-market-child-accounts

Gets Private Market child accounts that are associated with the given account

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AccountsApi;

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

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account Id
        Integer limit = 25; // Integer | The number of accounts to be returned. The default is 25.
        Integer offset = 0; // Integer | The (zero-based) offset into the collection of accounts. The default is 0.
        try {
            EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata result = apiInstance.getPrivateMarketChildAccountsByAccountId(accountId, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#getPrivateMarketChildAccountsByAccountId");
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
| **accountId** | **String**| Account Id | |
| **limit** | **Integer**| The number of accounts to be returned. The default is 25. | [optional] [default to 25] |
| **offset** | **Integer**| The (zero-based) offset into the collection of accounts. The default is 0. | [optional] [default to 0] |

### Return type

[**EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata**](EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchBrands

> EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata searchBrands(limit, offset, valueResourceInputBrandIdSearchRequest)

/experimental/retail-media/brands/search

Search for brands given a retailer ID and search term.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AccountsApi;

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

        AccountsApi apiInstance = new AccountsApi(defaultClient);
        Integer limit = 25; // Integer | the number of brands to return
        Integer offset = 0; // Integer | offset of paginated results
        ValueResourceInputBrandIdSearchRequest valueResourceInputBrandIdSearchRequest = new ValueResourceInputBrandIdSearchRequest(); // ValueResourceInputBrandIdSearchRequest | BrandIdSearchRequest which contains the request parameters
        try {
            EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata result = apiInstance.searchBrands(limit, offset, valueResourceInputBrandIdSearchRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AccountsApi#searchBrands");
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
| **limit** | **Integer**| the number of brands to return | [optional] [default to 25] |
| **offset** | **Integer**| offset of paginated results | [optional] [default to 0] |
| **valueResourceInputBrandIdSearchRequest** | [**ValueResourceInputBrandIdSearchRequest**](ValueResourceInputBrandIdSearchRequest.md)| BrandIdSearchRequest which contains the request parameters | [optional] |

### Return type

[**EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata**](EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

