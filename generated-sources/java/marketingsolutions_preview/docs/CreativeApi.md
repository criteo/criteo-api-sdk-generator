# CreativeApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdvertiserAd**](CreativeApi.md#createAdvertiserAd) | **POST** /preview/advertisers/{advertiser-id}/ads | /preview/advertisers/{advertiser-id}/ads |
| [**createAdvertiserCoupon**](CreativeApi.md#createAdvertiserCoupon) | **POST** /preview/advertisers/{advertiser-id}/coupons | /preview/advertisers/{advertiser-id}/coupons |
| [**createAdvertiserCreative**](CreativeApi.md#createAdvertiserCreative) | **POST** /preview/advertisers/{advertiser-id}/creatives | /preview/advertisers/{advertiser-id}/creatives |
| [**deleteAd**](CreativeApi.md#deleteAd) | **DELETE** /preview/ads/{id} | /preview/ads/{id} |
| [**deleteAdSegmentLink**](CreativeApi.md#deleteAdSegmentLink) | **DELETE** /preview/marketing-solutions/ads/{ad-id}/audience-segment | /preview/marketing-solutions/ads/{ad-id}/audience-segment |
| [**deleteAdvertiserCoupon**](CreativeApi.md#deleteAdvertiserCoupon) | **DELETE** /preview/advertisers/{advertiser-id}/coupons/{id} | /preview/advertisers/{advertiser-id}/coupons/{id} |
| [**deleteCreative**](CreativeApi.md#deleteCreative) | **DELETE** /preview/creatives/{id} | /preview/creatives/{id} |
| [**editAdvertiserCoupon**](CreativeApi.md#editAdvertiserCoupon) | **PUT** /preview/advertisers/{advertiser-id}/coupons/{id} | /preview/advertisers/{advertiser-id}/coupons/{id} |
| [**editCreative**](CreativeApi.md#editCreative) | **PUT** /preview/creatives/{id} | /preview/creatives/{id} |
| [**generateCreativePreview**](CreativeApi.md#generateCreativePreview) | **POST** /preview/creatives/{id}/preview | /preview/creatives/{id}/preview |
| [**getAd**](CreativeApi.md#getAd) | **GET** /preview/ads/{id} | /preview/ads/{id} |
| [**getAdSegmentLink**](CreativeApi.md#getAdSegmentLink) | **GET** /preview/marketing-solutions/ads/{ad-id}/audience-segment | /preview/marketing-solutions/ads/{ad-id}/audience-segment |
| [**getAdvertiserAds**](CreativeApi.md#getAdvertiserAds) | **GET** /preview/advertisers/{advertiser-id}/ads | /preview/advertisers/{advertiser-id}/ads |
| [**getAdvertiserCoupon**](CreativeApi.md#getAdvertiserCoupon) | **GET** /preview/advertisers/{advertiser-id}/coupons/{id} | /preview/advertisers/{advertiser-id}/coupons/{id} |
| [**getAdvertiserCouponPreview**](CreativeApi.md#getAdvertiserCouponPreview) | **GET** /preview/advertisers/{advertiser-id}/coupons/{id}/preview | /preview/advertisers/{advertiser-id}/coupons/{id}/preview |
| [**getAdvertiserCouponSupportedSizes**](CreativeApi.md#getAdvertiserCouponSupportedSizes) | **GET** /preview/advertisers/{advertiser-id}/coupons-supported-sizes | /preview/advertisers/{advertiser-id}/coupons-supported-sizes |
| [**getAdvertiserCoupons**](CreativeApi.md#getAdvertiserCoupons) | **GET** /preview/advertisers/{advertiser-id}/coupons | /preview/advertisers/{advertiser-id}/coupons |
| [**getAdvertiserCreatives**](CreativeApi.md#getAdvertiserCreatives) | **GET** /preview/advertisers/{advertiser-id}/creatives | /preview/advertisers/{advertiser-id}/creatives |
| [**getCreative**](CreativeApi.md#getCreative) | **GET** /preview/creatives/{id} | /preview/creatives/{id} |
| [**linkAdSegment**](CreativeApi.md#linkAdSegment) | **PUT** /preview/marketing-solutions/ads/{ad-id}/audience-segment | /preview/marketing-solutions/ads/{ad-id}/audience-segment |



## createAdvertiserAd

> ResourceOutcomeOfAd createAdvertiserAd(advertiserId, resourceInputOfAdWrite)

/preview/advertisers/{advertiser-id}/ads

Create an Ad

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        ResourceInputOfAdWrite resourceInputOfAdWrite = new ResourceInputOfAdWrite(); // ResourceInputOfAdWrite | 
        try {
            ResourceOutcomeOfAd result = apiInstance.createAdvertiserAd(advertiserId, resourceInputOfAdWrite);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#createAdvertiserAd");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **resourceInputOfAdWrite** | [**ResourceInputOfAdWrite**](ResourceInputOfAdWrite.md)|  | |

### Return type

[**ResourceOutcomeOfAd**](ResourceOutcomeOfAd.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created Ad is returned. |  -  |


## createAdvertiserCoupon

> ResourceOutcomeOfCoupon createAdvertiserCoupon(advertiserId, resourceInputOfCreateCoupon)

/preview/advertisers/{advertiser-id}/coupons

Create a Coupon

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        ResourceInputOfCreateCoupon resourceInputOfCreateCoupon = new ResourceInputOfCreateCoupon(); // ResourceInputOfCreateCoupon | 
        try {
            ResourceOutcomeOfCoupon result = apiInstance.createAdvertiserCoupon(advertiserId, resourceInputOfCreateCoupon);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#createAdvertiserCoupon");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **resourceInputOfCreateCoupon** | [**ResourceInputOfCreateCoupon**](ResourceInputOfCreateCoupon.md)|  | |

### Return type

[**ResourceOutcomeOfCoupon**](ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created Coupon is returned. |  -  |


## createAdvertiserCreative

> ResourceOutcomeOfCreative createAdvertiserCreative(advertiserId, resourceInputOfCreativeWrite)

/preview/advertisers/{advertiser-id}/creatives

Create a Creative

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        ResourceInputOfCreativeWrite resourceInputOfCreativeWrite = new ResourceInputOfCreativeWrite(); // ResourceInputOfCreativeWrite | 
        try {
            ResourceOutcomeOfCreative result = apiInstance.createAdvertiserCreative(advertiserId, resourceInputOfCreativeWrite);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#createAdvertiserCreative");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **resourceInputOfCreativeWrite** | [**ResourceInputOfCreativeWrite**](ResourceInputOfCreativeWrite.md)|  | |

### Return type

[**ResourceOutcomeOfCreative**](ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created creative is returned. |  -  |


## deleteAd

> deleteAd(id)

/preview/ads/{id}

Delete an Ad

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String id = "id_example"; // String | The ad identifier to delete.
        try {
            apiInstance.deleteAd(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#deleteAd");
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
| **id** | **String**| The ad identifier to delete. | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The ad was deleted. |  -  |


## deleteAdSegmentLink

> deleteAdSegmentLink(adId)

/preview/marketing-solutions/ads/{ad-id}/audience-segment

Delete the link between an Ad and an Audience Segment.

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String adId = "adId_example"; // String | The ad identifier.
        try {
            apiInstance.deleteAdSegmentLink(adId);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#deleteAdSegmentLink");
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
| **adId** | **String**| The ad identifier. | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The link between the ad and its audience segment has been deleted. |  -  |


## deleteAdvertiserCoupon

> deleteAdvertiserCoupon(advertiserId, id)

/preview/advertisers/{advertiser-id}/coupons/{id}

Delete a Coupon

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        String id = "id_example"; // String | The Coupon identifier to delete.
        try {
            apiInstance.deleteAdvertiserCoupon(advertiserId, id);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#deleteAdvertiserCoupon");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **id** | **String**| The Coupon identifier to delete. | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The Coupon was deleted. |  -  |


## deleteCreative

> deleteCreative(id)

/preview/creatives/{id}

Delete a Creative if there are no ads binded to it

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String id = "id_example"; // String | The creative identifier to delete.
        try {
            apiInstance.deleteCreative(id);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#deleteCreative");
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
| **id** | **String**| The creative identifier to delete. | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The creative was deleted. |  -  |


## editAdvertiserCoupon

> ResourceOutcomeOfCoupon editAdvertiserCoupon(advertiserId, id, resourceInputOfUpdateCoupon)

/preview/advertisers/{advertiser-id}/coupons/{id}

Edit a specific Coupon

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        String id = "id_example"; // String | The Coupon identifier to edit.
        ResourceInputOfUpdateCoupon resourceInputOfUpdateCoupon = new ResourceInputOfUpdateCoupon(); // ResourceInputOfUpdateCoupon | 
        try {
            ResourceOutcomeOfCoupon result = apiInstance.editAdvertiserCoupon(advertiserId, id, resourceInputOfUpdateCoupon);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#editAdvertiserCoupon");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **id** | **String**| The Coupon identifier to edit. | |
| **resourceInputOfUpdateCoupon** | [**ResourceInputOfUpdateCoupon**](ResourceInputOfUpdateCoupon.md)|  | |

### Return type

[**ResourceOutcomeOfCoupon**](ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The edited Coupon is returned. |  -  |


## editCreative

> ResourceOutcomeOfCreative editCreative(id, resourceInputOfCreativeWrite)

/preview/creatives/{id}

Edit a specific Creative

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String id = "id_example"; // String | The creative identifier to edit.
        ResourceInputOfCreativeWrite resourceInputOfCreativeWrite = new ResourceInputOfCreativeWrite(); // ResourceInputOfCreativeWrite | 
        try {
            ResourceOutcomeOfCreative result = apiInstance.editCreative(id, resourceInputOfCreativeWrite);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#editCreative");
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
| **id** | **String**| The creative identifier to edit. | |
| **resourceInputOfCreativeWrite** | [**ResourceInputOfCreativeWrite**](ResourceInputOfCreativeWrite.md)|  | |

### Return type

[**ResourceOutcomeOfCreative**](ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The edited creative is returned. |  -  |


## generateCreativePreview

> String generateCreativePreview(id, height, width)

/preview/creatives/{id}/preview

Get the preview of a specific Creative

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String id = "id_example"; // String | The Creative identifier to preview.
        Integer height = 56; // Integer | The height of the Creative to preview.
        Integer width = 56; // Integer | The width of the Creative to preview.
        try {
            String result = apiInstance.generateCreativePreview(id, height, width);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#generateCreativePreview");
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
| **id** | **String**| The Creative identifier to preview. | |
| **height** | **Integer**| The height of the Creative to preview. | [optional] |
| **width** | **Integer**| The width of the Creative to preview. | [optional] |

### Return type

**String**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The preview HTML of a specific Creative is returned. |  -  |


## getAd

> ResourceOutcomeOfAd getAd(id)

/preview/ads/{id}

Get an Ad with its id

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String id = "id_example"; // String | The ad identifier to retrieve.
        try {
            ResourceOutcomeOfAd result = apiInstance.getAd(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAd");
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
| **id** | **String**| The ad identifier to retrieve. | |

### Return type

[**ResourceOutcomeOfAd**](ResourceOutcomeOfAd.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found ad is returned. |  -  |


## getAdSegmentLink

> ValueResourceOutcomeOfExamAdAudienceSegmentLink getAdSegmentLink(adId)

/preview/marketing-solutions/ads/{ad-id}/audience-segment

Retrieve the Ad audience segment link.

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String adId = "adId_example"; // String | The ad identifier.
        try {
            ValueResourceOutcomeOfExamAdAudienceSegmentLink result = apiInstance.getAdSegmentLink(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdSegmentLink");
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
| **adId** | **String**| The ad identifier. | |

### Return type

[**ValueResourceOutcomeOfExamAdAudienceSegmentLink**](ValueResourceOutcomeOfExamAdAudienceSegmentLink.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found ad audience segment link is returned. |  -  |


## getAdvertiserAds

> ResourceCollectionOutcomeOfAd getAdvertiserAds(advertiserId, limit, offset)

/preview/advertisers/{advertiser-id}/ads

Get the list of self-services Ads for a given advertiser

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        Integer limit = 56; // Integer | The number of ads to be returned. The default is 50.
        Integer offset = 56; // Integer | The (zero-based) offset into the collection of ads. The default is 0.
        try {
            ResourceCollectionOutcomeOfAd result = apiInstance.getAdvertiserAds(advertiserId, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdvertiserAds");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **limit** | **Integer**| The number of ads to be returned. The default is 50. | [optional] |
| **offset** | **Integer**| The (zero-based) offset into the collection of ads. The default is 0. | [optional] |

### Return type

[**ResourceCollectionOutcomeOfAd**](ResourceCollectionOutcomeOfAd.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of self-services Ads is returned. |  -  |


## getAdvertiserCoupon

> ResourceOutcomeOfCoupon getAdvertiserCoupon(advertiserId, id)

/preview/advertisers/{advertiser-id}/coupons/{id}

Get a Coupon with its id

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        String id = "id_example"; // String | The Coupon identifier to retrieve.
        try {
            ResourceOutcomeOfCoupon result = apiInstance.getAdvertiserCoupon(advertiserId, id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdvertiserCoupon");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **id** | **String**| The Coupon identifier to retrieve. | |

### Return type

[**ResourceOutcomeOfCoupon**](ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found Coupon is returned. |  -  |


## getAdvertiserCouponPreview

> String getAdvertiserCouponPreview(advertiserId, id, height, width)

/preview/advertisers/{advertiser-id}/coupons/{id}/preview

Get the preview of a specific Coupon

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        String id = "id_example"; // String | The Coupon identifier to preview.
        Integer height = 56; // Integer | The height of the coupon to preview.
        Integer width = 56; // Integer | The width of the coupon to preview.
        try {
            String result = apiInstance.getAdvertiserCouponPreview(advertiserId, id, height, width);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdvertiserCouponPreview");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **id** | **String**| The Coupon identifier to preview. | |
| **height** | **Integer**| The height of the coupon to preview. | [optional] |
| **width** | **Integer**| The width of the coupon to preview. | [optional] |

### Return type

**String**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The preview HTML of a specific Coupon is returned. |  -  |


## getAdvertiserCouponSupportedSizes

> ResourceOutcomeOfCouponSupportedSizes getAdvertiserCouponSupportedSizes(advertiserId, adSetId)

/preview/advertisers/{advertiser-id}/coupons-supported-sizes

Get the list of Coupon supported sizes

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        String adSetId = "adSetId_example"; // String | The ad set id on which you want to check the Coupon supported sizes.
        try {
            ResourceOutcomeOfCouponSupportedSizes result = apiInstance.getAdvertiserCouponSupportedSizes(advertiserId, adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdvertiserCouponSupportedSizes");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **adSetId** | **String**| The ad set id on which you want to check the Coupon supported sizes. | [optional] |

### Return type

[**ResourceOutcomeOfCouponSupportedSizes**](ResourceOutcomeOfCouponSupportedSizes.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of Coupon supported sizes is returned. |  -  |


## getAdvertiserCoupons

> ResourceCollectionOutcomeOfCoupon getAdvertiserCoupons(advertiserId, limit, offset)

/preview/advertisers/{advertiser-id}/coupons

Get the list of self-services Coupons for a given advertiser

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        Integer limit = 56; // Integer | The number of coupons to be returned. The default is 50.
        Integer offset = 56; // Integer | The (zero-based) offset into the collection of coupons. The default is 0.
        try {
            ResourceCollectionOutcomeOfCoupon result = apiInstance.getAdvertiserCoupons(advertiserId, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdvertiserCoupons");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **limit** | **Integer**| The number of coupons to be returned. The default is 50. | [optional] |
| **offset** | **Integer**| The (zero-based) offset into the collection of coupons. The default is 0. | [optional] |

### Return type

[**ResourceCollectionOutcomeOfCoupon**](ResourceCollectionOutcomeOfCoupon.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of self-services Coupons is returned. |  -  |


## getAdvertiserCreatives

> ResourceCollectionOutcomeOfCreativeRead getAdvertiserCreatives(advertiserId, limit, offset)

/preview/advertisers/{advertiser-id}/creatives

Get the list of self-services Creatives for a given advertiser

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser identifier.
        Integer limit = 56; // Integer | The number of creatives to be returned. The default is 50.
        Integer offset = 56; // Integer | The (zero-based) offset into the collection of creatives. The default is 0.
        try {
            ResourceCollectionOutcomeOfCreativeRead result = apiInstance.getAdvertiserCreatives(advertiserId, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getAdvertiserCreatives");
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
| **advertiserId** | **String**| The advertiser identifier. | |
| **limit** | **Integer**| The number of creatives to be returned. The default is 50. | [optional] |
| **offset** | **Integer**| The (zero-based) offset into the collection of creatives. The default is 0. | [optional] |

### Return type

[**ResourceCollectionOutcomeOfCreativeRead**](ResourceCollectionOutcomeOfCreativeRead.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of self-services Creatives is returned.This list will contain creatives in draft status as well which will have some properties as null |  -  |


## getCreative

> ResourceOutcomeOfCreative getCreative(id)

/preview/creatives/{id}

Get a Creative with its id

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String id = "id_example"; // String | The creative identifier to retrieve.
        try {
            ResourceOutcomeOfCreative result = apiInstance.getCreative(id);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#getCreative");
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
| **id** | **String**| The creative identifier to retrieve. | |

### Return type

[**ResourceOutcomeOfCreative**](ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The found creative is returned. |  -  |


## linkAdSegment

> ValueResourceOutcomeOfExamAdAudienceSegmentLink linkAdSegment(adId, examAdAudienceSegmentLinkInput)

/preview/marketing-solutions/ads/{ad-id}/audience-segment

Link an Ad with an Audience Segment. If a link already exists, its segment ID will be updated.

### Example

```java
package com.criteo.api.marketingsolutions.preview;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.auth.*;
import com.criteo.api.marketingsolutions.preview.model.*;
import com.criteo.api.marketingsolutions.preview.api.CreativeApi;

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

        CreativeApi apiInstance = new CreativeApi(defaultClient);
        String adId = "adId_example"; // String | The ad identifier.
        ExamAdAudienceSegmentLinkInput examAdAudienceSegmentLinkInput = new ExamAdAudienceSegmentLinkInput(); // ExamAdAudienceSegmentLinkInput | The audience segment link information.
        try {
            ValueResourceOutcomeOfExamAdAudienceSegmentLink result = apiInstance.linkAdSegment(adId, examAdAudienceSegmentLinkInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CreativeApi#linkAdSegment");
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
| **adId** | **String**| The ad identifier. | |
| **examAdAudienceSegmentLinkInput** | [**ExamAdAudienceSegmentLinkInput**](ExamAdAudienceSegmentLinkInput.md)| The audience segment link information. | |

### Return type

[**ValueResourceOutcomeOfExamAdAudienceSegmentLink**](ValueResourceOutcomeOfExamAdAudienceSegmentLink.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The link between the Ad and the Audience Segment is returned. |  -  |

