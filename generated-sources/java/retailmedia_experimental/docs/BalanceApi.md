# BalanceApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBalanceHistoryV1**](BalanceApi.md#getBalanceHistoryV1) | **GET** /experimental/retail-media/balances/{balanceId}/history | /experimental/retail-media/balances/{balanceId}/history |
| [**getBalanceV1**](BalanceApi.md#getBalanceV1) | **GET** /experimental/retail-media/balances/{balanceId} | /experimental/retail-media/balances/{balanceId} |
| [**getPageOfBalancesV1**](BalanceApi.md#getPageOfBalancesV1) | **GET** /experimental/retail-media/accounts/{accountId}/balances | /experimental/retail-media/accounts/{accountId}/balances |
| [**updateBalanceV1**](BalanceApi.md#updateBalanceV1) | **PATCH** /experimental/retail-media/accounts/{account-id}/balances/{balance-id} | /experimental/retail-media/accounts/{account-id}/balances/{balance-id} |



## getBalanceHistoryV1

> ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata getBalanceHistoryV1(balanceId, limit, limitToChangeTypes, offset)

/experimental/retail-media/balances/{balanceId}/history

Gets the balance&#39;s historical change data.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.BalanceApi;

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

        BalanceApi apiInstance = new BalanceApi(defaultClient);
        String balanceId = "balanceId_example"; // String | Balance id.
        Integer limit = 25; // Integer | The number of elements to be returned.
        String limitToChangeTypes = "limitToChangeTypes_example"; // String | Comma separated change types string that will be queried.
        Integer offset = 0; // Integer | The (zero-based) starting offset in the collection.
        try {
            ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata result = apiInstance.getBalanceHistoryV1(balanceId, limit, limitToChangeTypes, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getBalanceHistoryV1");
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
| **balanceId** | **String**| Balance id. | |
| **limit** | **Integer**| The number of elements to be returned. | [optional] [default to 25] |
| **limitToChangeTypes** | **String**| Comma separated change types string that will be queried. | [optional] |
| **offset** | **Integer**| The (zero-based) starting offset in the collection. | [optional] [default to 0] |

### Return type

[**ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata**](ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getBalanceV1

> EntityResourceOutcomeBalanceV1 getBalanceV1(balanceId)

/experimental/retail-media/balances/{balanceId}

Get a balance for the given balance id.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.BalanceApi;

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

        BalanceApi apiInstance = new BalanceApi(defaultClient);
        String balanceId = "balanceId_example"; // String | The balance id.
        try {
            EntityResourceOutcomeBalanceV1 result = apiInstance.getBalanceV1(balanceId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getBalanceV1");
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
| **balanceId** | **String**| The balance id. | |

### Return type

[**EntityResourceOutcomeBalanceV1**](EntityResourceOutcomeBalanceV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getPageOfBalancesV1

> EntityResourceCollectionOutcomeBalanceV1AndMetadata getPageOfBalancesV1(accountId, limit, limitToId, offset)

/experimental/retail-media/accounts/{accountId}/balances

Gets page of balance objects for the given account id.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.BalanceApi;

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

        BalanceApi apiInstance = new BalanceApi(defaultClient);
        String accountId = "accountId_example"; // String | The account to get balances for.
        Integer limit = 25; // Integer | The number of elements to be returned.
        List<String> limitToId = Arrays.asList(); // List<String> | The balance ids which the result is limited to.
        Integer offset = 0; // Integer | The (zero-based) starting offset in the collection.
        try {
            EntityResourceCollectionOutcomeBalanceV1AndMetadata result = apiInstance.getPageOfBalancesV1(accountId, limit, limitToId, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getPageOfBalancesV1");
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
| **accountId** | **String**| The account to get balances for. | |
| **limit** | **Integer**| The number of elements to be returned. | [optional] [default to 25] |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The balance ids which the result is limited to. | [optional] |
| **offset** | **Integer**| The (zero-based) starting offset in the collection. | [optional] [default to 0] |

### Return type

[**EntityResourceCollectionOutcomeBalanceV1AndMetadata**](EntityResourceCollectionOutcomeBalanceV1AndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateBalanceV1

> EntityResourceOutcomeOfBalanceResponseV1 updateBalanceV1(accountId, balanceId, valueResourceInputOfUpdateBalanceModelV1)

/experimental/retail-media/accounts/{account-id}/balances/{balance-id}

Modify a balance for the given account id

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.BalanceApi;

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

        BalanceApi apiInstance = new BalanceApi(defaultClient);
        String accountId = "accountId_example"; // String | The account of the balance
        String balanceId = "balanceId_example"; // String | The balance to change the dates
        ValueResourceInputOfUpdateBalanceModelV1 valueResourceInputOfUpdateBalanceModelV1 = new ValueResourceInputOfUpdateBalanceModelV1(); // ValueResourceInputOfUpdateBalanceModelV1 | An object that represents the available options to modify a balance.
        try {
            EntityResourceOutcomeOfBalanceResponseV1 result = apiInstance.updateBalanceV1(accountId, balanceId, valueResourceInputOfUpdateBalanceModelV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#updateBalanceV1");
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
| **accountId** | **String**| The account of the balance | |
| **balanceId** | **String**| The balance to change the dates | |
| **valueResourceInputOfUpdateBalanceModelV1** | [**ValueResourceInputOfUpdateBalanceModelV1**](ValueResourceInputOfUpdateBalanceModelV1.md)| An object that represents the available options to modify a balance. | |

### Return type

[**EntityResourceOutcomeOfBalanceResponseV1**](EntityResourceOutcomeOfBalanceResponseV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

