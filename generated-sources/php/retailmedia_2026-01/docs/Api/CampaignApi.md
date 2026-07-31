# criteo\api\retailmedia\v2026_01\CampaignApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addRemoveKeywords()**](CampaignApi.md#addRemoveKeywords) | **POST** /2026-01/retail-media/line-items/{id}/keywords/add-remove | /2026-01/retail-media/line-items/{id}/keywords/add-remove |
| [**appendAddToBasketTargetsByLineItemId()**](CampaignApi.md#appendAddToBasketTargetsByLineItemId) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append |
| [**appendAudienceTargetsByLineItemId()**](CampaignApi.md#appendAudienceTargetsByLineItemId) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append |
| [**appendCampaignsByBalanceId()**](CampaignApi.md#appendCampaignsByBalanceId) | **POST** /2026-01/retail-media/balances/{balance-id}/campaigns/append | /2026-01/retail-media/balances/{balance-id}/campaigns/append |
| [**appendPromotedProducts()**](CampaignApi.md#appendPromotedProducts) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/append | /2026-01/retail-media/line-items/{line-item-id}/products/append |
| [**appendStoreTargetsByLineItemId()**](CampaignApi.md#appendStoreTargetsByLineItemId) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append |
| [**createAsset()**](CampaignApi.md#createAsset) | **POST** /2026-01/retail-media/assets | /2026-01/retail-media/assets |
| [**createAuctionLineItem()**](CampaignApi.md#createAuctionLineItem) | **POST** /2026-01/retail-media/campaigns/{campaignId}/auction-line-items | /2026-01/retail-media/campaigns/{campaignId}/auction-line-items |
| [**createBrandCatalogExport()**](CampaignApi.md#createBrandCatalogExport) | **POST** /2026-01/retail-media/accounts/{accountId}/brand-catalog-export | /2026-01/retail-media/accounts/{accountId}/brand-catalog-export |
| [**createCampaignsByAccountId()**](CampaignApi.md#createCampaignsByAccountId) | **POST** /2026-01/retail-media/accounts/{account-id}/campaigns | /2026-01/retail-media/accounts/{account-id}/campaigns |
| [**createCreative()**](CampaignApi.md#createCreative) | **POST** /2026-01/retail-media/accounts/{account-id}/creatives | /2026-01/retail-media/accounts/{account-id}/creatives |
| [**createPreferredLineItemByCampaignId()**](CampaignApi.md#createPreferredLineItemByCampaignId) | **POST** /2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items | /2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**createSellerCatalogExport()**](CampaignApi.md#createSellerCatalogExport) | **POST** /2026-01/retail-media/accounts/{accountId}/seller-catalog-export | /2026-01/retail-media/accounts/{accountId}/seller-catalog-export |
| [**deleteAddToBasketTargetsByLineItemId()**](CampaignApi.md#deleteAddToBasketTargetsByLineItemId) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete |
| [**deleteAudienceTargetsByLineItemId()**](CampaignApi.md#deleteAudienceTargetsByLineItemId) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete |
| [**deleteCampaignsByBalanceId()**](CampaignApi.md#deleteCampaignsByBalanceId) | **POST** /2026-01/retail-media/balances/{balance-id}/campaigns/delete | /2026-01/retail-media/balances/{balance-id}/campaigns/delete |
| [**deletePromotedProducts()**](CampaignApi.md#deletePromotedProducts) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/delete | /2026-01/retail-media/line-items/{line-item-id}/products/delete |
| [**deleteStoreTargetByLineItemId()**](CampaignApi.md#deleteStoreTargetByLineItemId) | **POST** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete |
| [**fetchKeywords()**](CampaignApi.md#fetchKeywords) | **GET** /2026-01/retail-media/line-items/{id}/keywords | /2026-01/retail-media/line-items/{id}/keywords |
| [**fetchPromotedProducts()**](CampaignApi.md#fetchPromotedProducts) | **GET** /2026-01/retail-media/line-items/{line-item-id}/products | /2026-01/retail-media/line-items/{line-item-id}/products |
| [**getAccountCreatives()**](CampaignApi.md#getAccountCreatives) | **GET** /2026-01/retail-media/accounts/{account-id}/creatives | /2026-01/retail-media/accounts/{account-id}/creatives |
| [**getAddToBasketTargetsByLineItemId()**](CampaignApi.md#getAddToBasketTargetsByLineItemId) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket |
| [**getApi202110ExternalRetailerPagesByRetailerId()**](CampaignApi.md#getApi202110ExternalRetailerPagesByRetailerId) | **GET** /2026-01/retail-media/retailers/{retailerId}/pages | /2026-01/retail-media/retailers/{retailerId}/pages |
| [**getApiExternalV1Categories()**](CampaignApi.md#getApiExternalV1Categories) | **GET** /2026-01/retail-media/categories | /2026-01/retail-media/categories |
| [**getAuctionLineItem()**](CampaignApi.md#getAuctionLineItem) | **GET** /2026-01/retail-media/auction-line-items/{lineItemId} | /2026-01/retail-media/auction-line-items/{lineItemId} |
| [**getAuctionLineItemsByCampaign()**](CampaignApi.md#getAuctionLineItemsByCampaign) | **GET** /2026-01/retail-media/campaigns/{campaignId}/auction-line-items | /2026-01/retail-media/campaigns/{campaignId}/auction-line-items |
| [**getAudienceTargetsByLineItemId()**](CampaignApi.md#getAudienceTargetsByLineItemId) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences |
| [**getBidMultipliersByLineItemId()**](CampaignApi.md#getBidMultipliersByLineItemId) | **GET** /2026-01/retail-media/line-items/{line-item-id}/bid-multipliers | /2026-01/retail-media/line-items/{line-item-id}/bid-multipliers |
| [**getBrandsByAccountId()**](CampaignApi.md#getBrandsByAccountId) | **GET** /2026-01/retail-media/accounts/{accountId}/brands | /2026-01/retail-media/accounts/{accountId}/brands |
| [**getCampaignBudgetOverrides()**](CampaignApi.md#getCampaignBudgetOverrides) | **GET** /2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | /2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides |
| [**getCampaignByCampaignId()**](CampaignApi.md#getCampaignByCampaignId) | **GET** /2026-01/retail-media/campaigns/{campaignId} | /2026-01/retail-media/campaigns/{campaignId} |
| [**getCampaignsByAccountId()**](CampaignApi.md#getCampaignsByAccountId) | **GET** /2026-01/retail-media/accounts/{account-id}/campaigns | /2026-01/retail-media/accounts/{account-id}/campaigns |
| [**getCatalogOutput()**](CampaignApi.md#getCatalogOutput) | **GET** /2026-01/retail-media/catalogs/{catalogId}/output | /2026-01/retail-media/catalogs/{catalogId}/output |
| [**getCatalogStatus()**](CampaignApi.md#getCatalogStatus) | **GET** /2026-01/retail-media/catalogs/{catalogId}/status | /2026-01/retail-media/catalogs/{catalogId}/status |
| [**getCategory()**](CampaignApi.md#getCategory) | **GET** /2026-01/retail-media/categories/{categoryId} | /2026-01/retail-media/categories/{categoryId} |
| [**getCpcMinBidsBySkuIdsV1()**](CampaignApi.md#getCpcMinBidsBySkuIdsV1) | **POST** /2026-01/retail-media/retailers/{retailerId}/cpc-min-bids | /2026-01/retail-media/retailers/{retailerId}/cpc-min-bids |
| [**getCreative()**](CampaignApi.md#getCreative) | **GET** /2026-01/retail-media/accounts/{account-id}/creatives/{creative-id} | /2026-01/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**getCreativeTemplate()**](CampaignApi.md#getCreativeTemplate) | **GET** /2026-01/retail-media/retailers/{retailer-id}/templates/{template-id} | /2026-01/retail-media/retailers/{retailer-id}/templates/{template-id} |
| [**getKeywordInReviewReport()**](CampaignApi.md#getKeywordInReviewReport) | **GET** /2026-01/retail-media/accounts/{account-id}/keywords/in-review-report | /2026-01/retail-media/accounts/{account-id}/keywords/in-review-report |
| [**getLineItemBudgetOverrides()**](CampaignApi.md#getLineItemBudgetOverrides) | **GET** /2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | /2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides |
| [**getLineItemsByAccountId()**](CampaignApi.md#getLineItemsByAccountId) | **GET** /2026-01/retail-media/accounts/{account-id}/line-items | /2026-01/retail-media/accounts/{account-id}/line-items |
| [**getLineItemsByCampaignId()**](CampaignApi.md#getLineItemsByCampaignId) | **GET** /2026-01/retail-media/line-items/{line-item-id} | /2026-01/retail-media/line-items/{line-item-id} |
| [**getPreferredLineItemsByCampaignId()**](CampaignApi.md#getPreferredLineItemsByCampaignId) | **GET** /2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items | /2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**getPreferredLineItemsByLineItemId()**](CampaignApi.md#getPreferredLineItemsByLineItemId) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id} | /2026-01/retail-media/preferred-line-items/{line-item-id} |
| [**getRecommendedCategories()**](CampaignApi.md#getRecommendedCategories) | **POST** /2026-01/retail-media/retailers/{retailerId}/recommend-categories | /2026-01/retail-media/retailers/{retailerId}/recommend-categories |
| [**getRecommendedKeywords()**](CampaignApi.md#getRecommendedKeywords) | **GET** /2026-01/retail-media/line-items/{externalLineItemId}/keywords/recommended | /2026-01/retail-media/line-items/{externalLineItemId}/keywords/recommended |
| [**getRetailerCreativeTemplates()**](CampaignApi.md#getRetailerCreativeTemplates) | **GET** /2026-01/retail-media/retailers/{retailer-id}/templates | /2026-01/retail-media/retailers/{retailer-id}/templates |
| [**getStoreTargetsByLineItemId()**](CampaignApi.md#getStoreTargetsByLineItemId) | **GET** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores |
| [**pausePromotedProducts()**](CampaignApi.md#pausePromotedProducts) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/pause | /2026-01/retail-media/line-items/{line-item-id}/products/pause |
| [**postApiExternalV1AccountCatalogsSellersByAccountId()**](CampaignApi.md#postApiExternalV1AccountCatalogsSellersByAccountId) | **POST** /2026-01/retail-media/accounts/{accountId}/catalogs/sellers | /2026-01/retail-media/accounts/{accountId}/catalogs/sellers |
| [**postApiV1ExternalAccountCatalogsByAccountId()**](CampaignApi.md#postApiV1ExternalAccountCatalogsByAccountId) | **POST** /2026-01/retail-media/accounts/{accountId}/catalogs | /2026-01/retail-media/accounts/{accountId}/catalogs |
| [**putAddToBasketTargetByLineItemId()**](CampaignApi.md#putAddToBasketTargetByLineItemId) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket |
| [**putAudienceTargetsByLineItemId()**](CampaignApi.md#putAudienceTargetsByLineItemId) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences |
| [**putStoreTargetByLineItemId()**](CampaignApi.md#putStoreTargetByLineItemId) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores | /2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores |
| [**recommendedKeywords()**](CampaignApi.md#recommendedKeywords) | **POST** /2026-01/retail-media/retailers/{retailerId}/recommend-keywords | /2026-01/retail-media/retailers/{retailerId}/recommend-keywords |
| [**searchAccountCreatives()**](CampaignApi.md#searchAccountCreatives) | **POST** /2026-01/retail-media/accounts/{account-id}/creatives/search | /2026-01/retail-media/accounts/{account-id}/creatives/search |
| [**searchAccountRetailers()**](CampaignApi.md#searchAccountRetailers) | **POST** /2026-01/retail-media/accounts/{accountId}/retailers/search | /2026-01/retail-media/accounts/{accountId}/retailers/search |
| [**searchCategory()**](CampaignApi.md#searchCategory) | **POST** /2026-01/retail-media/retailers/{retailerId}/categories/search | /2026-01/retail-media/retailers/{retailerId}/categories/search |
| [**setKeywordBids()**](CampaignApi.md#setKeywordBids) | **POST** /2026-01/retail-media/line-items/{id}/keywords/set-bid | /2026-01/retail-media/line-items/{id}/keywords/set-bid |
| [**unpausePromotedProducts()**](CampaignApi.md#unpausePromotedProducts) | **POST** /2026-01/retail-media/line-items/{line-item-id}/products/unpause | /2026-01/retail-media/line-items/{line-item-id}/products/unpause |
| [**updateAuctionLineItem()**](CampaignApi.md#updateAuctionLineItem) | **PUT** /2026-01/retail-media/auction-line-items/{lineItemId} | /2026-01/retail-media/auction-line-items/{lineItemId} |
| [**updateBidMultipliersByLineItemId()**](CampaignApi.md#updateBidMultipliersByLineItemId) | **PUT** /2026-01/retail-media/line-items/{line-item-id}/bid-multipliers | /2026-01/retail-media/line-items/{line-item-id}/bid-multipliers |
| [**updateCampaignBudgetOverrides()**](CampaignApi.md#updateCampaignBudgetOverrides) | **PUT** /2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides | /2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides |
| [**updateCampaignByCampaignId()**](CampaignApi.md#updateCampaignByCampaignId) | **PUT** /2026-01/retail-media/campaigns/{campaignId} | /2026-01/retail-media/campaigns/{campaignId} |
| [**updateCreative()**](CampaignApi.md#updateCreative) | **PUT** /2026-01/retail-media/accounts/{account-id}/creatives/{creative-id} | /2026-01/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**updateKeywordReviews()**](CampaignApi.md#updateKeywordReviews) | **POST** /2026-01/retail-media/line-items/{line-item-id}/keywords/review | /2026-01/retail-media/line-items/{line-item-id}/keywords/review |
| [**updateLineItemBudgetOverrides()**](CampaignApi.md#updateLineItemBudgetOverrides) | **PUT** /2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides | /2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides |
| [**updatePreferredLineItemByLineItemId()**](CampaignApi.md#updatePreferredLineItemByLineItemId) | **PUT** /2026-01/retail-media/preferred-line-items/{line-item-id} | /2026-01/retail-media/preferred-line-items/{line-item-id} |


## `addRemoveKeywords()`

```php
addRemoveKeywords($id, $add_remove_keywords_model_request): \criteo\api\retailmedia\v2026_01\Model\ResourceOutcome
```

/2026-01/retail-media/line-items/{id}/keywords/add-remove

Add or Remove keywords from the line item in bulk

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | ID of the line item
$add_remove_keywords_model_request = new \criteo\api\retailmedia\v2026_01\Model\AddRemoveKeywordsModelRequest(); // \criteo\api\retailmedia\v2026_01\Model\AddRemoveKeywordsModelRequest

try {
    $result = $apiInstance->addRemoveKeywords($id, $add_remove_keywords_model_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->addRemoveKeywords: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| ID of the line item | |
| **add_remove_keywords_model_request** | [**\criteo\api\retailmedia\v2026_01\Model\AddRemoveKeywordsModelRequest**](../Model/AddRemoveKeywordsModelRequest.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ResourceOutcome**](../Model/ResourceOutcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `appendAddToBasketTargetsByLineItemId()`

```php
appendAddToBasketTargetsByLineItemId($line_item_id, $add_to_basket_ids_update_model202110_request): \criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/append

This endpoint appends one or more add to basket ids to targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$add_to_basket_ids_update_model202110_request = new \criteo\api\retailmedia\v2026_01\Model\AddToBasketIdsUpdateModel202110Request(); // \criteo\api\retailmedia\v2026_01\Model\AddToBasketIdsUpdateModel202110Request | Ids to append to the target

try {
    $result = $apiInstance->appendAddToBasketTargetsByLineItemId($line_item_id, $add_to_basket_ids_update_model202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendAddToBasketTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **add_to_basket_ids_update_model202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\AddToBasketIdsUpdateModel202110Request**](../Model/AddToBasketIdsUpdateModel202110Request.md)| Ids to append to the target | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response**](../Model/AddToBasketTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `appendAudienceTargetsByLineItemId()`

```php
appendAudienceTargetsByLineItemId($line_item_id, $audience_ids_update_model202110_request): \criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/append

This endpoint appends one or more audiences ids to targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$audience_ids_update_model202110_request = new \criteo\api\retailmedia\v2026_01\Model\AudienceIdsUpdateModel202110Request(); // \criteo\api\retailmedia\v2026_01\Model\AudienceIdsUpdateModel202110Request | Audience ids to append to the target

try {
    $result = $apiInstance->appendAudienceTargetsByLineItemId($line_item_id, $audience_ids_update_model202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendAudienceTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **audience_ids_update_model202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\AudienceIdsUpdateModel202110Request**](../Model/AudienceIdsUpdateModel202110Request.md)| Audience ids to append to the target | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response**](../Model/AudienceTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `appendCampaignsByBalanceId()`

```php
appendCampaignsByBalanceId($balance_id, $balance_campaign202110_list_request): \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110PagedListResponse
```

/2026-01/retail-media/balances/{balance-id}/campaigns/append

appends one or more campaigns to the specified balance

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | The balance to add campaigns from
$balance_campaign202110_list_request = new \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110ListRequest(); // \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110ListRequest | The campaigns to append

try {
    $result = $apiInstance->appendCampaignsByBalanceId($balance_id, $balance_campaign202110_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendCampaignsByBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| The balance to add campaigns from | |
| **balance_campaign202110_list_request** | [**\criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110ListRequest**](../Model/BalanceCampaign202110ListRequest.md)| The campaigns to append | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110PagedListResponse**](../Model/BalanceCampaign202110PagedListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `appendPromotedProducts()`

```php
appendPromotedProducts($line_item_id, $promoted_product_resource_collection_input): \criteo\api\retailmedia\v2026_01\Model\ProductResourceOutcome
```

/2026-01/retail-media/line-items/{line-item-id}/products/append

Append a collection of promoted products to a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

try {
    $result = $apiInstance->appendPromotedProducts($line_item_id, $promoted_product_resource_collection_input);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendPromotedProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| ID of the line item | |
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ProductResourceOutcome**](../Model/ProductResourceOutcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `appendStoreTargetsByLineItemId()`

```php
appendStoreTargetsByLineItemId($line_item_id, $store_ids_update_model202110_request): \criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/append

This endpoint appends one or more store ids to targeting on the specified line item.  The resulting state of the store target is returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$store_ids_update_model202110_request = new \criteo\api\retailmedia\v2026_01\Model\StoreIdsUpdateModel202110Request(); // \criteo\api\retailmedia\v2026_01\Model\StoreIdsUpdateModel202110Request | Store ids to append to the target

try {
    $result = $apiInstance->appendStoreTargetsByLineItemId($line_item_id, $store_ids_update_model202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendStoreTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **store_ids_update_model202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\StoreIdsUpdateModel202110Request**](../Model/StoreIdsUpdateModel202110Request.md)| Store ids to append to the target | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response**](../Model/StoreTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAsset()`

```php
createAsset($asset_file): \criteo\api\retailmedia\v2026_01\Model\AssetResponse
```

/2026-01/retail-media/assets

Creates an asset

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$asset_file = "/path/to/file.txt"; // \SplFileObject | The asset binary content

try {
    $result = $apiInstance->createAsset($asset_file);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createAsset: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **asset_file** | **\SplFileObject****\SplFileObject**| The asset binary content | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AssetResponse**](../Model/AssetResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAuctionLineItem()`

```php
createAuctionLineItem($campaign_id, $value_resource_input_of_sponsored_products_line_item_create_request_model): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfSponsoredProductsLineItem
```

/2026-01/retail-media/campaigns/{campaignId}/auction-line-items

Creates new auction line item with the specified settings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id
$value_resource_input_of_sponsored_products_line_item_create_request_model = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel | The line item settings to create a line item with

try {
    $result = $apiInstance->createAuctionLineItem($campaign_id, $value_resource_input_of_sponsored_products_line_item_create_request_model);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createAuctionLineItem: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The given campaign id | |
| **value_resource_input_of_sponsored_products_line_item_create_request_model** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel**](../Model/ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel.md)| The line item settings to create a line item with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfSponsoredProductsLineItem**](../Model/EntityResourceOutcomeOfSponsoredProductsLineItem.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createBrandCatalogExport()`

```php
createBrandCatalogExport($account_id, $value_resource_input_of_brand_catalog_request_v2): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfCatalogStatusV2
```

/2026-01/retail-media/accounts/{accountId}/brand-catalog-export

Create a request for a Catalog available to the indicated account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to request the catalog for.
$value_resource_input_of_brand_catalog_request_v2 = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfBrandCatalogRequestV2(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfBrandCatalogRequestV2

try {
    $result = $apiInstance->createBrandCatalogExport($account_id, $value_resource_input_of_brand_catalog_request_v2);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createBrandCatalogExport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to request the catalog for. | |
| **value_resource_input_of_brand_catalog_request_v2** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfBrandCatalogRequestV2**](../Model/ValueResourceInputOfBrandCatalogRequestV2.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfCatalogStatusV2**](../Model/EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createCampaignsByAccountId()`

```php
createCampaignsByAccountId($account_id, $post_campaign_v202301): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCampaignV202301
```

/2026-01/retail-media/accounts/{account-id}/campaigns

Creates a new campaign with the specified settings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$post_campaign_v202301 = new \criteo\api\retailmedia\v2026_01\Model\PostCampaignV202301(); // \criteo\api\retailmedia\v2026_01\Model\PostCampaignV202301 | The campaign settings to create a campaign with

try {
    $result = $apiInstance->createCampaignsByAccountId($account_id, $post_campaign_v202301);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createCampaignsByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **post_campaign_v202301** | [**\criteo\api\retailmedia\v2026_01\Model\PostCampaignV202301**](../Model/PostCampaignV202301.md)| The campaign settings to create a campaign with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCampaignV202301**](../Model/JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createCreative()`

```php
createCreative($account_id, $creative_create_model202207): \criteo\api\retailmedia\v2026_01\Model\Creative202210Response
```

/2026-01/retail-media/accounts/{account-id}/creatives

Create a creative for an account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id to create a creative for
$creative_create_model202207 = new \criteo\api\retailmedia\v2026_01\Model\CreativeCreateModel202207(); // \criteo\api\retailmedia\v2026_01\Model\CreativeCreateModel202207 | The creative to create

try {
    $result = $apiInstance->createCreative($account_id, $creative_create_model202207);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id to create a creative for | |
| **creative_create_model202207** | [**\criteo\api\retailmedia\v2026_01\Model\CreativeCreateModel202207**](../Model/CreativeCreateModel202207.md)| The creative to create | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Creative202210Response**](../Model/Creative202210Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createPreferredLineItemByCampaignId()`

```php
createPreferredLineItemByCampaignId($campaign_id, $preferred_line_item_create_model_v2_request): \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2Response
```

/2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items

Creates a new preferred line item with the specified settings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id
$preferred_line_item_create_model_v2_request = new \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemCreateModelV2Request(); // \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemCreateModelV2Request | The line item settings to create a line item with

try {
    $result = $apiInstance->createPreferredLineItemByCampaignId($campaign_id, $preferred_line_item_create_model_v2_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createPreferredLineItemByCampaignId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The given campaign id | |
| **preferred_line_item_create_model_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\PreferredLineItemCreateModelV2Request**](../Model/PreferredLineItemCreateModelV2Request.md)| The line item settings to create a line item with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2Response**](../Model/PreferredLineItemV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createSellerCatalogExport()`

```php
createSellerCatalogExport($account_id, $value_resource_input_of_seller_catalog_request_v2): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfCatalogStatusV2
```

/2026-01/retail-media/accounts/{accountId}/seller-catalog-export

Create a request for a Catalog available to the indicated account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to request the catalog for.
$value_resource_input_of_seller_catalog_request_v2 = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSellerCatalogRequestV2(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSellerCatalogRequestV2

try {
    $result = $apiInstance->createSellerCatalogExport($account_id, $value_resource_input_of_seller_catalog_request_v2);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createSellerCatalogExport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to request the catalog for. | |
| **value_resource_input_of_seller_catalog_request_v2** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSellerCatalogRequestV2**](../Model/ValueResourceInputOfSellerCatalogRequestV2.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfCatalogStatusV2**](../Model/EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAddToBasketTargetsByLineItemId()`

```php
deleteAddToBasketTargetsByLineItemId($line_item_id, $add_to_basket_ids_update_model202110_request): \criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket/delete

This endpoint removes one or more add to basket ids from targeting on the specified line item.  The resulting state of the add to basket target is returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$add_to_basket_ids_update_model202110_request = new \criteo\api\retailmedia\v2026_01\Model\AddToBasketIdsUpdateModel202110Request(); // \criteo\api\retailmedia\v2026_01\Model\AddToBasketIdsUpdateModel202110Request | Ids to remove from the target

try {
    $result = $apiInstance->deleteAddToBasketTargetsByLineItemId($line_item_id, $add_to_basket_ids_update_model202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteAddToBasketTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **add_to_basket_ids_update_model202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\AddToBasketIdsUpdateModel202110Request**](../Model/AddToBasketIdsUpdateModel202110Request.md)| Ids to remove from the target | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response**](../Model/AddToBasketTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAudienceTargetsByLineItemId()`

```php
deleteAudienceTargetsByLineItemId($line_item_id, $audience_ids_update_model202110_request): \criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences/delete

This endpoint removes one or more audiences ids from targeting on the specified line item.  The resulting state of the audience target is returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$audience_ids_update_model202110_request = new \criteo\api\retailmedia\v2026_01\Model\AudienceIdsUpdateModel202110Request(); // \criteo\api\retailmedia\v2026_01\Model\AudienceIdsUpdateModel202110Request | Audience ids to remove from the target

try {
    $result = $apiInstance->deleteAudienceTargetsByLineItemId($line_item_id, $audience_ids_update_model202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteAudienceTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **audience_ids_update_model202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\AudienceIdsUpdateModel202110Request**](../Model/AudienceIdsUpdateModel202110Request.md)| Audience ids to remove from the target | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response**](../Model/AudienceTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCampaignsByBalanceId()`

```php
deleteCampaignsByBalanceId($balance_id, $balance_campaign202110_list_request): \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110PagedListResponse
```

/2026-01/retail-media/balances/{balance-id}/campaigns/delete

Removes one or more campaigns on the specified balance

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | The balance to remove campaigns from
$balance_campaign202110_list_request = new \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110ListRequest(); // \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110ListRequest | The campaigns to append

try {
    $result = $apiInstance->deleteCampaignsByBalanceId($balance_id, $balance_campaign202110_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteCampaignsByBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| The balance to remove campaigns from | |
| **balance_campaign202110_list_request** | [**\criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110ListRequest**](../Model/BalanceCampaign202110ListRequest.md)| The campaigns to append | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110PagedListResponse**](../Model/BalanceCampaign202110PagedListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deletePromotedProducts()`

```php
deletePromotedProducts($line_item_id, $promoted_product_resource_collection_input)
```

/2026-01/retail-media/line-items/{line-item-id}/products/delete

Remove a collection of promoted products from a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

try {
    $apiInstance->deletePromotedProducts($line_item_id, $promoted_product_resource_collection_input);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deletePromotedProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| ID of the line item | |
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteStoreTargetByLineItemId()`

```php
deleteStoreTargetByLineItemId($line_item_id, $store_ids_update_model202110_request): \criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores/delete

This endpoint removes one or more store ids from targeting on the specified line item.  The resulting state of the store target is returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$store_ids_update_model202110_request = new \criteo\api\retailmedia\v2026_01\Model\StoreIdsUpdateModel202110Request(); // \criteo\api\retailmedia\v2026_01\Model\StoreIdsUpdateModel202110Request | Store ids to remove from the target

try {
    $result = $apiInstance->deleteStoreTargetByLineItemId($line_item_id, $store_ids_update_model202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteStoreTargetByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **store_ids_update_model202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\StoreIdsUpdateModel202110Request**](../Model/StoreIdsUpdateModel202110Request.md)| Store ids to remove from the target | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response**](../Model/StoreTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `fetchKeywords()`

```php
fetchKeywords($id): \criteo\api\retailmedia\v2026_01\Model\KeywordsModelResponse
```

/2026-01/retail-media/line-items/{id}/keywords

Fetch keywords associated with the specified line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | ID of the line item

try {
    $result = $apiInstance->fetchKeywords($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->fetchKeywords: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| ID of the line item | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\KeywordsModelResponse**](../Model/KeywordsModelResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `fetchPromotedProducts()`

```php
fetchPromotedProducts($line_item_id, $fields, $limit, $offset): \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionOutcome
```

/2026-01/retail-media/line-items/{line-item-id}/products

Retrieve a page of promoted products for a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item.
$fields = 'fields_example'; // string | A comma separated list of attribute names from the response model to compute and return.              Valid values are `status` and `bidOverride` in any order. Defaults to `status`.
$limit = 56; // int | Maximum page size to fetch. Defaults to 500.
$offset = 56; // int | Offset of the first item to fetch. Defaults to zero.

try {
    $result = $apiInstance->fetchPromotedProducts($line_item_id, $fields, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->fetchPromotedProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| ID of the line item. | |
| **fields** | **string**| A comma separated list of attribute names from the response model to compute and return.              Valid values are &#x60;status&#x60; and &#x60;bidOverride&#x60; in any order. Defaults to &#x60;status&#x60;. | [optional] |
| **limit** | **int**| Maximum page size to fetch. Defaults to 500. | [optional] |
| **offset** | **int**| Offset of the first item to fetch. Defaults to zero. | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionOutcome**](../Model/PromotedProductResourceCollectionOutcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccountCreatives()`

```php
getAccountCreatives($account_id): \criteo\api\retailmedia\v2026_01\Model\Creative202110ListResponse
```

/2026-01/retail-media/accounts/{account-id}/creatives

Get account creatives

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id to retrieve creatives for

try {
    $result = $apiInstance->getAccountCreatives($account_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAccountCreatives: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id to retrieve creatives for | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Creative202110ListResponse**](../Model/Creative202110ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAddToBasketTargetsByLineItemId()`

```php
getAddToBasketTargetsByLineItemId($line_item_id): \criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket

This endpoint gets the add to basket target on the specified line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with

try {
    $result = $apiInstance->getAddToBasketTargetsByLineItemId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAddToBasketTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response**](../Model/AddToBasketTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getApi202110ExternalRetailerPagesByRetailerId()`

```php
getApi202110ExternalRetailerPagesByRetailerId($retailer_id): \criteo\api\retailmedia\v2026_01\Model\RetailerPages202110
```

/2026-01/retail-media/retailers/{retailerId}/pages

Get the page types available for the given retailer

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | The retailers to fetch pages for

try {
    $result = $apiInstance->getApi202110ExternalRetailerPagesByRetailerId($retailer_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getApi202110ExternalRetailerPagesByRetailerId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| The retailers to fetch pages for | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RetailerPages202110**](../Model/RetailerPages202110.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getApiExternalV1Categories()`

```php
getApiExternalV1Categories($page_index, $page_size, $retailer_id, $text_substring): \criteo\api\retailmedia\v2026_01\Model\Category202204ListResponse
```

/2026-01/retail-media/categories

Endpoint to search categories by text and retailer.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$page_index = 0; // int | The start position in the overall list of matches. Must be zero or greater.
$page_size = 100; // int | The maximum number of results to return with each call. Must be greater than zero.
$retailer_id = 56; // int | The retailer id for which Categories fetched
$text_substring = 'text_substring_example'; // string | Query string to search across Categories

try {
    $result = $apiInstance->getApiExternalV1Categories($page_index, $page_size, $retailer_id, $text_substring);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getApiExternalV1Categories: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **page_index** | **int**| The start position in the overall list of matches. Must be zero or greater. | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of results to return with each call. Must be greater than zero. | [optional] [default to 100] |
| **retailer_id** | **int**| The retailer id for which Categories fetched | [optional] |
| **text_substring** | **string**| Query string to search across Categories | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Category202204ListResponse**](../Model/Category202204ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAuctionLineItem()`

```php
getAuctionLineItem($line_item_id): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfSponsoredProductsLineItem
```

/2026-01/retail-media/auction-line-items/{lineItemId}

Gets a sponsored product line item by its id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The id of the line item

try {
    $result = $apiInstance->getAuctionLineItem($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAuctionLineItem: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The id of the line item | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfSponsoredProductsLineItem**](../Model/EntityResourceOutcomeOfSponsoredProductsLineItem.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAuctionLineItemsByCampaign()`

```php
getAuctionLineItemsByCampaign($campaign_id, $limit, $limit_to_ids, $offset): \criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata
```

/2026-01/retail-media/campaigns/{campaignId}/auction-line-items

Gets a page of sponsored product line items by campaign id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The id of the campaign
$limit = 25; // int | The number of elements to be returned on a page.
$limit_to_ids = array('limit_to_ids_example'); // string[] | The ids to limit the auction line item results to
$offset = 0; // int | The (zero-based) starting offset into the collection.

try {
    $result = $apiInstance->getAuctionLineItemsByCampaign($campaign_id, $limit, $limit_to_ids, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAuctionLineItemsByCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The id of the campaign | |
| **limit** | **int**| The number of elements to be returned on a page. | [optional] [default to 25] |
| **limit_to_ids** | [**string[]**](../Model/string.md)| The ids to limit the auction line item results to | [optional] |
| **offset** | **int**| The (zero-based) starting offset into the collection. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata**](../Model/EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAudienceTargetsByLineItemId()`

```php
getAudienceTargetsByLineItemId($line_item_id): \criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences

This endpoint gets the audience target on the specified line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with

try {
    $result = $apiInstance->getAudienceTargetsByLineItemId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAudienceTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response**](../Model/AudienceTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBidMultipliersByLineItemId()`

```php
getBidMultipliersByLineItemId($line_item_id): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfLineItemBidMultipliersV2
```

/2026-01/retail-media/line-items/{line-item-id}/bid-multipliers

Fetch all bid multipliers for a given line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for bid multiplier retrieval

try {
    $result = $apiInstance->getBidMultipliersByLineItemId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getBidMultipliersByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for bid multiplier retrieval | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfLineItemBidMultipliersV2**](../Model/JsonApiSingleResponseOfLineItemBidMultipliersV2.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBrandsByAccountId()`

```php
getBrandsByAccountId($account_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_01\Model\JsonApiPageResponseOfBrand
```

/2026-01/retail-media/accounts/{accountId}/brands

Gets page of retailer objects that are associated with the given account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getBrandsByAccountId($account_id, $limit_to_id, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getBrandsByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiPageResponseOfBrand**](../Model/JsonApiPageResponseOfBrand.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaignBudgetOverrides()`

```php
getCampaignBudgetOverrides($campaign_id): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfCampaignBudgetOverrides
```

/2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides

Get current campaign budget overrides by given campaign id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | Campaign id.

try {
    $result = $apiInstance->getCampaignBudgetOverrides($campaign_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCampaignBudgetOverrides: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| Campaign id. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfCampaignBudgetOverrides**](../Model/ValueResourceOutcomeOfCampaignBudgetOverrides.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaignByCampaignId()`

```php
getCampaignByCampaignId($campaign_id): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCampaignV202301
```

/2026-01/retail-media/campaigns/{campaignId}

Gets the campaign for the given campaign id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id

try {
    $result = $apiInstance->getCampaignByCampaignId($campaign_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCampaignByCampaignId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The given campaign id | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCampaignV202301**](../Model/JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaignsByAccountId()`

```php
getCampaignsByAccountId($account_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_01\Model\JsonApiPageResponseOfCampaignV202301
```

/2026-01/retail-media/accounts/{account-id}/campaigns

Gets page of campaign objects for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getCampaignsByAccountId($account_id, $limit_to_id, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCampaignsByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiPageResponseOfCampaignV202301**](../Model/JsonApiPageResponseOfCampaignV202301.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCatalogOutput()`

```php
getCatalogOutput($catalog_id): \SplFileObject
```

/2026-01/retail-media/catalogs/{catalogId}/output

Output the indicated catalog. Catalogs are only available for retrieval when their associated status request  is at a Success status.  Produces application/x-json-stream CatalogProduct json objects (first introduced in the 2021-07 version).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$catalog_id = 'catalog_id_example'; // string | A catalog ID returned from an account catalog request.

try {
    $result = $apiInstance->getCatalogOutput($catalog_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCatalogOutput: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **catalog_id** | **string**| A catalog ID returned from an account catalog request. | |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/x-json-stream`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCatalogStatus()`

```php
getCatalogStatus($catalog_id): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCatalogStatus
```

/2026-01/retail-media/catalogs/{catalogId}/status

Check the status of a catalog request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$catalog_id = 'catalog_id_example'; // string | A catalog ID returned from an account catalog request.

try {
    $result = $apiInstance->getCatalogStatus($catalog_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCatalogStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **catalog_id** | **string**| A catalog ID returned from an account catalog request. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCatalogStatus**](../Model/JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCategory()`

```php
getCategory($category_id): \criteo\api\retailmedia\v2026_01\Model\Category202204
```

/2026-01/retail-media/categories/{categoryId}

Endpoint to search for a specific category by categoryId.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$category_id = 'category_id_example'; // string | ID of the desired category

try {
    $result = $apiInstance->getCategory($category_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **category_id** | **string**| ID of the desired category | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Category202204**](../Model/Category202204.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCpcMinBidsBySkuIdsV1()`

```php
getCpcMinBidsBySkuIdsV1($retailer_id, $value_resource_input_cpc_min_bids_request): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeCpcMinBidsResponse
```

/2026-01/retail-media/retailers/{retailerId}/cpc-min-bids

Get overall and individual minimum bid amount for given retailer id and sku id list.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | Retailer Id.
$value_resource_input_cpc_min_bids_request = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputCpcMinBidsRequest(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputCpcMinBidsRequest | Cpc minimum bid amount request object.

try {
    $result = $apiInstance->getCpcMinBidsBySkuIdsV1($retailer_id, $value_resource_input_cpc_min_bids_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCpcMinBidsBySkuIdsV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| Retailer Id. | |
| **value_resource_input_cpc_min_bids_request** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputCpcMinBidsRequest**](../Model/ValueResourceInputCpcMinBidsRequest.md)| Cpc minimum bid amount request object. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeCpcMinBidsResponse**](../Model/ValueResourceOutcomeCpcMinBidsResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCreative()`

```php
getCreative($account_id, $creative_id): \criteo\api\retailmedia\v2026_01\Model\Creative2Response
```

/2026-01/retail-media/accounts/{account-id}/creatives/{creative-id}

Get the specified creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id to retrieve creatives for
$creative_id = 'creative_id_example'; // string | Creative to get

try {
    $result = $apiInstance->getCreative($account_id, $creative_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id to retrieve creatives for | |
| **creative_id** | **string**| Creative to get | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Creative2Response**](../Model/Creative2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCreativeTemplate()`

```php
getCreativeTemplate($retailer_id, $template_id): \criteo\api\retailmedia\v2026_01\Model\TemplateResponse
```

/2026-01/retail-media/retailers/{retailer-id}/templates/{template-id}

Gets the template for the specified retailer id and template id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | Retailer Id
$template_id = 'template_id_example'; // string | Template Id

try {
    $result = $apiInstance->getCreativeTemplate($retailer_id, $template_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCreativeTemplate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| Retailer Id | |
| **template_id** | **string**| Template Id | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\TemplateResponse**](../Model/TemplateResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getKeywordInReviewReport()`

```php
getKeywordInReviewReport($account_id, $limit, $offset): \criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata
```

/2026-01/retail-media/accounts/{account-id}/keywords/in-review-report

Generate a list of reports for line items which contain one or more actionable keyword reviews

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to generate a report for
$limit = 25; // int | Number of items per page
$offset = 0; // int | Offset for pagination

try {
    $result = $apiInstance->getKeywordInReviewReport($account_id, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getKeywordInReviewReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to generate a report for | |
| **limit** | **int**| Number of items per page | [optional] [default to 25] |
| **offset** | **int**| Offset for pagination | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata**](../Model/EntityResourceCollectionOutcomeLineItemKeywordReviewReportAndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getLineItemBudgetOverrides()`

```php
getLineItemBudgetOverrides($line_item_id): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfLineItemBudgetOverrides
```

/2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides

Gets a collection of monthly and daily budget overrides for the provided line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item id to get budget overrides for.

try {
    $result = $apiInstance->getLineItemBudgetOverrides($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getLineItemBudgetOverrides: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item id to get budget overrides for. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfLineItemBudgetOverrides**](../Model/ValueResourceOutcomeOfLineItemBudgetOverrides.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getLineItemsByAccountId()`

```php
getLineItemsByAccountId($account_id, $limit_to_campaign_id, $limit_to_id, $limit_to_type, $page_index, $page_size): \criteo\api\retailmedia\v2026_01\Model\CommonLineItemPagedListResponse
```

/2026-01/retail-media/accounts/{account-id}/line-items

Gets page of line item objects for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$limit_to_campaign_id = array('limit_to_campaign_id_example'); // string[] | The campaign ids that you would like to limit your result set to
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$limit_to_type = 'limit_to_type_example'; // string | The campaign types that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getLineItemsByAccountId($account_id, $limit_to_campaign_id, $limit_to_id, $limit_to_type, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getLineItemsByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **limit_to_campaign_id** | [**string[]**](../Model/string.md)| The campaign ids that you would like to limit your result set to | [optional] |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **limit_to_type** | **string**| The campaign types that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\CommonLineItemPagedListResponse**](../Model/CommonLineItemPagedListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getLineItemsByCampaignId()`

```php
getLineItemsByCampaignId($line_item_id): \criteo\api\retailmedia\v2026_01\Model\CommonLineItemResponse
```

/2026-01/retail-media/line-items/{line-item-id}

Gets the line item for the given line item id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The given line item id

try {
    $result = $apiInstance->getLineItemsByCampaignId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getLineItemsByCampaignId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The given line item id | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\CommonLineItemResponse**](../Model/CommonLineItemResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPreferredLineItemsByCampaignId()`

```php
getPreferredLineItemsByCampaignId($campaign_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2PagedListResponse
```

/2026-01/retail-media/campaigns/{campaign-id}/preferred-line-items

Gets page of preferred line item objects for the given campaign id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getPreferredLineItemsByCampaignId($campaign_id, $limit_to_id, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getPreferredLineItemsByCampaignId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The given campaign id | |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2PagedListResponse**](../Model/PreferredLineItemV2PagedListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPreferredLineItemsByLineItemId()`

```php
getPreferredLineItemsByLineItemId($line_item_id): \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}

Gets the preferred line item for the given line item id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The given line item id

try {
    $result = $apiInstance->getPreferredLineItemsByLineItemId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getPreferredLineItemsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The given line item id | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2Response**](../Model/PreferredLineItemV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRecommendedCategories()`

```php
getRecommendedCategories($retailer_id, $value_resource_input_recommended_categories_request_v1): \criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeCategory202204
```

/2026-01/retail-media/retailers/{retailerId}/recommend-categories

Endpoint to get recommended categories by given retailer id and sku id list.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | Retailer id.
$value_resource_input_recommended_categories_request_v1 = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRecommendedCategoriesRequestV1(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRecommendedCategoriesRequestV1 | Request of recommended categories.

try {
    $result = $apiInstance->getRecommendedCategories($retailer_id, $value_resource_input_recommended_categories_request_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getRecommendedCategories: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| Retailer id. | |
| **value_resource_input_recommended_categories_request_v1** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRecommendedCategoriesRequestV1**](../Model/ValueResourceInputRecommendedCategoriesRequestV1.md)| Request of recommended categories. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeCategory202204**](../Model/EntityResourceCollectionOutcomeCategory202204.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRecommendedKeywords()`

```php
getRecommendedKeywords($external_line_item_id): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfRecommendedKeywordsResult
```

/2026-01/retail-media/line-items/{externalLineItemId}/keywords/recommended

Retrieves a collection of recommended keywords for a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$external_line_item_id = 'external_line_item_id_example'; // string | The line item identifier

try {
    $result = $apiInstance->getRecommendedKeywords($external_line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getRecommendedKeywords: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **external_line_item_id** | **string**| The line item identifier | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfRecommendedKeywordsResult**](../Model/ValueResourceOutcomeOfRecommendedKeywordsResult.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRetailerCreativeTemplates()`

```php
getRetailerCreativeTemplates($retailer_id): \criteo\api\retailmedia\v2026_01\Model\TemplateListResponse
```

/2026-01/retail-media/retailers/{retailer-id}/templates

Get retailer creative templates

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | External retailer id to retrieve creative templates for

try {
    $result = $apiInstance->getRetailerCreativeTemplates($retailer_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getRetailerCreativeTemplates: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| External retailer id to retrieve creative templates for | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\TemplateListResponse**](../Model/TemplateListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getStoreTargetsByLineItemId()`

```php
getStoreTargetsByLineItemId($line_item_id): \criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores

This endpoint gets the store target on the specified line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with

try {
    $result = $apiInstance->getStoreTargetsByLineItemId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getStoreTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response**](../Model/StoreTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `pausePromotedProducts()`

```php
pausePromotedProducts($line_item_id, $promoted_product_resource_collection_input)
```

/2026-01/retail-media/line-items/{line-item-id}/products/pause

Pause a collection of promoted products associated with a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

try {
    $apiInstance->pausePromotedProducts($line_item_id, $promoted_product_resource_collection_input);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->pausePromotedProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| ID of the line item | |
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postApiExternalV1AccountCatalogsSellersByAccountId()`

```php
postApiExternalV1AccountCatalogsSellersByAccountId($account_id, $json_api_request_of_seller_catalog_request): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCatalogStatus
```

/2026-01/retail-media/accounts/{accountId}/catalogs/sellers

Create a request for a Catalog available to the indicated account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to request the catalog for.
$json_api_request_of_seller_catalog_request = new \criteo\api\retailmedia\v2026_01\Model\JsonApiRequestOfSellerCatalogRequest(); // \criteo\api\retailmedia\v2026_01\Model\JsonApiRequestOfSellerCatalogRequest

try {
    $result = $apiInstance->postApiExternalV1AccountCatalogsSellersByAccountId($account_id, $json_api_request_of_seller_catalog_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->postApiExternalV1AccountCatalogsSellersByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to request the catalog for. | |
| **json_api_request_of_seller_catalog_request** | [**\criteo\api\retailmedia\v2026_01\Model\JsonApiRequestOfSellerCatalogRequest**](../Model/JsonApiRequestOfSellerCatalogRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCatalogStatus**](../Model/JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postApiV1ExternalAccountCatalogsByAccountId()`

```php
postApiV1ExternalAccountCatalogsByAccountId($account_id, $json_api_request_of_catalog_request): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCatalogStatus
```

/2026-01/retail-media/accounts/{accountId}/catalogs

Create a request for a Catalog available to the indicated account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to request the catalog for.
$json_api_request_of_catalog_request = new \criteo\api\retailmedia\v2026_01\Model\JsonApiRequestOfCatalogRequest(); // \criteo\api\retailmedia\v2026_01\Model\JsonApiRequestOfCatalogRequest

try {
    $result = $apiInstance->postApiV1ExternalAccountCatalogsByAccountId($account_id, $json_api_request_of_catalog_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->postApiV1ExternalAccountCatalogsByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to request the catalog for. | |
| **json_api_request_of_catalog_request** | [**\criteo\api\retailmedia\v2026_01\Model\JsonApiRequestOfCatalogRequest**](../Model/JsonApiRequestOfCatalogRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCatalogStatus**](../Model/JsonApiSingleResponseOfCatalogStatus.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putAddToBasketTargetByLineItemId()`

```php
putAddToBasketTargetByLineItemId($line_item_id, $add_to_basket_target202110_request): \criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/add-to-basket

This endpoint sets the scope of the add to basket target on the specified line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$add_to_basket_target202110_request = new \criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Request(); // \criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Request | The add to basket target to set the scope for

try {
    $result = $apiInstance->putAddToBasketTargetByLineItemId($line_item_id, $add_to_basket_target202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putAddToBasketTargetByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **add_to_basket_target202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Request**](../Model/AddToBasketTarget202110Request.md)| The add to basket target to set the scope for | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AddToBasketTarget202110Response**](../Model/AddToBasketTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putAudienceTargetsByLineItemId()`

```php
putAudienceTargetsByLineItemId($line_item_id, $audience_target202110_request): \criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/audiences

This endpoint sets the scope of the audience target on the specified line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$audience_target202110_request = new \criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Request(); // \criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Request | The audience target to set the scope for

try {
    $result = $apiInstance->putAudienceTargetsByLineItemId($line_item_id, $audience_target202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putAudienceTargetsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **audience_target202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Request**](../Model/AudienceTarget202110Request.md)| The audience target to set the scope for | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AudienceTarget202110Response**](../Model/AudienceTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putStoreTargetByLineItemId()`

```php
putStoreTargetByLineItemId($line_item_id, $store_target202110_request): \criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}/targeting/stores

This endpoint sets the scope of the store target on the specified line item.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to interact with
$store_target202110_request = new \criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Request(); // \criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Request | The store target to set the scope for

try {
    $result = $apiInstance->putStoreTargetByLineItemId($line_item_id, $store_target202110_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putStoreTargetByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to interact with | |
| **store_target202110_request** | [**\criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Request**](../Model/StoreTarget202110Request.md)| The store target to set the scope for | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\StoreTarget202110Response**](../Model/StoreTarget202110Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `recommendedKeywords()`

```php
recommendedKeywords($retailer_id, $value_resource_input_recommended_keywords_request_v1): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeRecommendedKeywordsResponseV1
```

/2026-01/retail-media/retailers/{retailerId}/recommend-keywords

Recommend keywords by given retailer id and sku ids.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | Retailer id.
$value_resource_input_recommended_keywords_request_v1 = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRecommendedKeywordsRequestV1(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRecommendedKeywordsRequestV1 | Request of recommended keywords.

try {
    $result = $apiInstance->recommendedKeywords($retailer_id, $value_resource_input_recommended_keywords_request_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->recommendedKeywords: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| Retailer id. | |
| **value_resource_input_recommended_keywords_request_v1** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRecommendedKeywordsRequestV1**](../Model/ValueResourceInputRecommendedKeywordsRequestV1.md)| Request of recommended keywords. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeRecommendedKeywordsResponseV1**](../Model/ValueResourceOutcomeRecommendedKeywordsResponseV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAccountCreatives()`

```php
searchAccountCreatives($account_id, $creative_ids): \criteo\api\retailmedia\v2026_01\Model\Creative2ListResponse
```

/2026-01/retail-media/accounts/{account-id}/creatives/search

Get account creatives

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id to retrieve creatives for
$creative_ids = array('creative_ids_example'); // string[] | Creatives to filter by

try {
    $result = $apiInstance->searchAccountCreatives($account_id, $creative_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchAccountCreatives: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id to retrieve creatives for | |
| **creative_ids** | [**string[]**](../Model/string.md)| Creatives to filter by | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Creative2ListResponse**](../Model/Creative2ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAccountRetailers()`

```php
searchAccountRetailers($account_id, $value_resource_input_of_retailer_search_request, $limit, $offset): \criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeOfRetailerResultAndMetadata
```

/2026-01/retail-media/accounts/{accountId}/retailers/search

Searches for retailers associated with the specified account based on provided search criteria

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The external account identifier
$value_resource_input_of_retailer_search_request = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfRetailerSearchRequest(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfRetailerSearchRequest | The search request containing filtering parameters
$limit = 5; // int | The maximum number of items to return. Must be between 1 and 10. Default is 5.
$offset = 0; // int | The number of items to skip before starting to collect the result set. Default is 0.

try {
    $result = $apiInstance->searchAccountRetailers($account_id, $value_resource_input_of_retailer_search_request, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchAccountRetailers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The external account identifier | |
| **value_resource_input_of_retailer_search_request** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfRetailerSearchRequest**](../Model/ValueResourceInputOfRetailerSearchRequest.md)| The search request containing filtering parameters | |
| **limit** | **int**| The maximum number of items to return. Must be between 1 and 10. Default is 5. | [optional] [default to 5] |
| **offset** | **int**| The number of items to skip before starting to collect the result set. Default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeOfRetailerResultAndMetadata**](../Model/EntityResourceCollectionOutcomeOfRetailerResultAndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchCategory()`

```php
searchCategory($retailer_id, $limit, $offset, $value_resource_input_categories_search_request_v1): \criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeCategory202204Metadata
```

/2026-01/retail-media/retailers/{retailerId}/categories/search

Search a retailer categories by given text substring and category ids.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | Retailer id.
$limit = 50; // int | Limit of the search result.
$offset = 0; // int | Offset of the search result.
$value_resource_input_categories_search_request_v1 = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputCategoriesSearchRequestV1(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputCategoriesSearchRequestV1 | Request of categories search.

try {
    $result = $apiInstance->searchCategory($retailer_id, $limit, $offset, $value_resource_input_categories_search_request_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchCategory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| Retailer id. | |
| **limit** | **int**| Limit of the search result. | [optional] [default to 50] |
| **offset** | **int**| Offset of the search result. | [optional] [default to 0] |
| **value_resource_input_categories_search_request_v1** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputCategoriesSearchRequestV1**](../Model/ValueResourceInputCategoriesSearchRequestV1.md)| Request of categories search. | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceCollectionOutcomeCategory202204Metadata**](../Model/EntityResourceCollectionOutcomeCategory202204Metadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `setKeywordBids()`

```php
setKeywordBids($id, $set_bids_model_request): \criteo\api\retailmedia\v2026_01\Model\ResourceOutcome
```

/2026-01/retail-media/line-items/{id}/keywords/set-bid

Set bid overrides for associated keywords to the given line item in bulk

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | ID of the line item
$set_bids_model_request = new \criteo\api\retailmedia\v2026_01\Model\SetBidsModelRequest(); // \criteo\api\retailmedia\v2026_01\Model\SetBidsModelRequest

try {
    $result = $apiInstance->setKeywordBids($id, $set_bids_model_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->setKeywordBids: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| ID of the line item | |
| **set_bids_model_request** | [**\criteo\api\retailmedia\v2026_01\Model\SetBidsModelRequest**](../Model/SetBidsModelRequest.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ResourceOutcome**](../Model/ResourceOutcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `unpausePromotedProducts()`

```php
unpausePromotedProducts($line_item_id, $promoted_product_resource_collection_input)
```

/2026-01/retail-media/line-items/{line-item-id}/products/unpause

Un-pause a collection of promoted products associated with a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

try {
    $apiInstance->unpausePromotedProducts($line_item_id, $promoted_product_resource_collection_input);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->unpausePromotedProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| ID of the line item | |
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\v2026_01\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateAuctionLineItem()`

```php
updateAuctionLineItem($line_item_id, $value_resource_input_of_sponsored_products_line_item_update_request_model): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfSponsoredProductsLineItem
```

/2026-01/retail-media/auction-line-items/{lineItemId}

Updates a Sponsored Products Line Item given a line item id and a request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The external line item ID of the sponsored products line item.
$value_resource_input_of_sponsored_products_line_item_update_request_model = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel | An update request containing all details of the requested update.

try {
    $result = $apiInstance->updateAuctionLineItem($line_item_id, $value_resource_input_of_sponsored_products_line_item_update_request_model);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateAuctionLineItem: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The external line item ID of the sponsored products line item. | |
| **value_resource_input_of_sponsored_products_line_item_update_request_model** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel**](../Model/ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel.md)| An update request containing all details of the requested update. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomeOfSponsoredProductsLineItem**](../Model/EntityResourceOutcomeOfSponsoredProductsLineItem.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateBidMultipliersByLineItemId()`

```php
updateBidMultipliersByLineItemId($line_item_id, $line_item_bid_multipliers_v2_request): \criteo\api\retailmedia\v2026_01\Model\LineItemBidMultipliersV2Response
```

/2026-01/retail-media/line-items/{line-item-id}/bid-multipliers

Updates the bid multipliers for a given line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for bid multiplier retrieval
$line_item_bid_multipliers_v2_request = new \criteo\api\retailmedia\v2026_01\Model\LineItemBidMultipliersV2Request(); // \criteo\api\retailmedia\v2026_01\Model\LineItemBidMultipliersV2Request | New Bid Multipliers to be set

try {
    $result = $apiInstance->updateBidMultipliersByLineItemId($line_item_id, $line_item_bid_multipliers_v2_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateBidMultipliersByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for bid multiplier retrieval | |
| **line_item_bid_multipliers_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\LineItemBidMultipliersV2Request**](../Model/LineItemBidMultipliersV2Request.md)| New Bid Multipliers to be set | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\LineItemBidMultipliersV2Response**](../Model/LineItemBidMultipliersV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCampaignBudgetOverrides()`

```php
updateCampaignBudgetOverrides($campaign_id, $value_resource_input_of_campaign_budget_overrides): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfCampaignBudgetOverrides
```

/2026-01/retail-media/campaigns/{campaignId}/campaign-budget-overrides

Update campaign budget overrides by given campaign id and new campaign budget overrides settings.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | Campaign id.
$value_resource_input_of_campaign_budget_overrides = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfCampaignBudgetOverrides(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfCampaignBudgetOverrides | New campaign budget overrides settings value resource input.

try {
    $result = $apiInstance->updateCampaignBudgetOverrides($campaign_id, $value_resource_input_of_campaign_budget_overrides);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateCampaignBudgetOverrides: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| Campaign id. | |
| **value_resource_input_of_campaign_budget_overrides** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfCampaignBudgetOverrides**](../Model/ValueResourceInputOfCampaignBudgetOverrides.md)| New campaign budget overrides settings value resource input. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfCampaignBudgetOverrides**](../Model/ValueResourceOutcomeOfCampaignBudgetOverrides.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCampaignByCampaignId()`

```php
updateCampaignByCampaignId($campaign_id, $put_campaign_v202301): \criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCampaignV202301
```

/2026-01/retail-media/campaigns/{campaignId}

Updates the campaign for the given campaign id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id
$put_campaign_v202301 = new \criteo\api\retailmedia\v2026_01\Model\PutCampaignV202301(); // \criteo\api\retailmedia\v2026_01\Model\PutCampaignV202301 | The campaign settings to update that campaign with

try {
    $result = $apiInstance->updateCampaignByCampaignId($campaign_id, $put_campaign_v202301);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateCampaignByCampaignId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The given campaign id | |
| **put_campaign_v202301** | [**\criteo\api\retailmedia\v2026_01\Model\PutCampaignV202301**](../Model/PutCampaignV202301.md)| The campaign settings to update that campaign with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\JsonApiSingleResponseOfCampaignV202301**](../Model/JsonApiSingleResponseOfCampaignV202301.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCreative()`

```php
updateCreative($account_id, $creative_id, $creative_update_model202207): \criteo\api\retailmedia\v2026_01\Model\Creative202210Response
```

/2026-01/retail-media/accounts/{account-id}/creatives/{creative-id}

Update a creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id containing the creative
$creative_id = 'creative_id_example'; // string | Creative to update
$creative_update_model202207 = new \criteo\api\retailmedia\v2026_01\Model\CreativeUpdateModel202207(); // \criteo\api\retailmedia\v2026_01\Model\CreativeUpdateModel202207 | The creative to create

try {
    $result = $apiInstance->updateCreative($account_id, $creative_id, $creative_update_model202207);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id containing the creative | |
| **creative_id** | **string**| Creative to update | |
| **creative_update_model202207** | [**\criteo\api\retailmedia\v2026_01\Model\CreativeUpdateModel202207**](../Model/CreativeUpdateModel202207.md)| The creative to create | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\Creative202210Response**](../Model/Creative202210Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateKeywordReviews()`

```php
updateKeywordReviews($line_item_id, $value_resource_input_retail_media_keywords_review): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeRetailMediaKeywordsReviewResult
```

/2026-01/retail-media/line-items/{line-item-id}/keywords/review

Update the status of keyword reviews under a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The line item to update keyword review statuses for
$value_resource_input_retail_media_keywords_review = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRetailMediaKeywordsReview(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRetailMediaKeywordsReview | Request object containing a list of Phrase-ReviewState pairs to update

try {
    $result = $apiInstance->updateKeywordReviews($line_item_id, $value_resource_input_retail_media_keywords_review);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateKeywordReviews: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The line item to update keyword review statuses for | |
| **value_resource_input_retail_media_keywords_review** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputRetailMediaKeywordsReview**](../Model/ValueResourceInputRetailMediaKeywordsReview.md)| Request object containing a list of Phrase-ReviewState pairs to update | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeRetailMediaKeywordsReviewResult**](../Model/ValueResourceOutcomeRetailMediaKeywordsReviewResult.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateLineItemBudgetOverrides()`

```php
updateLineItemBudgetOverrides($line_item_id, $value_resource_input_of_line_item_budget_overrides): \criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfLineItemBudgetOverrides
```

/2026-01/retail-media/line-items/{lineItemId}/line-item-budget-overrides

Update line item budget overrides by given external line item id and new line item budget overrides settings.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | Line item external id.
$value_resource_input_of_line_item_budget_overrides = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfLineItemBudgetOverrides(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfLineItemBudgetOverrides | New line item budget overrides settings value resource input.

try {
    $result = $apiInstance->updateLineItemBudgetOverrides($line_item_id, $value_resource_input_of_line_item_budget_overrides);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateLineItemBudgetOverrides: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| Line item external id. | |
| **value_resource_input_of_line_item_budget_overrides** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputOfLineItemBudgetOverrides**](../Model/ValueResourceInputOfLineItemBudgetOverrides.md)| New line item budget overrides settings value resource input. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\ValueResourceOutcomeOfLineItemBudgetOverrides**](../Model/ValueResourceOutcomeOfLineItemBudgetOverrides.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updatePreferredLineItemByLineItemId()`

```php
updatePreferredLineItemByLineItemId($line_item_id, $preferred_line_item_update_model_v2_request): \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2Response
```

/2026-01/retail-media/preferred-line-items/{line-item-id}

Updates the preferred line item for the given line item id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The given line item id
$preferred_line_item_update_model_v2_request = new \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemUpdateModelV2Request(); // \criteo\api\retailmedia\v2026_01\Model\PreferredLineItemUpdateModelV2Request | The line item settings to create a line item with

try {
    $result = $apiInstance->updatePreferredLineItemByLineItemId($line_item_id, $preferred_line_item_update_model_v2_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updatePreferredLineItemByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| The given line item id | |
| **preferred_line_item_update_model_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\PreferredLineItemUpdateModelV2Request**](../Model/PreferredLineItemUpdateModelV2Request.md)| The line item settings to create a line item with | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\PreferredLineItemV2Response**](../Model/PreferredLineItemV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
