# AnalyticsApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateAsyncAccountsReportV2**](AnalyticsApi.md#generateAsyncAccountsReportV2) | **POST** /experimental/retail-media/reports/accounts | /experimental/retail-media/reports/accounts |
| [**generateAsyncCampaignsReportV2**](AnalyticsApi.md#generateAsyncCampaignsReportV2) | **POST** /experimental/retail-media/reports/campaigns | /experimental/retail-media/reports/campaigns |
| [**generateAsyncFillRateReport**](AnalyticsApi.md#generateAsyncFillRateReport) | **POST** /experimental/retail-media/reports/fillrate | /experimental/retail-media/reports/fillrate |
| [**generateAsyncLineItemsReportV2**](AnalyticsApi.md#generateAsyncLineItemsReportV2) | **POST** /experimental/retail-media/reports/line-items | /experimental/retail-media/reports/line-items |
| [**generateAsyncOffsiteReport**](AnalyticsApi.md#generateAsyncOffsiteReport) | **POST** /experimental/retail-media/reports/offsite | /experimental/retail-media/reports/offsite |
| [**generateAsyncUnfilledPlacementsReport**](AnalyticsApi.md#generateAsyncUnfilledPlacementsReport) | **POST** /experimental/retail-media/reports/unfilled-placements | /experimental/retail-media/reports/unfilled-placements |
| [**generateDigitalShelfIntelligenceInsight**](AnalyticsApi.md#generateDigitalShelfIntelligenceInsight) | **POST** /experimental/retail-media/insights/digital-shelf-intelligence | /experimental/retail-media/insights/digital-shelf-intelligence |
| [**generateShareOfVoiceInsight**](AnalyticsApi.md#generateShareOfVoiceInsight) | **POST** /experimental/retail-media/insights/share-of-voice | /experimental/retail-media/insights/share-of-voice |
| [**generateSyncAttributedTransactionsReport**](AnalyticsApi.md#generateSyncAttributedTransactionsReport) | **POST** /experimental/retail-media/reports/sync/attributed-transactions | /experimental/retail-media/reports/sync/attributed-transactions |
| [**generateSyncCampaignsReport**](AnalyticsApi.md#generateSyncCampaignsReport) | **POST** /experimental/retail-media/reports/sync/campaigns | /experimental/retail-media/reports/sync/campaigns |
| [**generateSyncLineItemsReport**](AnalyticsApi.md#generateSyncLineItemsReport) | **POST** /experimental/retail-media/reports/sync/line-items | /experimental/retail-media/reports/sync/line-items |
| [**generateSyncRealTimePerformanceReport**](AnalyticsApi.md#generateSyncRealTimePerformanceReport) | **POST** /experimental/retail-media/reports/sync/real-time-performance | /experimental/retail-media/reports/sync/real-time-performance |
| [**getAsyncExportOutput**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /experimental/retail-media/reports/{reportId}/output | /experimental/retail-media/reports/{reportId}/output |
| [**getAsyncExportStatus**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /experimental/retail-media/reports/{reportId}/status | /experimental/retail-media/reports/{reportId}/status |
| [**getInsightReportOutput**](AnalyticsApi.md#getInsightReportOutput) | **GET** /experimental/retail-media/insights/{insightId}/output | /experimental/retail-media/insights/{insightId}/output |
| [**getInsightReportStatus**](AnalyticsApi.md#getInsightReportStatus) | **GET** /experimental/retail-media/insights/{insightId}/status | /experimental/retail-media/insights/{insightId}/status |



## generateAsyncAccountsReportV2

> AsyncReportResponse generateAsyncAccountsReportV2(asyncAccountsReportRequest)

/experimental/retail-media/reports/accounts

Returns an asynchronous Accounts Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        AsyncAccountsReportRequest asyncAccountsReportRequest = new AsyncAccountsReportRequest(); // AsyncAccountsReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncAccountsReportV2(asyncAccountsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncAccountsReportV2");
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
| **asyncAccountsReportRequest** | [**AsyncAccountsReportRequest**](AsyncAccountsReportRequest.md)|  | |

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


## generateAsyncCampaignsReportV2

> AsyncReportResponse generateAsyncCampaignsReportV2(asyncCampaignsReportRequest)

/experimental/retail-media/reports/campaigns

Return an asynchronous Campaigns Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        AsyncCampaignsReportRequest asyncCampaignsReportRequest = new AsyncCampaignsReportRequest(); // AsyncCampaignsReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncCampaignsReportV2(asyncCampaignsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncCampaignsReportV2");
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
| **asyncCampaignsReportRequest** | [**AsyncCampaignsReportRequest**](AsyncCampaignsReportRequest.md)|  | |

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

/experimental/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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


## generateAsyncLineItemsReportV2

> AsyncReportResponse generateAsyncLineItemsReportV2(asyncLineItemsReportRequest)

/experimental/retail-media/reports/line-items

Returns an asynchronous Line Items Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        AsyncLineItemsReportRequest asyncLineItemsReportRequest = new AsyncLineItemsReportRequest(); // AsyncLineItemsReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncLineItemsReportV2(asyncLineItemsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncLineItemsReportV2");
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
| **asyncLineItemsReportRequest** | [**AsyncLineItemsReportRequest**](AsyncLineItemsReportRequest.md)|  | |

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


## generateAsyncOffsiteReport

> AsyncReportResponse generateAsyncOffsiteReport(asyncOffsiteReportRequest)

/experimental/retail-media/reports/offsite

Returns an asynchronous Offsite Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        AsyncOffsiteReportRequest asyncOffsiteReportRequest = new AsyncOffsiteReportRequest(); // AsyncOffsiteReportRequest | 
        try {
            AsyncReportResponse result = apiInstance.generateAsyncOffsiteReport(asyncOffsiteReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateAsyncOffsiteReport");
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
| **asyncOffsiteReportRequest** | [**AsyncOffsiteReportRequest**](AsyncOffsiteReportRequest.md)|  | |

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

/experimental/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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


## generateDigitalShelfIntelligenceInsight

> AsyncInsightResponse generateDigitalShelfIntelligenceInsight(digitalShelfIntelligenceInsightRequest)

/experimental/retail-media/insights/digital-shelf-intelligence

Generate a Digital Shelf Intelligence insight

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        DigitalShelfIntelligenceInsightRequest digitalShelfIntelligenceInsightRequest = new DigitalShelfIntelligenceInsightRequest(); // DigitalShelfIntelligenceInsightRequest | 
        try {
            AsyncInsightResponse result = apiInstance.generateDigitalShelfIntelligenceInsight(digitalShelfIntelligenceInsightRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateDigitalShelfIntelligenceInsight");
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
| **digitalShelfIntelligenceInsightRequest** | [**DigitalShelfIntelligenceInsightRequest**](DigitalShelfIntelligenceInsightRequest.md)|  | |

### Return type

[**AsyncInsightResponse**](AsyncInsightResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## generateShareOfVoiceInsight

> AsyncInsightResponse generateShareOfVoiceInsight(shareOfVoiceInsightRequest)

/experimental/retail-media/insights/share-of-voice

Generate a share of voice insight

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        ShareOfVoiceInsightRequest shareOfVoiceInsightRequest = new ShareOfVoiceInsightRequest(); // ShareOfVoiceInsightRequest | 
        try {
            AsyncInsightResponse result = apiInstance.generateShareOfVoiceInsight(shareOfVoiceInsightRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#generateShareOfVoiceInsight");
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
| **shareOfVoiceInsightRequest** | [**ShareOfVoiceInsightRequest**](ShareOfVoiceInsightRequest.md)|  | |

### Return type

[**AsyncInsightResponse**](AsyncInsightResponse.md)

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

/experimental/retail-media/reports/sync/attributed-transactions

Returns a synchronous Attributed Transactions Report

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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

/experimental/retail-media/reports/sync/campaigns

Returns a synchronous Campaigns Report

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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

/experimental/retail-media/reports/sync/line-items

Returns a synchronous Line Items Report

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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

/experimental/retail-media/reports/sync/real-time-performance

Returns a synchronous Real Time Performance Report. Returns empty rows; metadata includes dataCompleteThrough (latest time from streaming table in the request timezone).  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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

/experimental/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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

/experimental/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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


## getInsightReportOutput

> File getInsightReportOutput(insightId)

/experimental/retail-media/insights/{insightId}/output

Returns the output of an async insight

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        String insightId = "insightId_example"; // String | The ID of the asynchronous insight report. Must be a valid ID format.
        try {
            File result = apiInstance.getInsightReportOutput(insightId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#getInsightReportOutput");
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
| **insightId** | **String**| The ID of the asynchronous insight report. Must be a valid ID format. | |

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


## getInsightReportStatus

> AsyncInsightResponse getInsightReportStatus(insightId)

/experimental/retail-media/insights/{insightId}/status

Returns the status of an async insight

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.AnalyticsApi;

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
        String insightId = "insightId_example"; // String | The ID of the asynchronous insight report. Must be a valid ID format.
        try {
            AsyncInsightResponse result = apiInstance.getInsightReportStatus(insightId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AnalyticsApi#getInsightReportStatus");
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
| **insightId** | **String**| The ID of the asynchronous insight report. Must be a valid ID format. | |

### Return type

[**AsyncInsightResponse**](AsyncInsightResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

