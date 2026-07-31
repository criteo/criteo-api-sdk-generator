# AnalyticsApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateAsyncAccountsReportV2**](AnalyticsApi.md#generateAsyncAccountsReportV2) | **POST** /2026-01/retail-media/reports/accounts | /2026-01/retail-media/reports/accounts |
| [**generateAsyncCampaignsReportV2**](AnalyticsApi.md#generateAsyncCampaignsReportV2) | **POST** /2026-01/retail-media/reports/campaigns | /2026-01/retail-media/reports/campaigns |
| [**generateAsyncFillRateReport**](AnalyticsApi.md#generateAsyncFillRateReport) | **POST** /2026-01/retail-media/reports/fillrate | /2026-01/retail-media/reports/fillrate |
| [**generateAsyncLineItemsReportV2**](AnalyticsApi.md#generateAsyncLineItemsReportV2) | **POST** /2026-01/retail-media/reports/line-items | /2026-01/retail-media/reports/line-items |
| [**generateAsyncRevenueReport**](AnalyticsApi.md#generateAsyncRevenueReport) | **POST** /2026-01/retail-media/reports/revenue | /2026-01/retail-media/reports/revenue |
| [**generateAsyncUnfilledPlacementsReport**](AnalyticsApi.md#generateAsyncUnfilledPlacementsReport) | **POST** /2026-01/retail-media/reports/unfilled-placements | /2026-01/retail-media/reports/unfilled-placements |
| [**getAsyncExportOutput**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /2026-01/retail-media/reports/{reportId}/output | /2026-01/retail-media/reports/{reportId}/output |
| [**getAsyncExportStatus**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /2026-01/retail-media/reports/{reportId}/status | /2026-01/retail-media/reports/{reportId}/status |



## generateAsyncAccountsReportV2

> AsyncReportResponse generateAsyncAccountsReportV2(asyncAccountsReportRequest)

/2026-01/retail-media/reports/accounts

Returns an asynchronous Accounts Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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

/2026-01/retail-media/reports/campaigns

Return an asynchronous Campaigns Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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

/2026-01/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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

/2026-01/retail-media/reports/line-items

Returns an asynchronous Line Items Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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


## generateAsyncRevenueReport

> AsyncReportResponse generateAsyncRevenueReport(asyncRevenueReportRequest)

/2026-01/retail-media/reports/revenue

Returns an asynchronous Revenue Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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

/2026-01/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  &lt;br /&gt;  This endpoint is subject to specific rate limits.

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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


## getAsyncExportOutput

> File getAsyncExportOutput(reportId)

/2026-01/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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

/2026-01/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

```java
package com.criteo.api.retailmedia.v2026_01;

import com.criteo.api.retailmedia.v2026_01.ApiClient;
import com.criteo.api.retailmedia.v2026_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_01.ApiException;
import com.criteo.api.retailmedia.v2026_01.Configuration;
import com.criteo.api.retailmedia.v2026_01.auth.*;
import com.criteo.api.retailmedia.v2026_01.model.*;
import com.criteo.api.retailmedia.v2026_01.api.AnalyticsApi;

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

