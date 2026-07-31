# AudienceApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeAudienceSegmentsSizes**](AudienceApi.md#computeAudienceSegmentsSizes) | **POST** /experimental/marketing-solutions/audience-segments/compute-sizes | /experimental/marketing-solutions/audience-segments/compute-sizes |
| [**computeAudiencesSizes**](AudienceApi.md#computeAudiencesSizes) | **POST** /experimental/marketing-solutions/audiences/compute-sizes | /experimental/marketing-solutions/audiences/compute-sizes |
| [**createAudienceSegments**](AudienceApi.md#createAudienceSegments) | **POST** /experimental/marketing-solutions/audience-segments/create | /experimental/marketing-solutions/audience-segments/create |
| [**createAudiences**](AudienceApi.md#createAudiences) | **POST** /experimental/marketing-solutions/audiences/create | /experimental/marketing-solutions/audiences/create |
| [**deleteAudienceSegments**](AudienceApi.md#deleteAudienceSegments) | **POST** /experimental/marketing-solutions/audience-segments/delete | /experimental/marketing-solutions/audience-segments/delete |
| [**deleteAudiences**](AudienceApi.md#deleteAudiences) | **POST** /experimental/marketing-solutions/audiences/delete | /experimental/marketing-solutions/audiences/delete |
| [**deleteContactListByAudienceSegment**](AudienceApi.md#deleteContactListByAudienceSegment) | **DELETE** /experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list | /experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list |
| [**estimateAudienceSegmentsSizes**](AudienceApi.md#estimateAudienceSegmentsSizes) | **POST** /experimental/marketing-solutions/audience-segments/estimate-size | /experimental/marketing-solutions/audience-segments/estimate-size |
| [**estimateAudiencesSizes**](AudienceApi.md#estimateAudiencesSizes) | **POST** /experimental/marketing-solutions/audiences/estimate-size | /experimental/marketing-solutions/audiences/estimate-size |
| [**getAudienceSegmentContactListStatistics**](AudienceApi.md#getAudienceSegmentContactListStatistics) | **GET** /experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics | /experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics |
| [**getAudienceSegmentsInMarketBrands**](AudienceApi.md#getAudienceSegmentsInMarketBrands) | **GET** /experimental/marketing-solutions/audience-segments/in-market-brands | /experimental/marketing-solutions/audience-segments/in-market-brands |
| [**getAudienceSegmentsInMarketInterests**](AudienceApi.md#getAudienceSegmentsInMarketInterests) | **GET** /experimental/marketing-solutions/audience-segments/in-market-interests | /experimental/marketing-solutions/audience-segments/in-market-interests |
| [**modifyAudienceUsersWithAttributes**](AudienceApi.md#modifyAudienceUsersWithAttributes) | **PATCH** /experimental/marketing-solutions/audiences/{audience-id}/contactlist-attributes | /experimental/marketing-solutions/audiences/{audience-id}/contactlist-attributes |
| [**searchAudienceSegments**](AudienceApi.md#searchAudienceSegments) | **POST** /experimental/marketing-solutions/audience-segments/search | /experimental/marketing-solutions/audience-segments/search |
| [**searchAudiences**](AudienceApi.md#searchAudiences) | **POST** /experimental/marketing-solutions/audiences/search | /experimental/marketing-solutions/audiences/search |
| [**updateAudienceSegments**](AudienceApi.md#updateAudienceSegments) | **PATCH** /experimental/marketing-solutions/audience-segments | /experimental/marketing-solutions/audience-segments |
| [**updateAudiences**](AudienceApi.md#updateAudiences) | **PATCH** /experimental/marketing-solutions/audiences | /experimental/marketing-solutions/audiences |
| [**updateContactListByAudienceSegment**](AudienceApi.md#updateContactListByAudienceSegment) | **PATCH** /experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list | /experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list |



## computeAudienceSegmentsSizes

> AudienceSegmentSizeEntityV1ListResponse computeAudienceSegmentsSizes(audienceSegmentComputeSizesInputV1)

/experimental/marketing-solutions/audience-segments/compute-sizes

Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSegmentComputeSizesInputV1 audienceSegmentComputeSizesInputV1 = new AudienceSegmentComputeSizesInputV1(); // AudienceSegmentComputeSizesInputV1 | 
        try {
            AudienceSegmentSizeEntityV1ListResponse result = apiInstance.computeAudienceSegmentsSizes(audienceSegmentComputeSizesInputV1);
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
| **audienceSegmentComputeSizesInputV1** | [**AudienceSegmentComputeSizesInputV1**](AudienceSegmentComputeSizesInputV1.md)|  | |

### Return type

[**AudienceSegmentSizeEntityV1ListResponse**](AudienceSegmentSizeEntityV1ListResponse.md)

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

> AudienceSizeEntityV1ListResponse computeAudiencesSizes(audienceComputeSizesInputV1)

/experimental/marketing-solutions/audiences/compute-sizes

Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceComputeSizesInputV1 audienceComputeSizesInputV1 = new AudienceComputeSizesInputV1(); // AudienceComputeSizesInputV1 | 
        try {
            AudienceSizeEntityV1ListResponse result = apiInstance.computeAudiencesSizes(audienceComputeSizesInputV1);
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
| **audienceComputeSizesInputV1** | [**AudienceComputeSizesInputV1**](AudienceComputeSizesInputV1.md)|  | |

### Return type

[**AudienceSizeEntityV1ListResponse**](AudienceSizeEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## createAudienceSegments

> AudienceSegmentEntityV1ListResponse createAudienceSegments(audienceSegmentBulkCreateInputV1)

/experimental/marketing-solutions/audience-segments/create

Creates all segments with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSegmentBulkCreateInputV1 audienceSegmentBulkCreateInputV1 = new AudienceSegmentBulkCreateInputV1(); // AudienceSegmentBulkCreateInputV1 | Segment creation parameter
        try {
            AudienceSegmentEntityV1ListResponse result = apiInstance.createAudienceSegments(audienceSegmentBulkCreateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#createAudienceSegments");
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
| **audienceSegmentBulkCreateInputV1** | [**AudienceSegmentBulkCreateInputV1**](AudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**AudienceSegmentEntityV1ListResponse**](AudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## createAudiences

> AudienceEntityV1ListResponse createAudiences(audienceBulkCreateInputV1)

/experimental/marketing-solutions/audiences/create

Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceBulkCreateInputV1 audienceBulkCreateInputV1 = new AudienceBulkCreateInputV1(); // AudienceBulkCreateInputV1 | 
        try {
            AudienceEntityV1ListResponse result = apiInstance.createAudiences(audienceBulkCreateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#createAudiences");
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
| **audienceBulkCreateInputV1** | [**AudienceBulkCreateInputV1**](AudienceBulkCreateInputV1.md)|  | |

### Return type

[**AudienceEntityV1ListResponse**](AudienceEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## deleteAudienceSegments

> AudienceSegmentIdEntityV1ListResponse deleteAudienceSegments(audienceSegmentBulkDeleteInputV1)

/experimental/marketing-solutions/audience-segments/delete

Delete the segments associated to the given audience IDs.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSegmentBulkDeleteInputV1 audienceSegmentBulkDeleteInputV1 = new AudienceSegmentBulkDeleteInputV1(); // AudienceSegmentBulkDeleteInputV1 | Segment delete request.
        try {
            AudienceSegmentIdEntityV1ListResponse result = apiInstance.deleteAudienceSegments(audienceSegmentBulkDeleteInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#deleteAudienceSegments");
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
| **audienceSegmentBulkDeleteInputV1** | [**AudienceSegmentBulkDeleteInputV1**](AudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**AudienceSegmentIdEntityV1ListResponse**](AudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## deleteAudiences

> AudienceIdEntityV1ListResponse deleteAudiences(audienceBulkDeleteInputV1)

/experimental/marketing-solutions/audiences/delete

Deletes the audiences associated to the given audience IDs.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceBulkDeleteInputV1 audienceBulkDeleteInputV1 = new AudienceBulkDeleteInputV1(); // AudienceBulkDeleteInputV1 | 
        try {
            AudienceIdEntityV1ListResponse result = apiInstance.deleteAudiences(audienceBulkDeleteInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#deleteAudiences");
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
| **audienceBulkDeleteInputV1** | [**AudienceBulkDeleteInputV1**](AudienceBulkDeleteInputV1.md)|  | |

### Return type

[**AudienceIdEntityV1ListResponse**](AudienceIdEntityV1ListResponse.md)

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


## deleteContactListByAudienceSegment

> DeleteAudienceContactListResponse deleteContactListByAudienceSegment(audienceSegmentId)

/experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list

Delete all identifiers from a contact list audience-segment.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        String audienceSegmentId = "audienceSegmentId_example"; // String | The id of the contact list audience-segment to amend
        try {
            DeleteAudienceContactListResponse result = apiInstance.deleteContactListByAudienceSegment(audienceSegmentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#deleteContactListByAudienceSegment");
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
| **audienceSegmentId** | **String**| The id of the contact list audience-segment to amend | |

### Return type

[**DeleteAudienceContactListResponse**](DeleteAudienceContactListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Contact List was emptied |  -  |


## estimateAudienceSegmentsSizes

> AudienceSegmentSizeEstimationV1Response estimateAudienceSegmentsSizes(audienceSegmentEstimateSizeInputV1)

/experimental/marketing-solutions/audience-segments/estimate-size

Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSegmentEstimateSizeInputV1 audienceSegmentEstimateSizeInputV1 = new AudienceSegmentEstimateSizeInputV1(); // AudienceSegmentEstimateSizeInputV1 | 
        try {
            AudienceSegmentSizeEstimationV1Response result = apiInstance.estimateAudienceSegmentsSizes(audienceSegmentEstimateSizeInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#estimateAudienceSegmentsSizes");
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
| **audienceSegmentEstimateSizeInputV1** | [**AudienceSegmentEstimateSizeInputV1**](AudienceSegmentEstimateSizeInputV1.md)|  | |

### Return type

[**AudienceSegmentSizeEstimationV1Response**](AudienceSegmentSizeEstimationV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## estimateAudiencesSizes

> AudienceSizeEstimationV1Response estimateAudiencesSizes(audienceEstimateSizeInputV1)

/experimental/marketing-solutions/audiences/estimate-size

Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceEstimateSizeInputV1 audienceEstimateSizeInputV1 = new AudienceEstimateSizeInputV1(); // AudienceEstimateSizeInputV1 | 
        try {
            AudienceSizeEstimationV1Response result = apiInstance.estimateAudiencesSizes(audienceEstimateSizeInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#estimateAudiencesSizes");
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
| **audienceEstimateSizeInputV1** | [**AudienceEstimateSizeInputV1**](AudienceEstimateSizeInputV1.md)|  | |

### Return type

[**AudienceSizeEstimationV1Response**](AudienceSizeEstimationV1Response.md)

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

> ContactListStatisticsEntityV1Response getAudienceSegmentContactListStatistics(audienceSegmentId)

/experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics

Returns the statistics of a contact list segment.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        String audienceSegmentId = "audienceSegmentId_example"; // String | The segment ID.
        try {
            ContactListStatisticsEntityV1Response result = apiInstance.getAudienceSegmentContactListStatistics(audienceSegmentId);
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
| **audienceSegmentId** | **String**| The segment ID. | |

### Return type

[**ContactListStatisticsEntityV1Response**](ContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAudienceSegmentsInMarketBrands

> InMarketAudienceSegmentBrandEntityV1ListResponse getAudienceSegmentsInMarketBrands(advertiserId, country)

/experimental/marketing-solutions/audience-segments/in-market-brands

Returns a list with all available in-market brands that can be used to define an in-market segment.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        String advertiserId = "advertiserId_example"; // String | The advertiser ID.
        String country = "country_example"; // String | The ISO 3166-1 alpha-2 country code.
        try {
            InMarketAudienceSegmentBrandEntityV1ListResponse result = apiInstance.getAudienceSegmentsInMarketBrands(advertiserId, country);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#getAudienceSegmentsInMarketBrands");
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
| **advertiserId** | **String**| The advertiser ID. | |
| **country** | **String**| The ISO 3166-1 alpha-2 country code. | |

### Return type

[**InMarketAudienceSegmentBrandEntityV1ListResponse**](InMarketAudienceSegmentBrandEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAudienceSegmentsInMarketInterests

> InMarketAudienceSegmentInterestEntityV1ListResponse getAudienceSegmentsInMarketInterests(advertiserId, country)

/experimental/marketing-solutions/audience-segments/in-market-interests

Returns a list with all available in-market interests that can be used to define an in-market segment. These in-market interests correspond to the Google product taxonomy.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        String advertiserId = "advertiserId_example"; // String | The advertiser ID.
        String country = "country_example"; // String | The ISO 3166-1 alpha-2 country code.
        try {
            InMarketAudienceSegmentInterestEntityV1ListResponse result = apiInstance.getAudienceSegmentsInMarketInterests(advertiserId, country);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#getAudienceSegmentsInMarketInterests");
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
| **advertiserId** | **String**| The advertiser ID. | |
| **country** | **String**| The ISO 3166-1 alpha-2 country code. | |

### Return type

[**InMarketAudienceSegmentInterestEntityV1ListResponse**](InMarketAudienceSegmentInterestEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## modifyAudienceUsersWithAttributes

> ModifyAudienceResponse modifyAudienceUsersWithAttributes(audienceId, contactlistWithAttributesAmendmentRequest)

/experimental/marketing-solutions/audiences/{audience-id}/contactlist-attributes

Add/remove identifiers to or from a contact list.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        String audienceId = "audienceId_example"; // String | The id of the contact list audience-segment to amend
        ContactlistWithAttributesAmendmentRequest contactlistWithAttributesAmendmentRequest = new ContactlistWithAttributesAmendmentRequest(); // ContactlistWithAttributesAmendmentRequest | 
        try {
            ModifyAudienceResponse result = apiInstance.modifyAudienceUsersWithAttributes(audienceId, contactlistWithAttributesAmendmentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#modifyAudienceUsersWithAttributes");
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
| **audienceId** | **String**| The id of the contact list audience-segment to amend | |
| **contactlistWithAttributesAmendmentRequest** | [**ContactlistWithAttributesAmendmentRequest**](ContactlistWithAttributesAmendmentRequest.md)|  | |

### Return type

[**ModifyAudienceResponse**](ModifyAudienceResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of created request |  -  |


## searchAudienceSegments

> AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse searchAudienceSegments(audienceSegmentSearchInputV1, limit, offset)

/experimental/marketing-solutions/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSegmentSearchInputV1 audienceSegmentSearchInputV1 = new AudienceSegmentSearchInputV1(); // AudienceSegmentSearchInputV1 | Segment search filters.
        Integer limit = 50; // Integer | The number of elements to be returned. The default is 50 and the maximum is 100.
        Integer offset = 0; // Integer | The (zero-based) offset into the collection. The default is 0.
        try {
            AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse result = apiInstance.searchAudienceSegments(audienceSegmentSearchInputV1, limit, offset);
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
| **audienceSegmentSearchInputV1** | [**AudienceSegmentSearchInputV1**](AudienceSegmentSearchInputV1.md)| Segment search filters. | |
| **limit** | **Integer**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] [default to 50] |
| **offset** | **Integer**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse**](AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchAudiences

> AudienceEntityV1AudienceSearchMetadataV1ListResponse searchAudiences(audienceSearchInputV1, limit, offset)

/experimental/marketing-solutions/audiences/search

Returns a list of audiences that match the provided filters. If present, the filters are AND&#39;ed together when applied.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSearchInputV1 audienceSearchInputV1 = new AudienceSearchInputV1(); // AudienceSearchInputV1 | Audience search filters.
        Integer limit = 50; // Integer | The number of elements to be returned. The default is 50 and the maximum is 100.
        Integer offset = 0; // Integer | The (zero-based) offset into the collection. The default is 0.
        try {
            AudienceEntityV1AudienceSearchMetadataV1ListResponse result = apiInstance.searchAudiences(audienceSearchInputV1, limit, offset);
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
| **audienceSearchInputV1** | [**AudienceSearchInputV1**](AudienceSearchInputV1.md)| Audience search filters. | |
| **limit** | **Integer**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] [default to 50] |
| **offset** | **Integer**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**AudienceEntityV1AudienceSearchMetadataV1ListResponse**](AudienceEntityV1AudienceSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateAudienceSegments

> AudienceSegmentEntityV1ListResponse updateAudienceSegments(audienceSegmentBulkUpdateInputV1)

/experimental/marketing-solutions/audience-segments

Updates the properties of all segments with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceSegmentBulkUpdateInputV1 audienceSegmentBulkUpdateInputV1 = new AudienceSegmentBulkUpdateInputV1(); // AudienceSegmentBulkUpdateInputV1 | Segment Update request
        try {
            AudienceSegmentEntityV1ListResponse result = apiInstance.updateAudienceSegments(audienceSegmentBulkUpdateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#updateAudienceSegments");
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
| **audienceSegmentBulkUpdateInputV1** | [**AudienceSegmentBulkUpdateInputV1**](AudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**AudienceSegmentEntityV1ListResponse**](AudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## updateAudiences

> AudienceEntityV1ListResponse updateAudiences(audienceBulkUpdateInputV1)

/experimental/marketing-solutions/audiences

Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        AudienceBulkUpdateInputV1 audienceBulkUpdateInputV1 = new AudienceBulkUpdateInputV1(); // AudienceBulkUpdateInputV1 | 
        try {
            AudienceEntityV1ListResponse result = apiInstance.updateAudiences(audienceBulkUpdateInputV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#updateAudiences");
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
| **audienceBulkUpdateInputV1** | [**AudienceBulkUpdateInputV1**](AudienceBulkUpdateInputV1.md)|  | |

### Return type

[**AudienceEntityV1ListResponse**](AudienceEntityV1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success or partial success |  -  |


## updateContactListByAudienceSegment

> ModifyAudienceResponse updateContactListByAudienceSegment(audienceSegmentId, contactlistAmendmentRequest)

/experimental/marketing-solutions/audience-segments/{audience-segment-id}/contact-list

Add/remove identifiers to or from a contact list audience-segment.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AudienceApi;

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
        String audienceSegmentId = "audienceSegmentId_example"; // String | The id of the contact list audience-segment to amend
        ContactlistAmendmentRequest contactlistAmendmentRequest = new ContactlistAmendmentRequest(); // ContactlistAmendmentRequest | 
        try {
            ModifyAudienceResponse result = apiInstance.updateContactListByAudienceSegment(audienceSegmentId, contactlistAmendmentRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AudienceApi#updateContactListByAudienceSegment");
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
| **audienceSegmentId** | **String**| The id of the contact list audience-segment to amend | |
| **contactlistAmendmentRequest** | [**ContactlistAmendmentRequest**](ContactlistAmendmentRequest.md)|  | |

### Return type

[**ModifyAudienceResponse**](ModifyAudienceResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of created request |  -  |

