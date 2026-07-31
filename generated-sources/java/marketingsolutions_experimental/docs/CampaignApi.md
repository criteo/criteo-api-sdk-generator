# CampaignApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdSet**](CampaignApi.md#createAdSet) | **POST** /experimental/marketing-solutions/ad-sets | /experimental/marketing-solutions/ad-sets |
| [**createCampaign**](CampaignApi.md#createCampaign) | **POST** /experimental/marketing-solutions/campaigns | /experimental/marketing-solutions/campaigns |
| [**deleteAdvertiserBundleRules**](CampaignApi.md#deleteAdvertiserBundleRules) | **DELETE** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**deleteAdvertiserDomainRules**](CampaignApi.md#deleteAdvertiserDomainRules) | **DELETE** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**deleteCampaignBundleRules**](CampaignApi.md#deleteCampaignBundleRules) | **DELETE** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**deleteCampaignDomainRules**](CampaignApi.md#deleteCampaignDomainRules) | **DELETE** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**disableAdSetTargetingDealIds**](CampaignApi.md#disableAdSetTargetingDealIds) | **POST** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable |
| [**disableAdSetTargetingVideoPositioning**](CampaignApi.md#disableAdSetTargetingVideoPositioning) | **POST** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable |
| [**getAdSet**](CampaignApi.md#getAdSet) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id} | /experimental/marketing-solutions/ad-sets/{ad-set-id} |
| [**getAdSetCategoryBids**](CampaignApi.md#getAdSetCategoryBids) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**getAdSetTargetingDealIds**](CampaignApi.md#getAdSetTargetingDealIds) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids |
| [**getAdSetTargetingVideoPositioning**](CampaignApi.md#getAdSetTargetingVideoPositioning) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning |
| [**getAdvertiserBundleRules**](CampaignApi.md#getAdvertiserBundleRules) | **GET** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**getAdvertiserDomainRules**](CampaignApi.md#getAdvertiserDomainRules) | **GET** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**getCampaign**](CampaignApi.md#getCampaign) | **GET** /experimental/marketing-solutions/campaigns/{campaign-id} | /experimental/marketing-solutions/campaigns/{campaign-id} |
| [**getCampaignBundleRules**](CampaignApi.md#getCampaignBundleRules) | **GET** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**getCampaignDomainRules**](CampaignApi.md#getCampaignDomainRules) | **GET** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**getDisplayMultipliers**](CampaignApi.md#getDisplayMultipliers) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**getSupplyVendorList**](CampaignApi.md#getSupplyVendorList) | **GET** /experimental/marketing-solutions/ad-sets/targeting/supply-vendors | /experimental/marketing-solutions/ad-sets/targeting/supply-vendors |
| [**patchAdSetCategoryBids**](CampaignApi.md#patchAdSetCategoryBids) | **PATCH** /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**patchAdSets**](CampaignApi.md#patchAdSets) | **PATCH** /experimental/marketing-solutions/ad-sets | /experimental/marketing-solutions/ad-sets |
| [**patchCampaigns**](CampaignApi.md#patchCampaigns) | **PATCH** /experimental/marketing-solutions/campaigns | /experimental/marketing-solutions/campaigns |
| [**patchDisplayMultipliers**](CampaignApi.md#patchDisplayMultipliers) | **PATCH** /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**postAdvertiserBundleRules**](CampaignApi.md#postAdvertiserBundleRules) | **POST** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**postAdvertiserDomainRules**](CampaignApi.md#postAdvertiserDomainRules) | **POST** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**postCampaignBundleRules**](CampaignApi.md#postCampaignBundleRules) | **POST** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**postCampaignDomainRules**](CampaignApi.md#postCampaignDomainRules) | **POST** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**putAdvertiserBundleRules**](CampaignApi.md#putAdvertiserBundleRules) | **PUT** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**putAdvertiserDomainRules**](CampaignApi.md#putAdvertiserDomainRules) | **PUT** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**putCampaignBundleRules**](CampaignApi.md#putCampaignBundleRules) | **PUT** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**putCampaignDomainRules**](CampaignApi.md#putCampaignDomainRules) | **PUT** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**searchAdSets**](CampaignApi.md#searchAdSets) | **POST** /experimental/marketing-solutions/ad-sets/search | /experimental/marketing-solutions/ad-sets/search |
| [**searchCampaigns**](CampaignApi.md#searchCampaigns) | **POST** /experimental/marketing-solutions/campaigns/search | /experimental/marketing-solutions/campaigns/search |
| [**setAdSetTargetingDealIds**](CampaignApi.md#setAdSetTargetingDealIds) | **PUT** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids |
| [**setAdSetTargetingVideoPositioning**](CampaignApi.md#setAdSetTargetingVideoPositioning) | **PUT** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning |
| [**startAdSets**](CampaignApi.md#startAdSets) | **POST** /experimental/marketing-solutions/ad-sets/start | /experimental/marketing-solutions/ad-sets/start |
| [**stopAdSets**](CampaignApi.md#stopAdSets) | **POST** /experimental/marketing-solutions/ad-sets/stop | /experimental/marketing-solutions/ad-sets/stop |
| [**updateAdSetAudience**](CampaignApi.md#updateAdSetAudience) | **PUT** /experimental/marketing-solutions/ad-sets/{ad-set-id}/audience | /experimental/marketing-solutions/ad-sets/{ad-set-id}/audience |



## createAdSet

> ResponseReadAdSetV26Q1 createAdSet(createAdSetV26Q1Request)

/experimental/marketing-solutions/ad-sets

Create an ad set with the provided parameters

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        CreateAdSetV26Q1Request createAdSetV26Q1Request = new CreateAdSetV26Q1Request(); // CreateAdSetV26Q1Request | the ad sets to create
        try {
            ResponseReadAdSetV26Q1 result = apiInstance.createAdSet(createAdSetV26Q1Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createAdSet");
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
| **createAdSetV26Q1Request** | [**CreateAdSetV26Q1Request**](CreateAdSetV26Q1Request.md)| the ad sets to create | |

### Return type

[**ResponseReadAdSetV26Q1**](ResponseReadAdSetV26Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ad set that has been created and errors / warnings |  -  |


## createCampaign

> CampaignV23Q1Response createCampaign(createCampaignRequest)

/experimental/marketing-solutions/campaigns

Create the specified campaign                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        CreateCampaignRequest createCampaignRequest = new CreateCampaignRequest(); // CreateCampaignRequest | the campaigns to create
        try {
            CampaignV23Q1Response result = apiInstance.createCampaign(createCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createCampaign");
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
| **createCampaignRequest** | [**CreateCampaignRequest**](CreateCampaignRequest.md)| the campaigns to create | |

### Return type

[**CampaignV23Q1Response**](CampaignV23Q1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The campaign that has been created and errors / warnings |  -  |


## deleteAdvertiserBundleRules

> ApiResponseOfTargetingEntity deleteAdvertiserBundleRules(advertiserId, apiRequestOfTargetingEntity)

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Removes some bundles from the current list of targeted bundles for a given advertiser.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to delete from the list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.deleteAdvertiserBundleRules(advertiserId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteAdvertiserBundleRules");
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
| **advertiserId** | **String**| The advertiser id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## deleteAdvertiserDomainRules

> ApiResponseOfTargetingEntity deleteAdvertiserDomainRules(advertiserId, apiRequestOfTargetingEntity)

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Removes some domains from the current list of targeted domains for a given advertiser.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to delete from the list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.deleteAdvertiserDomainRules(advertiserId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteAdvertiserDomainRules");
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
| **advertiserId** | **String**| The advertiser id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## deleteCampaignBundleRules

> ApiResponseOfTargetingEntity deleteCampaignBundleRules(campaignId, apiRequestOfTargetingEntity)

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Removes some bundles from the current list of targeted bundles for a given campaign.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to delete from the list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.deleteCampaignBundleRules(campaignId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteCampaignBundleRules");
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
| **campaignId** | **String**| The campaign id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## deleteCampaignDomainRules

> ApiResponseOfTargetingEntity deleteCampaignDomainRules(campaignId, apiRequestOfTargetingEntity)

/experimental/campaigns/{campaignId}/targeting/domain-rules

Removes some domains from the current list of targeted domains for a given campaign.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to delete from the list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.deleteCampaignDomainRules(campaignId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteCampaignDomainRules");
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
| **campaignId** | **String**| The campaign id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## disableAdSetTargetingDealIds

> AdSetTargetingDealIdsDisableResultResponse disableAdSetTargetingDealIds(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable

Disable the Deal Id Targeting configuration for the ad set whose id is specified

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        try {
            AdSetTargetingDealIdsDisableResultResponse result = apiInstance.disableAdSetTargetingDealIds(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#disableAdSetTargetingDealIds");
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
| **adSetId** | **String**| Id of the Ad Set | |

### Return type

[**AdSetTargetingDealIdsDisableResultResponse**](AdSetTargetingDealIdsDisableResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the errors/warnings if any |  -  |


## disableAdSetTargetingVideoPositioning

> AdSetTargetingVideoPositioningDisableResultResponse disableAdSetTargetingVideoPositioning(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable

Disable the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        try {
            AdSetTargetingVideoPositioningDisableResultResponse result = apiInstance.disableAdSetTargetingVideoPositioning(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#disableAdSetTargetingVideoPositioning");
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
| **adSetId** | **String**| Id of the Ad Set | |

### Return type

[**AdSetTargetingVideoPositioningDisableResultResponse**](AdSetTargetingVideoPositioningDisableResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the errors/warnings if any |  -  |


## getAdSet

> ResponseReadAdSetV26Q1 getAdSet(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}

Get the data for the specified ad set

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the ad set
        try {
            ResponseReadAdSetV26Q1 result = apiInstance.getAdSet(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAdSet");
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
| **adSetId** | **String**| Id of the ad set | |

### Return type

[**ResponseReadAdSetV26Q1**](ResponseReadAdSetV26Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | data for the ad set |  -  |


## getAdSetCategoryBids

> AdSetCategoryBidListResponse getAdSetCategoryBids(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Get the Category Bids for all valid Categories associated to an Ad Set

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        try {
            AdSetCategoryBidListResponse result = apiInstance.getAdSetCategoryBids(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAdSetCategoryBids");
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
| **adSetId** | **String**| Id of the Ad Set | |

### Return type

[**AdSetCategoryBidListResponse**](AdSetCategoryBidListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Category Bids for all valid Categories associated to an Ad Set. |  -  |


## getAdSetTargetingDealIds

> AdSetTargetingDealIdsResponse getAdSetTargetingDealIds(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids

Get the Deal Id Targeting configuration for the ad set whose id is specified

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        try {
            AdSetTargetingDealIdsResponse result = apiInstance.getAdSetTargetingDealIds(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAdSetTargetingDealIds");
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
| **adSetId** | **String**| Id of the Ad Set | |

### Return type

[**AdSetTargetingDealIdsResponse**](AdSetTargetingDealIdsResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the Deal Id Targeting configuration |  -  |


## getAdSetTargetingVideoPositioning

> AdSetTargetingVideoPositioningResponse getAdSetTargetingVideoPositioning(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning

Get the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        try {
            AdSetTargetingVideoPositioningResponse result = apiInstance.getAdSetTargetingVideoPositioning(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAdSetTargetingVideoPositioning");
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
| **adSetId** | **String**| Id of the Ad Set | |

### Return type

[**AdSetTargetingVideoPositioningResponse**](AdSetTargetingVideoPositioningResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the Video Positioning Targeting configuration |  -  |


## getAdvertiserBundleRules

> ApiResponseOfTargetingEntity getAdvertiserBundleRules(advertiserId)

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Returns a list of all targeted bundles for an advertiser.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        try {
            ApiResponseOfTargetingEntity result = apiInstance.getAdvertiserBundleRules(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAdvertiserBundleRules");
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
| **advertiserId** | **String**| The advertiser id | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAdvertiserDomainRules

> ApiResponseOfTargetingEntity getAdvertiserDomainRules(advertiserId)

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Returns a list of all targeted domains for an advertiser.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        try {
            ApiResponseOfTargetingEntity result = apiInstance.getAdvertiserDomainRules(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAdvertiserDomainRules");
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
| **advertiserId** | **String**| The advertiser id | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCampaign

> CampaignV23Q1Response getCampaign(campaignId)

/experimental/marketing-solutions/campaigns/{campaign-id}

Get the data for the specified campaign.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | ID of the marketing campaign; This field is required.
        try {
            CampaignV23Q1Response result = apiInstance.getCampaign(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCampaign");
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
| **campaignId** | **String**| ID of the marketing campaign; This field is required. | |

### Return type

[**CampaignV23Q1Response**](CampaignV23Q1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the data of the specified marketing campaign. |  -  |


## getCampaignBundleRules

> ApiResponseOfTargetingEntity getCampaignBundleRules(campaignId)

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Returns a list of all targeted bundles for a campaign.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        try {
            ApiResponseOfTargetingEntity result = apiInstance.getCampaignBundleRules(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCampaignBundleRules");
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
| **campaignId** | **String**| The campaign id | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCampaignDomainRules

> ApiResponseOfTargetingEntity getCampaignDomainRules(campaignId)

/experimental/campaigns/{campaignId}/targeting/domain-rules

Returns a list of all targeted domains for a campaign.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        try {
            ApiResponseOfTargetingEntity result = apiInstance.getCampaignDomainRules(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCampaignDomainRules");
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
| **campaignId** | **String**| The campaign id | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getDisplayMultipliers

> AdSetDisplayMultiplierListResponse getDisplayMultipliers(adSetId)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        try {
            AdSetDisplayMultiplierListResponse result = apiInstance.getDisplayMultipliers(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getDisplayMultipliers");
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
| **adSetId** | **String**| Id of the Ad Set | |

### Return type

[**AdSetDisplayMultiplierListResponse**](AdSetDisplayMultiplierListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Display Multipliers for all valid Categories associated to an Ad Set. |  -  |


## getSupplyVendorList

> SupplyVendorListResponse getSupplyVendorList()

/experimental/marketing-solutions/ad-sets/targeting/supply-vendors

Fetch the list of available supply vendors for any Ad Set targetings

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        try {
            SupplyVendorListResponse result = apiInstance.getSupplyVendorList();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getSupplyVendorList");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SupplyVendorListResponse**](SupplyVendorListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the errors/warnings if any |  -  |


## patchAdSetCategoryBids

> PatchAdSetCategoryBidResultListResponse patchAdSetCategoryBids(adSetId, patchAdSetCategoryBidListRequest)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Update the Category Bids for given Categories associated to an Ad Set  Patch Category Bids for one or more Categories in a single request. Partial success policy is followed.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        PatchAdSetCategoryBidListRequest patchAdSetCategoryBidListRequest = new PatchAdSetCategoryBidListRequest(); // PatchAdSetCategoryBidListRequest | Collection of category bids to update
        try {
            PatchAdSetCategoryBidResultListResponse result = apiInstance.patchAdSetCategoryBids(adSetId, patchAdSetCategoryBidListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#patchAdSetCategoryBids");
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
| **adSetId** | **String**| Id of the Ad Set | |
| **patchAdSetCategoryBidListRequest** | [**PatchAdSetCategoryBidListRequest**](PatchAdSetCategoryBidListRequest.md)| Collection of category bids to update | |

### Return type

[**PatchAdSetCategoryBidResultListResponse**](PatchAdSetCategoryBidResultListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Category Bids for given Categories associated to an Ad Set, used for partial successes as well. |  -  |


## patchAdSets

> ResponsesAdSetIdV26Q1 patchAdSets(requestsPatchAdSetV26Q1)

/experimental/marketing-solutions/ad-sets

Patch a list of AdSets.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        RequestsPatchAdSetV26Q1 requestsPatchAdSetV26Q1 = new RequestsPatchAdSetV26Q1(); // RequestsPatchAdSetV26Q1 | List of adsets to patch.
        try {
            ResponsesAdSetIdV26Q1 result = apiInstance.patchAdSets(requestsPatchAdSetV26Q1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#patchAdSets");
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
| **requestsPatchAdSetV26Q1** | [**RequestsPatchAdSetV26Q1**](RequestsPatchAdSetV26Q1.md)| List of adsets to patch. | |

### Return type

[**ResponsesAdSetIdV26Q1**](ResponsesAdSetIdV26Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Patched attributes for adSets specified in the request. |  -  |


## patchCampaigns

> PatchResultCampaignListResponse patchCampaigns(patchCampaignListRequest)

/experimental/marketing-solutions/campaigns

Patch a list of Campaigns.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        PatchCampaignListRequest patchCampaignListRequest = new PatchCampaignListRequest(); // PatchCampaignListRequest | List of campaigns to patch.
        try {
            PatchResultCampaignListResponse result = apiInstance.patchCampaigns(patchCampaignListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#patchCampaigns");
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
| **patchCampaignListRequest** | [**PatchCampaignListRequest**](PatchCampaignListRequest.md)| List of campaigns to patch. | |

### Return type

[**PatchResultCampaignListResponse**](PatchResultCampaignListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of patched campaigns. |  -  |


## patchDisplayMultipliers

> PatchAdSetDisplayMultiplierResultListResponse patchDisplayMultipliers(adSetId, patchAdSetDisplayMultiplierListRequest)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Update the Display Multipliers for given Categories associated to an Ad Set  Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        PatchAdSetDisplayMultiplierListRequest patchAdSetDisplayMultiplierListRequest = new PatchAdSetDisplayMultiplierListRequest(); // PatchAdSetDisplayMultiplierListRequest | List of display multiplier values to change
        try {
            PatchAdSetDisplayMultiplierResultListResponse result = apiInstance.patchDisplayMultipliers(adSetId, patchAdSetDisplayMultiplierListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#patchDisplayMultipliers");
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
| **adSetId** | **String**| Id of the Ad Set | |
| **patchAdSetDisplayMultiplierListRequest** | [**PatchAdSetDisplayMultiplierListRequest**](PatchAdSetDisplayMultiplierListRequest.md)| List of display multiplier values to change | |

### Return type

[**PatchAdSetDisplayMultiplierResultListResponse**](PatchAdSetDisplayMultiplierResultListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Display Multipliers for given Categories associated to an Ad Set. Make sure to check the error field in the response since a partial success will result in a 200 response code. |  -  |


## postAdvertiserBundleRules

> ApiResponseOfTargetingEntity postAdvertiserBundleRules(advertiserId, apiRequestOfTargetingEntity)

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Inserts a list of targeted bundles for an advertiser and sets the targeting mode : blocklisting or allowlisting.&lt;br /&gt;  It will replace the current list if any.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Description of the targeting rule to setup
        try {
            ApiResponseOfTargetingEntity result = apiInstance.postAdvertiserBundleRules(advertiserId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#postAdvertiserBundleRules");
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
| **advertiserId** | **String**| The advertiser id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## postAdvertiserDomainRules

> ApiResponseOfTargetingEntity postAdvertiserDomainRules(advertiserId, apiRequestOfTargetingEntity)

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Inserts a list of targeted domains for an advertiser and sets the targeting mode : blocklisting or allowlisting.&lt;br /&gt;  It will replace the current list if any.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Description of the targeting rule to setup
        try {
            ApiResponseOfTargetingEntity result = apiInstance.postAdvertiserDomainRules(advertiserId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#postAdvertiserDomainRules");
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
| **advertiserId** | **String**| The advertiser id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## postCampaignBundleRules

> ApiResponseOfTargetingEntity postCampaignBundleRules(campaignId, apiRequestOfTargetingEntity)

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Inserts a list of targeted bundles for a campaign and sets the targeting mode : blocklisting or allowlisting.&lt;br /&gt;  It will replace the current list if any.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Description of the targeting rule to setup
        try {
            ApiResponseOfTargetingEntity result = apiInstance.postCampaignBundleRules(campaignId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#postCampaignBundleRules");
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
| **campaignId** | **String**| The campaign id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## postCampaignDomainRules

> ApiResponseOfTargetingEntity postCampaignDomainRules(campaignId, apiRequestOfTargetingEntity)

/experimental/campaigns/{campaignId}/targeting/domain-rules

Inserts a list of targeted domains for a campaign and sets the targeting mode : blocklisting or allowlisting.&lt;br /&gt;  It will replace the current list if any.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Description of the targeting rule to setup
        try {
            ApiResponseOfTargetingEntity result = apiInstance.postCampaignDomainRules(campaignId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#postCampaignDomainRules");
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
| **campaignId** | **String**| The campaign id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## putAdvertiserBundleRules

> ApiResponseOfTargetingEntity putAdvertiserBundleRules(advertiserId, apiRequestOfTargetingEntity)

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Updates the targeted bundles for an advertiser by adding a list of bundles to the current list.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.putAdvertiserBundleRules(advertiserId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putAdvertiserBundleRules");
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
| **advertiserId** | **String**| The advertiser id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## putAdvertiserDomainRules

> ApiResponseOfTargetingEntity putAdvertiserDomainRules(advertiserId, apiRequestOfTargetingEntity)

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Updates the targeted domains for an advertiser by adding a list of domains to the current list.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The advertiser id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.putAdvertiserDomainRules(advertiserId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putAdvertiserDomainRules");
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
| **advertiserId** | **String**| The advertiser id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## putCampaignBundleRules

> ApiResponseOfTargetingEntity putCampaignBundleRules(campaignId, apiRequestOfTargetingEntity)

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Updates the targeted bundles for a campaign by adding a list of bundles to the current list.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.putCampaignBundleRules(campaignId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putCampaignBundleRules");
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
| **campaignId** | **String**| The campaign id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## putCampaignDomainRules

> ApiResponseOfTargetingEntity putCampaignDomainRules(campaignId, apiRequestOfTargetingEntity)

/experimental/campaigns/{campaignId}/targeting/domain-rules

Updates the targeted domains for a campaign by adding a list of domains to the current list.&lt;br /&gt;  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String campaignId = "campaignId_example"; // String | The campaign id
        ApiRequestOfTargetingEntity apiRequestOfTargetingEntity = new ApiRequestOfTargetingEntity(); // ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list
        try {
            ApiResponseOfTargetingEntity result = apiInstance.putCampaignDomainRules(campaignId, apiRequestOfTargetingEntity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putCampaignDomainRules");
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
| **campaignId** | **String**| The campaign id | |
| **apiRequestOfTargetingEntity** | [**ApiRequestOfTargetingEntity**](ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**ApiResponseOfTargetingEntity**](ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchAdSets

> ResponsesReadAdSetV26Q1 searchAdSets(adSetSearchRequestV26Q1)

/experimental/marketing-solutions/ad-sets/search

Search for ad sets based on provided criteria.  This returns the full configuration of ad sets matching those criteria.  Field projection can be used if only a subset of fields is required, instead of the full configuration.                If specific fields are precised in the user prompt, use meta.fields field projection in order to query only the value of these fields, else, provide every field.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        AdSetSearchRequestV26Q1 adSetSearchRequestV26Q1 = new AdSetSearchRequestV26Q1(); // AdSetSearchRequestV26Q1 | 
        try {
            ResponsesReadAdSetV26Q1 result = apiInstance.searchAdSets(adSetSearchRequestV26Q1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#searchAdSets");
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
| **adSetSearchRequestV26Q1** | [**AdSetSearchRequestV26Q1**](AdSetSearchRequestV26Q1.md)|  | [optional] |

### Return type

[**ResponsesReadAdSetV26Q1**](ResponsesReadAdSetV26Q1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | data for the ad sets |  -  |


## searchCampaigns

> CampaignV23Q1ListResponse searchCampaigns(campaignSearchRequestV23Q1)

/experimental/marketing-solutions/campaigns/search

Search endpoint for campaigns                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        CampaignSearchRequestV23Q1 campaignSearchRequestV23Q1 = new CampaignSearchRequestV23Q1(); // CampaignSearchRequestV23Q1 | Filters for searching for campaigns
        try {
            CampaignV23Q1ListResponse result = apiInstance.searchCampaigns(campaignSearchRequestV23Q1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#searchCampaigns");
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
| **campaignSearchRequestV23Q1** | [**CampaignSearchRequestV23Q1**](CampaignSearchRequestV23Q1.md)| Filters for searching for campaigns | [optional] |

### Return type

[**CampaignV23Q1ListResponse**](CampaignV23Q1ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of marketing campaigns&#39; data. |  -  |


## setAdSetTargetingDealIds

> AdSetTargetingDealIdsSetResultResponse setAdSetTargetingDealIds(adSetId, setAdSetTargetingDealIdsRequest)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids

Set the Deal Id Targeting configuration for the ad set whose id is specified

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        SetAdSetTargetingDealIdsRequest setAdSetTargetingDealIdsRequest = new SetAdSetTargetingDealIdsRequest(); // SetAdSetTargetingDealIdsRequest | the new Deal Id Targeting configuration
        try {
            AdSetTargetingDealIdsSetResultResponse result = apiInstance.setAdSetTargetingDealIds(adSetId, setAdSetTargetingDealIdsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#setAdSetTargetingDealIds");
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
| **adSetId** | **String**| Id of the Ad Set | |
| **setAdSetTargetingDealIdsRequest** | [**SetAdSetTargetingDealIdsRequest**](SetAdSetTargetingDealIdsRequest.md)| the new Deal Id Targeting configuration | |

### Return type

[**AdSetTargetingDealIdsSetResultResponse**](AdSetTargetingDealIdsSetResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the errors/warnings if any |  -  |


## setAdSetTargetingVideoPositioning

> AdSetTargetingVideoPositioningSetResultResponse setAdSetTargetingVideoPositioning(adSetId, setAdSetTargetingVideoPositioningRequest)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning

Set the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Id of the Ad Set
        SetAdSetTargetingVideoPositioningRequest setAdSetTargetingVideoPositioningRequest = new SetAdSetTargetingVideoPositioningRequest(); // SetAdSetTargetingVideoPositioningRequest | the new Video Positioning Targeting configuration
        try {
            AdSetTargetingVideoPositioningSetResultResponse result = apiInstance.setAdSetTargetingVideoPositioning(adSetId, setAdSetTargetingVideoPositioningRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#setAdSetTargetingVideoPositioning");
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
| **adSetId** | **String**| Id of the Ad Set | |
| **setAdSetTargetingVideoPositioningRequest** | [**SetAdSetTargetingVideoPositioningRequest**](SetAdSetTargetingVideoPositioningRequest.md)| the new Video Positioning Targeting configuration | |

### Return type

[**AdSetTargetingVideoPositioningSetResultResponse**](AdSetTargetingVideoPositioningSetResultResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the errors/warnings if any |  -  |


## startAdSets

> ResponsesAdSetId startAdSets(requestsAdSetId)

/experimental/marketing-solutions/ad-sets/start

Start the specified list of ad sets

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        RequestsAdSetId requestsAdSetId = new RequestsAdSetId(); // RequestsAdSetId | All the ad sets to start
        try {
            ResponsesAdSetId result = apiInstance.startAdSets(requestsAdSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#startAdSets");
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
| **requestsAdSetId** | [**RequestsAdSetId**](RequestsAdSetId.md)| All the ad sets to start | [optional] |

### Return type

[**ResponsesAdSetId**](ResponsesAdSetId.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of ad sets that have been started and errors / warnings by ad set |  -  |


## stopAdSets

> ResponsesAdSetId stopAdSets(requestsAdSetId)

/experimental/marketing-solutions/ad-sets/stop

Stop the specified list of ad sets

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        RequestsAdSetId requestsAdSetId = new RequestsAdSetId(); // RequestsAdSetId | All the ad sets to stop
        try {
            ResponsesAdSetId result = apiInstance.stopAdSets(requestsAdSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#stopAdSets");
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
| **requestsAdSetId** | [**RequestsAdSetId**](RequestsAdSetId.md)| All the ad sets to stop | [optional] |

### Return type

[**ResponsesAdSetId**](ResponsesAdSetId.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of ad sets that have been stopped and errors / warnings by ad set |  -  |


## updateAdSetAudience

> AdSetAudienceLinkEntityV1Response updateAdSetAudience(adSetId, adSetAudienceLinkInputEntityV1)

/experimental/marketing-solutions/ad-sets/{ad-set-id}/audience

Link or unlink an audience with an ad set

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.CampaignApi;

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

        CampaignApi apiInstance = new CampaignApi(defaultClient);
        String adSetId = "adSetId_example"; // String | The ad set ID.
        AdSetAudienceLinkInputEntityV1 adSetAudienceLinkInputEntityV1 = new AdSetAudienceLinkInputEntityV1(); // AdSetAudienceLinkInputEntityV1 | Ad set-Audience update request.
        try {
            AdSetAudienceLinkEntityV1Response result = apiInstance.updateAdSetAudience(adSetId, adSetAudienceLinkInputEntityV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateAdSetAudience");
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
| **adSetId** | **String**| The ad set ID. | |
| **adSetAudienceLinkInputEntityV1** | [**AdSetAudienceLinkInputEntityV1**](AdSetAudienceLinkInputEntityV1.md)| Ad set-Audience update request. | |

### Return type

[**AdSetAudienceLinkEntityV1Response**](AdSetAudienceLinkEntityV1Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

