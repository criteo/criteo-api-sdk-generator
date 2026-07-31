# criteo\api\retailmedia\experimental\CampaignApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**appendCampaignsToBalanceV1()**](CampaignApi.md#appendCampaignsToBalanceV1) | **POST** /experimental/retail-media/balances/{balanceId}/campaigns/append | /experimental/retail-media/balances/{balanceId}/campaigns/append |
| [**appendProductButtonByLineItemId()**](CampaignApi.md#appendProductButtonByLineItemId) | **POST** /experimental/retail-media/line-items/{line-item-id}/product-buttons/create | /experimental/retail-media/line-items/{line-item-id}/product-buttons/create |
| [**appendPromotedProducts()**](CampaignApi.md#appendPromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/append | /experimental/retail-media/line-items/{line-item-id}/products/append |
| [**computeDisplayMinBidByRetailerId()**](CampaignApi.md#computeDisplayMinBidByRetailerId) | **POST** /experimental/retail-media/retailers/{retailerId}/compute-display-min-bid | /experimental/retail-media/retailers/{retailerId}/compute-display-min-bid |
| [**createAuctionLineItem()**](CampaignApi.md#createAuctionLineItem) | **POST** /experimental/retail-media/campaigns/{campaignId}/auction-line-items | /experimental/retail-media/campaigns/{campaignId}/auction-line-items |
| [**createCreative()**](CampaignApi.md#createCreative) | **POST** /experimental/retail-media/accounts/{account-id}/creatives | /experimental/retail-media/accounts/{account-id}/creatives |
| [**createPreferredLineItemByCampaignId()**](CampaignApi.md#createPreferredLineItemByCampaignId) | **POST** /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items | /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**deleteCampaignsFromBalanceV1()**](CampaignApi.md#deleteCampaignsFromBalanceV1) | **POST** /experimental/retail-media/balances/{balanceId}/campaigns/delete | /experimental/retail-media/balances/{balanceId}/campaigns/delete |
| [**deleteProductButtonByLineItemAndProductButtonId()**](CampaignApi.md#deleteProductButtonByLineItemAndProductButtonId) | **DELETE** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} |
| [**deletePromotedProducts()**](CampaignApi.md#deletePromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/delete | /experimental/retail-media/line-items/{line-item-id}/products/delete |
| [**fetchPromotedProducts()**](CampaignApi.md#fetchPromotedProducts) | **GET** /experimental/retail-media/line-items/{line-item-id}/products | /experimental/retail-media/line-items/{line-item-id}/products |
| [**getAuctionLineItem()**](CampaignApi.md#getAuctionLineItem) | **GET** /experimental/retail-media/auction-line-items/{lineItemId} | /experimental/retail-media/auction-line-items/{lineItemId} |
| [**getAuctionLineItemsByCampaign()**](CampaignApi.md#getAuctionLineItemsByCampaign) | **GET** /experimental/retail-media/campaigns/{campaignId}/auction-line-items | /experimental/retail-media/campaigns/{campaignId}/auction-line-items |
| [**getCapoutHistory()**](CampaignApi.md#getCapoutHistory) | **POST** /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history | /experimental/retail-media/accounts/{account-id}/line-items/cap-out-history |
| [**getCatalogStatus()**](CampaignApi.md#getCatalogStatus) | **GET** /experimental/retail-media/catalogs/{catalogId}/status | /experimental/retail-media/catalogs/{catalogId}/status |
| [**getCreative()**](CampaignApi.md#getCreative) | **GET** /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} | /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**getPreferredLineItemsByCampaignId()**](CampaignApi.md#getPreferredLineItemsByCampaignId) | **GET** /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items | /experimental/retail-media/campaigns/{campaign-id}/preferred-line-items |
| [**getPreferredLineItemsByLineItemId()**](CampaignApi.md#getPreferredLineItemsByLineItemId) | **GET** /experimental/retail-media/preferred-line-items/{line-item-id} | /experimental/retail-media/preferred-line-items/{line-item-id} |
| [**getProductButtonByLineItemAndProductButtonId()**](CampaignApi.md#getProductButtonByLineItemAndProductButtonId) | **GET** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} |
| [**getProductButtonsByLineItemId()**](CampaignApi.md#getProductButtonsByLineItemId) | **GET** /experimental/retail-media/line-items/{line-item-id}/product-buttons | /experimental/retail-media/line-items/{line-item-id}/product-buttons |
| [**pausePromotedProducts()**](CampaignApi.md#pausePromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/pause | /experimental/retail-media/line-items/{line-item-id}/products/pause |
| [**searchAccountCreatives()**](CampaignApi.md#searchAccountCreatives) | **POST** /experimental/retail-media/accounts/{account-id}/creatives/search | /experimental/retail-media/accounts/{account-id}/creatives/search |
| [**searchAccountRetailers()**](CampaignApi.md#searchAccountRetailers) | **POST** /experimental/retail-media/accounts/{accountId}/retailers/search | /experimental/retail-media/accounts/{accountId}/retailers/search |
| [**unpausePromotedProducts()**](CampaignApi.md#unpausePromotedProducts) | **POST** /experimental/retail-media/line-items/{line-item-id}/products/unpause | /experimental/retail-media/line-items/{line-item-id}/products/unpause |
| [**updateAuctionLineItem()**](CampaignApi.md#updateAuctionLineItem) | **PUT** /experimental/retail-media/auction-line-items/{lineItemId} | /experimental/retail-media/auction-line-items/{lineItemId} |
| [**updateCreative()**](CampaignApi.md#updateCreative) | **PUT** /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} | /experimental/retail-media/accounts/{account-id}/creatives/{creative-id} |
| [**updatePreferredLineItemByLineItemId()**](CampaignApi.md#updatePreferredLineItemByLineItemId) | **PUT** /experimental/retail-media/preferred-line-items/{line-item-id} | /experimental/retail-media/preferred-line-items/{line-item-id} |
| [**updateProductButtonByLineItemAndProductButtonId()**](CampaignApi.md#updateProductButtonByLineItemAndProductButtonId) | **PUT** /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} | /experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id} |


## `appendCampaignsToBalanceV1()`

```php
appendCampaignsToBalanceV1($balance_id, $value_resource_input_append_campaigns_request_v1): \criteo\api\retailmedia\experimental\Model\ValueResourceOutcomeBalanceCampaignsV1
```

/experimental/retail-media/balances/{balanceId}/campaigns/append

Appends one or more campaigns to the specified balance

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | The balance to add campaigns from
$value_resource_input_append_campaigns_request_v1 = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputAppendCampaignsRequestV1(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputAppendCampaignsRequestV1 | The balance campaign appending request.

try {
    $result = $apiInstance->appendCampaignsToBalanceV1($balance_id, $value_resource_input_append_campaigns_request_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendCampaignsToBalanceV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| The balance to add campaigns from | |
| **value_resource_input_append_campaigns_request_v1** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputAppendCampaignsRequestV1**](../Model/ValueResourceInputAppendCampaignsRequestV1.md)| The balance campaign appending request. | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ValueResourceOutcomeBalanceCampaignsV1**](../Model/ValueResourceOutcomeBalanceCampaignsV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `appendProductButtonByLineItemId()`

```php
appendProductButtonByLineItemId($line_item_id, $product_button_request_list_request): \criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse
```

/experimental/retail-media/line-items/{line-item-id}/product-buttons/create

Add Specific Product Buttons

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for productButton retrieval
$product_button_request_list_request = new \criteo\api\retailmedia\experimental\Model\ProductButtonRequestListRequest(); // \criteo\api\retailmedia\experimental\Model\ProductButtonRequestListRequest | List of Product Buttons to append

try {
    $result = $apiInstance->appendProductButtonByLineItemId($line_item_id, $product_button_request_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->appendProductButtonByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for productButton retrieval | |
| **product_button_request_list_request** | [**\criteo\api\retailmedia\experimental\Model\ProductButtonRequestListRequest**](../Model/ProductButtonRequestListRequest.md)| List of Product Buttons to append | [optional] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse**](../Model/ProductButtonResponseListResponse.md)

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
appendPromotedProducts($line_item_id, $promoted_product_resource_collection_input): \criteo\api\retailmedia\experimental\Model\ProductResourceOutcome
```

/experimental/retail-media/line-items/{line-item-id}/products/append

Append a collection of promoted products to a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

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
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ProductResourceOutcome**](../Model/ProductResourceOutcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `computeDisplayMinBidByRetailerId()`

```php
computeDisplayMinBidByRetailerId($retailer_id, $value_resource_input_display_auction_min_bid_request): \criteo\api\retailmedia\experimental\Model\ValueResourceCollectionOutcomeDisplayAuctionMinBidResult
```

/experimental/retail-media/retailers/{retailerId}/compute-display-min-bid

Computes the min bid for relevant page types based on the provided information

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | The retailer id
$value_resource_input_display_auction_min_bid_request = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputDisplayAuctionMinBidRequest(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputDisplayAuctionMinBidRequest | The details for what creatives and product ids to use to compute the min bids

try {
    $result = $apiInstance->computeDisplayMinBidByRetailerId($retailer_id, $value_resource_input_display_auction_min_bid_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->computeDisplayMinBidByRetailerId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| The retailer id | |
| **value_resource_input_display_auction_min_bid_request** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputDisplayAuctionMinBidRequest**](../Model/ValueResourceInputDisplayAuctionMinBidRequest.md)| The details for what creatives and product ids to use to compute the min bids | [optional] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ValueResourceCollectionOutcomeDisplayAuctionMinBidResult**](../Model/ValueResourceCollectionOutcomeDisplayAuctionMinBidResult.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAuctionLineItem()`

```php
createAuctionLineItem($campaign_id, $value_resource_input_of_sponsored_products_line_item_create_request_model): \criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfSponsoredProductsLineItem
```

/experimental/retail-media/campaigns/{campaignId}/auction-line-items

Creates new auction line item with the specified settings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id
$value_resource_input_of_sponsored_products_line_item_create_request_model = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel | The line item settings to create a line item with

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
| **value_resource_input_of_sponsored_products_line_item_create_request_model** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel**](../Model/ValueResourceInputOfSponsoredProductsLineItemCreateRequestModel.md)| The line item settings to create a line item with | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfSponsoredProductsLineItem**](../Model/EntityResourceOutcomeOfSponsoredProductsLineItem.md)

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
createCreative($account_id, $creative_create_model2): \criteo\api\retailmedia\experimental\Model\Creative2Response
```

/experimental/retail-media/accounts/{account-id}/creatives

Create a creative for an account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id to create a creative for
$creative_create_model2 = new \criteo\api\retailmedia\experimental\Model\CreativeCreateModel2(); // \criteo\api\retailmedia\experimental\Model\CreativeCreateModel2 | The creative to create

try {
    $result = $apiInstance->createCreative($account_id, $creative_create_model2);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id to create a creative for | |
| **creative_create_model2** | [**\criteo\api\retailmedia\experimental\Model\CreativeCreateModel2**](../Model/CreativeCreateModel2.md)| The creative to create | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\Creative2Response**](../Model/Creative2Response.md)

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
createPreferredLineItemByCampaignId($campaign_id, $preferred_line_item_create_model_v2_request): \criteo\api\retailmedia\experimental\Model\PreferredLineItemV2Response
```

/experimental/retail-media/campaigns/{campaign-id}/preferred-line-items

Creates a new preferred line item with the specified settings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The given campaign id
$preferred_line_item_create_model_v2_request = new \criteo\api\retailmedia\experimental\Model\PreferredLineItemCreateModelV2Request(); // \criteo\api\retailmedia\experimental\Model\PreferredLineItemCreateModelV2Request | The line item settings to create a line item with

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
| **preferred_line_item_create_model_v2_request** | [**\criteo\api\retailmedia\experimental\Model\PreferredLineItemCreateModelV2Request**](../Model/PreferredLineItemCreateModelV2Request.md)| The line item settings to create a line item with | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\PreferredLineItemV2Response**](../Model/PreferredLineItemV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCampaignsFromBalanceV1()`

```php
deleteCampaignsFromBalanceV1($balance_id, $value_resource_input_delete_campaigns_request_v1): \criteo\api\retailmedia\experimental\Model\ValueResourceOutcomeBalanceCampaignsV1
```

/experimental/retail-media/balances/{balanceId}/campaigns/delete

Deletes one or more campaigns on the specified balance

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | The balance to remove campaigns from
$value_resource_input_delete_campaigns_request_v1 = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputDeleteCampaignsRequestV1(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputDeleteCampaignsRequestV1 | The balance campaign deleting request.

try {
    $result = $apiInstance->deleteCampaignsFromBalanceV1($balance_id, $value_resource_input_delete_campaigns_request_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteCampaignsFromBalanceV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| The balance to remove campaigns from | |
| **value_resource_input_delete_campaigns_request_v1** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputDeleteCampaignsRequestV1**](../Model/ValueResourceInputDeleteCampaignsRequestV1.md)| The balance campaign deleting request. | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ValueResourceOutcomeBalanceCampaignsV1**](../Model/ValueResourceOutcomeBalanceCampaignsV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteProductButtonByLineItemAndProductButtonId()`

```php
deleteProductButtonByLineItemAndProductButtonId($line_item_id, $product_button_id): \criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse
```

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Delete Specific Product Button

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for productButton delete
$product_button_id = 'product_button_id_example'; // string | productButtonId used for delete

try {
    $result = $apiInstance->deleteProductButtonByLineItemAndProductButtonId($line_item_id, $product_button_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteProductButtonByLineItemAndProductButtonId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for productButton delete | |
| **product_button_id** | **string**| productButtonId used for delete | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse**](../Model/ProductButtonResponseListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deletePromotedProducts()`

```php
deletePromotedProducts($line_item_id, $promoted_product_resource_collection_input)
```

/experimental/retail-media/line-items/{line-item-id}/products/delete

Remove a collection of promoted products from a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

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
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

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

## `fetchPromotedProducts()`

```php
fetchPromotedProducts($line_item_id, $fields, $limit, $offset): \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionOutcome
```

/experimental/retail-media/line-items/{line-item-id}/products

Retrieve a page of promoted products for a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionOutcome**](../Model/PromotedProductResourceCollectionOutcome.md)

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
getAuctionLineItem($line_item_id): \criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfSponsoredProductsLineItem
```

/experimental/retail-media/auction-line-items/{lineItemId}

Gets a sponsored product line item by its id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfSponsoredProductsLineItem**](../Model/EntityResourceOutcomeOfSponsoredProductsLineItem.md)

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
getAuctionLineItemsByCampaign($campaign_id, $limit, $limit_to_ids, $offset): \criteo\api\retailmedia\experimental\Model\EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata
```

/experimental/retail-media/campaigns/{campaignId}/auction-line-items

Gets a page of sponsored product line items by campaign id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata**](../Model/EntityResourceCollectionOutcomeOfSponsoredProductsLineItemAndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCapoutHistory()`

```php
getCapoutHistory($account_id, $value_resource_input_line_item_budget_cap_out_history_request): \criteo\api\retailmedia\experimental\Model\ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse
```

/experimental/retail-media/accounts/{account-id}/line-items/cap-out-history

Get the cap out history for line items

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | account id that own the lineitem
$value_resource_input_line_item_budget_cap_out_history_request = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputLineItemBudgetCapOutHistoryRequest(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputLineItemBudgetCapOutHistoryRequest | lineitem budgetcapout history  object

try {
    $result = $apiInstance->getCapoutHistory($account_id, $value_resource_input_line_item_budget_cap_out_history_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCapoutHistory: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| account id that own the lineitem | |
| **value_resource_input_line_item_budget_cap_out_history_request** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputLineItemBudgetCapOutHistoryRequest**](../Model/ValueResourceInputLineItemBudgetCapOutHistoryRequest.md)| lineitem budgetcapout history  object | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse**](../Model/ValueResourceOutcomeLineItemBudgetCapOutHistoryResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCatalogStatus()`

```php
getCatalogStatus($catalog_id): \criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfCatalogStatusV2
```

/experimental/retail-media/catalogs/{catalogId}/status

Check the status of a catalog request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfCatalogStatusV2**](../Model/EntityResourceOutcomeOfCatalogStatusV2.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCreative()`

```php
getCreative($account_id, $creative_id): \criteo\api\retailmedia\experimental\Model\Creative2Response
```

/experimental/retail-media/accounts/{account-id}/creatives/{creative-id}

Get the specified creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\Creative2Response**](../Model/Creative2Response.md)

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
getPreferredLineItemsByCampaignId($campaign_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\experimental\Model\PreferredLineItemV2PagedListResponse
```

/experimental/retail-media/campaigns/{campaign-id}/preferred-line-items

Gets page of preferred line item objects for the given campaign id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\PreferredLineItemV2PagedListResponse**](../Model/PreferredLineItemV2PagedListResponse.md)

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
getPreferredLineItemsByLineItemId($line_item_id): \criteo\api\retailmedia\experimental\Model\PreferredLineItemV2Response
```

/experimental/retail-media/preferred-line-items/{line-item-id}

Gets the preferred line item for the given line item id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
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

[**\criteo\api\retailmedia\experimental\Model\PreferredLineItemV2Response**](../Model/PreferredLineItemV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProductButtonByLineItemAndProductButtonId()`

```php
getProductButtonByLineItemAndProductButtonId($line_item_id, $product_button_id): \criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse
```

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Get Specific Product Button

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for productButton retrieval
$product_button_id = 'product_button_id_example'; // string | productButtonId used for retrieval

try {
    $result = $apiInstance->getProductButtonByLineItemAndProductButtonId($line_item_id, $product_button_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getProductButtonByLineItemAndProductButtonId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for productButton retrieval | |
| **product_button_id** | **string**| productButtonId used for retrieval | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse**](../Model/ProductButtonResponseListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getProductButtonsByLineItemId()`

```php
getProductButtonsByLineItemId($line_item_id): \criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse
```

/experimental/retail-media/line-items/{line-item-id}/product-buttons

Get LineItem Product Buttons

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for productButton retrieval

try {
    $result = $apiInstance->getProductButtonsByLineItemId($line_item_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getProductButtonsByLineItemId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for productButton retrieval | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse**](../Model/ProductButtonResponseListResponse.md)

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

/experimental/retail-media/line-items/{line-item-id}/products/pause

Pause a collection of promoted products associated with a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

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
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

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

## `searchAccountCreatives()`

```php
searchAccountCreatives($account_id, $entity_resource_input_creative_search_request, $limit, $offset): \criteo\api\retailmedia\experimental\Model\EntityResourceCollectionOutcomeCreativeSearchResponse
```

/experimental/retail-media/accounts/{account-id}/creatives/search

Get account creatives

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id to retrieve creatives for
$entity_resource_input_creative_search_request = new \criteo\api\retailmedia\experimental\Model\EntityResourceInputCreativeSearchRequest(); // \criteo\api\retailmedia\experimental\Model\EntityResourceInputCreativeSearchRequest | search request filter
$limit = 50; // int | limit to paginated result
$offset = 0; // int | offset to paginated result

try {
    $result = $apiInstance->searchAccountCreatives($account_id, $entity_resource_input_creative_search_request, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchAccountCreatives: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| External account id to retrieve creatives for | |
| **entity_resource_input_creative_search_request** | [**\criteo\api\retailmedia\experimental\Model\EntityResourceInputCreativeSearchRequest**](../Model/EntityResourceInputCreativeSearchRequest.md)| search request filter | |
| **limit** | **int**| limit to paginated result | [optional] [default to 50] |
| **offset** | **int**| offset to paginated result | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\EntityResourceCollectionOutcomeCreativeSearchResponse**](../Model/EntityResourceCollectionOutcomeCreativeSearchResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAccountRetailers()`

```php
searchAccountRetailers($account_id, $value_resource_input_of_retailer_search_request_v2, $limit, $offset): \criteo\api\retailmedia\experimental\Model\EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata
```

/experimental/retail-media/accounts/{accountId}/retailers/search

Searches for retailers associated with the specified account and returns budget model availability for each retailer

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The external account identifier
$value_resource_input_of_retailer_search_request_v2 = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputOfRetailerSearchRequestV2(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputOfRetailerSearchRequestV2 | The search request containing filtering parameters
$limit = 5; // int | The maximum number of items to return. Must be between 1 and 10. Default is 5.
$offset = 0; // int | The number of items to skip before starting to collect the result set. Default is 0.

try {
    $result = $apiInstance->searchAccountRetailers($account_id, $value_resource_input_of_retailer_search_request_v2, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchAccountRetailers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The external account identifier | |
| **value_resource_input_of_retailer_search_request_v2** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputOfRetailerSearchRequestV2**](../Model/ValueResourceInputOfRetailerSearchRequestV2.md)| The search request containing filtering parameters | |
| **limit** | **int**| The maximum number of items to return. Must be between 1 and 10. Default is 5. | [optional] [default to 5] |
| **offset** | **int**| The number of items to skip before starting to collect the result set. Default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata**](../Model/EntityResourceCollectionOutcomeOfRetailerResultV2AndMetadata.md)

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

/experimental/retail-media/line-items/{line-item-id}/products/unpause

Un-pause a collection of promoted products associated with a line item

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | ID of the line item
$promoted_product_resource_collection_input = new \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput(); // \criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput | Request body whose {data} contains an array of promoted products.

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
| **promoted_product_resource_collection_input** | [**\criteo\api\retailmedia\experimental\Model\PromotedProductResourceCollectionInput**](../Model/PromotedProductResourceCollectionInput.md)| Request body whose {data} contains an array of promoted products. | [optional] |

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
updateAuctionLineItem($line_item_id, $value_resource_input_of_sponsored_products_line_item_update_request_model): \criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfSponsoredProductsLineItem
```

/experimental/retail-media/auction-line-items/{lineItemId}

Updates a Sponsored Products Line Item given a line item id and a request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The external line item ID of the sponsored products line item.
$value_resource_input_of_sponsored_products_line_item_update_request_model = new \criteo\api\retailmedia\experimental\Model\ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel(); // \criteo\api\retailmedia\experimental\Model\ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel | An update request containing all details of the requested update.

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
| **value_resource_input_of_sponsored_products_line_item_update_request_model** | [**\criteo\api\retailmedia\experimental\Model\ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel**](../Model/ValueResourceInputOfSponsoredProductsLineItemUpdateRequestModel.md)| An update request containing all details of the requested update. | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\EntityResourceOutcomeOfSponsoredProductsLineItem**](../Model/EntityResourceOutcomeOfSponsoredProductsLineItem.md)

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
updateCreative($account_id, $creative_id, $creative_update_model2): \criteo\api\retailmedia\experimental\Model\Creative2Response
```

/experimental/retail-media/accounts/{account-id}/creatives/{creative-id}

Update a creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | External account id containing the creative
$creative_id = 'creative_id_example'; // string | Creative to update
$creative_update_model2 = new \criteo\api\retailmedia\experimental\Model\CreativeUpdateModel2(); // \criteo\api\retailmedia\experimental\Model\CreativeUpdateModel2 | The creative to create

try {
    $result = $apiInstance->updateCreative($account_id, $creative_id, $creative_update_model2);
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
| **creative_update_model2** | [**\criteo\api\retailmedia\experimental\Model\CreativeUpdateModel2**](../Model/CreativeUpdateModel2.md)| The creative to create | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\Creative2Response**](../Model/Creative2Response.md)

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
updatePreferredLineItemByLineItemId($line_item_id, $preferred_line_item_update_model_v2_request): \criteo\api\retailmedia\experimental\Model\PreferredLineItemV2Response
```

/experimental/retail-media/preferred-line-items/{line-item-id}

Updates the preferred line item for the given line item id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | The given line item id
$preferred_line_item_update_model_v2_request = new \criteo\api\retailmedia\experimental\Model\PreferredLineItemUpdateModelV2Request(); // \criteo\api\retailmedia\experimental\Model\PreferredLineItemUpdateModelV2Request | The line item settings to create a line item with

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
| **preferred_line_item_update_model_v2_request** | [**\criteo\api\retailmedia\experimental\Model\PreferredLineItemUpdateModelV2Request**](../Model/PreferredLineItemUpdateModelV2Request.md)| The line item settings to create a line item with | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\PreferredLineItemV2Response**](../Model/PreferredLineItemV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateProductButtonByLineItemAndProductButtonId()`

```php
updateProductButtonByLineItemAndProductButtonId($line_item_id, $product_button_id, $product_button_request_request): \criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse
```

/experimental/retail-media/line-items/{line-item-id}/product-buttons/{product-button-id}

Update Specific Product Button

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$line_item_id = 'line_item_id_example'; // string | LineItemId for productButton update
$product_button_id = 'product_button_id_example'; // string | productButtonId used for update
$product_button_request_request = new \criteo\api\retailmedia\experimental\Model\ProductButtonRequestRequest(); // \criteo\api\retailmedia\experimental\Model\ProductButtonRequestRequest | Specific Product button update info

try {
    $result = $apiInstance->updateProductButtonByLineItemAndProductButtonId($line_item_id, $product_button_id, $product_button_request_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateProductButtonByLineItemAndProductButtonId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **line_item_id** | **string**| LineItemId for productButton update | |
| **product_button_id** | **string**| productButtonId used for update | |
| **product_button_request_request** | [**\criteo\api\retailmedia\experimental\Model\ProductButtonRequestRequest**](../Model/ProductButtonRequestRequest.md)| Specific Product button update info | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ProductButtonResponseListResponse**](../Model/ProductButtonResponseListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
