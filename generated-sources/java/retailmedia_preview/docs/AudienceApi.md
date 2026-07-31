# AudienceApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRemoveContactListByAudienceSegment**](AudienceApi.md#addRemoveContactListByAudienceSegment) | **POST** /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove |
| [**bulkCreateAudience**](AudienceApi.md#bulkCreateAudience) | **POST** /preview/retail-media/accounts/{account-id}/audiences/create | /preview/retail-media/accounts/{account-id}/audiences/create |
| [**bulkCreateAudienceSegments**](AudienceApi.md#bulkCreateAudienceSegments) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/create | /preview/retail-media/accounts/{account-id}/audience-segments/create |
| [**bulkDeleteAudienceSegments**](AudienceApi.md#bulkDeleteAudienceSegments) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/delete | /preview/retail-media/accounts/{account-id}/audience-segments/delete |
| [**bulkDeleteAudiences**](AudienceApi.md#bulkDeleteAudiences) | **POST** /preview/retail-media/accounts/{account-id}/audiences/delete | /preview/retail-media/accounts/{account-id}/audiences/delete |
| [**bulkUpdateAudience**](AudienceApi.md#bulkUpdateAudience) | **PATCH** /preview/retail-media/accounts/{account-id}/audiences | /preview/retail-media/accounts/{account-id}/audiences |
| [**bulkUpdateAudienceSegments**](AudienceApi.md#bulkUpdateAudienceSegments) | **PATCH** /preview/retail-media/accounts/{account-id}/audience-segments | /preview/retail-media/accounts/{account-id}/audience-segments |
| [**clearContactListByAudienceSegment**](AudienceApi.md#clearContactListByAudienceSegment) | **POST** /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | /preview/retail-media/audience-segments/{audience-segment-id}/contact-list/clear |
| [**computeAudienceSegmentsSizes**](AudienceApi.md#computeAudienceSegmentsSizes) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/compute-sizes | /preview/retail-media/accounts/{account-id}/audience-segments/compute-sizes |
| [**computeAudiencesSizes**](AudienceApi.md#computeAudiencesSizes) | **POST** /preview/retail-media/accounts/{account-id}/audiences/compute-sizes | /preview/retail-media/accounts/{account-id}/audiences/compute-sizes |
| [**estimateAudienceSegmentSize**](AudienceApi.md#estimateAudienceSegmentSize) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/estimate-size | /preview/retail-media/accounts/{account-id}/audience-segments/estimate-size |
| [**estimateAudienceSize**](AudienceApi.md#estimateAudienceSize) | **POST** /preview/retail-media/accounts/{account-id}/audiences/estimate-size | /preview/retail-media/accounts/{account-id}/audiences/estimate-size |
| [**getAudienceSegmentContactListStatistics**](AudienceApi.md#getAudienceSegmentContactListStatistics) | **GET** /preview/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | /preview/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list |
| [**searchAudienceSegments**](AudienceApi.md#searchAudienceSegments) | **POST** /preview/retail-media/accounts/{account-id}/audience-segments/search | /preview/retail-media/accounts/{account-id}/audience-segments/search |
| [**searchAudiences**](AudienceApi.md#searchAudiences) | **POST** /preview/retail-media/accounts/{account-id}/audiences/search | /preview/retail-media/accounts/{account-id}/audiences/search |



## addRemoveContactListByAudienceSegment

> RetailMediaContactlistOperation addRemoveContactListByAudienceSegment(audienceSegmentId, retailMediaContactlistAmendmentRequest)

/preview/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove

Add/remove identifiers to or from a retail-media contact list audience-segment, with external audience segment id.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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


## bulkCreateAudience

> RmAudienceEntityV1ListResponse bulkCreateAudience(accountId, rmAudienceBulkCreateInputV1)

/preview/retail-media/accounts/{account-id}/audiences/create

Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceBulkCreateInputV1 rmAudienceBulkCreateInputV1 = new RmAudienceBulkCreateInputV1(); // RmAudienceBulkCreateInputV1 | Audience creation parameter
        try {
            RmAudienceEntityV1ListResponse result = apiInstance.bulkCreateAudience(accountId, rmAudienceBulkCreateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#bulkCreateAudience");
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
| **rmAudienceBulkCreateInputV1** | [**RmAudienceBulkCreateInputV1**](RmAudienceBulkCreateInputV1.md)| Audience creation parameter | |

### Return type

[**RmAudienceEntityV1ListResponse**](RmAudienceEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## bulkCreateAudienceSegments

> RmAudienceSegmentEntityV1ListResponse bulkCreateAudienceSegments(accountId, rmAudienceSegmentBulkCreateInputV1)

/preview/retail-media/accounts/{account-id}/audience-segments/create

Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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

/preview/retail-media/accounts/{account-id}/audience-segments/delete

Delete the segments associated to the given IDs.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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


## bulkDeleteAudiences

> RmAudienceSegmentIdEntityV1ListResponse bulkDeleteAudiences(accountId, rmAudienceBulkDeleteInputV1)

/preview/retail-media/accounts/{account-id}/audiences/delete

Deletes the audiences associated to the given IDs.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceBulkDeleteInputV1 rmAudienceBulkDeleteInputV1 = new RmAudienceBulkDeleteInputV1(); // RmAudienceBulkDeleteInputV1 | 
        try {
            RmAudienceSegmentIdEntityV1ListResponse result = apiInstance.bulkDeleteAudiences(accountId, rmAudienceBulkDeleteInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#bulkDeleteAudiences");
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
| **rmAudienceBulkDeleteInputV1** | [**RmAudienceBulkDeleteInputV1**](RmAudienceBulkDeleteInputV1.md)|  | |

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
| **200** | Success |  -  |
| **204** | Success or partial success |  -  |


## bulkUpdateAudience

> RmAudienceEntityV1ListResponse bulkUpdateAudience(accountId, rmAudienceBulkUpdateInputV1)

/preview/retail-media/accounts/{account-id}/audiences

Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceBulkUpdateInputV1 rmAudienceBulkUpdateInputV1 = new RmAudienceBulkUpdateInputV1(); // RmAudienceBulkUpdateInputV1 | 
        try {
            RmAudienceEntityV1ListResponse result = apiInstance.bulkUpdateAudience(accountId, rmAudienceBulkUpdateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#bulkUpdateAudience");
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
| **rmAudienceBulkUpdateInputV1** | [**RmAudienceBulkUpdateInputV1**](RmAudienceBulkUpdateInputV1.md)|  | |

### Return type

[**RmAudienceEntityV1ListResponse**](RmAudienceEntityV1ListResponse.md)

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

/preview/retail-media/accounts/{account-id}/audience-segments

Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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

/preview/retail-media/audience-segments/{audience-segment-id}/contact-list/clear

Delete all identifiers from a retail-media contact list audience-segment, with external audience segment id.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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


## computeAudienceSegmentsSizes

> RmAudienceSegmentSizeEntityV1ListResponse computeAudienceSegmentsSizes(accountId, rmAudienceSegmentComputeSizesInputV1)

/preview/retail-media/accounts/{account-id}/audience-segments/compute-sizes

Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceSegmentComputeSizesInputV1 rmAudienceSegmentComputeSizesInputV1 = new RmAudienceSegmentComputeSizesInputV1(); // RmAudienceSegmentComputeSizesInputV1 | 
        try {
            RmAudienceSegmentSizeEntityV1ListResponse result = apiInstance.computeAudienceSegmentsSizes(accountId, rmAudienceSegmentComputeSizesInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#computeAudienceSegmentsSizes");
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
| **rmAudienceSegmentComputeSizesInputV1** | [**RmAudienceSegmentComputeSizesInputV1**](RmAudienceSegmentComputeSizesInputV1.md)|  | |

### Return type

[**RmAudienceSegmentSizeEntityV1ListResponse**](RmAudienceSegmentSizeEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## computeAudiencesSizes

> RmAudienceSizeEntityV1ListResponse computeAudiencesSizes(accountId, rmAudienceComputeSizesInputV1)

/preview/retail-media/accounts/{account-id}/audiences/compute-sizes

Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceComputeSizesInputV1 rmAudienceComputeSizesInputV1 = new RmAudienceComputeSizesInputV1(); // RmAudienceComputeSizesInputV1 | 
        try {
            RmAudienceSizeEntityV1ListResponse result = apiInstance.computeAudiencesSizes(accountId, rmAudienceComputeSizesInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#computeAudiencesSizes");
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
| **rmAudienceComputeSizesInputV1** | [**RmAudienceComputeSizesInputV1**](RmAudienceComputeSizesInputV1.md)|  | |

### Return type

[**RmAudienceSizeEntityV1ListResponse**](RmAudienceSizeEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## estimateAudienceSegmentSize

> RmAudienceSegmentSizeEstimationV1Response estimateAudienceSegmentSize(accountId, rmAudienceSegmentEstimateSizeInputV1)

/preview/retail-media/accounts/{account-id}/audience-segments/estimate-size

Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceSegmentEstimateSizeInputV1 rmAudienceSegmentEstimateSizeInputV1 = new RmAudienceSegmentEstimateSizeInputV1(); // RmAudienceSegmentEstimateSizeInputV1 | 
        try {
            RmAudienceSegmentSizeEstimationV1Response result = apiInstance.estimateAudienceSegmentSize(accountId, rmAudienceSegmentEstimateSizeInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#estimateAudienceSegmentSize");
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
| **rmAudienceSegmentEstimateSizeInputV1** | [**RmAudienceSegmentEstimateSizeInputV1**](RmAudienceSegmentEstimateSizeInputV1.md)|  | |

### Return type

[**RmAudienceSegmentSizeEstimationV1Response**](RmAudienceSegmentSizeEstimationV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## estimateAudienceSize

> RmAudienceSizeEstimationV1Response estimateAudienceSize(accountId, rmAudienceEstimateSizeInputV1)

/preview/retail-media/accounts/{account-id}/audiences/estimate-size

Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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
        RmAudienceEstimateSizeInputV1 rmAudienceEstimateSizeInputV1 = new RmAudienceEstimateSizeInputV1(); // RmAudienceEstimateSizeInputV1 | 
        try {
            RmAudienceSizeEstimationV1Response result = apiInstance.estimateAudienceSize(accountId, rmAudienceEstimateSizeInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#estimateAudienceSize");
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
| **rmAudienceEstimateSizeInputV1** | [**RmAudienceEstimateSizeInputV1**](RmAudienceEstimateSizeInputV1.md)|  | |

### Return type

[**RmAudienceSizeEstimationV1Response**](RmAudienceSizeEstimationV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## getAudienceSegmentContactListStatistics

> RmContactListStatisticsEntityV1Response getAudienceSegmentContactListStatistics(accountId, audienceSegmentId)

/preview/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list

Returns the statistics of a contact list segment.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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

/preview/retail-media/accounts/{account-id}/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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

/preview/retail-media/accounts/{account-id}/audiences/search

Returns a list of audiences that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.AudienceApi;

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

