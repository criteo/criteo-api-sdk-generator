# BillingApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPartnerBillingReportRequestV1**](BillingApi.md#createPartnerBillingReportRequestV1) | **POST** /2026-07/retail-media/billing/partner-report | /2026-07/retail-media/billing/partner-report |
| [**getPartnerBillingReportOutputV1**](BillingApi.md#getPartnerBillingReportOutputV1) | **GET** /2026-07/retail-media/billing/partner-report/{requestId}/output | /2026-07/retail-media/billing/partner-report/{requestId}/output |
| [**getPartnerBillingReportStatusV1**](BillingApi.md#getPartnerBillingReportStatusV1) | **GET** /2026-07/retail-media/billing/partner-report/{requestId}/status | /2026-07/retail-media/billing/partner-report/{requestId}/status |



## createPartnerBillingReportRequestV1

> EntityResourceOutcomePartnerBillingReportStatusV1 createPartnerBillingReportRequestV1(valueResourceInputPartnerBillingReportRequestV1)

/2026-07/retail-media/billing/partner-report

Create a Partner Billing Report request.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.BillingApi;

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

        BillingApi apiInstance = new BillingApi(defaultClient);
        ValueResourceInputPartnerBillingReportRequestV1 valueResourceInputPartnerBillingReportRequestV1 = new ValueResourceInputPartnerBillingReportRequestV1(); // ValueResourceInputPartnerBillingReportRequestV1 | Partner Billing Report request object.
        try {
            EntityResourceOutcomePartnerBillingReportStatusV1 result = apiInstance.createPartnerBillingReportRequestV1(valueResourceInputPartnerBillingReportRequestV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BillingApi#createPartnerBillingReportRequestV1");
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
| **valueResourceInputPartnerBillingReportRequestV1** | [**ValueResourceInputPartnerBillingReportRequestV1**](ValueResourceInputPartnerBillingReportRequestV1.md)| Partner Billing Report request object. | |

### Return type

[**EntityResourceOutcomePartnerBillingReportStatusV1**](EntityResourceOutcomePartnerBillingReportStatusV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## getPartnerBillingReportOutputV1

> File getPartnerBillingReportOutputV1(requestId)

/2026-07/retail-media/billing/partner-report/{requestId}/output

Get the output of an existing Partner Billing Report.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.BillingApi;

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

        BillingApi apiInstance = new BillingApi(defaultClient);
        String requestId = "requestId_example"; // String | The id of a Partner Billing Report request.
        try {
            File result = apiInstance.getPartnerBillingReportOutputV1(requestId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BillingApi#getPartnerBillingReportOutputV1");
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
| **requestId** | **String**| The id of a Partner Billing Report request. | |

### Return type

[**File**](File.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/csv, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getPartnerBillingReportStatusV1

> EntityResourceOutcomePartnerBillingReportStatusV1 getPartnerBillingReportStatusV1(requestId)

/2026-07/retail-media/billing/partner-report/{requestId}/status

Get the status of an existing Partner Billing Report.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.BillingApi;

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

        BillingApi apiInstance = new BillingApi(defaultClient);
        String requestId = "requestId_example"; // String | The id of a Partner Billing Report request.
        try {
            EntityResourceOutcomePartnerBillingReportStatusV1 result = apiInstance.getPartnerBillingReportStatusV1(requestId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BillingApi#getPartnerBillingReportStatusV1");
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
| **requestId** | **String**| The id of a Partner Billing Report request. | |

### Return type

[**EntityResourceOutcomePartnerBillingReportStatusV1**](EntityResourceOutcomePartnerBillingReportStatusV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

