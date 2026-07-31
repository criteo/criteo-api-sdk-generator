# AnalyticsApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateAsyncAttributedTransactionsReport**](AnalyticsApi.md#generateAsyncAttributedTransactionsReport) | **POST** /2026-07/retail-media/reports/attributed-transactions | /2026-07/retail-media/reports/attributed-transactions |
| [**generateAsyncFillRateReport**](AnalyticsApi.md#generateAsyncFillRateReport) | **POST** /2026-07/retail-media/reports/fillrate | /2026-07/retail-media/reports/fillrate |
| [**generateAsyncMissedOpportunitiesReport**](AnalyticsApi.md#generateAsyncMissedOpportunitiesReport) | **POST** /2026-07/retail-media/reports/missed-opportunities | /2026-07/retail-media/reports/missed-opportunities |
| [**generateAsyncPerformanceReport**](AnalyticsApi.md#generateAsyncPerformanceReport) | **POST** /2026-07/retail-media/reports/performance | /2026-07/retail-media/reports/performance |
| [**generateAsyncRevenueReport**](AnalyticsApi.md#generateAsyncRevenueReport) | **POST** /2026-07/retail-media/reports/revenue | /2026-07/retail-media/reports/revenue |
| [**generateAsyncUnfilledPlacementsReport**](AnalyticsApi.md#generateAsyncUnfilledPlacementsReport) | **POST** /2026-07/retail-media/reports/unfilled-placements | /2026-07/retail-media/reports/unfilled-placements |
| [**generateSyncAttributedTransactionsReport**](AnalyticsApi.md#generateSyncAttributedTransactionsReport) | **POST** /2026-07/retail-media/reports/sync/attributed-transactions | /2026-07/retail-media/reports/sync/attributed-transactions |
| [**generateSyncCampaignsReport**](AnalyticsApi.md#generateSyncCampaignsReport) | **POST** /2026-07/retail-media/reports/sync/campaigns | /2026-07/retail-media/reports/sync/campaigns |
| [**generateSyncLineItemsReport**](AnalyticsApi.md#generateSyncLineItemsReport) | **POST** /2026-07/retail-media/reports/sync/line-items | /2026-07/retail-media/reports/sync/line-items |
| [**generateSyncRealTimePerformanceReport**](AnalyticsApi.md#generateSyncRealTimePerformanceReport) | **POST** /2026-07/retail-media/reports/sync/real-time-performance | /2026-07/retail-media/reports/sync/real-time-performance |
| [**getAsyncExportOutput**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /2026-07/retail-media/reports/{reportId}/output | /2026-07/retail-media/reports/{reportId}/output |
| [**getAsyncExportStatus**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /2026-07/retail-media/reports/{reportId}/status | /2026-07/retail-media/reports/{reportId}/status |



## generateAsyncAttributedTransactionsReport

> AsyncReportResponse generateAsyncAttributedTransactionsReport(asyncAttributedTransactionsReportRequest)

/2026-07/retail-media/reports/attributed-transactions

Creates an attributed-transactions async report. The request accepts explicit attributed-transaction dimensions, metrics, and filters.  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        AsyncAttributedTransactionsReportRequest asyncAttributedTransactionsReportRequest = new AsyncAttributedTransactionsReportRequest(); // AsyncAttributedTransactionsReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncAttributedTransactionsReport(asyncAttributedTransactionsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncAttributedTransactionsReport");
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
| **asyncAttributedTransactionsReportRequest** | [**AsyncAttributedTransactionsReportRequest**](AsyncAttributedTransactionsReportRequest.md)|  | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateAsyncFillRateReport

> AsyncReportResponse generateAsyncFillRateReport(asyncFillRateReportRequest)

/2026-07/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        AsyncFillRateReportRequest asyncFillRateReportRequest = new AsyncFillRateReportRequest(); // AsyncFillRateReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncFillRateReport(asyncFillRateReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncFillRateReport");
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
| **asyncFillRateReportRequest** | [**AsyncFillRateReportRequest**](AsyncFillRateReportRequest.md)|  | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateAsyncMissedOpportunitiesReport

> AsyncReportResponse generateAsyncMissedOpportunitiesReport(asyncMissedOpportunitiesReportRequest)

/2026-07/retail-media/reports/missed-opportunities

Creates a missed-opportunities async report. The request accepts explicit missed-opportunities dimensions, metrics, and filters.  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        AsyncMissedOpportunitiesReportRequest asyncMissedOpportunitiesReportRequest = new AsyncMissedOpportunitiesReportRequest(); // AsyncMissedOpportunitiesReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncMissedOpportunitiesReport(asyncMissedOpportunitiesReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncMissedOpportunitiesReport");
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
| **asyncMissedOpportunitiesReportRequest** | [**AsyncMissedOpportunitiesReportRequest**](AsyncMissedOpportunitiesReportRequest.md)|  | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateAsyncPerformanceReport

> AsyncReportResponse generateAsyncPerformanceReport(asyncPerformanceReportRequest)

/2026-07/retail-media/reports/performance

Creates a performance DSP analytics async report. Dimensions and metrics select the output schema, and filters constrain eligible data.  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        AsyncPerformanceReportRequest asyncPerformanceReportRequest = new AsyncPerformanceReportRequest(); // AsyncPerformanceReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncPerformanceReport(asyncPerformanceReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncPerformanceReport");
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
| **asyncPerformanceReportRequest** | [**AsyncPerformanceReportRequest**](AsyncPerformanceReportRequest.md)|  | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateAsyncRevenueReport

> AsyncReportResponse generateAsyncRevenueReport(asyncRevenueReportRequest)

/2026-07/retail-media/reports/revenue

Returns an asynchronous Revenue Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        AsyncRevenueReportRequest asyncRevenueReportRequest = new AsyncRevenueReportRequest(); // AsyncRevenueReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncRevenueReport(asyncRevenueReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncRevenueReport");
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
| **asyncRevenueReportRequest** | [**AsyncRevenueReportRequest**](AsyncRevenueReportRequest.md)|  | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateAsyncUnfilledPlacementsReport

> AsyncReportResponse generateAsyncUnfilledPlacementsReport(asyncUnfilledPlacementsReportRequest)

/2026-07/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        AsyncUnfilledPlacementsReportRequest asyncUnfilledPlacementsReportRequest = new AsyncUnfilledPlacementsReportRequest(); // AsyncUnfilledPlacementsReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncUnfilledPlacementsReport(asyncUnfilledPlacementsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncUnfilledPlacementsReport");
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
| **asyncUnfilledPlacementsReportRequest** | [**AsyncUnfilledPlacementsReportRequest**](AsyncUnfilledPlacementsReportRequest.md)|  | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateSyncAttributedTransactionsReport

> ReportResponse generateSyncAttributedTransactionsReport(syncAttributedTransactionsReportRequest)

/2026-07/retail-media/reports/sync/attributed-transactions

Returns a synchronous Attributed Transactions Report

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        SyncAttributedTransactionsReportRequest syncAttributedTransactionsReportRequest = new SyncAttributedTransactionsReportRequest(); // SyncAttributedTransactionsReportRequest | 
        try {
            ReportResponse result = apiInstance.generateSyncAttributedTransactionsReport(syncAttributedTransactionsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateSyncAttributedTransactionsReport");
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
| **syncAttributedTransactionsReportRequest** | [**SyncAttributedTransactionsReportRequest**](SyncAttributedTransactionsReportRequest.md)|  | |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateSyncCampaignsReport

> ReportResponse generateSyncCampaignsReport(syncCampaignsReportRequest)

/2026-07/retail-media/reports/sync/campaigns

Returns a synchronous Campaigns Report

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        SyncCampaignsReportRequest syncCampaignsReportRequest = new SyncCampaignsReportRequest(); // SyncCampaignsReportRequest | 
        try {
            ReportResponse result = apiInstance.generateSyncCampaignsReport(syncCampaignsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateSyncCampaignsReport");
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
| **syncCampaignsReportRequest** | [**SyncCampaignsReportRequest**](SyncCampaignsReportRequest.md)|  | |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateSyncLineItemsReport

> ReportResponse generateSyncLineItemsReport(syncLineItemsReportRequest)

/2026-07/retail-media/reports/sync/line-items

Returns a synchronous Line Items Report

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        SyncLineItemsReportRequest syncLineItemsReportRequest = new SyncLineItemsReportRequest(); // SyncLineItemsReportRequest | 
        try {
            ReportResponse result = apiInstance.generateSyncLineItemsReport(syncLineItemsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateSyncLineItemsReport");
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
| **syncLineItemsReportRequest** | [**SyncLineItemsReportRequest**](SyncLineItemsReportRequest.md)|  | |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateSyncRealTimePerformanceReport

> ReportResponse generateSyncRealTimePerformanceReport(syncRealTimePerformanceReportRequest)

/2026-07/retail-media/reports/sync/real-time-performance

Returns a synchronous Real Time Performance Report. Returns empty rows; metadata includes dataCompleteThrough (latest time from streaming table in the request timezone).  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        SyncRealTimePerformanceReportRequest syncRealTimePerformanceReportRequest = new SyncRealTimePerformanceReportRequest(); // SyncRealTimePerformanceReportRequest | 
        try {
            ReportResponse result = apiInstance.generateSyncRealTimePerformanceReport(syncRealTimePerformanceReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateSyncRealTimePerformanceReport");
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
| **syncRealTimePerformanceReportRequest** | [**SyncRealTimePerformanceReportRequest**](SyncRealTimePerformanceReportRequest.md)|  | |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAsyncExportOutput

> File getAsyncExportOutput(reportId)

/2026-07/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        String reportId = "reportId_example"; // String | The ID of the report to retrieve
        try {
            File result = apiInstance.getAsyncExportOutput(reportId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#getAsyncExportOutput");
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
| **reportId** | **String**| The ID of the report to retrieve | |

### Return type

[**File**](File.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAsyncExportStatus

> AsyncReportResponse getAsyncExportStatus(reportId)

/2026-07/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AnalyticsApi;

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
        String reportId = "reportId_example"; // String | The ID of the report to retrieve
        try {
            AsyncReportResponse result = apiInstance.getAsyncExportStatus(reportId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#getAsyncExportStatus");
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
| **reportId** | **String**| The ID of the report to retrieve | |

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

