# AudienceApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRemoveContactListByAudienceSegment**](AudienceApi.md#addRemoveContactListByAudienceSegment) | **POST** /2026-07/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | /2026-07/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove |
| [**bulkCreateAudienceSegments**](AudienceApi.md#bulkCreateAudienceSegments) | **POST** /2026-07/retail-media/accounts/{account-id}/audience-segments/create | /2026-07/retail-media/accounts/{account-id}/audience-segments/create |
| [**bulkDeleteAudienceSegments**](AudienceApi.md#bulkDeleteAudienceSegments) | **POST** /2026-07/retail-media/accounts/{account-id}/audience-segments/delete | /2026-07/retail-media/accounts/{account-id}/audience-segments/delete |
| [**bulkUpdateAudienceSegments**](AudienceApi.md#bulkUpdateAudienceSegments) | **PATCH** /2026-07/retail-media/accounts/{account-id}/audience-segments | /2026-07/retail-media/accounts/{account-id}/audience-segments |
| [**clearContactListByAudienceSegment**](AudienceApi.md#clearContactListByAudienceSegment) | **POST** /2026-07/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | /2026-07/retail-media/audience-segments/{audience-segment-id}/contact-list/clear |
| [**getAudienceSegmentContactListStatistics**](AudienceApi.md#getAudienceSegmentContactListStatistics) | **GET** /2026-07/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | /2026-07/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list |
| [**searchAudienceSegments**](AudienceApi.md#searchAudienceSegments) | **POST** /2026-07/retail-media/accounts/{account-id}/audience-segments/search | /2026-07/retail-media/accounts/{account-id}/audience-segments/search |
| [**searchAudiences**](AudienceApi.md#searchAudiences) | **POST** /2026-07/retail-media/accounts/{account-id}/audiences/search | /2026-07/retail-media/accounts/{account-id}/audiences/search |



## addRemoveContactListByAudienceSegment

> RetailMediaContactlistOperation addRemoveContactListByAudienceSegment(audienceSegmentId, retailMediaContactlistAmendmentRequest)

/2026-07/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove

Add/remove identifiers to or from a retail-media contact list audience-segment, with external audience segment id.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String audienceSegmentId = "audienceSegmentId_example"; // String | The id of the contact list audience-segment to amend, we only accept external Id here
        RetailMediaContactlistAmendmentRequest retailMediaContactlistAmendmentRequest = new RetailMediaContactlistAmendmentRequest(); // RetailMediaContactlistAmendmentRequest | 
        try {
            RetailMediaContactlistOperation result = apiInstance.addRemoveContactListByAudienceSegment(audienceSegmentId, retailMediaContactlistAmendmentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#addRemoveContactListByAudienceSegment");
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
| **audienceSegmentId** | **String**| The id of the contact list audience-segment to amend, we only accept external Id here | |
| **retailMediaContactlistAmendmentRequest** | [**RetailMediaContactlistAmendmentRequest**](RetailMediaContactlistAmendmentRequest.md)|  | |

### Return type

[**RetailMediaContactlistOperation**](RetailMediaContactlistOperation.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of created request |  -  |


## bulkCreateAudienceSegments

> RmAudienceSegmentEntityV1ListResponse bulkCreateAudienceSegments(accountId, rmAudienceSegmentBulkCreateInputV1)

/2026-07/retail-media/accounts/{account-id}/audience-segments/create

Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String accountId = "accountId_example"; // String | Account Id
        RmAudienceSegmentBulkCreateInputV1 rmAudienceSegmentBulkCreateInputV1 = new RmAudienceSegmentBulkCreateInputV1(); // RmAudienceSegmentBulkCreateInputV1 | Segment creation parameter
        try {
            RmAudienceSegmentEntityV1ListResponse result = apiInstance.bulkCreateAudienceSegments(accountId, rmAudienceSegmentBulkCreateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#bulkCreateAudienceSegments");
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
| **rmAudienceSegmentBulkCreateInputV1** | [**RmAudienceSegmentBulkCreateInputV1**](RmAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**RmAudienceSegmentEntityV1ListResponse**](RmAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## bulkDeleteAudienceSegments

> RmAudienceSegmentIdEntityV1ListResponse bulkDeleteAudienceSegments(accountId, rmAudienceSegmentBulkDeleteInputV1)

/2026-07/retail-media/accounts/{account-id}/audience-segments/delete

Delete the segments associated to the given IDs.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String accountId = "accountId_example"; // String | Account id
        RmAudienceSegmentBulkDeleteInputV1 rmAudienceSegmentBulkDeleteInputV1 = new RmAudienceSegmentBulkDeleteInputV1(); // RmAudienceSegmentBulkDeleteInputV1 | Segment delete request.
        try {
            RmAudienceSegmentIdEntityV1ListResponse result = apiInstance.bulkDeleteAudienceSegments(accountId, rmAudienceSegmentBulkDeleteInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#bulkDeleteAudienceSegments");
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
| **accountId** | **String**| Account id | |
| **rmAudienceSegmentBulkDeleteInputV1** | [**RmAudienceSegmentBulkDeleteInputV1**](RmAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**RmAudienceSegmentIdEntityV1ListResponse**](RmAudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## bulkUpdateAudienceSegments

> RmAudienceSegmentEntityV1ListResponse bulkUpdateAudienceSegments(accountId, rmAudienceSegmentBulkUpdateInputV1)

/2026-07/retail-media/accounts/{account-id}/audience-segments

Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String accountId = "accountId_example"; // String | Account id
        RmAudienceSegmentBulkUpdateInputV1 rmAudienceSegmentBulkUpdateInputV1 = new RmAudienceSegmentBulkUpdateInputV1(); // RmAudienceSegmentBulkUpdateInputV1 | Segment Update request
        try {
            RmAudienceSegmentEntityV1ListResponse result = apiInstance.bulkUpdateAudienceSegments(accountId, rmAudienceSegmentBulkUpdateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#bulkUpdateAudienceSegments");
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
| **accountId** | **String**| Account id | |
| **rmAudienceSegmentBulkUpdateInputV1** | [**RmAudienceSegmentBulkUpdateInputV1**](RmAudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**RmAudienceSegmentEntityV1ListResponse**](RmAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## clearContactListByAudienceSegment

> clearContactListByAudienceSegment(audienceSegmentId)

/2026-07/retail-media/audience-segments/{audience-segment-id}/contact-list/clear

Delete all identifiers from a retail-media contact list audience-segment, with external audience segment id.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String audienceSegmentId = "audienceSegmentId_example"; // String | The id of the contact list audience-segment to amend, we only accept external Id here
        try {
            apiInstance.clearContactListByAudienceSegment(audienceSegmentId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#clearContactListByAudienceSegment");
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
| **audienceSegmentId** | **String**| The id of the contact list audience-segment to amend, we only accept external Id here | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Contact List identifiers were deleted |  -  |


## getAudienceSegmentContactListStatistics

> RmContactListStatisticsEntityV1Response getAudienceSegmentContactListStatistics(accountId, audienceSegmentId)

/2026-07/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list

Returns the statistics of a contact list segment.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String accountId = "accountId_example"; // String | Account Id
        String audienceSegmentId = "audienceSegmentId_example"; // String | Segment Id.
        try {
            RmContactListStatisticsEntityV1Response result = apiInstance.getAudienceSegmentContactListStatistics(accountId, audienceSegmentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#getAudienceSegmentContactListStatistics");
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
| **audienceSegmentId** | **String**| Segment Id. | |

### Return type

[**RmContactListStatisticsEntityV1Response**](RmContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## searchAudienceSegments

> RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse searchAudienceSegments(accountId, rmAudienceSegmentSearchInputV1, limit, offset)

/2026-07/retail-media/accounts/{account-id}/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String accountId = "accountId_example"; // String | Account Id
        RmAudienceSegmentSearchInputV1 rmAudienceSegmentSearchInputV1 = new RmAudienceSegmentSearchInputV1(); // RmAudienceSegmentSearchInputV1 | Segment search filters.
        Integer limit = 50; // Integer | The number of elements to be returned. The default is 50 and the maximum is 500.
        Integer offset = 0; // Integer | The (zero-based) offset into the collection. The default is 0.
        try {
            RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse result = apiInstance.searchAudienceSegments(accountId, rmAudienceSegmentSearchInputV1, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#searchAudienceSegments");
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
| **rmAudienceSegmentSearchInputV1** | [**RmAudienceSegmentSearchInputV1**](RmAudienceSegmentSearchInputV1.md)| Segment search filters. | |
| **limit** | **Integer**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] [default to 50] |
| **offset** | **Integer**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse**](RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## searchAudiences

> RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse searchAudiences(accountId, rmAudienceSearchInputV1, limit, offset)

/2026-07/retail-media/accounts/{account-id}/audiences/search

Returns a list of audiences that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.retailmedia.v2026_07;

import com.criteo.api.retailmedia.v2026_07.ApiClient;
import com.criteo.api.retailmedia.v2026_07.ApiClientBuilder;
import com.criteo.api.retailmedia.v2026_07.ApiException;
import com.criteo.api.retailmedia.v2026_07.Configuration;
import com.criteo.api.retailmedia.v2026_07.auth.*;
import com.criteo.api.retailmedia.v2026_07.model.*;
import com.criteo.api.retailmedia.v2026_07.api.AudienceApi;

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

        AudienceApi apiInstance = new AudienceApi(defaultClient);
        String accountId = "accountId_example"; // String | Account Id
        RmAudienceSearchInputV1 rmAudienceSearchInputV1 = new RmAudienceSearchInputV1(); // RmAudienceSearchInputV1 | Audience search filters.
        Integer limit = 50; // Integer | The number of elements to be returned. The default is 50 and the maximum is 500.
        Integer offset = 0; // Integer | The (zero-based) offset into the collection. The default is 0.
        try {
            RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse result = apiInstance.searchAudiences(accountId, rmAudienceSearchInputV1, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#searchAudiences");
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
| **rmAudienceSearchInputV1** | [**RmAudienceSearchInputV1**](RmAudienceSearchInputV1.md)| Audience search filters. | |
| **limit** | **Integer**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] [default to 50] |
| **offset** | **Integer**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse**](RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |

