# CampaignApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appendCampaignsToBalanceV1**](CampaignApi.md#appendCampaignsToBalanceV1) | **POST** /experimental/retail-media/balances/{balanceId}/campaigns/append | /experimental/retail-media/balances/{balanceId}/campaigns/append |
| [**appendProductButtonByLineItemId**](CampaignApi.md#appendProductButtonByLineItemId) | **POST** /experimental/retail-media/line-items/{line-item-id}/product-buttons/create | /experimental/retail-media/line-items/{line-item-id}/product-buttons/create |
| [**appendPromotedProducts**](CampaignApi.md#appendPromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/append | /experimental/retail-media/line-items/{line-item-id}/products/append |
| [**computeDisplayMinBidByRetailerId**](CampaignApi.md#computeDisplayMinBidByRetailerId) | **POST** /experimental/retail-media/retailers/{retailerId}/compute-display-min-bid | /experimental/retail-media/retailers/{retailerId}/compute-display-min-bid |
| [**createAuctionLineItem**](CampaignApi.md#createAuctionLineItem) | **POST** /experimental/retail-media/campaigns/{campaignId}/auction-line-items | /experimental/retail-media/campaigns/{campaignId}/auction-line-items |
| [**createCreative**](CampaignApi.md#createCreative) | **POST** /experimental/retail-media/accounts/{account-id}/creatives | /experimental/retail-media/accounts/{account-id}/creatives |
| [**createPreferredLineItemByCampaignId**](CampaignApi.md#createPreferredLineItemByCampaignId) | **POST** /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items | /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**deleteCampaignsFromBalanceV1**](CampaignApi.md#deleteCampaignsFromBalanceV1) | **POST** /experimental/retail-media/balances/{balanceId}/campaigns/delete | /experimental/retail-media/balances/{balanceId}/campaigns/delete |
| [**deleteProductButtonByLineItemAndProductButtonId**](CampaignApi.md#deleteProductButtonByLineItemAndProductButtonId) | **DELETE** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} |
| [**deletePromotedProducts**](CampaignApi.md#deletePromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/delete | /experimental/retail-media/line-items/{line-item-id}/products/delete |
| [**fetchPromotedProducts**](CampaignApi.md#fetchPromotedProducts) | **GET** /experimental/retail-media/line-items/{line-item-id}/products | /experimental/retail-media/line-items/{line-item-id}/products |
| [**getAuctionLineItem**](CampaignApi.md#getAuctionLineItem) | **GET** /experimental/retail-media/auction-line-items/{lineItemId} | /experimental/retail-media/auction-line-items/{lineItemId} |
| [**getAuctionLineItemsByCampaign**](CampaignApi.md#getAuctionLineItemsByCampaign) | **GET** /experimental/retail-media/campaigns/{campaignId}/auction-line-items | /experimental/retail-media/campaigns/{campaignId}/auction-line-items |
| [**getCapoutHistory**](CampaignApi.md#getCapoutHistory) | **POST** /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history | /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history |
| [**getCatalogStatus**](CampaignApi.md#getCatalogStatus) | **GET** /experimental/retail-media/catalogs/{catalogId}/status | /experimental/retail-media/catalogs/{catalogId}/status |
| [**getCreative**](CampaignApi.md#getCreative) | **GET** /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} | /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**getPreferredLineItemsByCampaignId**](CampaignApi.md#getPreferredLineItemsByCampaignId) | **GET** /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items | /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**getPreferredLineItemsByLineItemId**](CampaignApi.md#getPreferredLineItemsByLineItemId) | **GET** /experimental/retail-media/preferred-line-items/{line-item-id} | /experimental/retail-media/preferred-line-items/{line-item-id} |
| [**getProductButtonByLineItemAndProductButtonId**](CampaignApi.md#getProductButtonByLineItemAndProductButtonId) | **GET** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} |
| [**getProductButtonsByLineItemId**](CampaignApi.md#getProductButtonsByLineItemId) | **GET** /experimental/retail-media/line-items/{line-item-id}/product-buttons | /experimental/retail-media/line-items/{line-item-id}/product-buttons |
| [**pausePromotedProducts**](CampaignApi.md#pausePromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/pause | /experimental/retail-media/line-items/{line-item-id}/products/pause |
| [**searchAccountCreatives**](CampaignApi.md#searchAccountCreatives) | **POST** /experimental/retail-media/accounts/{account-id}/creatives/search | /experimental/retail-media/accounts/{account-id}/creatives/search |
| [**searchAccountRetailers**](CampaignApi.md#searchAccountRetailers) | **POST** /experimental/retail-media/accounts/{accountId}/retailers/search | /experimental/retail-media/accounts/{accountId}/retailers/search |
| [**unpausePromotedProducts**](CampaignApi.md#unpausePromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/unpause | /experimental/retail-media/line-items/{line-item-id}/products/unpause |
| [**updateAuctionLineItem**](CampaignApi.md#updateAuctionLineItem) | **PUT** /experimental/retail-media/auction-line-items/{lineItemId} | /experimental/retail-media/auction-line-items/{lineItemId} |
| [**updateCreative**](CampaignApi.md#updateCreative) | **PUT** /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} | /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**updatePreferredLineItemByLineItemId**](CampaignApi.md#updatePreferredLineItemByLineItemId) | **PUT** /experimental/retail-media/preferred-line-items/{line-item-id} | /experimental/retail-media/preferred-line-items/{line-item-id} |
| [**updateProductButtonByLineItemAndProductButtonId**](CampaignApi.md#updateProductButtonByLineItemAndProductButtonId) | **PUT** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} |



## appendCampaignsToBalanceV1

> ValueResourceOutcomeBalanceCampaignsV1 appendCampaignsToBalanceV1(balanceId, valueResourceInputAppendCampaignsRequestV1)

/experimental/retail-media/balances/{balanceId}/campaigns/append

Appends one or more campaigns to the specified balance

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## appendProductButtonByLineItemId

> ProductButtonResponseListResponse appendProductButtonByLineItemId(lineItemId, productButtonRequestListRequest)

/experimental/retail-media/line-items/{line-item-id}/product-buttons/create

Add Specific Product Buttons

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for productButton retrieval
        ProductButtonRequestListRequest productButtonRequestListRequest = new ProductButtonRequestListRequest(); // ProductButtonRequestListRequest | List of Product Buttons to append
        try {
            ProductButtonResponseListResponse result = apiInstance.appendProductButtonByLineItemId(lineItemId, productButtonRequestListRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#appendProductButtonByLineItemId");
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
| **lineItemId** | **String**| LineItemId for productButton retrieval | |
| **productButtonRequestListRequest** | [**ProductButtonRequestListRequest**](ProductButtonRequestListRequest.md)| List of Product Buttons to append | [optional] |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProductButtons added |  -  |


## appendPromotedProducts

> ProductResourceOutcome appendPromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/experimental/retail-media/line-items/{line-item-id}/products/append

Append a collection of promoted products to a line item

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## computeDisplayMinBidByRetailerId

> ValueResourceCollectionOutcomeDisplayAuctionMinBidResult computeDisplayMinBidByRetailerId(retailerId, valueResourceInputDisplayAuctionMinBidRequest)

/experimental/retail-media/retailers/{retailerId}/compute-display-min-bid

Computes the min bid for relevant page types based on the provided information

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String retailerId = "retailerId_example"; // String | The retailer id
        ValueResourceInputDisplayAuctionMinBidRequest valueResourceInputDisplayAuctionMinBidRequest = new ValueResourceInputDisplayAuctionMinBidRequest(); // ValueResourceInputDisplayAuctionMinBidRequest | The details for what creatives and product ids to use to compute the min bids
        try {
            ValueResourceCollectionOutcomeDisplayAuctionMinBidResult result = apiInstance.computeDisplayMinBidByRetailerId(retailerId, valueResourceInputDisplayAuctionMinBidRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#computeDisplayMinBidByRetailerId");
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
| **retailerId** | **String**| The retailer id | |
| **valueResourceInputDisplayAuctionMinBidRequest** | [**ValueResourceInputDisplayAuctionMinBidRequest**](ValueResourceInputDisplayAuctionMinBidRequest.md)| The details for what creatives and product ids to use to compute the min bids | [optional] |

### Return type

[**ValueResourceCollectionOutcomeDisplayAuctionMinBidResult**](ValueResourceCollectionOutcomeDisplayAuctionMinBidResult.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## createAuctionLineItem

> EntityResourceOutcomeOfSponsoredProductsLineItem createAuctionLineItem(campaignId, valueResourceInputOfSponsoredProductsLineItemCreateRequestModel)

/experimental/retail-media/campaigns/{campaignId}/auction-line-items

Creates new auction line item with the specified settings

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## createCreative

> Creative2Response createCreative(accountId, creativeCreateModel2)

/experimental/retail-media/accounts/{account-id}/creatives

Create a creative for an account

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        CreativeCreateModel2 creativeCreateModel2 = new CreativeCreateModel2(); // CreativeCreateModel2 | The creative to create
        try {
            Creative2Response result = apiInstance.createCreative(accountId, creativeCreateModel2);
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
| **creativeCreateModel2** | [**CreativeCreateModel2**](CreativeCreateModel2.md)| The creative to create | |

### Return type

[**Creative2Response**](Creative2Response.md)

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

/experimental/retail-media/campaigns/{campaign-id}/preferred-line-items

Creates a new preferred line item with the specified settings

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## deleteCampaignsFromBalanceV1

> ValueResourceOutcomeBalanceCampaignsV1 deleteCampaignsFromBalanceV1(balanceId, valueResourceInputDeleteCampaignsRequestV1)

/experimental/retail-media/balances/{balanceId}/campaigns/delete

Deletes one or more campaigns on the specified balance

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## deleteProductButtonByLineItemAndProductButtonId

> ProductButtonResponseListResponse deleteProductButtonByLineItemAndProductButtonId(lineItemId, productButtonId)

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Delete Specific Product Button

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for productButton delete
        String productButtonId = "productButtonId_example"; // String | productButtonId used for delete
        try {
            ProductButtonResponseListResponse result = apiInstance.deleteProductButtonByLineItemAndProductButtonId(lineItemId, productButtonId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#deleteProductButtonByLineItemAndProductButtonId");
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
| **lineItemId** | **String**| LineItemId for productButton delete | |
| **productButtonId** | **String**| productButtonId used for delete | |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProductButton deleted |  -  |


## deletePromotedProducts

> deletePromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/experimental/retail-media/line-items/{line-item-id}/products/delete

Remove a collection of promoted products from a line item

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## fetchPromotedProducts

> PromotedProductResourceCollectionOutcome fetchPromotedProducts(lineItemId, fields, limit, offset)

/experimental/retail-media/line-items/{line-item-id}/products

Retrieve a page of promoted products for a line item

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## getAuctionLineItem

> EntityResourceOutcomeOfSponsoredProductsLineItem getAuctionLineItem(lineItemId)

/experimental/retail-media/auction-line-items/{lineItemId}

Gets a sponsored product line item by its id.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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

/experimental/retail-media/campaigns/{campaignId}/auction-line-items

Gets a page of sponsored product line items by campaign id.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## getCapoutHistory

> ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse getCapoutHistory(accountId, valueResourceInputLineItemBudgetCapOutHistoryRequest)

/experimental/retail-media/accounts/{account-id}/line-items/cap-out-history

Get the cap out history for line items

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String accountId = "accountId_example"; // String | account id that own the lineitem
        ValueResourceInputLineItemBudgetCapOutHistoryRequest valueResourceInputLineItemBudgetCapOutHistoryRequest = new ValueResourceInputLineItemBudgetCapOutHistoryRequest(); // ValueResourceInputLineItemBudgetCapOutHistoryRequest | lineitem budgetcapout history  object
        try {
            ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse result = apiInstance.getCapoutHistory(accountId, valueResourceInputLineItemBudgetCapOutHistoryRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getCapoutHistory");
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
| **accountId** | **String**| account id that own the lineitem | |
| **valueResourceInputLineItemBudgetCapOutHistoryRequest** | [**ValueResourceInputLineItemBudgetCapOutHistoryRequest**](ValueResourceInputLineItemBudgetCapOutHistoryRequest.md)| lineitem budgetcapout history  object | |

### Return type

[**ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse**](ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## getCatalogStatus

> EntityResourceOutcomeOfCatalogStatusV2 getCatalogStatus(catalogId)

/experimental/retail-media/catalogs/{catalogId}/status

Check the status of a catalog request.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
            EntityResourceOutcomeOfCatalogStatusV2 result = apiInstance.getCatalogStatus(catalogId);
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

[**EntityResourceOutcomeOfCatalogStatusV2**](EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog request found. |  -  |


## getCreative

> Creative2Response getCreative(accountId, creativeId)

/experimental/retail-media/accounts/{account-id}/creatives/{creative-id}

Get the specified creative

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## getPreferredLineItemsByCampaignId

> PreferredLineItemV2PagedListResponse getPreferredLineItemsByCampaignId(campaignId, limitToId, pageIndex, pageSize)

/experimental/retail-media/campaigns/{campaign-id}/preferred-line-items

Gets page of preferred line item objects for the given campaign id

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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

/experimental/retail-media/preferred-line-items/{line-item-id}

Gets the preferred line item for the given line item id

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## getProductButtonByLineItemAndProductButtonId

> ProductButtonResponseListResponse getProductButtonByLineItemAndProductButtonId(lineItemId, productButtonId)

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Get Specific Product Button

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for productButton retrieval
        String productButtonId = "productButtonId_example"; // String | productButtonId used for retrieval
        try {
            ProductButtonResponseListResponse result = apiInstance.getProductButtonByLineItemAndProductButtonId(lineItemId, productButtonId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getProductButtonByLineItemAndProductButtonId");
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
| **lineItemId** | **String**| LineItemId for productButton retrieval | |
| **productButtonId** | **String**| productButtonId used for retrieval | |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProductButton found |  -  |


## getProductButtonsByLineItemId

> ProductButtonResponseListResponse getProductButtonsByLineItemId(lineItemId)

/experimental/retail-media/line-items/{line-item-id}/product-buttons

Get LineItem Product Buttons

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for productButton retrieval
        try {
            ProductButtonResponseListResponse result = apiInstance.getProductButtonsByLineItemId(lineItemId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#getProductButtonsByLineItemId");
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
| **lineItemId** | **String**| LineItemId for productButton retrieval | |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProductButtons found |  -  |


## pausePromotedProducts

> pausePromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/experimental/retail-media/line-items/{line-item-id}/products/pause

Pause a collection of promoted products associated with a line item

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## searchAccountCreatives

> EntityResourceCollectionOutcomeCreativeSearchResponse searchAccountCreatives(accountId, entityResourceInputCreativeSearchRequest, limit, offset)

/experimental/retail-media/accounts/{account-id}/creatives/search

Get account creatives

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        EntityResourceInputCreativeSearchRequest entityResourceInputCreativeSearchRequest = new EntityResourceInputCreativeSearchRequest(); // EntityResourceInputCreativeSearchRequest | search request filter
        Integer limit = 50; // Integer | limit to paginated result
        Integer offset = 0; // Integer | offset to paginated result
        try {
            EntityResourceCollectionOutcomeCreativeSearchResponse result = apiInstance.searchAccountCreatives(accountId, entityResourceInputCreativeSearchRequest, limit, offset);
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
| **entityResourceInputCreativeSearchRequest** | [**EntityResourceInputCreativeSearchRequest**](EntityResourceInputCreativeSearchRequest.md)| search request filter | |
| **limit** | **Integer**| limit to paginated result | [optional] [default to 50] |
| **offset** | **Integer**| offset to paginated result | [optional] [default to 0] |

### Return type

[**EntityResourceCollectionOutcomeCreativeSearchResponse**](EntityResourceCollectionOutcomeCreativeSearchResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives found |  -  |


## searchAccountRetailers

> EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata searchAccountRetailers(accountId, valueResourceInputOfRetailerSearchRequestV2, limit, offset)

/experimental/retail-media/accounts/{accountId}/retailers/search

Searches for retailers associated with the specified account and returns budget model availability for each retailer

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## unpausePromotedProducts

> unpausePromotedProducts(lineItemId, promotedProductResourceCollectionInput)

/experimental/retail-media/line-items/{line-item-id}/products/unpause

Un-pause a collection of promoted products associated with a line item

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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

/experimental/retail-media/auction-line-items/{lineItemId}

Updates a Sponsored Products Line Item given a line item id and a request.

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## updateCreative

> Creative2Response updateCreative(accountId, creativeId, creativeUpdateModel2)

/experimental/retail-media/accounts/{account-id}/creatives/{creative-id}

Update a creative

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        CreativeUpdateModel2 creativeUpdateModel2 = new CreativeUpdateModel2(); // CreativeUpdateModel2 | The creative to create
        try {
            Creative2Response result = apiInstance.updateCreative(accountId, creativeId, creativeUpdateModel2);
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
| **creativeUpdateModel2** | [**CreativeUpdateModel2**](CreativeUpdateModel2.md)| The creative to create | |

### Return type

[**Creative2Response**](Creative2Response.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | Creative updated |  -  |


## updatePreferredLineItemByLineItemId

> PreferredLineItemV2Response updatePreferredLineItemByLineItemId(lineItemId, preferredLineItemUpdateModelV2Request)

/experimental/retail-media/preferred-line-items/{line-item-id}

Updates the preferred line item for the given line item id

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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


## updateProductButtonByLineItemAndProductButtonId

> ProductButtonResponseListResponse updateProductButtonByLineItemAndProductButtonId(lineItemId, productButtonId, productButtonRequestRequest)

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Update Specific Product Button

### Example

```java
package com.criteo.api.retailmedia.experimental;

import com.criteo.api.retailmedia.experimental.ApiClient;
import com.criteo.api.retailmedia.experimental.ApiClientBuilder;
import com.criteo.api.retailmedia.experimental.ApiException;
import com.criteo.api.retailmedia.experimental.Configuration;
import com.criteo.api.retailmedia.experimental.auth.*;
import com.criteo.api.retailmedia.experimental.model.*;
import com.criteo.api.retailmedia.experimental.api.CampaignApi;

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
        String lineItemId = "lineItemId_example"; // String | LineItemId for productButton update
        String productButtonId = "productButtonId_example"; // String | productButtonId used for update
        ProductButtonRequestRequest productButtonRequestRequest = new ProductButtonRequestRequest(); // ProductButtonRequestRequest | Specific Product button update info
        try {
            ProductButtonResponseListResponse result = apiInstance.updateProductButtonByLineItemAndProductButtonId(lineItemId, productButtonId, productButtonRequestRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CampaignApi#updateProductButtonByLineItemAndProductButtonId");
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
| **lineItemId** | **String**| LineItemId for productButton update | |
| **productButtonId** | **String**| productButtonId used for update | |
| **productButtonRequestRequest** | [**ProductButtonRequestRequest**](ProductButtonRequestRequest.md)| Specific Product button update info | |

### Return type

[**ProductButtonResponseListResponse**](ProductButtonResponseListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProductButton updated |  -  |

