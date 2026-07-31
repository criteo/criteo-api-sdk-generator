# SegmentApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRemoveContactListByAudienceSegment**](SegmentApi.md#addRemoveContactListByAudienceSegment) | **POST** /preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove | /preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove |
| [**bulkCreateAudienceSegments**](SegmentApi.md#bulkCreateAudienceSegments) | **POST** /preview/commerce-grid/audience-segments/create | /preview/commerce-grid/audience-segments/create |
| [**bulkDeleteAudienceSegments**](SegmentApi.md#bulkDeleteAudienceSegments) | **POST** /preview/commerce-grid/audience-segments/delete | /preview/commerce-grid/audience-segments/delete |
| [**bulkUpdateAudienceSegments**](SegmentApi.md#bulkUpdateAudienceSegments) | **PATCH** /preview/commerce-grid/audience-segments | /preview/commerce-grid/audience-segments |
| [**clearContactListByAudienceSegment**](SegmentApi.md#clearContactListByAudienceSegment) | **POST** /preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear | /preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear |
| [**getAudienceSegmentContactListStatistics**](SegmentApi.md#getAudienceSegmentContactListStatistics) | **GET** /preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics | /preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics |
| [**searchAudienceSegments**](SegmentApi.md#searchAudienceSegments) | **POST** /preview/commerce-grid/audience-segments/search | /preview/commerce-grid/audience-segments/search |



## addRemoveContactListByAudienceSegment

> CommerceGridContactlistOperation addRemoveContactListByAudienceSegment(audienceSegmentId, commerceGridContactlistAmendmentRequest)

/preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove

Add/remove identifiers to or from a Commerce Grid audience segment of type Contact List.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        String audienceSegmentId = "audienceSegmentId_example"; // String | The ID of the audience segment of type contact list to amend
        CommerceGridContactlistAmendmentRequest commerceGridContactlistAmendmentRequest = new CommerceGridContactlistAmendmentRequest(); // CommerceGridContactlistAmendmentRequest | 
        try {
            CommerceGridContactlistOperation result = apiInstance.addRemoveContactListByAudienceSegment(audienceSegmentId, commerceGridContactlistAmendmentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#addRemoveContactListByAudienceSegment");
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
| **audienceSegmentId** | **String**| The ID of the audience segment of type contact list to amend | |
| **commerceGridContactlistAmendmentRequest** | [**CommerceGridContactlistAmendmentRequest**](CommerceGridContactlistAmendmentRequest.md)|  | |

### Return type

[**CommerceGridContactlistOperation**](CommerceGridContactlistOperation.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the add/remove operation of identifiers |  -  |


## bulkCreateAudienceSegments

> CgAudienceSegmentEntityV1ListResponse bulkCreateAudienceSegments(cgAudienceSegmentBulkCreateInputV1)

/preview/commerce-grid/audience-segments/create

Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        CgAudienceSegmentBulkCreateInputV1 cgAudienceSegmentBulkCreateInputV1 = new CgAudienceSegmentBulkCreateInputV1(); // CgAudienceSegmentBulkCreateInputV1 | Segment creation parameter
        try {
            CgAudienceSegmentEntityV1ListResponse result = apiInstance.bulkCreateAudienceSegments(cgAudienceSegmentBulkCreateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#bulkCreateAudienceSegments");
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
| **cgAudienceSegmentBulkCreateInputV1** | [**CgAudienceSegmentBulkCreateInputV1**](CgAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**CgAudienceSegmentEntityV1ListResponse**](CgAudienceSegmentEntityV1ListResponse.md)

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

> CgAudienceSegmentIdEntityV1ListResponse bulkDeleteAudienceSegments(cgAudienceSegmentBulkDeleteInputV1)

/preview/commerce-grid/audience-segments/delete

Delete the segments associated to the given IDs.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        CgAudienceSegmentBulkDeleteInputV1 cgAudienceSegmentBulkDeleteInputV1 = new CgAudienceSegmentBulkDeleteInputV1(); // CgAudienceSegmentBulkDeleteInputV1 | Segment delete request.
        try {
            CgAudienceSegmentIdEntityV1ListResponse result = apiInstance.bulkDeleteAudienceSegments(cgAudienceSegmentBulkDeleteInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#bulkDeleteAudienceSegments");
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
| **cgAudienceSegmentBulkDeleteInputV1** | [**CgAudienceSegmentBulkDeleteInputV1**](CgAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**CgAudienceSegmentIdEntityV1ListResponse**](CgAudienceSegmentIdEntityV1ListResponse.md)

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

> CgAudienceSegmentEntityV1ListResponse bulkUpdateAudienceSegments(cgAudienceSegmentBulkUpdateInputV1)

/preview/commerce-grid/audience-segments

Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        CgAudienceSegmentBulkUpdateInputV1 cgAudienceSegmentBulkUpdateInputV1 = new CgAudienceSegmentBulkUpdateInputV1(); // CgAudienceSegmentBulkUpdateInputV1 | Segment Update request
        try {
            CgAudienceSegmentEntityV1ListResponse result = apiInstance.bulkUpdateAudienceSegments(cgAudienceSegmentBulkUpdateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#bulkUpdateAudienceSegments");
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
| **cgAudienceSegmentBulkUpdateInputV1** | [**CgAudienceSegmentBulkUpdateInputV1**](CgAudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**CgAudienceSegmentEntityV1ListResponse**](CgAudienceSegmentEntityV1ListResponse.md)

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

/preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear

Delete all identifiers from a Commerce Grid audience segment of type Contact List.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        String audienceSegmentId = "audienceSegmentId_example"; // String | The ID of the audience segment of type contact list to amend
        try {
            apiInstance.clearContactListByAudienceSegment(audienceSegmentId);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#clearContactListByAudienceSegment");
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
| **audienceSegmentId** | **String**| The ID of the audience segment of type contact list to amend | |

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

> CgContactListStatisticsEntityV1Response getAudienceSegmentContactListStatistics(audienceSegmentId)

/preview/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics

Returns the statistics of a contact list segment.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        String audienceSegmentId = "audienceSegmentId_example"; // String | The segment ID.
        try {
            CgContactListStatisticsEntityV1Response result = apiInstance.getAudienceSegmentContactListStatistics(audienceSegmentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#getAudienceSegmentContactListStatistics");
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
| **audienceSegmentId** | **String**| The segment ID. | |

### Return type

[**CgContactListStatisticsEntityV1Response**](CgContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchAudienceSegments

> CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse searchAudienceSegments(cgAudienceSegmentSearchInputV1, limit, offset)

/preview/commerce-grid/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.commercegrid.preview;

import com.criteo.api.commercegrid.preview.ApiClient;
import com.criteo.api.commercegrid.preview.ApiClientBuilder;
import com.criteo.api.commercegrid.preview.ApiException;
import com.criteo.api.commercegrid.preview.Configuration;
import com.criteo.api.commercegrid.preview.auth.*;
import com.criteo.api.commercegrid.preview.model.*;
import com.criteo.api.commercegrid.preview.api.SegmentApi;

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

        SegmentApi apiInstance = new SegmentApi(defaultClient);
        CgAudienceSegmentSearchInputV1 cgAudienceSegmentSearchInputV1 = new CgAudienceSegmentSearchInputV1(); // CgAudienceSegmentSearchInputV1 | 
        Integer limit = 50; // Integer | The number of elements to be returned. The default is 50 and the maximum is 100.
        Integer offset = 0; // Integer | The (zero-based) offset into the collection. The default is 0.
        try {
            CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse result = apiInstance.searchAudienceSegments(cgAudienceSegmentSearchInputV1, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling SegmentApi#searchAudienceSegments");
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
| **cgAudienceSegmentSearchInputV1** | [**CgAudienceSegmentSearchInputV1**](CgAudienceSegmentSearchInputV1.md)|  | |
| **limit** | **Integer**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] [default to 50] |
| **offset** | **Integer**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse**](CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

