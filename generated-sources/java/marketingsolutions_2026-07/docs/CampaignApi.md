# CampaignApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdSet**](CampaignApi.md#createAdSet) | **POST** /2026-07/marketing-solutions/ad-sets | /2026-07/marketing-solutions/ad-sets |
| [**createCampaign**](CampaignApi.md#createCampaign) | **POST** /2026-07/marketing-solutions/campaigns | /2026-07/marketing-solutions/campaigns |
| [**createMarketplaceSellerBudgets**](CampaignApi.md#createMarketplaceSellerBudgets) | **POST** /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets | /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets |
| [**createMarketplaceSellerCampaignsBySeller**](CampaignApi.md#createMarketplaceSellerCampaignsBySeller) | **POST** /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns |
| [**getAdSet**](CampaignApi.md#getAdSet) | **GET** /2026-07/marketing-solutions/ad-sets/{ad-set-id} | /2026-07/marketing-solutions/ad-sets/{ad-set-id} |
| [**getAdSetCategoryBids**](CampaignApi.md#getAdSetCategoryBids) | **GET** /2026-07/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /2026-07/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**getCampaign**](CampaignApi.md#getCampaign) | **GET** /2026-07/marketing-solutions/campaigns/{campaign-id} | /2026-07/marketing-solutions/campaigns/{campaign-id} |
| [**getDisplayMultipliers**](CampaignApi.md#getDisplayMultipliers) | **GET** /2026-07/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /2026-07/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**getMarketplaceAdSetsByAdvertiser**](CampaignApi.md#getMarketplaceAdSetsByAdvertiser) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets |
| [**getMarketplaceAdvertiser**](CampaignApi.md#getMarketplaceAdvertiser) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId} | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId} |
| [**getMarketplaceAdvertiserPreviewLimits**](CampaignApi.md#getMarketplaceAdvertiserPreviewLimits) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit |
| [**getMarketplaceAdvertisers**](CampaignApi.md#getMarketplaceAdvertisers) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers |
| [**getMarketplaceBudgetsByAdvertiser**](CampaignApi.md#getMarketplaceBudgetsByAdvertiser) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets |
| [**getMarketplaceBudgetsBySeller**](CampaignApi.md#getMarketplaceBudgetsBySeller) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets | /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets |
| [**getMarketplaceBudgetsBySellerCampaign**](CampaignApi.md#getMarketplaceBudgetsBySellerCampaign) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets | /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets |
| [**getMarketplaceCampaignsByAdvertiser**](CampaignApi.md#getMarketplaceCampaignsByAdvertiser) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns |
| [**getMarketplaceCampaignsStats**](CampaignApi.md#getMarketplaceCampaignsStats) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/stats/campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/stats/campaigns |
| [**getMarketplaceSeller**](CampaignApi.md#getMarketplaceSeller) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId} | /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId} |
| [**getMarketplaceSellerAdPreview**](CampaignApi.md#getMarketplaceSellerAdPreview) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview |
| [**getMarketplaceSellerBudget**](CampaignApi.md#getMarketplaceSellerBudget) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} | /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} |
| [**getMarketplaceSellerBudgets**](CampaignApi.md#getMarketplaceSellerBudgets) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets | /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets |
| [**getMarketplaceSellerCampaign**](CampaignApi.md#getMarketplaceSellerCampaign) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} | /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} |
| [**getMarketplaceSellerCampaigns**](CampaignApi.md#getMarketplaceSellerCampaigns) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns |
| [**getMarketplaceSellerCampaignsByAdvertiser**](CampaignApi.md#getMarketplaceSellerCampaignsByAdvertiser) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns |
| [**getMarketplaceSellerCampaignsBySeller**](CampaignApi.md#getMarketplaceSellerCampaignsBySeller) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns |
| [**getMarketplaceSellerCampaignsStats**](CampaignApi.md#getMarketplaceSellerCampaignsStats) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns |
| [**getMarketplaceSellers**](CampaignApi.md#getMarketplaceSellers) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers | /2026-07/marketing-solutions/marketplace-performance-outcomes/sellers |
| [**getMarketplaceSellersByAdvertiser**](CampaignApi.md#getMarketplaceSellersByAdvertiser) | **POST** /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers | /2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers |
| [**getMarketplaceSellersStats**](CampaignApi.md#getMarketplaceSellersStats) | **GET** /2026-07/marketing-solutions/marketplace-performance-outcomes/stats/sellers | /2026-07/marketing-solutions/marketplace-performance-outcomes/stats/sellers |
| [**patchAdSetCategoryBids**](CampaignApi.md#patchAdSetCategoryBids) | **PATCH** /2026-07/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /2026-07/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**patchAdSets**](CampaignApi.md#patchAdSets) | **PATCH** /2026-07/marketing-solutions/ad-sets | /2026-07/marketing-solutions/ad-sets |
| [**patchCampaigns**](CampaignApi.md#patchCampaigns) | **PATCH** /2026-07/marketing-solutions/campaigns | /2026-07/marketing-solutions/campaigns |
| [**patchDisplayMultipliers**](CampaignApi.md#patchDisplayMultipliers) | **PATCH** /2026-07/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /2026-07/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**searchAdSets**](CampaignApi.md#searchAdSets) | **POST** /2026-07/marketing-solutions/ad-sets/search | /2026-07/marketing-solutions/ad-sets/search |
| [**searchCampaigns**](CampaignApi.md#searchCampaigns) | **POST** /2026-07/marketing-solutions/campaigns/search | /2026-07/marketing-solutions/campaigns/search |
| [**startAdSets**](CampaignApi.md#startAdSets) | **POST** /2026-07/marketing-solutions/ad-sets/start | /2026-07/marketing-solutions/ad-sets/start |
| [**stopAdSets**](CampaignApi.md#stopAdSets) | **POST** /2026-07/marketing-solutions/ad-sets/stop | /2026-07/marketing-solutions/ad-sets/stop |
| [**updateAdSetAudience**](CampaignApi.md#updateAdSetAudience) | **PUT** /2026-07/marketing-solutions/ad-sets/{ad-set-id}/audience | /2026-07/marketing-solutions/ad-sets/{ad-set-id}/audience |
| [**updateMarketplaceSellerBudget**](CampaignApi.md#updateMarketplaceSellerBudget) | **PATCH** /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} | /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} |
| [**updateMarketplaceSellerBudgets**](CampaignApi.md#updateMarketplaceSellerBudgets) | **PATCH** /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets | /2026-07/marketing-solutions/marketplace-performance-outcomes/budgets |
| [**updateMarketplaceSellerCampaign**](CampaignApi.md#updateMarketplaceSellerCampaign) | **PATCH** /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} | /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} |
| [**updateMarketplaceSellerCampaigns**](CampaignApi.md#updateMarketplaceSellerCampaigns) | **PATCH** /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns | /2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns |



## createAdSet

> ResponseReadAdSetV26Q1 createAdSet(createAdSetV26Q1Request)

/2026-07/marketing-solutions/ad-sets

Create an ad set with the provided parameters

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/campaigns

Create the specified campaign                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## createMarketplaceSellerBudgets

> List&lt;SellerBudgetMessage&gt; createMarketplaceSellerBudgets(createSellerBudgetMapiMessage)

/2026-07/marketing-solutions/marketplace-performance-outcomes/budgets

Create one or more new budgets to enable spending with the given limitations.  All three types of budgets can be created this way.                The following constraints apply when creating a new budget.                • &lt;b&gt;sellerId&lt;/b&gt;: the seller MUST be supplied&lt;br /&gt;  • &lt;b&gt;campaignIds&lt;/b&gt;: a non-empty array of campaign ids MUST be supplied&lt;br /&gt;  • &lt;b&gt;budgetType&lt;/b&gt;: a budget type MUST be supplied&lt;br /&gt;  • &lt;b&gt;amount&lt;/b&gt;: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative&lt;br /&gt;  • &lt;b&gt;startDate&lt;/b&gt;: a future start date MUST be supplied&lt;br /&gt;  • &lt;b&gt;endDate&lt;/b&gt;: an end date MAY be supplied and if supplied MUST be greater than the start date&lt;br /&gt;                Other attributes MUST NOT be supplied.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        List<CreateSellerBudgetMapiMessage> createSellerBudgetMapiMessage = Arrays.asList(); // List<CreateSellerBudgetMapiMessage> | 
        try {
            List<SellerBudgetMessage> result = apiInstance.createMarketplaceSellerBudgets(createSellerBudgetMapiMessage);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createMarketplaceSellerBudgets");
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
| **createSellerBudgetMapiMessage** | [**List&lt;CreateSellerBudgetMapiMessage&gt;**](CreateSellerBudgetMapiMessage.md)|  | |

### Return type

[**List&lt;SellerBudgetMessage&gt;**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## createMarketplaceSellerCampaignsBySeller

> SellerCampaignMessage createMarketplaceSellerCampaignsBySeller(sellerId, createSellerCampaignMessageMapi)

/2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns

Associate an existing Seller with an existing Campaign allowing for budget creation

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerId = "sellerId_example"; // String | Supply a generated Id of an existing Seller
        CreateSellerCampaignMessageMapi createSellerCampaignMessageMapi = new CreateSellerCampaignMessageMapi(); // CreateSellerCampaignMessageMapi | Supply the campaign Id and bid to create the mapping
        try {
            SellerCampaignMessage result = apiInstance.createMarketplaceSellerCampaignsBySeller(sellerId, createSellerCampaignMessageMapi);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createMarketplaceSellerCampaignsBySeller");
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
| **sellerId** | **String**| Supply a generated Id of an existing Seller | |
| **createSellerCampaignMessageMapi** | [**CreateSellerCampaignMessageMapi**](CreateSellerCampaignMessageMapi.md)| Supply the campaign Id and bid to create the mapping | |

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAdSet

> ResponseReadAdSetV26Q1 getAdSet(adSetId)

/2026-07/marketing-solutions/ad-sets/{ad-set-id}

Get the data for the specified ad set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Get the Category Bids for all valid Categories associated to an Ad Set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## getCampaign

> CampaignV23Q1Response getCampaign(campaignId)

/2026-07/marketing-solutions/campaigns/{campaign-id}

Get the data for the specified campaign.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## getDisplayMultipliers

> AdSetDisplayMultiplierListResponse getDisplayMultipliers(adSetId)

/2026-07/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## getMarketplaceAdSetsByAdvertiser

> List&lt;AdvertiserAdsetMessage&gt; getMarketplaceAdSetsByAdvertiser(advertiserId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets

Get the collection of adsets associated with the advertiserId.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        try {
            List<AdvertiserAdsetMessage> result = apiInstance.getMarketplaceAdSetsByAdvertiser(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceAdSetsByAdvertiser");
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
| **advertiserId** | **String**| Id of the advertiser | |

### Return type

[**List&lt;AdvertiserAdsetMessage&gt;**](AdvertiserAdsetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceAdvertiser

> AdvertiserInfoMessage getMarketplaceAdvertiser(advertiserId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}

Get an advertiser.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        try {
            AdvertiserInfoMessage result = apiInstance.getMarketplaceAdvertiser(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceAdvertiser");
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
| **advertiserId** | **String**| Id of the advertiser | |

### Return type

[**AdvertiserInfoMessage**](AdvertiserInfoMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceAdvertiserPreviewLimits

> List&lt;AdvertiserQuotaMessage&gt; getMarketplaceAdvertiserPreviewLimits()

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit

Get the collection of advertisers preview limits associated with the authorized user.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
            List<AdvertiserQuotaMessage> result = apiInstance.getMarketplaceAdvertiserPreviewLimits();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceAdvertiserPreviewLimits");
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

[**List&lt;AdvertiserQuotaMessage&gt;**](AdvertiserQuotaMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceAdvertisers

> List&lt;AdvertiserInfoMessage&gt; getMarketplaceAdvertisers()

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers

Get the collection of advertisers associated with the user.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
            List<AdvertiserInfoMessage> result = apiInstance.getMarketplaceAdvertisers();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceAdvertisers");
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

[**List&lt;AdvertiserInfoMessage&gt;**](AdvertiserInfoMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceBudgetsByAdvertiser

> List&lt;SellerBudgetMessage&gt; getMarketplaceBudgetsByAdvertiser(advertiserId, budgetId, endAfterDate, sellerId, startBeforeDate, status, type, withBalance, withSpend)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets

Get CRP budgets for a specific advertiser

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        Long budgetId = 56L; // Long | Return only budgets with given Id
        OffsetDateTime endAfterDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended.
        Long sellerId = 56L; // Long | Return only budgets belonging to given sellerId
        OffsetDateTime startBeforeDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
        String status = "Archived"; // String | Return only budgets with the given status.
        String type = "type_example"; // String | Return only budgets with the given budget type.
        Boolean withBalance = true; // Boolean | Return only budgets with the given status.
        Boolean withSpend = true; // Boolean | Return budgets with any positive spend.
        try {
            List<SellerBudgetMessage> result = apiInstance.getMarketplaceBudgetsByAdvertiser(advertiserId, budgetId, endAfterDate, sellerId, startBeforeDate, status, type, withBalance, withSpend);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceBudgetsByAdvertiser");
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
| **advertiserId** | **String**| Id of the advertiser | |
| **budgetId** | **Long**| Return only budgets with given Id | [optional] |
| **endAfterDate** | **OffsetDateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **sellerId** | **Long**| Return only budgets belonging to given sellerId | [optional] |
| **startBeforeDate** | **OffsetDateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **String**| Return only budgets with the given status. | [optional] [enum: Archived, Current, Scheduled] |
| **type** | **String**| Return only budgets with the given budget type. | [optional] |
| **withBalance** | **Boolean**| Return only budgets with the given status. | [optional] |
| **withSpend** | **Boolean**| Return budgets with any positive spend. | [optional] |

### Return type

[**List&lt;SellerBudgetMessage&gt;**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceBudgetsBySeller

> List&lt;SellerBudgetMessage&gt; getMarketplaceBudgetsBySeller(sellerId, campaignId, endAfterDate, startBeforeDate, status, type, withBalance, withSpend)

/2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets

Return current (non-archived) budgets for this seller. Budgets whose endDate is in the past are excluded by default. To retrieve archived or past budgets, use the &#x60;/budgets&#x60; endpoint (GetMarketplaceSellerBudgets) with the &#x60;endAfterDate&#x60; filter instead.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerId = "sellerId_example"; // String | Return only budgets belonging to the given seller.
        Integer campaignId = 56; // Integer | Return only budgets that pay for a given campaign.
        OffsetDateTime endAfterDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended.
        OffsetDateTime startBeforeDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
        String status = "Archived"; // String | Return only budgets with the given status.
        String type = "type_example"; // String | Return only budgets with the given budget type.
        Boolean withBalance = true; // Boolean | Return only budgets with the given status.
        Boolean withSpend = true; // Boolean | Return budgets with any positive spend.
        try {
            List<SellerBudgetMessage> result = apiInstance.getMarketplaceBudgetsBySeller(sellerId, campaignId, endAfterDate, startBeforeDate, status, type, withBalance, withSpend);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceBudgetsBySeller");
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
| **sellerId** | **String**| Return only budgets belonging to the given seller. | |
| **campaignId** | **Integer**| Return only budgets that pay for a given campaign. | [optional] |
| **endAfterDate** | **OffsetDateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **startBeforeDate** | **OffsetDateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **String**| Return only budgets with the given status. | [optional] [enum: Archived, Current, Scheduled] |
| **type** | **String**| Return only budgets with the given budget type. | [optional] |
| **withBalance** | **Boolean**| Return only budgets with the given status. | [optional] |
| **withSpend** | **Boolean**| Return budgets with any positive spend. | [optional] |

### Return type

[**List&lt;SellerBudgetMessage&gt;**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceBudgetsBySellerCampaign

> List&lt;SellerBudgetMessage&gt; getMarketplaceBudgetsBySellerCampaign(sellerCampaignId, endAfterDate, startBeforeDate, status, type, withBalance, withSpend)

/2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets

Return a collection of budgets for this seller campaign filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used.                See the budgets endpoint for additional details.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerCampaignId = "sellerCampaignId_example"; // String | Return only budgets belonging to the given seller campaign. Format: `{sellerId}.{campaignId}`, e.g. `2578464.187625`.
        OffsetDateTime endAfterDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended.
        OffsetDateTime startBeforeDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
        String status = "Archived"; // String | Return only budgets with the given status.
        String type = "type_example"; // String | Return only budgets with the given budget type.
        Boolean withBalance = true; // Boolean | Return only budgets with a positive balance.
        Boolean withSpend = true; // Boolean | Return budgets with a positive spend.
        try {
            List<SellerBudgetMessage> result = apiInstance.getMarketplaceBudgetsBySellerCampaign(sellerCampaignId, endAfterDate, startBeforeDate, status, type, withBalance, withSpend);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceBudgetsBySellerCampaign");
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
| **sellerCampaignId** | **String**| Return only budgets belonging to the given seller campaign. Format: &#x60;{sellerId}.{campaignId}&#x60;, e.g. &#x60;2578464.187625&#x60;. | |
| **endAfterDate** | **OffsetDateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **startBeforeDate** | **OffsetDateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **String**| Return only budgets with the given status. | [optional] [enum: Archived, Current, Scheduled] |
| **type** | **String**| Return only budgets with the given budget type. | [optional] |
| **withBalance** | **Boolean**| Return only budgets with a positive balance. | [optional] |
| **withSpend** | **Boolean**| Return budgets with a positive spend. | [optional] |

### Return type

[**List&lt;SellerBudgetMessage&gt;**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceCampaignsByAdvertiser

> List&lt;AdvertiserCampaignMessage&gt; getMarketplaceCampaignsByAdvertiser(advertiserId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns

Get the collection of CRP campaigns associated with the advertiserId.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        try {
            List<AdvertiserCampaignMessage> result = apiInstance.getMarketplaceCampaignsByAdvertiser(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceCampaignsByAdvertiser");
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
| **advertiserId** | **String**| Id of the advertiser | |

### Return type

[**List&lt;AdvertiserCampaignMessage&gt;**](AdvertiserCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceCampaignsStats

> StatsReportMessage getMarketplaceCampaignsStats(advertiserId, campaignId, clickAttributionPolicy, count, endDate, intervalSize, startDate, timeZoneId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/stats/campaigns

## Dimensions                Get performance statistics aggregated for _campaigns_. The campaign id appears  in the output as the first column.                Aggregation can be done by &#x60;hour&#x60;, &#x60;day&#x60;, &#x60;month&#x60;, or &#x60;year&#x60; aligned with the user timezone  if provided. The aggregation interval size is controlled by &#x60;intervalSize&#x60;. The time  interval appears in the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR &#x3D; Conversion Rate | salesUnits / clicks  G | CPO &#x3D; Cost Per Order | cost / salesUnits  H | COS &#x3D; Cost of Sale | cost / revenue  I | ROAS &#x3D; Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by &#x60;clickAttributionPolicy&#x60;.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by campaign, date or count.                Filtering the results to events associated with a specific campaign is done by setting  the &#x60;campaignId&#x60; filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the &#x60;startDate&#x60; and  &#x60;endDate&#x60; filter parameters using the &#x60;yyyy-MM-DD&#x60; format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is &#x60;hour&#x60;, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  &#x60;count&#x60; filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is &#x60;application/json&#x60; and  &#x60;text/csv&#x60;.                &#x60;&#x60;&#x60;json  {     \&quot;columns\&quot;: [ \&quot;campaignId\&quot;, \&quot;month\&quot;, \&quot;impressions\&quot;, \&quot;clicks\&quot;, \&quot;cost\&quot;, \&quot;saleUnits\&quot;, \&quot;revenue\&quot;, \&quot;cr\&quot;, \&quot;cpo\&quot;, \&quot;cos\&quot;, \&quot;roas\&quot; ],     \&quot;data\&quot;: [         [168423, \&quot;2019-05-01\&quot;, 3969032, 13410, 1111.295, 985, 190758099, 0.073, 1.128, 0.000, 171653.880 ],         [168423, \&quot;2019-06-01\&quot;, 8479603, 25619, 2190.705, 740, 152783656, 0.028, 2.960, 0.000, 69741.775 ]         ],     \&quot;rows\&quot;: 2  }  &#x60;&#x60;&#x60;                The JSON result is an object with three fields (&#x60;columns&#x60;, &#x60;data&#x60;, and &#x60;rows&#x60;). The  “columns” array acts as the header for the data rows. The categorical dimension  column comes first and consists of the campaign id.  The interval column comes next and defines the aggregation period.  The interval size is  determined by the &#x60;intervalSize&#x60; parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the &#x60;clickAttributionPolicy&#x60; parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        Integer advertiserId = 56; // Integer | Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts.
        String campaignId = "campaignId_example"; // String | Show only metrics for this campaign (default all campaigns)
        String clickAttributionPolicy = "Both"; // String | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS
        Integer count = 56; // Integer | Return up to the first count rows of data (default is all rows)
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Filter out all events that occur after date (default is today’s date)
        String intervalSize = "Hour"; // String | Specify the aggregation interval for events used to compute stats (default is \"day\")
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Filter out all events that occur before date (default is the value of `endDate`)
        String timeZoneId = "timeZoneId_example"; // String | Specify the timezone used in the aggregations (IANA code).
        try {
            StatsReportMessage result = apiInstance.getMarketplaceCampaignsStats(advertiserId, campaignId, clickAttributionPolicy, count, endDate, intervalSize, startDate, timeZoneId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceCampaignsStats");
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
| **advertiserId** | **Integer**| Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts. | [optional] |
| **campaignId** | **String**| Show only metrics for this campaign (default all campaigns) | [optional] |
| **clickAttributionPolicy** | **String**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] [default to AnySeller] [enum: Both, SameSeller, AnySeller] |
| **count** | **Integer**| Return up to the first count rows of data (default is all rows) | [optional] |
| **endDate** | **OffsetDateTime**| Filter out all events that occur after date (default is today’s date) | [optional] |
| **intervalSize** | **String**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] [default to Day] [enum: Hour, Day, Month, Year] |
| **startDate** | **OffsetDateTime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] |
| **timeZoneId** | **String**| Specify the timezone used in the aggregations (IANA code). | [optional] |

### Return type

[**StatsReportMessage**](StatsReportMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSeller

> SellerBase getMarketplaceSeller(sellerId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}

Return details for the selected seller. For example,                    {          \&quot;id\&quot; : \&quot;123456\&quot;          \&quot;sellerName\&quot;: \&quot;HBogart\&quot;,      }

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerId = "sellerId_example"; // String | Id of the seller.
        try {
            SellerBase result = apiInstance.getMarketplaceSeller(sellerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSeller");
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
| **sellerId** | **String**| Id of the seller. | |

### Return type

[**SellerBase**](SellerBase.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerAdPreview

> String getMarketplaceSellerAdPreview(advertiserId, sellerId, campaignId, height, width)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview

Get a preview of an HTML ad with products belonging to the provided seller  • &lt;b&gt;advertiserId&lt;/b&gt;: Valid crp advertiserId, seller belongs to provided advertiser&lt;br /&gt;  • &lt;b&gt;sellerId&lt;/b&gt;: Products from given SellerId will fill the ad preview, must be existing crp sellerId&lt;br /&gt;  • &lt;b&gt;height&lt;/b&gt;: height may be supplied to request a specific ad preview height. Default height: 250&lt;br /&gt;  • &lt;b&gt;width&lt;/b&gt;: width may be supplied to request a specific ad preview width. Default width: 300&lt;br /&gt;                Ad preview api calls are capped to 1000 per day per advertiser by default. Current usage, limit, and period can be found using v2/crp/advertisers/preview-limit

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        Long sellerId = 56L; // Long | Id of the seller
        Integer campaignId = 56; // Integer | Seller CampaignId
        Integer height = 56; // Integer | Height of the ad to display
        Integer width = 56; // Integer | Width of the ad to display
        try {
            String result = apiInstance.getMarketplaceSellerAdPreview(advertiserId, sellerId, campaignId, height, width);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerAdPreview");
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
| **advertiserId** | **String**| Id of the advertiser | |
| **sellerId** | **Long**| Id of the seller | |
| **campaignId** | **Integer**| Seller CampaignId | [optional] |
| **height** | **Integer**| Height of the ad to display | [optional] |
| **width** | **Integer**| Width of the ad to display | [optional] |

### Return type

**String**

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerBudget

> SellerBudgetMessage getMarketplaceSellerBudget(budgetId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId}

Return a budget. For example,                    {          \&quot;id\&quot;: \&quot;1759183\&quot;,          \&quot;sellerId\&quot;: \&quot;321392\&quot;,          \&quot;campaignIds\&quot;: [              143962          ],          \&quot;budgetType\&quot;: \&quot;Capped\&quot;,          \&quot;amount\&quot;: 1000,          \&quot;startDate\&quot;: \&quot;2021-01-11\&quot;,          \&quot;endDate\&quot;: \&quot;2021-01-12\&quot;,          \&quot;spend\&quot;: null,          \&quot;status\&quot;: \&quot;Active\&quot;      }                A budget limits the spend of a seller for one or more campaigns.                There are three types of budget:&lt;br /&gt;&lt;b&gt;Uncapped&lt;/b&gt; budgets put no limit on the total amount of spend.&lt;br /&gt;&lt;b&gt;Capped&lt;/b&gt; budgets limit the total spend to a fixed amount.&lt;br /&gt;&lt;b&gt;Daily&lt;/b&gt; budgets limit daily spend to a fixed amount.&lt;br /&gt;                In addition, budgets can limit the spend to a specific range of dates using  the start and end date attributes. Finally a budget must be active to be used.                &lt;b&gt;Spend&lt;/b&gt; approximates the current spend against this budget. There may be a lag  between when an ad is clicked and the time it accrues to the spend. Daily budgets  show spend against the most recent day only.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String budgetId = "budgetId_example"; // String | Id of the budget.
        try {
            SellerBudgetMessage result = apiInstance.getMarketplaceSellerBudget(budgetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerBudget");
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
| **budgetId** | **String**| Id of the budget. | |

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerBudgets

> List&lt;SellerBudgetMessage&gt; getMarketplaceSellerBudgets(advertiserId, campaignId, endAfterDate, sellerId, startBeforeDate, status, type, withBalance, withSpend)

/2026-07/marketing-solutions/marketplace-performance-outcomes/budgets

Return a collection of budgets filtered by optional filter parameters, **including archived budgets**. This is the endpoint to use when investigating past budget history.                By default, budgets whose endDate is in the past are excluded. Use &#x60;endAfterDate&#x60; to retrieve archived budgets (e.g. &#x60;endAfterDate&#x3D;2025-01-01&#x60; returns all budgets ending after that date). Use &#x60;sellerId&#x60; to filter to a specific seller — omitting it on large advertisers causes timeouts.                &lt;b&gt;Date filter.&lt;/b&gt; To find budgets that were active on a specific date, set both &#x60;startBeforeDate&#x60; and &#x60;endAfterDate&#x60; to that day.                &lt;b&gt;Spend.&lt;/b&gt; If &#x60;endAfterDate&#x60; is supplied, the spend excludes spend that happened after that date. For daily budgets, only the spend for the final day is displayed.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        Integer advertiserId = 56; // Integer | Return only budgets belonging to the specified advertiser
        Integer campaignId = 56; // Integer | Return only budgets that pay for a given campaign.
        OffsetDateTime endAfterDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended.
        String sellerId = "sellerId_example"; // String | Return only budgets belonging to the given seller.
        OffsetDateTime startBeforeDate = OffsetDateTime.now(); // OffsetDateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
        String status = "Archived"; // String | Return only budgets with the given status.
        String type = "type_example"; // String | Return only budgets with the given budget type.
        Boolean withBalance = true; // Boolean | Return only budgets with the given status.
        Boolean withSpend = true; // Boolean | Return budgets with any positive spend.
        try {
            List<SellerBudgetMessage> result = apiInstance.getMarketplaceSellerBudgets(advertiserId, campaignId, endAfterDate, sellerId, startBeforeDate, status, type, withBalance, withSpend);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerBudgets");
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
| **advertiserId** | **Integer**| Return only budgets belonging to the specified advertiser | [optional] |
| **campaignId** | **Integer**| Return only budgets that pay for a given campaign. | [optional] |
| **endAfterDate** | **OffsetDateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **sellerId** | **String**| Return only budgets belonging to the given seller. | [optional] |
| **startBeforeDate** | **OffsetDateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **String**| Return only budgets with the given status. | [optional] [enum: Archived, Current, Scheduled] |
| **type** | **String**| Return only budgets with the given budget type. | [optional] |
| **withBalance** | **Boolean**| Return only budgets with the given status. | [optional] |
| **withSpend** | **Boolean**| Return budgets with any positive spend. | [optional] |

### Return type

[**List&lt;SellerBudgetMessage&gt;**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerCampaign

> SellerCampaignMessage getMarketplaceSellerCampaign(sellerCampaignId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}

Return details for a seller campaign. For example,                    {          \&quot;id\&quot;: \&quot;543210.123456\&quot;,          \&quot;sellerId\&quot;: \&quot;543210\&quot;,          \&quot;campaignId\&quot;: 123456,          \&quot;bid\&quot;: 1.55,          \&quot;suspendedSince\&quot;: \&quot;2018-07-30T15:15:24.813\&quot;,          \&quot;suspensionReasons\&quot;: [              \&quot;NoMoreBudget\&quot;          ]      }                An active seller campaign is one for which the value of &lt;b&gt;suspendedSince&lt;/b&gt; is null and  the &lt;b&gt;bid&lt;/b&gt; is positive. The currency of the bid is the &lt;b&gt;bidCurrency&lt;/b&gt; of the  associated campaign.                Any active seller campaign must also have an active total (capped or uncapped) budget.  It may optionally have an active daily budget as well to further limit spending.                Suspension reasons:  - ManuallyStopped: The Seller-Campaign has been manually paused. This is not related to the other suspension reasons.  - NoBudgetDefined: No valid budget has been linked to the Seller-Campaign.  - NoCpcDefined: No CPC has been set for the Seller-Campaign.  - NoMoreBudget: The current budget of the Seller-Campaign has been exhausted.  - RemovedFromCatalog: All the products of the Seller-Campaign have been deleted from the catalog.  - NotYetStarted: The Seller-Campaign has just been created and has not yet been processed.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerCampaignId = "sellerCampaignId_example"; // String | Composite id of the seller campaign in the format `{sellerId}.{campaignId}`, e.g. `2578464.187625`.
        try {
            SellerCampaignMessage result = apiInstance.getMarketplaceSellerCampaign(sellerCampaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerCampaign");
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
| **sellerCampaignId** | **String**| Composite id of the seller campaign in the format &#x60;{sellerId}.{campaignId}&#x60;, e.g. &#x60;2578464.187625&#x60;. | |

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerCampaigns

> List&lt;SellerCampaignMessage&gt; getMarketplaceSellerCampaigns(advertiserId, budgetStatus, campaignId, sellerId, sellerStatus)

/2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns

Return a collection of seller campaigns filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        Integer advertiserId = 56; // Integer | Return only seller belonging to the specified advertiser
        String budgetStatus = "Archived"; // String | Return only seller campaigns whose budget has the given status.
        Integer campaignId = 56; // Integer | Return only seller campaigns associated with the given campaign.
        String sellerId = "sellerId_example"; // String | Return only seller campaigns belonging to the given seller.
        String sellerStatus = "Inactive"; // String | Return only seller campaigns for sellers with the given status.
        try {
            List<SellerCampaignMessage> result = apiInstance.getMarketplaceSellerCampaigns(advertiserId, budgetStatus, campaignId, sellerId, sellerStatus);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerCampaigns");
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
| **advertiserId** | **Integer**| Return only seller belonging to the specified advertiser | [optional] |
| **budgetStatus** | **String**| Return only seller campaigns whose budget has the given status. | [optional] [enum: Archived, Current, Scheduled] |
| **campaignId** | **Integer**| Return only seller campaigns associated with the given campaign. | [optional] |
| **sellerId** | **String**| Return only seller campaigns belonging to the given seller. | [optional] |
| **sellerStatus** | **String**| Return only seller campaigns for sellers with the given status. | [optional] [enum: Inactive, Active] |

### Return type

[**List&lt;SellerCampaignMessage&gt;**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerCampaignsByAdvertiser

> List&lt;SellerCampaignMessage&gt; getMarketplaceSellerCampaignsByAdvertiser(advertiserId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns

Get CRP seller campaigns for a specific advertiser

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        try {
            List<SellerCampaignMessage> result = apiInstance.getMarketplaceSellerCampaignsByAdvertiser(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerCampaignsByAdvertiser");
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
| **advertiserId** | **String**| Id of the advertiser | |

### Return type

[**List&lt;SellerCampaignMessage&gt;**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerCampaignsBySeller

> List&lt;SellerCampaignMessage&gt; getMarketplaceSellerCampaignsBySeller(sellerId, budgetStatus, campaignId, sellerStatus)

/2026-07/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns

Return a collection of seller campaigns for this seller filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used. See the seller campaigns endpoint for additional details.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerId = "sellerId_example"; // String | Return only seller campaigns belonging to the given seller.
        String budgetStatus = "Archived"; // String | Return only seller campaigns whose budget has the given status.
        Integer campaignId = 56; // Integer | Return only seller campaigns associated with the given campaign.
        String sellerStatus = "Inactive"; // String | Return only seller campaigns for sellers with the given status.
        try {
            List<SellerCampaignMessage> result = apiInstance.getMarketplaceSellerCampaignsBySeller(sellerId, budgetStatus, campaignId, sellerStatus);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerCampaignsBySeller");
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
| **sellerId** | **String**| Return only seller campaigns belonging to the given seller. | |
| **budgetStatus** | **String**| Return only seller campaigns whose budget has the given status. | [optional] [enum: Archived, Current, Scheduled] |
| **campaignId** | **Integer**| Return only seller campaigns associated with the given campaign. | [optional] |
| **sellerStatus** | **String**| Return only seller campaigns for sellers with the given status. | [optional] [enum: Inactive, Active] |

### Return type

[**List&lt;SellerCampaignMessage&gt;**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellerCampaignsStats

> StatsReportMessage getMarketplaceSellerCampaignsStats(advertiserId, campaignId, clickAttributionPolicy, count, endDate, intervalSize, sellerId, startDate, timeZoneId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns

## Dimensions                Get performance statistics aggregated for _seller campaigns_.The campaign id, seller id, and  seller name appear in the first three columns of the output. These are followed by the interval  size column.                Aggregation can be done by &#x60;hour&#x60;, &#x60;day&#x60;, &#x60;month&#x60;, or &#x60;year&#x60; aligned with the user timezone if  provided. The aggregation interval size is controlled by &#x60;intervalSize&#x60;. The remaining columns  are metrics.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR &#x3D; Conversion Rate | salesUnits / clicks  G | CPO &#x3D; Cost Per Order | cost / salesUnits  H | COS &#x3D; Cost of Sale | cost / revenue  I | ROAS &#x3D; Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by &#x60;clickAttributionPolicy&#x60;.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by date or count.                Filtering the results to events associated with a specific campaign is done by setting  the &#x60;campaignId&#x60; filter parameter to the desired value.                Filtering the results to events associated with a specific seller is done by setting  the &#x60;sellerId&#x60; filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the &#x60;startDate&#x60; and  &#x60;endDate&#x60; filter parameters using the &#x60;yyyy-MM-DD&#x60; format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is &#x60;hour&#x60;, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  &#x60;count&#x60; filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is &#x60;application/json&#x60; and  &#x60;text/csv&#x60;.                &#x60;&#x60;&#x60;json  {      \&quot;columns\&quot;: [          \&quot;campaignId\&quot;, \&quot;sellerId\&quot;, \&quot;sellerName\&quot;, \&quot;month\&quot;, \&quot;impressions\&quot;, \&quot;clicks\&quot;, \&quot;cost\&quot;, \&quot;saleUnits\&quot;, \&quot;revenue\&quot;, \&quot;cr\&quot;, \&quot;cpo\&quot;, \&quot;cos\&quot;, \&quot;roas\&quot;      ],      \&quot;data\&quot;: [          [168423, 1110222, \&quot;118883955\&quot;, \&quot;2019-05-01\&quot;, 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110222, \&quot;118883955\&quot;, \&quot;2019-06-01\&quot;, 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \&quot;117980027\&quot;, \&quot;2019-05-01\&quot;, 12502, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \&quot;117980027\&quot;, \&quot;2019-06-01\&quot;, 20266, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0]      ],      \&quot;rows\&quot;: 4  }  &#x60;&#x60;&#x60;                The JSON result is an object with three fields (&#x60;columns&#x60;, &#x60;data&#x60;, and &#x60;rows&#x60;). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the campaign id, seller id, and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the &#x60;intervalSize&#x60; parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the &#x60;clickAttributionPolicy&#x60; parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        Integer advertiserId = 56; // Integer | Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts.
        String campaignId = "campaignId_example"; // String | Show only metrics for this campaign (default all campaigns)
        String clickAttributionPolicy = "Both"; // String | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS
        Integer count = 56; // Integer | Return up to the first count rows of data (default is all rows)
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Filter out all events that occur after date (default is today’s date)
        String intervalSize = "Hour"; // String | Specify the aggregation interval for events used to compute stats (default is \"day\")
        String sellerId = "sellerId_example"; // String | Show only metrics for this seller (default all sellers)
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Filter out all events that occur before date (default is the value of `endDate`)
        String timeZoneId = "timeZoneId_example"; // String | Specify the timezone used in the aggregations (IANA code).
        try {
            StatsReportMessage result = apiInstance.getMarketplaceSellerCampaignsStats(advertiserId, campaignId, clickAttributionPolicy, count, endDate, intervalSize, sellerId, startDate, timeZoneId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellerCampaignsStats");
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
| **advertiserId** | **Integer**| Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts. | [optional] |
| **campaignId** | **String**| Show only metrics for this campaign (default all campaigns) | [optional] |
| **clickAttributionPolicy** | **String**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] [default to AnySeller] [enum: Both, SameSeller, AnySeller] |
| **count** | **Integer**| Return up to the first count rows of data (default is all rows) | [optional] |
| **endDate** | **OffsetDateTime**| Filter out all events that occur after date (default is today’s date) | [optional] |
| **intervalSize** | **String**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] [default to Day] [enum: Hour, Day, Month, Year] |
| **sellerId** | **String**| Show only metrics for this seller (default all sellers) | [optional] |
| **startDate** | **OffsetDateTime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] |
| **timeZoneId** | **String**| Specify the timezone used in the aggregations (IANA code). | [optional] |

### Return type

[**StatsReportMessage**](StatsReportMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellers

> List&lt;SellerBase&gt; getMarketplaceSellers(advertiserId, campaignId, sellerName, sellerStatus, withBudgetStatus, withProducts)

/2026-07/marketing-solutions/marketplace-performance-outcomes/sellers

Return a collection of sellers filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        Integer advertiserId = 56; // Integer | Return only sellers belonging to the specified advertiser
        Integer campaignId = 56; // Integer | Return only sellers belonging to the specified campaign
        String sellerName = "sellerName_example"; // String | Return only sellers with the matching name.
        String sellerStatus = "Inactive"; // String | Return only sellers with specific status.
        String withBudgetStatus = "Archived"; // String | Return only sellers with specific budget status.
        Boolean withProducts = true; // Boolean | Return only sellers with or without products in catalog.
        try {
            List<SellerBase> result = apiInstance.getMarketplaceSellers(advertiserId, campaignId, sellerName, sellerStatus, withBudgetStatus, withProducts);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellers");
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
| **advertiserId** | **Integer**| Return only sellers belonging to the specified advertiser | [optional] |
| **campaignId** | **Integer**| Return only sellers belonging to the specified campaign | [optional] |
| **sellerName** | **String**| Return only sellers with the matching name. | [optional] |
| **sellerStatus** | **String**| Return only sellers with specific status. | [optional] [enum: Inactive, Active] |
| **withBudgetStatus** | **String**| Return only sellers with specific budget status. | [optional] [enum: Archived, Current, Scheduled] |
| **withProducts** | **Boolean**| Return only sellers with or without products in catalog. | [optional] |

### Return type

[**List&lt;SellerBase&gt;**](SellerBase.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellersByAdvertiser

> List&lt;SellerBase&gt; getMarketplaceSellersByAdvertiser(advertiserId, requestBody, partnerId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers

Create new sellers for an advertiser

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String advertiserId = "advertiserId_example"; // String | Id of the advertiser
        List<String> requestBody = Arrays.asList(); // List<String> | Names of the sellers to associate with new Ids
        Integer partnerId = 56; // Integer | Id of the partner
        try {
            List<SellerBase> result = apiInstance.getMarketplaceSellersByAdvertiser(advertiserId, requestBody, partnerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellersByAdvertiser");
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
| **advertiserId** | **String**| Id of the advertiser | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| Names of the sellers to associate with new Ids | |
| **partnerId** | **Integer**| Id of the partner | [optional] |

### Return type

[**List&lt;SellerBase&gt;**](SellerBase.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getMarketplaceSellersStats

> StatsReportMessage getMarketplaceSellersStats(advertiserId, clickAttributionPolicy, count, endDate, intervalSize, sellerId, startDate, timeZoneId)

/2026-07/marketing-solutions/marketplace-performance-outcomes/stats/sellers

## Dimensions                Get performance statistics aggregated for _sellers_. The seller id appears  in the output in the first column and the seller name appears in the second.                Aggregation can be done by &#x60;hour&#x60;, &#x60;day&#x60;, &#x60;month&#x60;, or &#x60;year&#x60; aligned with the user timezone  if provided. The aggregation interval size is controlled by &#x60;intervalSize&#x60;. The time interval  appears in the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR &#x3D; Conversion Rate | salesUnits / clicks  G | CPO &#x3D; Cost Per Order | cost / salesUnits  H | COS &#x3D; Cost of Sale | cost / revenue  I | ROAS &#x3D; Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by &#x60;clickAttributionPolicy&#x60;.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by seller id, date or count.                Filtering the results to events associated with a specific seller is done by setting  the &#x60;sellerId&#x60; filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the &#x60;startDate&#x60; and  &#x60;endDate&#x60; filter parameters using the &#x60;yyyy-MM-DD&#x60; format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is &#x60;hour&#x60;, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  &#x60;count&#x60; filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is &#x60;application/json&#x60; and  &#x60;text/csv&#x60;.                &#x60;&#x60;&#x60;json  {      \&quot;columns\&quot;: [\&quot;sellerId\&quot;, \&quot;sellerName\&quot;, \&quot;month\&quot;, \&quot;impressions\&quot;, \&quot;clicks\&quot;, \&quot;cost\&quot;, \&quot;saleUnits\&quot;, \&quot;revenue\&quot;, \&quot;cr\&quot;, \&quot;cpo\&quot;, \&quot;cos\&quot;, \&quot;roas\&quot;],      \&quot;data\&quot;: [         [1200972, \&quot;sellerA\&quot;, \&quot;2019-05-01\&quot;, 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],         [1200972, \&quot;sellerA\&quot;, \&quot;2019-06-01\&quot;, 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],         [1200974, \&quot;sellerB\&quot;, \&quot;2019-05-01\&quot;, 10102, 47, 3.29, 3, 396000.0, 0.063, 1.096, 8.308E-6, 120364.741],         [1200974, \&quot;sellerB\&quot;, \&quot;2019-06-01\&quot;, 11576, 54, 3.78, 1, 132000.0, 0.018, 3.78, 2.863E-5, 34920.634]      ],      \&quot;rows\&quot;: 4  }  &#x60;&#x60;&#x60;                The JSON result is an object with three fields (&#x60;columns&#x60;, &#x60;data&#x60;, and &#x60;rows&#x60;). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the seller id and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the &#x60;intervalSize&#x60; parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining metrics depend on the &#x60;clickAttributionPolicy&#x60; parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        Integer advertiserId = 56; // Integer | Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts.
        String clickAttributionPolicy = "Both"; // String | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS
        Integer count = 56; // Integer | Return up to the first count rows of data (default is all rows)
        OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Filter out all events that occur after date (default is today’s date)
        String intervalSize = "Hour"; // String | Specify the aggregation interval for events used to compute stats (default is \"day\")
        String sellerId = "sellerId_example"; // String | Show only metrics for this seller (default all sellers)
        OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Filter out all events that occur before date (default is the value of `endDate`)
        String timeZoneId = "timeZoneId_example"; // String | Specify the timezone used in the aggregations (IANA code).
        try {
            StatsReportMessage result = apiInstance.getMarketplaceSellersStats(advertiserId, clickAttributionPolicy, count, endDate, intervalSize, sellerId, startDate, timeZoneId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getMarketplaceSellersStats");
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
| **advertiserId** | **Integer**| Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts. | [optional] |
| **clickAttributionPolicy** | **String**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] [default to AnySeller] [enum: Both, SameSeller, AnySeller] |
| **count** | **Integer**| Return up to the first count rows of data (default is all rows) | [optional] |
| **endDate** | **OffsetDateTime**| Filter out all events that occur after date (default is today’s date) | [optional] |
| **intervalSize** | **String**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] [default to Day] [enum: Hour, Day, Month, Year] |
| **sellerId** | **String**| Show only metrics for this seller (default all sellers) | [optional] |
| **startDate** | **OffsetDateTime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] |
| **timeZoneId** | **String**| Specify the timezone used in the aggregations (IANA code). | [optional] |

### Return type

[**StatsReportMessage**](StatsReportMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## patchAdSetCategoryBids

> PatchAdSetCategoryBidResultListResponse patchAdSetCategoryBids(adSetId, patchAdSetCategoryBidListRequest)

/2026-07/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Update the Category Bids for given Categories associated to an Ad Set  Patch Category Bids for one or more Categories in a single request. Partial success policy is followed.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/ad-sets

Patch a list of AdSets.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/campaigns

Patch a list of Campaigns.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Update the Display Multipliers for given Categories associated to an Ad Set  Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## searchAdSets

> ResponsesReadAdSetV26Q1 searchAdSets(adSetSearchRequestV26Q1)

/2026-07/marketing-solutions/ad-sets/search

Search for ad sets based on provided criteria.  This returns the full configuration of ad sets matching those criteria.  Field projection can be used if only a subset of fields is required, instead of the full configuration.                If specific fields are precised in the user prompt, use meta.fields field projection in order to query only the value of these fields, else, provide every field.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/campaigns/search

Search endpoint for campaigns                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## startAdSets

> ResponsesAdSetId startAdSets(requestsAdSetId)

/2026-07/marketing-solutions/ad-sets/start

Start the specified list of ad sets

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/ad-sets/stop

Stop the specified list of ad sets

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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

/2026-07/marketing-solutions/ad-sets/{ad-set-id}/audience

Link or unlink an audience with an ad set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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


## updateMarketplaceSellerBudget

> SellerBudgetMessage updateMarketplaceSellerBudget(budgetId, updateSellerBudgetMessageBase)

/2026-07/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId}

Modify an existing active budget to change its limitations or status.  All three types of budgets can be modified.                See the additional restrictions listed in the PATCH budgets endpoint.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String budgetId = "budgetId_example"; // String | Id of the budget
        UpdateSellerBudgetMessageBase updateSellerBudgetMessageBase = new UpdateSellerBudgetMessageBase(); // UpdateSellerBudgetMessageBase | 
        try {
            SellerBudgetMessage result = apiInstance.updateMarketplaceSellerBudget(budgetId, updateSellerBudgetMessageBase);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateMarketplaceSellerBudget");
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
| **budgetId** | **String**| Id of the budget | |
| **updateSellerBudgetMessageBase** | [**UpdateSellerBudgetMessageBase**](UpdateSellerBudgetMessageBase.md)|  | |

### Return type

[**SellerBudgetMessage**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateMarketplaceSellerBudgets

> List&lt;SellerBudgetMessage&gt; updateMarketplaceSellerBudgets(updateSellerBudgetMessage)

/2026-07/marketing-solutions/marketplace-performance-outcomes/budgets

Modify one or more existing active budgets to change their limitations or status.  All three types of budgets can be modified.                The following constraints apply when modifying an existing budget.                • &lt;b&gt;campaignIds&lt;/b&gt;: a non-empty subset of the original campaign ids MAY be supplied&lt;br /&gt;  • &lt;b&gt;amount&lt;/b&gt;: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative&lt;br /&gt;  • &lt;b&gt;startDate&lt;/b&gt;: a future start date MAY be supplied for budgets that have not yet started&lt;br /&gt;  • &lt;b&gt;endDate&lt;/b&gt;: an end date MAY be supplied and if supplied MUST be a future date greater than the start date&lt;br /&gt;                Other attributes MUST NOT be supplied.                Adding new campaigns to a budget is not allowed. In addition, reducing the amount for  a Capped budget to a value less than the current spend not allowed.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        List<UpdateSellerBudgetMessage> updateSellerBudgetMessage = Arrays.asList(); // List<UpdateSellerBudgetMessage> | 
        try {
            List<SellerBudgetMessage> result = apiInstance.updateMarketplaceSellerBudgets(updateSellerBudgetMessage);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateMarketplaceSellerBudgets");
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
| **updateSellerBudgetMessage** | [**List&lt;UpdateSellerBudgetMessage&gt;**](UpdateSellerBudgetMessage.md)|  | |

### Return type

[**List&lt;SellerBudgetMessage&gt;**](SellerBudgetMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateMarketplaceSellerCampaign

> SellerCampaignMessage updateMarketplaceSellerCampaign(sellerCampaignId, bid)

/2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}

Patching a seller campaign allows the bid to be modified. The bid must be a non-negative value.  Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        String sellerCampaignId = "sellerCampaignId_example"; // String | Composite id of the seller campaign to update in the format `{sellerId}.{campaignId}`, e.g. `2578464.187625`.
        Double bid = 3.4D; // Double | The new bid for the seller campaign.
        try {
            SellerCampaignMessage result = apiInstance.updateMarketplaceSellerCampaign(sellerCampaignId, bid);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateMarketplaceSellerCampaign");
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
| **sellerCampaignId** | **String**| Composite id of the seller campaign to update in the format &#x60;{sellerId}.{campaignId}&#x60;, e.g. &#x60;2578464.187625&#x60;. | |
| **bid** | **Double**| The new bid for the seller campaign. | [optional] |

### Return type

[**SellerCampaignMessage**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateMarketplaceSellerCampaigns

> List&lt;SellerCampaignMessage&gt; updateMarketplaceSellerCampaigns(sellerCampaignUpdate)

/2026-07/marketing-solutions/marketplace-performance-outcomes/seller-campaigns

Patching a collection of seller campaigns allows their bids to be modified.  Each bid must be a non-negative value. Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.CampaignApi;

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
        List<SellerCampaignUpdate> sellerCampaignUpdate = Arrays.asList(); // List<SellerCampaignUpdate> | 
        try {
            List<SellerCampaignMessage> result = apiInstance.updateMarketplaceSellerCampaigns(sellerCampaignUpdate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateMarketplaceSellerCampaigns");
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
| **sellerCampaignUpdate** | [**List&lt;SellerCampaignUpdate&gt;**](SellerCampaignUpdate.md)|  | |

### Return type

[**List&lt;SellerCampaignMessage&gt;**](SellerCampaignMessage.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

