# CampaignApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRemoveKeywords**](CampaignApi.md#addRemoveKeywords) | **POST** /2027-01/retail-media/line-items/{id}/keywords/add-remove | /2027-01/retail-media/line-items/{id}/keywords/add-remove |
| [**appendAddToBasketTargetsByLineItemId**](CampaignApi.md#appendAddToBasketTargetsByLineItemId) | **POST** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append |
| [**appendAudienceTargetsByLineItemId**](CampaignApi.md#appendAudienceTargetsByLineItemId) | **POST** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append |
| [**appendCampaignsToBalanceV1**](CampaignApi.md#appendCampaignsToBalanceV1) | **POST** /2027-01/retail-media/balances/{balanceId}/campaigns/append | /2027-01/retail-media/balances/{balanceId}/campaigns/append |
| [**appendPromotedProducts**](CampaignApi.md#appendPromotedProducts) | **POST** /2027-01/retail-media/line-items/{line-item-id}/products/append | /2027-01/retail-media/line-items/{line-item-id}/products/append |
| [**appendStoreTargetsByLineItemId**](CampaignApi.md#appendStoreTargetsByLineItemId) | **POST** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append |
| [**createAsset**](CampaignApi.md#createAsset) | **POST** /2027-01/retail-media/assets | /2027-01/retail-media/assets |
| [**createAuctionLineItem**](CampaignApi.md#createAuctionLineItem) | **POST** /2027-01/retail-media/campaigns/{campaignId}/auction-line-items | /2027-01/retail-media/campaigns/{campaignId}/auction-line-items |
| [**createBrandCatalogExport**](CampaignApi.md#createBrandCatalogExport) | **POST** /2027-01/retail-media/accounts/{accountId}/brand-catalog-export | /2027-01/retail-media/accounts/{accountId}/brand-catalog-export |
| [**createCampaignsByAccountId**](CampaignApi.md#createCampaignsByAccountId) | **POST** /2027-01/retail-media/accounts/{account-id}/campaigns | /2027-01/retail-media/accounts/{account-id}/campaigns |
| [**createCreative**](CampaignApi.md#createCreative) | **POST** /2027-01/retail-media/accounts/{account-id}/creatives | /2027-01/retail-media/accounts/{account-id}/creatives |
| [**createPreferredLineItemByCampaignId**](CampaignApi.md#createPreferredLineItemByCampaignId) | **POST** /2027-01/retail-media/campaigns/{campaign-id}/preferred-line-items | /2027-01/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**createSellerCatalogExport**](CampaignApi.md#createSellerCatalogExport) | **POST** /2027-01/retail-media/accounts/{accountId}/seller-catalog-export | /2027-01/retail-media/accounts/{accountId}/seller-catalog-export |
| [**deleteAddToBasketTargetsByLineItemId**](CampaignApi.md#deleteAddToBasketTargetsByLineItemId) | **POST** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete |
| [**deleteAudienceTargetsByLineItemId**](CampaignApi.md#deleteAudienceTargetsByLineItemId) | **POST** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete |
| [**deleteCampaignsFromBalanceV1**](CampaignApi.md#deleteCampaignsFromBalanceV1) | **POST** /2027-01/retail-media/balances/{balanceId}/campaigns/delete | /2027-01/retail-media/balances/{balanceId}/campaigns/delete |
| [**deletePromotedProducts**](CampaignApi.md#deletePromotedProducts) | **POST** /2027-01/retail-media/line-items/{line-item-id}/products/delete | /2027-01/retail-media/line-items/{line-item-id}/products/delete |
| [**deleteStoreTargetByLineItemId**](CampaignApi.md#deleteStoreTargetByLineItemId) | **POST** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete |
| [**fetchPromotedProducts**](CampaignApi.md#fetchPromotedProducts) | **GET** /2027-01/retail-media/line-items/{line-item-id}/products | /2027-01/retail-media/line-items/{line-item-id}/products |
| [**getAccountCreatives**](CampaignApi.md#getAccountCreatives) | **GET** /2027-01/retail-media/accounts/{account-id}/creatives | /2027-01/retail-media/accounts/{account-id}/creatives |
| [**getAddToBasketTargetsByLineItemId**](CampaignApi.md#getAddToBasketTargetsByLineItemId) | **GET** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket |
| [**getApi202110ExternalRetailerPagesByRetailerId**](CampaignApi.md#getApi202110ExternalRetailerPagesByRetailerId) | **GET** /2027-01/retail-media/retailers/{retailerId}/pages | /2027-01/retail-media/retailers/{retailerId}/pages |
| [**getApiExternalV1Categories**](CampaignApi.md#getApiExternalV1Categories) | **GET** /2027-01/retail-media/categories | /2027-01/retail-media/categories |
| [**getAuctionLineItem**](CampaignApi.md#getAuctionLineItem) | **GET** /2027-01/retail-media/auction-line-items/{lineItemId} | /2027-01/retail-media/auction-line-items/{lineItemId} |
| [**getAuctionLineItemsByCampaign**](CampaignApi.md#getAuctionLineItemsByCampaign) | **GET** /2027-01/retail-media/campaigns/{campaignId}/auction-line-items | /2027-01/retail-media/campaigns/{campaignId}/auction-line-items |
| [**getAudienceTargetsByLineItemId**](CampaignApi.md#getAudienceTargetsByLineItemId) | **GET** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences |
| [**getBidMultipliersByLineItemId**](CampaignApi.md#getBidMultipliersByLineItemId) | **GET** /2027-01/retail-media/line-items/{line-item-id}/bid-multipliers | /2027-01/retail-media/line-items/{line-item-id}/bid-multipliers |
| [**getBrandsByAccountId**](CampaignApi.md#getBrandsByAccountId) | **GET** /2027-01/retail-media/accounts/{accountId}/brands | /2027-01/retail-media/accounts/{accountId}/brands |
| [**getCampaignBudgetOverrides**](CampaignApi.md#getCampaignBudgetOverrides) | **GET** /2027-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | /2027-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides |
| [**getCampaignByCampaignId**](CampaignApi.md#getCampaignByCampaignId) | **GET** /2027-01/retail-media/campaigns/{campaignId} | /2027-01/retail-media/campaigns/{campaignId} |
| [**getCampaignsByAccountId**](CampaignApi.md#getCampaignsByAccountId) | **GET** /2027-01/retail-media/accounts/{account-id}/campaigns | /2027-01/retail-media/accounts/{account-id}/campaigns |
| [**getCatalogOutput**](CampaignApi.md#getCatalogOutput) | **GET** /2027-01/retail-media/catalogs/{catalogId}/output | /2027-01/retail-media/catalogs/{catalogId}/output |
| [**getCatalogStatus**](CampaignApi.md#getCatalogStatus) | **GET** /2027-01/retail-media/catalogs/{catalogId}/status | /2027-01/retail-media/catalogs/{catalogId}/status |
| [**getCategory**](CampaignApi.md#getCategory) | **GET** /2027-01/retail-media/categories/{categoryId} | /2027-01/retail-media/categories/{categoryId} |
| [**getCpcMinBidsBySkuIdsV1**](CampaignApi.md#getCpcMinBidsBySkuIdsV1) | **POST** /2027-01/retail-media/retailers/{retailerId}/cpc-min-bids | /2027-01/retail-media/retailers/{retailerId}/cpc-min-bids |
| [**getCreative**](CampaignApi.md#getCreative) | **GET** /2027-01/retail-media/accounts/{account-id}/creatives/{creative-id} | /2027-01/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**getCreativeTemplate**](CampaignApi.md#getCreativeTemplate) | **GET** /2027-01/retail-media/retailers/{retailer-id}/templates/{template-id} | /2027-01/retail-media/retailers/{retailer-id}/templates/{template-id} |
| [**getKeywordInReviewReport**](CampaignApi.md#getKeywordInReviewReport) | **GET** /2027-01/retail-media/accounts/{account-id}/keywords/in-review-report | /2027-01/retail-media/accounts/{account-id}/keywords/in-review-report |
| [**getLineItemBudgetOverrides**](CampaignApi.md#getLineItemBudgetOverrides) | **GET** /2027-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | /2027-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides |
| [**getLineItemsByAccountId**](CampaignApi.md#getLineItemsByAccountId) | **GET** /2027-01/retail-media/accounts/{account-id}/line-items | /2027-01/retail-media/accounts/{account-id}/line-items |
| [**getLineItemsByCampaignId**](CampaignApi.md#getLineItemsByCampaignId) | **GET** /2027-01/retail-media/line-items/{line-item-id} | /2027-01/retail-media/line-items/{line-item-id} |
| [**getPreferredLineItemsByCampaignId**](CampaignApi.md#getPreferredLineItemsByCampaignId) | **GET** /2027-01/retail-media/campaigns/{campaign-id}/preferred-line-items | /2027-01/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**getPreferredLineItemsByLineItemId**](CampaignApi.md#getPreferredLineItemsByLineItemId) | **GET** /2027-01/retail-media/preferred-line-items/{line-item-id} | /2027-01/retail-media/preferred-line-items/{line-item-id} |
| [**getRecommendedCategories**](CampaignApi.md#getRecommendedCategories) | **POST** /2027-01/retail-media/retailers/{retailerId}/recommend-categories | /2027-01/retail-media/retailers/{retailerId}/recommend-categories |
| [**getRecommendedKeywords**](CampaignApi.md#getRecommendedKeywords) | **GET** /2027-01/retail-media/line-items/{externalLineItemId}/keywords/recommended | /2027-01/retail-media/line-items/{externalLineItemId}/keywords/recommended |
| [**getRetailerCreativeTemplates**](CampaignApi.md#getRetailerCreativeTemplates) | **GET** /2027-01/retail-media/retailers/{retailer-id}/templates | /2027-01/retail-media/retailers/{retailer-id}/templates |
| [**getStoreTargetsByLineItemId**](CampaignApi.md#getStoreTargetsByLineItemId) | **GET** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores |
| [**pausePromotedProducts**](CampaignApi.md#pausePromotedProducts) | **POST** /2027-01/retail-media/line-items/{line-item-id}/products/pause | /2027-01/retail-media/line-items/{line-item-id}/products/pause |
| [**postApiExternalV1AccountCatalogsSellersByAccountId**](CampaignApi.md#postApiExternalV1AccountCatalogsSellersByAccountId) | **POST** /2027-01/retail-media/accounts/{accountId}/catalogs/sellers | /2027-01/retail-media/accounts/{accountId}/catalogs/sellers |
| [**postApiV1ExternalAccountCatalogsByAccountId**](CampaignApi.md#postApiV1ExternalAccountCatalogsByAccountId) | **POST** /2027-01/retail-media/accounts/{accountId}/catalogs | /2027-01/retail-media/accounts/{accountId}/catalogs |
| [**putAddToBasketTargetByLineItemId**](CampaignApi.md#putAddToBasketTargetByLineItemId) | **PUT** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket |
| [**putAudienceTargetsByLineItemId**](CampaignApi.md#putAudienceTargetsByLineItemId) | **PUT** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences |
| [**putStoreTargetByLineItemId**](CampaignApi.md#putStoreTargetByLineItemId) | **PUT** /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | /2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores |
| [**recommendedKeywords**](CampaignApi.md#recommendedKeywords) | **POST** /2027-01/retail-media/retailers/{retailerId}/recommend-keywords | /2027-01/retail-media/retailers/{retailerId}/recommend-keywords |
| [**searchAccountCreatives**](CampaignApi.md#searchAccountCreatives) | **POST** /2027-01/retail-media/accounts/{account-id}/creatives/search | /2027-01/retail-media/accounts/{account-id}/creatives/search |
| [**searchAccountRetailers**](CampaignApi.md#searchAccountRetailers) | **POST** /2027-01/retail-media/accounts/{accountId}/retailers/search | /2027-01/retail-media/accounts/{accountId}/retailers/search |
| [**searchCategory**](CampaignApi.md#searchCategory) | **POST** /2027-01/retail-media/retailers/{retailerId}/categories/search | /2027-01/retail-media/retailers/{retailerId}/categories/search |
| [**setKeywordBids**](CampaignApi.md#setKeywordBids) | **POST** /2027-01/retail-media/line-items/{id}/keywords/set-bid | /2027-01/retail-media/line-items/{id}/keywords/set-bid |
| [**unpausePromotedProducts**](CampaignApi.md#unpausePromotedProducts) | **POST** /2027-01/retail-media/line-items/{line-item-id}/products/unpause | /2027-01/retail-media/line-items/{line-item-id}/products/unpause |
| [**updateAuctionLineItem**](CampaignApi.md#updateAuctionLineItem) | **PUT** /2027-01/retail-media/auction-line-items/{lineItemId} | /2027-01/retail-media/auction-line-items/{lineItemId} |
| [**updateBidMultipliersByLineItemId**](CampaignApi.md#updateBidMultipliersByLineItemId) | **PUT** /2027-01/retail-media/line-items/{line-item-id}/bid-multipliers | /2027-01/retail-media/line-items/{line-item-id}/bid-multipliers |
| [**updateCampaignBudgetOverrides**](CampaignApi.md#updateCampaignBudgetOverrides) | **PUT** /2027-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | /2027-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides |
| [**updateCampaignByCampaignId**](CampaignApi.md#updateCampaignByCampaignId) | **PUT** /2027-01/retail-media/campaigns/{campaignId} | /2027-01/retail-media/campaigns/{campaignId} |
| [**updateCreative**](CampaignApi.md#updateCreative) | **PUT** /2027-01/retail-media/accounts/{account-id}/creatives/{creative-id} | /2027-01/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**updateKeywordReviews**](CampaignApi.md#updateKeywordReviews) | **POST** /2027-01/retail-media/line-items/{line-item-id}/keywords/review | /2027-01/retail-media/line-items/{line-item-id}/keywords/review |
| [**updateLineItemBudgetOverrides**](CampaignApi.md#updateLineItemBudgetOverrides) | **PUT** /2027-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | /2027-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides |
| [**updatePreferredLineItemByLineItemId**](CampaignApi.md#updatePreferredLineItemByLineItemId) | **PUT** /2027-01/retail-media/preferred-line-items/{line-item-id} | /2027-01/retail-media/preferred-line-items/{line-item-id} |



## addRemoveKeywords

> ResourceOutcome addRemoveKeywords(id, addRemoveKeywordsModelRequest)

/2027-01/retail-media/line-items/{id}/keywords/add-remove

Add or Remove keywords from the line item in bulk

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String id = "id_example"; // String | ID of the line item
        AddRemoveKeywordsModelRequest addRemoveKeywordsModelRequest = new AddRemoveKeywordsModelRequest(); // AddRemoveKeywordsModelRequest | 
        try {
            ResourceOutcome result = apiInstance.addRemoveKeywords(id, addRemoveKeywordsModelRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#addRemoveKeywords");
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
| **id** | **String**| ID of the line item | |
| **addRemoveKeywordsModelRequest** | [**AddRemoveKeywordsModelRequest**](AddRemoveKeywordsModelRequest.md)|  | [optional] |

### Return type

[**ResourceOutcome**](ResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## appendAddToBasketTargetsByLineItemId

> AddToBasketTarget202110Response appendAddToBasketTargetsByLineItemId(lineItemId, addToBasketIdsUpdateModel202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append

This endpoint appends one or more add to basket ids to targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        AddToBasketIdsUpdateModel202110Request addToBasketIdsUpdateModel202110Request = new AddToBasketIdsUpdateModel202110Request(); // AddToBasketIdsUpdateModel202110Request | Ids to append to the target
        try {
            AddToBasketTarget202110Response result = apiInstance.appendAddToBasketTargetsByLineItemId(lineItemId, addToBasketIdsUpdateModel202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#appendAddToBasketTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **addToBasketIdsUpdateModel202110Request** | [**AddToBasketIdsUpdateModel202110Request**](AddToBasketIdsUpdateModel202110Request.md)| Ids to append to the target | [optional] |

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## appendAudienceTargetsByLineItemId

> AudienceTarget202110Response appendAudienceTargetsByLineItemId(lineItemId, audienceIdsUpdateModel202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append

This endpoint appends one or more audiences ids to targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        AudienceIdsUpdateModel202110Request audienceIdsUpdateModel202110Request = new AudienceIdsUpdateModel202110Request(); // AudienceIdsUpdateModel202110Request | Audience ids to append to the target
        try {
            AudienceTarget202110Response result = apiInstance.appendAudienceTargetsByLineItemId(lineItemId, audienceIdsUpdateModel202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#appendAudienceTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **audienceIdsUpdateModel202110Request** | [**AudienceIdsUpdateModel202110Request**](AudienceIdsUpdateModel202110Request.md)| Audience ids to append to the target | [optional] |

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## appendCampaignsToBalanceV1

> ValueResourceOutcomeBalanceCampaignsV1 appendCampaignsToBalanceV1(balanceId, valueResourceInputAppendCampaignsRequestV1)

/2027-01/retail-media/balances/{balanceId}/campaigns/append

Appends one or more campaigns to the specified balance

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String balanceId = "balanceId_example"; // String | The balance to add campaigns from
        ValueResourceInputAppendCampaignsRequestV1 valueResourceInputAppendCampaignsRequestV1 = new ValueResourceInputAppendCampaignsRequestV1(); // ValueResourceInputAppendCampaignsRequestV1 | The balance campaign appending request.
        try {
            ValueResourceOutcomeBalanceCampaignsV1 result = apiInstance.appendCampaignsToBalanceV1(balanceId, valueResourceInputAppendCampaignsRequestV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#appendCampaignsToBalanceV1");
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
| **balanceId** | **String**| The balance to add campaigns from | |
| **valueResourceInputAppendCampaignsRequestV1** | [**ValueResourceInputAppendCampaignsRequestV1**](ValueResourceInputAppendCampaignsRequestV1.md)| The balance campaign appending request. | |

### Return type

[**ValueResourceOutcomeBalanceCampaignsV1**](ValueResourceOutcomeBalanceCampaignsV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## appendPromotedProducts

> ProductResourceOutcome appendPromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/2027-01/retail-media/line-items/{line-item-id}/products/append

Append a collection of promoted products to a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | ID of the line item
        PromotedProductResourceCollectionInput promotedProductResourceCollectionInput = new PromotedProductResourceCollectionInput(); // PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.
        try {
            ProductResourceOutcome result = apiInstance.appendPromotedProducts(lineItemId, promotedProductResourceCollectionInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#appendPromotedProducts");
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
| **lineItemId** | **String**| ID of the line item | |
| **promotedProductResourceCollectionInput** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

[**ProductResourceOutcome**](ProductResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Promoted products appended to the line item with warnings |  -  |
| **204** | Promoted products appended to the line item |  -  |


## appendStoreTargetsByLineItemId

> StoreTarget202110Response appendStoreTargetsByLineItemId(lineItemId, storeIdsUpdateModel202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append

This endpoint appends one or more store ids to targeting on the specified line item.  The resulting state of the store target is returned.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        StoreIdsUpdateModel202110Request storeIdsUpdateModel202110Request = new StoreIdsUpdateModel202110Request(); // StoreIdsUpdateModel202110Request | Store ids to append to the target
        try {
            StoreTarget202110Response result = apiInstance.appendStoreTargetsByLineItemId(lineItemId, storeIdsUpdateModel202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#appendStoreTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **storeIdsUpdateModel202110Request** | [**StoreIdsUpdateModel202110Request**](StoreIdsUpdateModel202110Request.md)| Store ids to append to the target | [optional] |

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## createAsset

> AssetResponse createAsset(assetFile)

/2027-01/retail-media/assets

Creates an asset

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        File assetFile = new File("/path/to/file"); // File | The asset binary content
        try {
            AssetResponse result = apiInstance.createAsset(assetFile);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createAsset");
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
| **assetFile** | **File**| The asset binary content | |

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## createAuctionLineItem

> EntityResourceOutcomeOfSponsoredProductsLineItem createAuctionLineItem(campaignId, valueResourceInputOfSponsoredProductsLineItemCreateRequestModel)

/2027-01/retail-media/campaigns/{campaignId}/auction-line-items

Creates new auction line item with the specified settings

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | The given campaign id
        ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel valueResourceInputOfSponsoredProductsLineItemCreateRequestModel = new ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel(); // ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel | The line item settings to create a line item with
        try {
            EntityResourceOutcomeOfSponsoredProductsLineItem result = apiInstance.createAuctionLineItem(campaignId, valueResourceInputOfSponsoredProductsLineItemCreateRequestModel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createAuctionLineItem");
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
| **campaignId** | **String**| The given campaign id | |
| **valueResourceInputOfSponsoredProductsLineItemCreateRequestModel** | [**ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel**](ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel.md)| The line item settings to create a line item with | |

### Return type

[**EntityResourceOutcomeOfSponsoredProductsLineItem**](EntityResourceOutcomeOfSponsoredProductsLineItem.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## createBrandCatalogExport

> EntityResourceOutcomeOfCatalogStatusV2 createBrandCatalogExport(accountId, valueResourceInputOfBrandCatalogRequestV2)

/2027-01/retail-media/accounts/{accountId}/brand-catalog-export

Create a request for a Catalog available to the indicated account.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The account to request the catalog for.
        ValueResourceInputOfBrandCatalogRequestV2 valueResourceInputOfBrandCatalogRequestV2 = new ValueResourceInputOfBrandCatalogRequestV2(); // ValueResourceInputOfBrandCatalogRequestV2 | 
        try {
            EntityResourceOutcomeOfCatalogStatusV2 result = apiInstance.createBrandCatalogExport(accountId, valueResourceInputOfBrandCatalogRequestV2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createBrandCatalogExport");
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
| **accountId** | **String**| The account to request the catalog for. | |
| **valueResourceInputOfBrandCatalogRequestV2** | [**ValueResourceInputOfBrandCatalogRequestV2**](ValueResourceInputOfBrandCatalogRequestV2.md)|  | |

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog request successfully created |  -  |


## createCampaignsByAccountId

> JsonApiSingleResponseOfCampaignV202301 createCampaignsByAccountId(accountId, postCampaignV202301)

/2027-01/retail-media/accounts/{account-id}/campaigns

Creates a new campaign with the specified settings

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The given account id
        PostCampaignV202301 postCampaignV202301 = new PostCampaignV202301(); // PostCampaignV202301 | The campaign settings to create a campaign with
        try {
            JsonApiSingleResponseOfCampaignV202301 result = apiInstance.createCampaignsByAccountId(accountId, postCampaignV202301);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createCampaignsByAccountId");
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
| **accountId** | **String**| The given account id | |
| **postCampaignV202301** | [**PostCampaignV202301**](PostCampaignV202301.md)| The campaign settings to create a campaign with | |

### Return type

[**JsonApiSingleResponseOfCampaignV202301**](JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## createCreative

> Creative202210Response createCreative(accountId, creativeCreateModel202207)

/2027-01/retail-media/accounts/{account-id}/creatives

Create a creative for an account

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | External account id to create a creative for
        CreativeCreateModel202207 creativeCreateModel202207 = new CreativeCreateModel202207(); // CreativeCreateModel202207 | The creative to create
        try {
            Creative202210Response result = apiInstance.createCreative(accountId, creativeCreateModel202207);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createCreative");
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
| **accountId** | **String**| External account id to create a creative for | |
| **creativeCreateModel202207** | [**CreativeCreateModel202207**](CreativeCreateModel202207.md)| The creative to create | |

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creatives created |  -  |


## createPreferredLineItemByCampaignId

> PreferredLineItemV2Response createPreferredLineItemByCampaignId(campaignId, preferredLineItemCreateModelV2Request)

/2027-01/retail-media/campaigns/{campaign-id}/preferred-line-items

Creates a new preferred line item with the specified settings

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | The given campaign id
        PreferredLineItemCreateModelV2Request preferredLineItemCreateModelV2Request = new PreferredLineItemCreateModelV2Request(); // PreferredLineItemCreateModelV2Request | The line item settings to create a line item with
        try {
            PreferredLineItemV2Response result = apiInstance.createPreferredLineItemByCampaignId(campaignId, preferredLineItemCreateModelV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createPreferredLineItemByCampaignId");
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
| **campaignId** | **String**| The given campaign id | |
| **preferredLineItemCreateModelV2Request** | [**PreferredLineItemCreateModelV2Request**](PreferredLineItemCreateModelV2Request.md)| The line item settings to create a line item with | |

### Return type

[**PreferredLineItemV2Response**](PreferredLineItemV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## createSellerCatalogExport

> EntityResourceOutcomeOfCatalogStatusV2 createSellerCatalogExport(accountId, valueResourceInputOfSellerCatalogRequestV2)

/2027-01/retail-media/accounts/{accountId}/seller-catalog-export

Create a request for a Catalog available to the indicated account.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The account to request the catalog for.
        ValueResourceInputOfSellerCatalogRequestV2 valueResourceInputOfSellerCatalogRequestV2 = new ValueResourceInputOfSellerCatalogRequestV2(); // ValueResourceInputOfSellerCatalogRequestV2 | 
        try {
            EntityResourceOutcomeOfCatalogStatusV2 result = apiInstance.createSellerCatalogExport(accountId, valueResourceInputOfSellerCatalogRequestV2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#createSellerCatalogExport");
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
| **accountId** | **String**| The account to request the catalog for. | |
| **valueResourceInputOfSellerCatalogRequestV2** | [**ValueResourceInputOfSellerCatalogRequestV2**](ValueResourceInputOfSellerCatalogRequestV2.md)|  | |

### Return type

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog request successfully created |  -  |


## deleteAddToBasketTargetsByLineItemId

> AddToBasketTarget202110Response deleteAddToBasketTargetsByLineItemId(lineItemId, addToBasketIdsUpdateModel202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete

This endpoint removes one or more add to basket ids from targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        AddToBasketIdsUpdateModel202110Request addToBasketIdsUpdateModel202110Request = new AddToBasketIdsUpdateModel202110Request(); // AddToBasketIdsUpdateModel202110Request | Ids to remove from the target
        try {
            AddToBasketTarget202110Response result = apiInstance.deleteAddToBasketTargetsByLineItemId(lineItemId, addToBasketIdsUpdateModel202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteAddToBasketTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **addToBasketIdsUpdateModel202110Request** | [**AddToBasketIdsUpdateModel202110Request**](AddToBasketIdsUpdateModel202110Request.md)| Ids to remove from the target | [optional] |

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## deleteAudienceTargetsByLineItemId

> AudienceTarget202110Response deleteAudienceTargetsByLineItemId(lineItemId, audienceIdsUpdateModel202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete

This endpoint removes one or more audiences ids from targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        AudienceIdsUpdateModel202110Request audienceIdsUpdateModel202110Request = new AudienceIdsUpdateModel202110Request(); // AudienceIdsUpdateModel202110Request | Audience ids to remove from the target
        try {
            AudienceTarget202110Response result = apiInstance.deleteAudienceTargetsByLineItemId(lineItemId, audienceIdsUpdateModel202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteAudienceTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **audienceIdsUpdateModel202110Request** | [**AudienceIdsUpdateModel202110Request**](AudienceIdsUpdateModel202110Request.md)| Audience ids to remove from the target | [optional] |

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## deleteCampaignsFromBalanceV1

> ValueResourceOutcomeBalanceCampaignsV1 deleteCampaignsFromBalanceV1(balanceId, valueResourceInputDeleteCampaignsRequestV1)

/2027-01/retail-media/balances/{balanceId}/campaigns/delete

Deletes one or more campaigns on the specified balance

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String balanceId = "balanceId_example"; // String | The balance to remove campaigns from
        ValueResourceInputDeleteCampaignsRequestV1 valueResourceInputDeleteCampaignsRequestV1 = new ValueResourceInputDeleteCampaignsRequestV1(); // ValueResourceInputDeleteCampaignsRequestV1 | The balance campaign deleting request.
        try {
            ValueResourceOutcomeBalanceCampaignsV1 result = apiInstance.deleteCampaignsFromBalanceV1(balanceId, valueResourceInputDeleteCampaignsRequestV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteCampaignsFromBalanceV1");
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
| **balanceId** | **String**| The balance to remove campaigns from | |
| **valueResourceInputDeleteCampaignsRequestV1** | [**ValueResourceInputDeleteCampaignsRequestV1**](ValueResourceInputDeleteCampaignsRequestV1.md)| The balance campaign deleting request. | |

### Return type

[**ValueResourceOutcomeBalanceCampaignsV1**](ValueResourceOutcomeBalanceCampaignsV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## deletePromotedProducts

> deletePromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/2027-01/retail-media/line-items/{line-item-id}/products/delete

Remove a collection of promoted products from a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | ID of the line item
        PromotedProductResourceCollectionInput promotedProductResourceCollectionInput = new PromotedProductResourceCollectionInput(); // PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.
        try {
            apiInstance.deletePromotedProducts(lineItemId, promotedProductResourceCollectionInput);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deletePromotedProducts");
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
| **lineItemId** | **String**| ID of the line item | |
| **promotedProductResourceCollectionInput** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Promoted products removed from the line item |  -  |


## deleteStoreTargetByLineItemId

> StoreTarget202110Response deleteStoreTargetByLineItemId(lineItemId, storeIdsUpdateModel202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete

This endpoint removes one or more store ids from targeting on the specified line item.  The resulting state of the store target is returned.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        StoreIdsUpdateModel202110Request storeIdsUpdateModel202110Request = new StoreIdsUpdateModel202110Request(); // StoreIdsUpdateModel202110Request | Store ids to remove from the target
        try {
            StoreTarget202110Response result = apiInstance.deleteStoreTargetByLineItemId(lineItemId, storeIdsUpdateModel202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteStoreTargetByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **storeIdsUpdateModel202110Request** | [**StoreIdsUpdateModel202110Request**](StoreIdsUpdateModel202110Request.md)| Store ids to remove from the target | [optional] |

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## fetchPromotedProducts

> PromotedProductResourceCollectionOutcome fetchPromotedProducts(lineItemId, fields, limit, offset)

/2027-01/retail-media/line-items/{line-item-id}/products

Retrieve a page of promoted products for a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | ID of the line item.
        String fields = "fields_example"; // String | A comma separated list of attribute names from the response model to compute and return.              Valid values are `status` and `bidOverride` in any order. Defaults to `status`.
        Integer limit = 56; // Integer | Maximum page size to fetch. Defaults to 500.
        Integer offset = 56; // Integer | Offset of the first item to fetch. Defaults to zero.
        try {
            PromotedProductResourceCollectionOutcome result = apiInstance.fetchPromotedProducts(lineItemId, fields, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#fetchPromotedProducts");
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
| **lineItemId** | **String**| ID of the line item. | |
| **fields** | **String**| A comma separated list of attribute names from the response model to compute and return.              Valid values are &#x60;status&#x60; and &#x60;bidOverride&#x60; in any order. Defaults to &#x60;status&#x60;. | [optional] |
| **limit** | **Integer**| Maximum page size to fetch. Defaults to 500. | [optional] |
| **offset** | **Integer**| Offset of the first item to fetch. Defaults to zero. | [optional] |

### Return type

[**PromotedProductResourceCollectionOutcome**](PromotedProductResourceCollectionOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Promoted products associated with the line item |  -  |


## getAccountCreatives

> Creative202110ListResponse getAccountCreatives(accountId)

/2027-01/retail-media/accounts/{account-id}/creatives

Get account creatives

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | External account id to retrieve creatives for
        try {
            Creative202110ListResponse result = apiInstance.getAccountCreatives(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAccountCreatives");
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
| **accountId** | **String**| External account id to retrieve creatives for | |

### Return type

[**Creative202110ListResponse**](Creative202110ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives found |  -  |


## getAddToBasketTargetsByLineItemId

> AddToBasketTarget202110Response getAddToBasketTargetsByLineItemId(lineItemId)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket

This endpoint gets the add to basket target on the specified line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        try {
            AddToBasketTarget202110Response result = apiInstance.getAddToBasketTargetsByLineItemId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAddToBasketTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getApi202110ExternalRetailerPagesByRetailerId

> RetailerPages202110 getApi202110ExternalRetailerPagesByRetailerId(retailerId)

/2027-01/retail-media/retailers/{retailerId}/pages

Get the page types available for the given retailer

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | The retailers to fetch pages for
        try {
            RetailerPages202110 result = apiInstance.getApi202110ExternalRetailerPagesByRetailerId(retailerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getApi202110ExternalRetailerPagesByRetailerId");
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
| **retailerId** | **String**| The retailers to fetch pages for | |

### Return type

[**RetailerPages202110**](RetailerPages202110.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pages fetched successfully |  -  |


## getApiExternalV1Categories

> Category202204ListResponse getApiExternalV1Categories(pageIndex, pageSize, retailerId, textSubstring)

/2027-01/retail-media/categories

Endpoint to search categories by text and retailer.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        Integer pageIndex = 0; // Integer | The start position in the overall list of matches. Must be zero or greater.
        Integer pageSize = 100; // Integer | The maximum number of results to return with each call. Must be greater than zero.
        Integer retailerId = 56; // Integer | The retailer id for which Categories fetched
        String textSubstring = "textSubstring_example"; // String | Query string to search across Categories
        try {
            Category202204ListResponse result = apiInstance.getApiExternalV1Categories(pageIndex, pageSize, retailerId, textSubstring);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getApiExternalV1Categories");
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
| **pageIndex** | **Integer**| The start position in the overall list of matches. Must be zero or greater. | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of results to return with each call. Must be greater than zero. | [optional] [default to 100] |
| **retailerId** | **Integer**| The retailer id for which Categories fetched | [optional] |
| **textSubstring** | **String**| Query string to search across Categories | [optional] |

### Return type

[**Category202204ListResponse**](Category202204ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Categories found. |  -  |


## getAuctionLineItem

> EntityResourceOutcomeOfSponsoredProductsLineItem getAuctionLineItem(lineItemId)

/2027-01/retail-media/auction-line-items/{lineItemId}

Gets a sponsored product line item by its id.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The id of the line item
        try {
            EntityResourceOutcomeOfSponsoredProductsLineItem result = apiInstance.getAuctionLineItem(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAuctionLineItem");
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
| **lineItemId** | **String**| The id of the line item | |

### Return type

[**EntityResourceOutcomeOfSponsoredProductsLineItem**](EntityResourceOutcomeOfSponsoredProductsLineItem.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAuctionLineItemsByCampaign

> EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata getAuctionLineItemsByCampaign(campaignId, limit, limitToIds, offset)

/2027-01/retail-media/campaigns/{campaignId}/auction-line-items

Gets a page of sponsored product line items by campaign id.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | The id of the campaign
        Integer limit = 25; // Integer | The number of elements to be returned on a page.
        List<String> limitToIds = Arrays.asList(); // List<String> | The ids to limit the auction line item results to
        Integer offset = 0; // Integer | The (zero-based) starting offset into the collection.
        try {
            EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata result = apiInstance.getAuctionLineItemsByCampaign(campaignId, limit, limitToIds, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAuctionLineItemsByCampaign");
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
| **campaignId** | **String**| The id of the campaign | |
| **limit** | **Integer**| The number of elements to be returned on a page. | [optional] [default to 25] |
| **limitToIds** | [**List&lt;String&gt;**](String.md)| The ids to limit the auction line item results to | [optional] |
| **offset** | **Integer**| The (zero-based) starting offset into the collection. | [optional] [default to 0] |

### Return type

[**EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata**](EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getAudienceTargetsByLineItemId

> AudienceTarget202110Response getAudienceTargetsByLineItemId(lineItemId)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences

This endpoint gets the audience target on the specified line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        try {
            AudienceTarget202110Response result = apiInstance.getAudienceTargetsByLineItemId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getAudienceTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getBidMultipliersByLineItemId

> JsonApiSingleResponseOfLineItemBidMultipliersV2 getBidMultipliersByLineItemId(lineItemId)

/2027-01/retail-media/line-items/{line-item-id}/bid-multipliers

Fetch all bid multipliers for a given line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for bid multiplier retrieval
        try {
            JsonApiSingleResponseOfLineItemBidMultipliersV2 result = apiInstance.getBidMultipliersByLineItemId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getBidMultipliersByLineItemId");
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
| **lineItemId** | **String**| LineItemId for bid multiplier retrieval | |

### Return type

[**JsonApiSingleResponseOfLineItemBidMultipliersV2**](JsonApiSingleResponseOfLineItemBidMultipliersV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | BidMultipliers Found |  -  |


## getBrandsByAccountId

> JsonApiPageResponseOfBrand getBrandsByAccountId(accountId, limitToId, pageIndex, pageSize)

/2027-01/retail-media/accounts/{accountId}/brands

Gets page of retailer objects that are associated with the given account

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The given account id
        List<String> limitToId = Arrays.asList(); // List<String> | The ids that you would like to limit your result set to
        Integer pageIndex = 0; // Integer | The 0 indexed page index you would like to receive given the page size
        Integer pageSize = 25; // Integer | The maximum number of items you would like to receive in this request
        try {
            JsonApiPageResponseOfBrand result = apiInstance.getBrandsByAccountId(accountId, limitToId, pageIndex, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getBrandsByAccountId");
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
| **accountId** | **String**| The given account id | |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The ids that you would like to limit your result set to | [optional] |
| **pageIndex** | **Integer**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**JsonApiPageResponseOfBrand**](JsonApiPageResponseOfBrand.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCampaignBudgetOverrides

> ValueResourceOutcomeOfCampaignBudgetOverrides getCampaignBudgetOverrides(campaignId)

/2027-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides

Get current campaign budget overrides by given campaign id.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | Campaign id.
        try {
            ValueResourceOutcomeOfCampaignBudgetOverrides result = apiInstance.getCampaignBudgetOverrides(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCampaignBudgetOverrides");
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
| **campaignId** | **String**| Campaign id. | |

### Return type

[**ValueResourceOutcomeOfCampaignBudgetOverrides**](ValueResourceOutcomeOfCampaignBudgetOverrides.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCampaignByCampaignId

> JsonApiSingleResponseOfCampaignV202301 getCampaignByCampaignId(campaignId)

/2027-01/retail-media/campaigns/{campaignId}

Gets the campaign for the given campaign id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | The given campaign id
        try {
            JsonApiSingleResponseOfCampaignV202301 result = apiInstance.getCampaignByCampaignId(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCampaignByCampaignId");
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
| **campaignId** | **String**| The given campaign id | |

### Return type

[**JsonApiSingleResponseOfCampaignV202301**](JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCampaignsByAccountId

> JsonApiPageResponseOfCampaignV202301 getCampaignsByAccountId(accountId, limitToId, pageIndex, pageSize)

/2027-01/retail-media/accounts/{account-id}/campaigns

Gets page of campaign objects for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The given account id
        List<String> limitToId = Arrays.asList(); // List<String> | The ids that you would like to limit your result set to
        Integer pageIndex = 0; // Integer | The 0 indexed page index you would like to receive given the page size
        Integer pageSize = 25; // Integer | The maximum number of items you would like to receive in this request
        try {
            JsonApiPageResponseOfCampaignV202301 result = apiInstance.getCampaignsByAccountId(accountId, limitToId, pageIndex, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCampaignsByAccountId");
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
| **accountId** | **String**| The given account id | |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The ids that you would like to limit your result set to | [optional] |
| **pageIndex** | **Integer**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**JsonApiPageResponseOfCampaignV202301**](JsonApiPageResponseOfCampaignV202301.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCatalogOutput

> File getCatalogOutput(catalogId)

/2027-01/retail-media/catalogs/{catalogId}/output

Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream CatalogProduct json objects (first introduced in the 2021-07 version).

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String catalogId = "catalogId_example"; // String | A catalog ID returned from an account catalog request.
        try {
            File result = apiInstance.getCatalogOutput(catalogId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCatalogOutput");
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
| **catalogId** | **String**| A catalog ID returned from an account catalog request. | |

### Return type

[**File**](File.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-json-stream


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog download initiated. |  -  |
| **204** | Catalog has expired. |  -  |


## getCatalogStatus

> JsonApiSingleResponseOfCatalogStatus getCatalogStatus(catalogId)

/2027-01/retail-media/catalogs/{catalogId}/status

Check the status of a catalog request.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String catalogId = "catalogId_example"; // String | A catalog ID returned from an account catalog request.
        try {
            JsonApiSingleResponseOfCatalogStatus result = apiInstance.getCatalogStatus(catalogId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCatalogStatus");
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
| **catalogId** | **String**| A catalog ID returned from an account catalog request. | |

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog request found. |  -  |


## getCategory

> Category202204 getCategory(categoryId)

/2027-01/retail-media/categories/{categoryId}

Endpoint to search for a specific category by categoryId.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String categoryId = "categoryId_example"; // String | ID of the desired category
        try {
            Category202204 result = apiInstance.getCategory(categoryId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCategory");
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
| **categoryId** | **String**| ID of the desired category | |

### Return type

[**Category202204**](Category202204.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieval completed and category is returned. |  -  |


## getCpcMinBidsBySkuIdsV1

> ValueResourceOutcomeCpcMinBidsResponse getCpcMinBidsBySkuIdsV1(retailerId, valueResourceInputCpcMinBidsRequest)

/2027-01/retail-media/retailers/{retailerId}/cpc-min-bids

Get overall and individual minimum bid amount for given retailer id and sku id list.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | Retailer Id.
        ValueResourceInputCpcMinBidsRequest valueResourceInputCpcMinBidsRequest = new ValueResourceInputCpcMinBidsRequest(); // ValueResourceInputCpcMinBidsRequest | Cpc minimum bid amount request object.
        try {
            ValueResourceOutcomeCpcMinBidsResponse result = apiInstance.getCpcMinBidsBySkuIdsV1(retailerId, valueResourceInputCpcMinBidsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCpcMinBidsBySkuIdsV1");
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
| **retailerId** | **String**| Retailer Id. | |
| **valueResourceInputCpcMinBidsRequest** | [**ValueResourceInputCpcMinBidsRequest**](ValueResourceInputCpcMinBidsRequest.md)| Cpc minimum bid amount request object. | |

### Return type

[**ValueResourceOutcomeCpcMinBidsResponse**](ValueResourceOutcomeCpcMinBidsResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCreative

> Creative2Response getCreative(accountId, creativeId)

/2027-01/retail-media/accounts/{account-id}/creatives/{creative-id}

Get the specified creative

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | External account id to retrieve creatives for
        String creativeId = "creativeId_example"; // String | Creative to get
        try {
            Creative2Response result = apiInstance.getCreative(accountId, creativeId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCreative");
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
| **accountId** | **String**| External account id to retrieve creatives for | |
| **creativeId** | **String**| Creative to get | |

### Return type

[**Creative2Response**](Creative2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives found |  -  |


## getCreativeTemplate

> TemplateResponse getCreativeTemplate(retailerId, templateId)

/2027-01/retail-media/retailers/{retailer-id}/templates/{template-id}

Gets the template for the specified retailer id and template id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | Retailer Id
        String templateId = "templateId_example"; // String | Template Id
        try {
            TemplateResponse result = apiInstance.getCreativeTemplate(retailerId, templateId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCreativeTemplate");
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
| **retailerId** | **String**| Retailer Id | |
| **templateId** | **String**| Template Id | |

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template found for the retailer |  -  |


## getKeywordInReviewReport

> EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata getKeywordInReviewReport(accountId, limit, offset)

/2027-01/retail-media/accounts/{account-id}/keywords/in-review-report

Generate a list of reports for line items which contain one or more actionable keyword reviews

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The account to generate a report for
        Integer limit = 25; // Integer | Number of items per page
        Integer offset = 0; // Integer | Offset for pagination
        try {
            EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata result = apiInstance.getKeywordInReviewReport(accountId, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getKeywordInReviewReport");
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
| **accountId** | **String**| The account to generate a report for | |
| **limit** | **Integer**| Number of items per page | [optional] [default to 25] |
| **offset** | **Integer**| Offset for pagination | [optional] [default to 0] |

### Return type

[**EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata**](EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getLineItemBudgetOverrides

> ValueResourceOutcomeOfLineItemBudgetOverrides getLineItemBudgetOverrides(lineItemId)

/2027-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides

Gets a collection of monthly and daily budget overrides for the provided line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item id to get budget overrides for.
        try {
            ValueResourceOutcomeOfLineItemBudgetOverrides result = apiInstance.getLineItemBudgetOverrides(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getLineItemBudgetOverrides");
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
| **lineItemId** | **String**| The line item id to get budget overrides for. | |

### Return type

[**ValueResourceOutcomeOfLineItemBudgetOverrides**](ValueResourceOutcomeOfLineItemBudgetOverrides.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getLineItemsByAccountId

> CommonLineItemPagedListResponse getLineItemsByAccountId(accountId, limitToCampaignId, limitToId, limitToType, pageIndex, pageSize)

/2027-01/retail-media/accounts/{account-id}/line-items

Gets page of line item objects for the given account id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The given account id
        List<String> limitToCampaignId = Arrays.asList(); // List<String> | The campaign ids that you would like to limit your result set to
        List<String> limitToId = Arrays.asList(); // List<String> | The ids that you would like to limit your result set to
        String limitToType = "Unknown"; // String | The campaign types that you would like to limit your result set to
        Integer pageIndex = 0; // Integer | The 0 indexed page index you would like to receive given the page size
        Integer pageSize = 25; // Integer | The maximum number of items you would like to receive in this request
        try {
            CommonLineItemPagedListResponse result = apiInstance.getLineItemsByAccountId(accountId, limitToCampaignId, limitToId, limitToType, pageIndex, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getLineItemsByAccountId");
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
| **accountId** | **String**| The given account id | |
| **limitToCampaignId** | [**List&lt;String&gt;**](String.md)| The campaign ids that you would like to limit your result set to | [optional] |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The ids that you would like to limit your result set to | [optional] |
| **limitToType** | **String**| The campaign types that you would like to limit your result set to | [optional] [enum: Unknown, Auction, Preferred] |
| **pageIndex** | **Integer**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**CommonLineItemPagedListResponse**](CommonLineItemPagedListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getLineItemsByCampaignId

> CommonLineItemResponse getLineItemsByCampaignId(lineItemId)

/2027-01/retail-media/line-items/{line-item-id}

Gets the line item for the given line item id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The given line item id
        try {
            CommonLineItemResponse result = apiInstance.getLineItemsByCampaignId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getLineItemsByCampaignId");
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
| **lineItemId** | **String**| The given line item id | |

### Return type

[**CommonLineItemResponse**](CommonLineItemResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getPreferredLineItemsByCampaignId

> PreferredLineItemV2PagedListResponse getPreferredLineItemsByCampaignId(campaignId, limitToId, pageIndex, pageSize)

/2027-01/retail-media/campaigns/{campaign-id}/preferred-line-items

Gets page of preferred line item objects for the given campaign id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | The given campaign id
        List<String> limitToId = Arrays.asList(); // List<String> | The ids that you would like to limit your result set to
        Integer pageIndex = 0; // Integer | The 0 indexed page index you would like to receive given the page size
        Integer pageSize = 25; // Integer | The maximum number of items you would like to receive in this request
        try {
            PreferredLineItemV2PagedListResponse result = apiInstance.getPreferredLineItemsByCampaignId(campaignId, limitToId, pageIndex, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getPreferredLineItemsByCampaignId");
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
| **campaignId** | **String**| The given campaign id | |
| **limitToId** | [**List&lt;String&gt;**](String.md)| The ids that you would like to limit your result set to | [optional] |
| **pageIndex** | **Integer**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **pageSize** | **Integer**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**PreferredLineItemV2PagedListResponse**](PreferredLineItemV2PagedListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getPreferredLineItemsByLineItemId

> PreferredLineItemV2Response getPreferredLineItemsByLineItemId(lineItemId)

/2027-01/retail-media/preferred-line-items/{line-item-id}

Gets the preferred line item for the given line item id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The given line item id
        try {
            PreferredLineItemV2Response result = apiInstance.getPreferredLineItemsByLineItemId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getPreferredLineItemsByLineItemId");
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
| **lineItemId** | **String**| The given line item id | |

### Return type

[**PreferredLineItemV2Response**](PreferredLineItemV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getRecommendedCategories

> EntityResourceCollectionOutcomeCategory202204 getRecommendedCategories(retailerId, valueResourceInputRecommendedCategoriesRequestV1)

/2027-01/retail-media/retailers/{retailerId}/recommend-categories

Endpoint to get recommended categories by given retailer id and sku id list.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | Retailer id.
        ValueResourceInputRecommendedCategoriesRequestV1 valueResourceInputRecommendedCategoriesRequestV1 = new ValueResourceInputRecommendedCategoriesRequestV1(); // ValueResourceInputRecommendedCategoriesRequestV1 | Request of recommended categories.
        try {
            EntityResourceCollectionOutcomeCategory202204 result = apiInstance.getRecommendedCategories(retailerId, valueResourceInputRecommendedCategoriesRequestV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getRecommendedCategories");
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
| **retailerId** | **String**| Retailer id. | |
| **valueResourceInputRecommendedCategoriesRequestV1** | [**ValueResourceInputRecommendedCategoriesRequestV1**](ValueResourceInputRecommendedCategoriesRequestV1.md)| Request of recommended categories. | |

### Return type

[**EntityResourceCollectionOutcomeCategory202204**](EntityResourceCollectionOutcomeCategory202204.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getRecommendedKeywords

> ValueResourceOutcomeOfRecommendedKeywordsResult getRecommendedKeywords(externalLineItemId)

/2027-01/retail-media/line-items/{externalLineItemId}/keywords/recommended

Retrieves a collection of recommended keywords for a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String externalLineItemId = "externalLineItemId_example"; // String | The line item identifier
        try {
            ValueResourceOutcomeOfRecommendedKeywordsResult result = apiInstance.getRecommendedKeywords(externalLineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getRecommendedKeywords");
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
| **externalLineItemId** | **String**| The line item identifier | |

### Return type

[**ValueResourceOutcomeOfRecommendedKeywordsResult**](ValueResourceOutcomeOfRecommendedKeywordsResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getRetailerCreativeTemplates

> TemplateListResponse getRetailerCreativeTemplates(retailerId)

/2027-01/retail-media/retailers/{retailer-id}/templates

Get retailer creative templates

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | External retailer id to retrieve creative templates for
        try {
            TemplateListResponse result = apiInstance.getRetailerCreativeTemplates(retailerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getRetailerCreativeTemplates");
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
| **retailerId** | **String**| External retailer id to retrieve creative templates for | |

### Return type

[**TemplateListResponse**](TemplateListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Templates found |  -  |


## getStoreTargetsByLineItemId

> StoreTarget202110Response getStoreTargetsByLineItemId(lineItemId)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores

This endpoint gets the store target on the specified line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        try {
            StoreTarget202110Response result = apiInstance.getStoreTargetsByLineItemId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getStoreTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## pausePromotedProducts

> pausePromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/2027-01/retail-media/line-items/{line-item-id}/products/pause

Pause a collection of promoted products associated with a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | ID of the line item
        PromotedProductResourceCollectionInput promotedProductResourceCollectionInput = new PromotedProductResourceCollectionInput(); // PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.
        try {
            apiInstance.pausePromotedProducts(lineItemId, promotedProductResourceCollectionInput);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#pausePromotedProducts");
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
| **lineItemId** | **String**| ID of the line item | |
| **promotedProductResourceCollectionInput** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Promoted products paused |  -  |


## postApiExternalV1AccountCatalogsSellersByAccountId

> JsonApiSingleResponseOfCatalogStatus postApiExternalV1AccountCatalogsSellersByAccountId(accountId, jsonApiRequestOfSellerCatalogRequest)

/2027-01/retail-media/accounts/{accountId}/catalogs/sellers

Create a request for a Catalog available to the indicated account.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The account to request the catalog for.
        JsonApiRequestOfSellerCatalogRequest jsonApiRequestOfSellerCatalogRequest = new JsonApiRequestOfSellerCatalogRequest(); // JsonApiRequestOfSellerCatalogRequest | 
        try {
            JsonApiSingleResponseOfCatalogStatus result = apiInstance.postApiExternalV1AccountCatalogsSellersByAccountId(accountId, jsonApiRequestOfSellerCatalogRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#postApiExternalV1AccountCatalogsSellersByAccountId");
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
| **accountId** | **String**| The account to request the catalog for. | |
| **jsonApiRequestOfSellerCatalogRequest** | [**JsonApiRequestOfSellerCatalogRequest**](JsonApiRequestOfSellerCatalogRequest.md)|  | |

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog request successfully created |  -  |


## postApiV1ExternalAccountCatalogsByAccountId

> JsonApiSingleResponseOfCatalogStatus postApiV1ExternalAccountCatalogsByAccountId(accountId, jsonApiRequestOfCatalogRequest)

/2027-01/retail-media/accounts/{accountId}/catalogs

Create a request for a Catalog available to the indicated account.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The account to request the catalog for.
        JsonApiRequestOfCatalogRequest jsonApiRequestOfCatalogRequest = new JsonApiRequestOfCatalogRequest(); // JsonApiRequestOfCatalogRequest | 
        try {
            JsonApiSingleResponseOfCatalogStatus result = apiInstance.postApiV1ExternalAccountCatalogsByAccountId(accountId, jsonApiRequestOfCatalogRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#postApiV1ExternalAccountCatalogsByAccountId");
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
| **accountId** | **String**| The account to request the catalog for. | |
| **jsonApiRequestOfCatalogRequest** | [**JsonApiRequestOfCatalogRequest**](JsonApiRequestOfCatalogRequest.md)|  | |

### Return type

[**JsonApiSingleResponseOfCatalogStatus**](JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog request successfully created |  -  |


## putAddToBasketTargetByLineItemId

> AddToBasketTarget202110Response putAddToBasketTargetByLineItemId(lineItemId, addToBasketTarget202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket

This endpoint sets the scope of the add to basket target on the specified line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        AddToBasketTarget202110Request addToBasketTarget202110Request = new AddToBasketTarget202110Request(); // AddToBasketTarget202110Request | The add to basket target to set the scope for
        try {
            AddToBasketTarget202110Response result = apiInstance.putAddToBasketTargetByLineItemId(lineItemId, addToBasketTarget202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putAddToBasketTargetByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **addToBasketTarget202110Request** | [**AddToBasketTarget202110Request**](AddToBasketTarget202110Request.md)| The add to basket target to set the scope for | |

### Return type

[**AddToBasketTarget202110Response**](AddToBasketTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## putAudienceTargetsByLineItemId

> AudienceTarget202110Response putAudienceTargetsByLineItemId(lineItemId, audienceTarget202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences

This endpoint sets the scope of the audience target on the specified line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        AudienceTarget202110Request audienceTarget202110Request = new AudienceTarget202110Request(); // AudienceTarget202110Request | The audience target to set the scope for
        try {
            AudienceTarget202110Response result = apiInstance.putAudienceTargetsByLineItemId(lineItemId, audienceTarget202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putAudienceTargetsByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **audienceTarget202110Request** | [**AudienceTarget202110Request**](AudienceTarget202110Request.md)| The audience target to set the scope for | |

### Return type

[**AudienceTarget202110Response**](AudienceTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## putStoreTargetByLineItemId

> StoreTarget202110Response putStoreTargetByLineItemId(lineItemId, storeTarget202110Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores

This endpoint sets the scope of the store target on the specified line item.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to interact with
        StoreTarget202110Request storeTarget202110Request = new StoreTarget202110Request(); // StoreTarget202110Request | The store target to set the scope for
        try {
            StoreTarget202110Response result = apiInstance.putStoreTargetByLineItemId(lineItemId, storeTarget202110Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#putStoreTargetByLineItemId");
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
| **lineItemId** | **String**| The line item to interact with | |
| **storeTarget202110Request** | [**StoreTarget202110Request**](StoreTarget202110Request.md)| The store target to set the scope for | |

### Return type

[**StoreTarget202110Response**](StoreTarget202110Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## recommendedKeywords

> ValueResourceOutcomeRecommendedKeywordsResponseV1 recommendedKeywords(retailerId, valueResourceInputRecommendedKeywordsRequestV1)

/2027-01/retail-media/retailers/{retailerId}/recommend-keywords

Recommend keywords by given retailer id and sku ids.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | Retailer id.
        ValueResourceInputRecommendedKeywordsRequestV1 valueResourceInputRecommendedKeywordsRequestV1 = new ValueResourceInputRecommendedKeywordsRequestV1(); // ValueResourceInputRecommendedKeywordsRequestV1 | Request of recommended keywords.
        try {
            ValueResourceOutcomeRecommendedKeywordsResponseV1 result = apiInstance.recommendedKeywords(retailerId, valueResourceInputRecommendedKeywordsRequestV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#recommendedKeywords");
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
| **retailerId** | **String**| Retailer id. | |
| **valueResourceInputRecommendedKeywordsRequestV1** | [**ValueResourceInputRecommendedKeywordsRequestV1**](ValueResourceInputRecommendedKeywordsRequestV1.md)| Request of recommended keywords. | |

### Return type

[**ValueResourceOutcomeRecommendedKeywordsResponseV1**](ValueResourceOutcomeRecommendedKeywordsResponseV1.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchAccountCreatives

> Creative2ListResponse searchAccountCreatives(accountId, creativeIds)

/2027-01/retail-media/accounts/{account-id}/creatives/search

Get account creatives

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | External account id to retrieve creatives for
        List<String> creativeIds = Arrays.asList(); // List<String> | Creatives to filter by
        try {
            Creative2ListResponse result = apiInstance.searchAccountCreatives(accountId, creativeIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#searchAccountCreatives");
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
| **accountId** | **String**| External account id to retrieve creatives for | |
| **creativeIds** | [**List&lt;String&gt;**](String.md)| Creatives to filter by | [optional] |

### Return type

[**Creative2ListResponse**](Creative2ListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives found |  -  |


## searchAccountRetailers

> EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata searchAccountRetailers(accountId, valueResourceInputOfRetailerSearchRequestV2, limit, offset)

/2027-01/retail-media/accounts/{accountId}/retailers/search

Searches for retailers associated with the specified account and returns budget model availability for each retailer

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | The external account identifier
        ValueResourceInputOfRetailerSearchRequestV2 valueResourceInputOfRetailerSearchRequestV2 = new ValueResourceInputOfRetailerSearchRequestV2(); // ValueResourceInputOfRetailerSearchRequestV2 | The search request containing filtering parameters
        Integer limit = 5; // Integer | The maximum number of items to return. Must be between 1 and 10. Default is 5.
        Integer offset = 0; // Integer | The number of items to skip before starting to collect the result set. Default is 0.
        try {
            EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata result = apiInstance.searchAccountRetailers(accountId, valueResourceInputOfRetailerSearchRequestV2, limit, offset);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#searchAccountRetailers");
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
| **accountId** | **String**| The external account identifier | |
| **valueResourceInputOfRetailerSearchRequestV2** | [**ValueResourceInputOfRetailerSearchRequestV2**](ValueResourceInputOfRetailerSearchRequestV2.md)| The search request containing filtering parameters | |
| **limit** | **Integer**| The maximum number of items to return. Must be between 1 and 10. Default is 5. | [optional] [default to 5] |
| **offset** | **Integer**| The number of items to skip before starting to collect the result set. Default is 0. | [optional] [default to 0] |

### Return type

[**EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata**](EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## searchCategory

> EntityResourceCollectionOutcomeCategory202204Metadata searchCategory(retailerId, limit, offset, valueResourceInputCategoriesSearchRequestV1)

/2027-01/retail-media/retailers/{retailerId}/categories/search

Search a retailer categories by given text substring and category ids.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | Retailer id.
        Integer limit = 50; // Integer | Limit of the search result.
        Integer offset = 0; // Integer | Offset of the search result.
        ValueResourceInputCategoriesSearchRequestV1 valueResourceInputCategoriesSearchRequestV1 = new ValueResourceInputCategoriesSearchRequestV1(); // ValueResourceInputCategoriesSearchRequestV1 | Request of categories search.
        try {
            EntityResourceCollectionOutcomeCategory202204Metadata result = apiInstance.searchCategory(retailerId, limit, offset, valueResourceInputCategoriesSearchRequestV1);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#searchCategory");
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
| **retailerId** | **String**| Retailer id. | |
| **limit** | **Integer**| Limit of the search result. | [optional] [default to 50] |
| **offset** | **Integer**| Offset of the search result. | [optional] [default to 0] |
| **valueResourceInputCategoriesSearchRequestV1** | [**ValueResourceInputCategoriesSearchRequestV1**](ValueResourceInputCategoriesSearchRequestV1.md)| Request of categories search. | [optional] |

### Return type

[**EntityResourceCollectionOutcomeCategory202204Metadata**](EntityResourceCollectionOutcomeCategory202204Metadata.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## setKeywordBids

> ResourceOutcome setKeywordBids(id, setBidsModelRequest)

/2027-01/retail-media/line-items/{id}/keywords/set-bid

Set bid overrides for associated keywords to the given line item in bulk

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String id = "id_example"; // String | ID of the line item
        SetBidsModelRequest setBidsModelRequest = new SetBidsModelRequest(); // SetBidsModelRequest | 
        try {
            ResourceOutcome result = apiInstance.setKeywordBids(id, setBidsModelRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#setKeywordBids");
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
| **id** | **String**| ID of the line item | |
| **setBidsModelRequest** | [**SetBidsModelRequest**](SetBidsModelRequest.md)|  | [optional] |

### Return type

[**ResourceOutcome**](ResourceOutcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## unpausePromotedProducts

> unpausePromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/2027-01/retail-media/line-items/{line-item-id}/products/unpause

Un-pause a collection of promoted products associated with a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | ID of the line item
        PromotedProductResourceCollectionInput promotedProductResourceCollectionInput = new PromotedProductResourceCollectionInput(); // PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.
        try {
            apiInstance.unpausePromotedProducts(lineItemId, promotedProductResourceCollectionInput);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#unpausePromotedProducts");
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
| **lineItemId** | **String**| ID of the line item | |
| **promotedProductResourceCollectionInput** | [**PromotedProductResourceCollectionInput**](PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Promoted products un-paused |  -  |


## updateAuctionLineItem

> EntityResourceOutcomeOfSponsoredProductsLineItem updateAuctionLineItem(lineItemId, valueResourceInputOfSponsoredProductsLineItemUpdateRequestModel)

/2027-01/retail-media/auction-line-items/{lineItemId}

Updates a Sponsored Products Line Item given a line item id and a request.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The external line item ID of the sponsored products line item.
        ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel valueResourceInputOfSponsoredProductsLineItemUpdateRequestModel = new ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel(); // ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel | An update request containing all details of the requested update.
        try {
            EntityResourceOutcomeOfSponsoredProductsLineItem result = apiInstance.updateAuctionLineItem(lineItemId, valueResourceInputOfSponsoredProductsLineItemUpdateRequestModel);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateAuctionLineItem");
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
| **lineItemId** | **String**| The external line item ID of the sponsored products line item. | |
| **valueResourceInputOfSponsoredProductsLineItemUpdateRequestModel** | [**ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel**](ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel.md)| An update request containing all details of the requested update. | |

### Return type

[**EntityResourceOutcomeOfSponsoredProductsLineItem**](EntityResourceOutcomeOfSponsoredProductsLineItem.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateBidMultipliersByLineItemId

> LineItemBidMultipliersV2Response updateBidMultipliersByLineItemId(lineItemId, lineItemBidMultipliersV2Request)

/2027-01/retail-media/line-items/{line-item-id}/bid-multipliers

Updates the bid multipliers for a given line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for bid multiplier retrieval
        LineItemBidMultipliersV2Request lineItemBidMultipliersV2Request = new LineItemBidMultipliersV2Request(); // LineItemBidMultipliersV2Request | New Bid Multipliers to be set
        try {
            LineItemBidMultipliersV2Response result = apiInstance.updateBidMultipliersByLineItemId(lineItemId, lineItemBidMultipliersV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateBidMultipliersByLineItemId");
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
| **lineItemId** | **String**| LineItemId for bid multiplier retrieval | |
| **lineItemBidMultipliersV2Request** | [**LineItemBidMultipliersV2Request**](LineItemBidMultipliersV2Request.md)| New Bid Multipliers to be set | |

### Return type

[**LineItemBidMultipliersV2Response**](LineItemBidMultipliersV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | BidMultipliers Updated |  -  |


## updateCampaignBudgetOverrides

> ValueResourceOutcomeOfCampaignBudgetOverrides updateCampaignBudgetOverrides(campaignId, valueResourceInputOfCampaignBudgetOverrides)

/2027-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides

Update campaign budget overrides by given campaign id and new campaign budget overrides settings.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | Campaign id.
        ValueResourceInputOfCampaignBudgetOverrides valueResourceInputOfCampaignBudgetOverrides = new ValueResourceInputOfCampaignBudgetOverrides(); // ValueResourceInputOfCampaignBudgetOverrides | New campaign budget overrides settings value resource input.
        try {
            ValueResourceOutcomeOfCampaignBudgetOverrides result = apiInstance.updateCampaignBudgetOverrides(campaignId, valueResourceInputOfCampaignBudgetOverrides);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateCampaignBudgetOverrides");
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
| **campaignId** | **String**| Campaign id. | |
| **valueResourceInputOfCampaignBudgetOverrides** | [**ValueResourceInputOfCampaignBudgetOverrides**](ValueResourceInputOfCampaignBudgetOverrides.md)| New campaign budget overrides settings value resource input. | |

### Return type

[**ValueResourceOutcomeOfCampaignBudgetOverrides**](ValueResourceOutcomeOfCampaignBudgetOverrides.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## updateCampaignByCampaignId

> JsonApiSingleResponseOfCampaignV202301 updateCampaignByCampaignId(campaignId, putCampaignV202301)

/2027-01/retail-media/campaigns/{campaignId}

Updates the campaign for the given campaign id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String campaignId = "campaignId_example"; // String | The given campaign id
        PutCampaignV202301 putCampaignV202301 = new PutCampaignV202301(); // PutCampaignV202301 | The campaign settings to update that campaign with
        try {
            JsonApiSingleResponseOfCampaignV202301 result = apiInstance.updateCampaignByCampaignId(campaignId, putCampaignV202301);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateCampaignByCampaignId");
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
| **campaignId** | **String**| The given campaign id | |
| **putCampaignV202301** | [**PutCampaignV202301**](PutCampaignV202301.md)| The campaign settings to update that campaign with | |

### Return type

[**JsonApiSingleResponseOfCampaignV202301**](JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateCreative

> Creative202210Response updateCreative(accountId, creativeId, creativeUpdateModel202207)

/2027-01/retail-media/accounts/{account-id}/creatives/{creative-id}

Update a creative

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | External account id containing the creative
        String creativeId = "creativeId_example"; // String | Creative to update
        CreativeUpdateModel202207 creativeUpdateModel202207 = new CreativeUpdateModel202207(); // CreativeUpdateModel202207 | The creative to create
        try {
            Creative202210Response result = apiInstance.updateCreative(accountId, creativeId, creativeUpdateModel202207);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateCreative");
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
| **accountId** | **String**| External account id containing the creative | |
| **creativeId** | **String**| Creative to update | |
| **creativeUpdateModel202207** | [**CreativeUpdateModel202207**](CreativeUpdateModel202207.md)| The creative to create | |

### Return type

[**Creative202210Response**](Creative202210Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creative updated |  -  |


## updateKeywordReviews

> ValueResourceOutcomeRetailMediaKeywordsReviewResult updateKeywordReviews(lineItemId, valueResourceInputRetailMediaKeywordsReview)

/2027-01/retail-media/line-items/{line-item-id}/keywords/review

Update the status of keyword reviews under a line item

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The line item to update keyword review statuses for
        ValueResourceInputRetailMediaKeywordsReview valueResourceInputRetailMediaKeywordsReview = new ValueResourceInputRetailMediaKeywordsReview(); // ValueResourceInputRetailMediaKeywordsReview | Request object containing a list of Phrase-ReviewState pairs to update
        try {
            ValueResourceOutcomeRetailMediaKeywordsReviewResult result = apiInstance.updateKeywordReviews(lineItemId, valueResourceInputRetailMediaKeywordsReview);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateKeywordReviews");
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
| **lineItemId** | **String**| The line item to update keyword review statuses for | |
| **valueResourceInputRetailMediaKeywordsReview** | [**ValueResourceInputRetailMediaKeywordsReview**](ValueResourceInputRetailMediaKeywordsReview.md)| Request object containing a list of Phrase-ReviewState pairs to update | [optional] |

### Return type

[**ValueResourceOutcomeRetailMediaKeywordsReviewResult**](ValueResourceOutcomeRetailMediaKeywordsReviewResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateLineItemBudgetOverrides

> ValueResourceOutcomeOfLineItemBudgetOverrides updateLineItemBudgetOverrides(lineItemId, valueResourceInputOfLineItemBudgetOverrides)

/2027-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides

Update line item budget overrides by given external line item id and new line item budget overrides settings.

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | Line item external id.
        ValueResourceInputOfLineItemBudgetOverrides valueResourceInputOfLineItemBudgetOverrides = new ValueResourceInputOfLineItemBudgetOverrides(); // ValueResourceInputOfLineItemBudgetOverrides | New line item budget overrides settings value resource input.
        try {
            ValueResourceOutcomeOfLineItemBudgetOverrides result = apiInstance.updateLineItemBudgetOverrides(lineItemId, valueResourceInputOfLineItemBudgetOverrides);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateLineItemBudgetOverrides");
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
| **lineItemId** | **String**| Line item external id. | |
| **valueResourceInputOfLineItemBudgetOverrides** | [**ValueResourceInputOfLineItemBudgetOverrides**](ValueResourceInputOfLineItemBudgetOverrides.md)| New line item budget overrides settings value resource input. | |

### Return type

[**ValueResourceOutcomeOfLineItemBudgetOverrides**](ValueResourceOutcomeOfLineItemBudgetOverrides.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## updatePreferredLineItemByLineItemId

> PreferredLineItemV2Response updatePreferredLineItemByLineItemId(lineItemId, preferredLineItemUpdateModelV2Request)

/2027-01/retail-media/preferred-line-items/{line-item-id}

Updates the preferred line item for the given line item id

### Example

```java
package com.criteo.api.retailmedia.v2027_01;

import com.criteo.api.retailmedia.v2027_01.ApiClient;
import com.criteo.api.retailmedia.v2027_01.ApiClientBuilder;
import com.criteo.api.retailmedia.v2027_01.ApiException;
import com.criteo.api.retailmedia.v2027_01.Configuration;
import com.criteo.api.retailmedia.v2027_01.auth.*;
import com.criteo.api.retailmedia.v2027_01.model.*;
import com.criteo.api.retailmedia.v2027_01.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | The given line item id
        PreferredLineItemUpdateModelV2Request preferredLineItemUpdateModelV2Request = new PreferredLineItemUpdateModelV2Request(); // PreferredLineItemUpdateModelV2Request | The line item settings to create a line item with
        try {
            PreferredLineItemV2Response result = apiInstance.updatePreferredLineItemByLineItemId(lineItemId, preferredLineItemUpdateModelV2Request);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updatePreferredLineItemByLineItemId");
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
| **lineItemId** | **String**| The given line item id | |
| **preferredLineItemUpdateModelV2Request** | [**PreferredLineItemUpdateModelV2Request**](PreferredLineItemUpdateModelV2Request.md)| The line item settings to create a line item with | |

### Return type

[**PreferredLineItemV2Response**](PreferredLineItemV2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

