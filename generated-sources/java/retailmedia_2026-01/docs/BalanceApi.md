# BalanceApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFundsByAccountAndBalanceId**](BalanceApi.md#addFundsByAccountAndBalanceId) | **POST** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds |
| [**changeDatesByAccountAndBalanceId**](BalanceApi.md#changeDatesByAccountAndBalanceId) | **POST** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates |
| [**createBalanceByAccountId**](BalanceApi.md#createBalanceByAccountId) | **POST** /2026-01/retail-media/accounts/{account-id}/balances | /2026-01/retail-media/accounts/{account-id}/balances |
| [**getBalanceByAccountAndBalanceId**](BalanceApi.md#getBalanceByAccountAndBalanceId) | **GET** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} |
| [**getBalanceHistory**](BalanceApi.md#getBalanceHistory) | **GET** /2026-01/retail-media/balances/{balanceId}/history | /2026-01/retail-media/balances/{balanceId}/history |
| [**getBalancesByAccountId**](BalanceApi.md#getBalancesByAccountId) | **GET** /2026-01/retail-media/accounts/{account-id}/balances | /2026-01/retail-media/accounts/{account-id}/balances |
| [**getCampaignsByBalanceId**](BalanceApi.md#getCampaignsByBalanceId) | **GET** /2026-01/retail-media/balances/{balance-id}/campaigns | /2026-01/retail-media/balances/{balance-id}/campaigns |
| [**modifyBalanceByAccountAndBalanceId**](BalanceApi.md#modifyBalanceByAccountAndBalanceId) | **PATCH** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} |



## addFundsByAccountAndBalanceId

> BalanceResponseV2Response addFundsByAccountAndBalanceId(accountId, balanceId, addFundsToBalanceV2Request)

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds

Add funds to a balance for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        String balanceId = "balanceId_example"; // String | The balance to add funds to
        AddFundsToBalanceV2Request addFundsToBalanceV2Request = new AddFundsToBalanceV2Request(); // AddFundsToBalanceV2Request | An object that represents the available options of adding funds to a balance.
        try {
            BalanceResponseV2Response result = apiInstance.addFundsByAccountAndBalanceId(accountId, balanceId, addFundsToBalanceV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#addFundsByAccountAndBalanceId");
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
| **balanceId** | **String**| The balance to add funds to | |
| **addFundsToBalanceV2Request** | [**AddFundsToBalanceV2Request**](AddFundsToBalanceV2Request.md)| An object that represents the available options of adding funds to a balance. | |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## changeDatesByAccountAndBalanceId

> BalanceResponseV2Response changeDatesByAccountAndBalanceId(accountId, balanceId, changeDatesOfBalanceV2Request)

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates

Change dates of a balance for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        ChangeDatesOfBalanceV2Request changeDatesOfBalanceV2Request = new ChangeDatesOfBalanceV2Request(); // ChangeDatesOfBalanceV2Request | An object that represents the available options to modify schedule of a balance.
        try {
            BalanceResponseV2Response result = apiInstance.changeDatesByAccountAndBalanceId(accountId, balanceId, changeDatesOfBalanceV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#changeDatesByAccountAndBalanceId");
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
| **changeDatesOfBalanceV2Request** | [**ChangeDatesOfBalanceV2Request**](ChangeDatesOfBalanceV2Request.md)| An object that represents the available options to modify schedule of a balance. | |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## createBalanceByAccountId

> BalanceResponseV2Response createBalanceByAccountId(accountId, createBalanceV2Request)

/2026-01/retail-media/accounts/{account-id}/balances

Create balance for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        String accountId = "accountId_example"; // String | The account to create balances for
        CreateBalanceV2Request createBalanceV2Request = new CreateBalanceV2Request(); // CreateBalanceV2Request | An object that represents the available options to set when creating a Retail Media Balance
        try {
            BalanceResponseV2Response result = apiInstance.createBalanceByAccountId(accountId, createBalanceV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#createBalanceByAccountId");
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
| **accountId** | **String**| The account to create balances for | |
| **createBalanceV2Request** | [**CreateBalanceV2Request**](CreateBalanceV2Request.md)| An object that represents the available options to set when creating a Retail Media Balance | |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## getBalanceByAccountAndBalanceId

> BalanceResponseV2Response getBalanceByAccountAndBalanceId(accountId, balanceId)

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}

Get a balance for the given account id and balance id

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        String balanceId = "balanceId_example"; // String | The balance id
        try {
            BalanceResponseV2Response result = apiInstance.getBalanceByAccountAndBalanceId(accountId, balanceId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getBalanceByAccountAndBalanceId");
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
| **balanceId** | **String**| The balance id | |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getBalanceHistory

> PageOfBalanceHistoryChangeDataCaptureV1 getBalanceHistory(balanceId, limit, limitToChangeTypes, offset)

/2026-01/retail-media/balances/{balanceId}/history

Gets the balance&#39;s historical change data.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
            PageOfBalanceHistoryChangeDataCaptureV1 result = apiInstance.getBalanceHistory(balanceId, limit, limitToChangeTypes, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getBalanceHistory");
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

[**PageOfBalanceHistoryChangeDataCaptureV1**](PageOfBalanceHistoryChangeDataCaptureV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getBalancesByAccountId

> BalanceResponseV2PagedListResponse getBalancesByAccountId(accountId, limitToId, pageIndex, pageSize)

/2026-01/retail-media/accounts/{account-id}/balances

Gets page of balance objects for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        String accountId = "accountId_example"; // String | The account to get balances for
        List<String> limitToId = Arrays.asList(); // List<String> | The ids that you would like to limit your result set to
        Integer pageIndex = 0; // Integer | The 0 indexed page index you would like to receive given the page size
        Integer pageSize = 25; // Integer | The maximum number of items you would like to receive in this request
        try {
            BalanceResponseV2PagedListResponse result = apiInstance.getBalancesByAccountId(accountId, limitToId, pageIndex, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getBalancesByAccountId");
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
| **accountId** | **String**| The account to get balances for | |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The ids that you would like to limit your result set to | [optional] |
| **pageIndex** | **Integer**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**BalanceResponseV2PagedListResponse**](BalanceResponseV2PagedListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCampaignsByBalanceId

> BalanceCampaign202110PagedListResponse getCampaignsByBalanceId(balanceId, limitToId, pageIndex, pageSize)

/2026-01/retail-media/balances/{balance-id}/campaigns

Gets page of campaigns for the given balanceId

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        String balanceId = "balanceId_example"; // String | The balance to get campaigns from
        List<String> limitToId = Arrays.asList(); // List<String> | The ids that you would like to limit your result set to
        Integer pageIndex = 0; // Integer | The 0 indexed page index you would like to receive given the page size
        Integer pageSize = 25; // Integer | The maximum number of items you would like to receive in this request
        try {
            BalanceCampaign202110PagedListResponse result = apiInstance.getCampaignsByBalanceId(balanceId, limitToId, pageIndex, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#getCampaignsByBalanceId");
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
| **balanceId** | **String**| The balance to get campaigns from | |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The ids that you would like to limit your result set to | [optional] |
| **pageIndex** | **Integer**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**BalanceCampaign202110PagedListResponse**](BalanceCampaign202110PagedListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## modifyBalanceByAccountAndBalanceId

> BalanceResponseV2Response modifyBalanceByAccountAndBalanceId(accountId, balanceId, updateBalanceModelV2Request)

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}

Modify a balance for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.BalanceApi;

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
        UpdateBalanceModelV2Request updateBalanceModelV2Request = new UpdateBalanceModelV2Request(); // UpdateBalanceModelV2Request | An object that represents the available options to modify a balance.
        try {
            BalanceResponseV2Response result = apiInstance.modifyBalanceByAccountAndBalanceId(accountId, balanceId, updateBalanceModelV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BalanceApi#modifyBalanceByAccountAndBalanceId");
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
| **updateBalanceModelV2Request** | [**UpdateBalanceModelV2Request**](UpdateBalanceModelV2Request.md)| An object that represents the available options to modify a balance. | |

### Return type

[**BalanceResponseV2Response**](BalanceResponseV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

