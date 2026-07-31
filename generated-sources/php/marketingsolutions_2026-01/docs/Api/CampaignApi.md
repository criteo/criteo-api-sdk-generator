# criteo\api\marketingsolutions\v2026_01\CampaignApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createAdSet()**](CampaignApi.md#createAdSet) | **POST** /2026-01/marketing-solutions/ad-sets | /2026-01/marketing-solutions/ad-sets |
| [**createCampaign()**](CampaignApi.md#createCampaign) | **POST** /2026-01/marketing-solutions/campaigns | /2026-01/marketing-solutions/campaigns |
| [**createMarketplaceSellerBudgets()**](CampaignApi.md#createMarketplaceSellerBudgets) | **POST** /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets | /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets |
| [**createMarketplaceSellerCampaignsBySeller()**](CampaignApi.md#createMarketplaceSellerCampaignsBySeller) | **POST** /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns |
| [**getAdSet()**](CampaignApi.md#getAdSet) | **GET** /2026-01/marketing-solutions/ad-sets/{ad-set-id} | /2026-01/marketing-solutions/ad-sets/{ad-set-id} |
| [**getAdSetCategoryBids()**](CampaignApi.md#getAdSetCategoryBids) | **GET** /2026-01/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /2026-01/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**getCampaign()**](CampaignApi.md#getCampaign) | **GET** /2026-01/marketing-solutions/campaigns/{campaign-id} | /2026-01/marketing-solutions/campaigns/{campaign-id} |
| [**getDisplayMultipliers()**](CampaignApi.md#getDisplayMultipliers) | **GET** /2026-01/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /2026-01/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**getMarketplaceAdSetsByAdvertiser()**](CampaignApi.md#getMarketplaceAdSetsByAdvertiser) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets |
| [**getMarketplaceAdvertiser()**](CampaignApi.md#getMarketplaceAdvertiser) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId} | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId} |
| [**getMarketplaceAdvertiserPreviewLimits()**](CampaignApi.md#getMarketplaceAdvertiserPreviewLimits) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit |
| [**getMarketplaceAdvertisers()**](CampaignApi.md#getMarketplaceAdvertisers) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers |
| [**getMarketplaceBudgetsByAdvertiser()**](CampaignApi.md#getMarketplaceBudgetsByAdvertiser) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets |
| [**getMarketplaceBudgetsBySeller()**](CampaignApi.md#getMarketplaceBudgetsBySeller) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets | /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets |
| [**getMarketplaceBudgetsBySellerCampaign()**](CampaignApi.md#getMarketplaceBudgetsBySellerCampaign) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets | /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets |
| [**getMarketplaceCampaignsByAdvertiser()**](CampaignApi.md#getMarketplaceCampaignsByAdvertiser) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns |
| [**getMarketplaceCampaignsStats()**](CampaignApi.md#getMarketplaceCampaignsStats) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/stats/campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/stats/campaigns |
| [**getMarketplaceSeller()**](CampaignApi.md#getMarketplaceSeller) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId} | /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId} |
| [**getMarketplaceSellerAdPreview()**](CampaignApi.md#getMarketplaceSellerAdPreview) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview |
| [**getMarketplaceSellerBudget()**](CampaignApi.md#getMarketplaceSellerBudget) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} | /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} |
| [**getMarketplaceSellerBudgets()**](CampaignApi.md#getMarketplaceSellerBudgets) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets | /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets |
| [**getMarketplaceSellerCampaign()**](CampaignApi.md#getMarketplaceSellerCampaign) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} | /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} |
| [**getMarketplaceSellerCampaigns()**](CampaignApi.md#getMarketplaceSellerCampaigns) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns |
| [**getMarketplaceSellerCampaignsByAdvertiser()**](CampaignApi.md#getMarketplaceSellerCampaignsByAdvertiser) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns |
| [**getMarketplaceSellerCampaignsBySeller()**](CampaignApi.md#getMarketplaceSellerCampaignsBySeller) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns |
| [**getMarketplaceSellerCampaignsStats()**](CampaignApi.md#getMarketplaceSellerCampaignsStats) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns |
| [**getMarketplaceSellers()**](CampaignApi.md#getMarketplaceSellers) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers | /2026-01/marketing-solutions/marketplace-performance-outcomes/sellers |
| [**getMarketplaceSellersByAdvertiser()**](CampaignApi.md#getMarketplaceSellersByAdvertiser) | **POST** /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers | /2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers |
| [**getMarketplaceSellersStats()**](CampaignApi.md#getMarketplaceSellersStats) | **GET** /2026-01/marketing-solutions/marketplace-performance-outcomes/stats/sellers | /2026-01/marketing-solutions/marketplace-performance-outcomes/stats/sellers |
| [**patchAdSetCategoryBids()**](CampaignApi.md#patchAdSetCategoryBids) | **PATCH** /2026-01/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /2026-01/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**patchAdSets()**](CampaignApi.md#patchAdSets) | **PATCH** /2026-01/marketing-solutions/ad-sets | /2026-01/marketing-solutions/ad-sets |
| [**patchCampaigns()**](CampaignApi.md#patchCampaigns) | **PATCH** /2026-01/marketing-solutions/campaigns | /2026-01/marketing-solutions/campaigns |
| [**patchDisplayMultipliers()**](CampaignApi.md#patchDisplayMultipliers) | **PATCH** /2026-01/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /2026-01/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**searchAdSets()**](CampaignApi.md#searchAdSets) | **POST** /2026-01/marketing-solutions/ad-sets/search | /2026-01/marketing-solutions/ad-sets/search |
| [**searchCampaigns()**](CampaignApi.md#searchCampaigns) | **POST** /2026-01/marketing-solutions/campaigns/search | /2026-01/marketing-solutions/campaigns/search |
| [**startAdSets()**](CampaignApi.md#startAdSets) | **POST** /2026-01/marketing-solutions/ad-sets/start | /2026-01/marketing-solutions/ad-sets/start |
| [**stopAdSets()**](CampaignApi.md#stopAdSets) | **POST** /2026-01/marketing-solutions/ad-sets/stop | /2026-01/marketing-solutions/ad-sets/stop |
| [**updateAdSetAudience()**](CampaignApi.md#updateAdSetAudience) | **PUT** /2026-01/marketing-solutions/ad-sets/{ad-set-id}/audience | /2026-01/marketing-solutions/ad-sets/{ad-set-id}/audience |
| [**updateMarketplaceSellerBudget()**](CampaignApi.md#updateMarketplaceSellerBudget) | **PATCH** /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} | /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId} |
| [**updateMarketplaceSellerBudgets()**](CampaignApi.md#updateMarketplaceSellerBudgets) | **PATCH** /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets | /2026-01/marketing-solutions/marketplace-performance-outcomes/budgets |
| [**updateMarketplaceSellerCampaign()**](CampaignApi.md#updateMarketplaceSellerCampaign) | **PATCH** /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} | /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId} |
| [**updateMarketplaceSellerCampaigns()**](CampaignApi.md#updateMarketplaceSellerCampaigns) | **PATCH** /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns | /2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns |


## `createAdSet()`

```php
createAdSet($create_ad_set_v24_q3_request): \criteo\api\marketingsolutions\v2026_01\Model\ResponseReadAdSetV24Q3
```

/2026-01/marketing-solutions/ad-sets

Create the specified ad set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$create_ad_set_v24_q3_request = new \criteo\api\marketingsolutions\v2026_01\Model\CreateAdSetV24Q3Request(); // \criteo\api\marketingsolutions\v2026_01\Model\CreateAdSetV24Q3Request | the ad sets to create

try {
    $result = $apiInstance->createAdSet($create_ad_set_v24_q3_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createAdSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_ad_set_v24_q3_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\CreateAdSetV24Q3Request**](../Model/CreateAdSetV24Q3Request.md)| the ad sets to create | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResponseReadAdSetV24Q3**](../Model/ResponseReadAdSetV24Q3.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createCampaign()`

```php
createCampaign($create_campaign_request): \criteo\api\marketingsolutions\v2026_01\Model\CampaignV23Q1Response
```

/2026-01/marketing-solutions/campaigns

Create the specified campaign                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$create_campaign_request = new \criteo\api\marketingsolutions\v2026_01\Model\CreateCampaignRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\CreateCampaignRequest | the campaigns to create

try {
    $result = $apiInstance->createCampaign($create_campaign_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_campaign_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\CreateCampaignRequest**](../Model/CreateCampaignRequest.md)| the campaigns to create | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\CampaignV23Q1Response**](../Model/CampaignV23Q1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createMarketplaceSellerBudgets()`

```php
createMarketplaceSellerBudgets($create_seller_budget_mapi_message): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/budgets

Create one or more new budgets to enable spending with the given limitations.  All three types of budgets can be created this way.                The following constraints apply when creating a new budget.                • <b>sellerId</b>: the seller MUST be supplied<br />  • <b>campaignIds</b>: a non-empty array of campaign ids MUST be supplied<br />  • <b>budgetType</b>: a budget type MUST be supplied<br />  • <b>amount</b>: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative<br />  • <b>startDate</b>: a future start date MUST be supplied<br />  • <b>endDate</b>: an end date MAY be supplied and if supplied MUST be greater than the start date<br />                Other attributes MUST NOT be supplied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$create_seller_budget_mapi_message = array(new \criteo\api\marketingsolutions\v2026_01\Model\CreateSellerBudgetMapiMessage()); // \criteo\api\marketingsolutions\v2026_01\Model\CreateSellerBudgetMapiMessage[] | 

try {
    $result = $apiInstance->createMarketplaceSellerBudgets($create_seller_budget_mapi_message);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createMarketplaceSellerBudgets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_seller_budget_mapi_message** | [**\criteo\api\marketingsolutions\v2026_01\Model\CreateSellerBudgetMapiMessage[]**](../Model/CreateSellerBudgetMapiMessage.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createMarketplaceSellerCampaignsBySeller()`

```php
createMarketplaceSellerCampaignsBySeller($seller_id, $create_seller_campaign_message_mapi): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns

Associate an existing Seller with an existing Campaign allowing for budget creation

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_id = 'seller_id_example'; // string | Supply a generated Id of an existing Seller
$create_seller_campaign_message_mapi = new \criteo\api\marketingsolutions\v2026_01\Model\CreateSellerCampaignMessageMapi(); // \criteo\api\marketingsolutions\v2026_01\Model\CreateSellerCampaignMessageMapi | Supply the campaign Id and bid to create the mapping

try {
    $result = $apiInstance->createMarketplaceSellerCampaignsBySeller($seller_id, $create_seller_campaign_message_mapi);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createMarketplaceSellerCampaignsBySeller: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_id** | **string**| Supply a generated Id of an existing Seller | |
| **create_seller_campaign_message_mapi** | [**\criteo\api\marketingsolutions\v2026_01\Model\CreateSellerCampaignMessageMapi**](../Model/CreateSellerCampaignMessageMapi.md)| Supply the campaign Id and bid to create the mapping | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdSet()`

```php
getAdSet($ad_set_id): \criteo\api\marketingsolutions\v2026_01\Model\ResponseReadAdSetV24Q3
```

/2026-01/marketing-solutions/ad-sets/{ad-set-id}

Get the data for the specified ad set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the ad set

try {
    $result = $apiInstance->getAdSet($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAdSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the ad set | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResponseReadAdSetV24Q3**](../Model/ResponseReadAdSetV24Q3.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdSetCategoryBids()`

```php
getAdSetCategoryBids($ad_set_id): \criteo\api\marketingsolutions\v2026_01\Model\AdSetCategoryBidListResponse
```

/2026-01/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Get the Category Bids for all valid Categories associated to an Ad Set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set

try {
    $result = $apiInstance->getAdSetCategoryBids($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAdSetCategoryBids: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdSetCategoryBidListResponse**](../Model/AdSetCategoryBidListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaign()`

```php
getCampaign($campaign_id): \criteo\api\marketingsolutions\v2026_01\Model\CampaignV23Q1Response
```

/2026-01/marketing-solutions/campaigns/{campaign-id}

Get the data for the specified campaign.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | ID of the marketing campaign; This field is required.

try {
    $result = $apiInstance->getCampaign($campaign_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| ID of the marketing campaign; This field is required. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\CampaignV23Q1Response**](../Model/CampaignV23Q1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getDisplayMultipliers()`

```php
getDisplayMultipliers($ad_set_id): \criteo\api\marketingsolutions\v2026_01\Model\AdSetDisplayMultiplierListResponse
```

/2026-01/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set

try {
    $result = $apiInstance->getDisplayMultipliers($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getDisplayMultipliers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdSetDisplayMultiplierListResponse**](../Model/AdSetDisplayMultiplierListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceAdSetsByAdvertiser()`

```php
getMarketplaceAdSetsByAdvertiser($advertiser_id): \criteo\api\marketingsolutions\v2026_01\Model\AdvertiserAdsetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/adsets

Get the collection of adsets associated with the advertiserId.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser

try {
    $result = $apiInstance->getMarketplaceAdSetsByAdvertiser($advertiser_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceAdSetsByAdvertiser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdvertiserAdsetMessage[]**](../Model/AdvertiserAdsetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceAdvertiser()`

```php
getMarketplaceAdvertiser($advertiser_id): \criteo\api\marketingsolutions\v2026_01\Model\AdvertiserInfoMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}

Get an advertiser.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser

try {
    $result = $apiInstance->getMarketplaceAdvertiser($advertiser_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceAdvertiser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdvertiserInfoMessage**](../Model/AdvertiserInfoMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceAdvertiserPreviewLimits()`

```php
getMarketplaceAdvertiserPreviewLimits(): \criteo\api\marketingsolutions\v2026_01\Model\AdvertiserQuotaMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/preview-limit

Get the collection of advertisers preview limits associated with the authorized user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMarketplaceAdvertiserPreviewLimits();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceAdvertiserPreviewLimits: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdvertiserQuotaMessage[]**](../Model/AdvertiserQuotaMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceAdvertisers()`

```php
getMarketplaceAdvertisers(): \criteo\api\marketingsolutions\v2026_01\Model\AdvertiserInfoMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers

Get the collection of advertisers associated with the user.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getMarketplaceAdvertisers();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceAdvertisers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdvertiserInfoMessage[]**](../Model/AdvertiserInfoMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceBudgetsByAdvertiser()`

```php
getMarketplaceBudgetsByAdvertiser($advertiser_id, $budget_id, $end_after_date, $seller_id, $start_before_date, $status, $type, $with_balance, $with_spend): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/budgets

Get CRP budgets for a specific advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser
$budget_id = 56; // int | Return only budgets with given Id
$end_after_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended.
$seller_id = 56; // int | Return only budgets belonging to given sellerId
$start_before_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
$status = 'status_example'; // string | Return only budgets with the given status.
$type = 'type_example'; // string | Return only budgets with the given budget type.
$with_balance = True; // bool | Return only budgets with the given status.
$with_spend = True; // bool | Return budgets with any positive spend.

try {
    $result = $apiInstance->getMarketplaceBudgetsByAdvertiser($advertiser_id, $budget_id, $end_after_date, $seller_id, $start_before_date, $status, $type, $with_balance, $with_spend);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceBudgetsByAdvertiser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |
| **budget_id** | **int**| Return only budgets with given Id | [optional] |
| **end_after_date** | **\DateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **seller_id** | **int**| Return only budgets belonging to given sellerId | [optional] |
| **start_before_date** | **\DateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **string**| Return only budgets with the given status. | [optional] |
| **type** | **string**| Return only budgets with the given budget type. | [optional] |
| **with_balance** | **bool**| Return only budgets with the given status. | [optional] |
| **with_spend** | **bool**| Return budgets with any positive spend. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceBudgetsBySeller()`

```php
getMarketplaceBudgetsBySeller($seller_id, $campaign_id, $end_after_date, $start_before_date, $status, $type, $with_balance, $with_spend): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/budgets

Return current (non-archived) budgets for this seller. Budgets whose endDate is in the past are excluded by default. To retrieve archived or past budgets, use the `/budgets` endpoint (GetMarketplaceSellerBudgets) with the `endAfterDate` filter instead.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_id = 'seller_id_example'; // string | Return only budgets belonging to the given seller.
$campaign_id = 56; // int | Return only budgets that pay for a given campaign.
$end_after_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.              If param is not provided, default behavior is to only return budgets that have not yet ended.
$start_before_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
$status = 'status_example'; // string | Return only budgets with the given status.
$type = 'type_example'; // string | Return only budgets with the given budget type.
$with_balance = True; // bool | Return only budgets with the given status.
$with_spend = True; // bool | Return budgets with any positive spend.

try {
    $result = $apiInstance->getMarketplaceBudgetsBySeller($seller_id, $campaign_id, $end_after_date, $start_before_date, $status, $type, $with_balance, $with_spend);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceBudgetsBySeller: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_id** | **string**| Return only budgets belonging to the given seller. | |
| **campaign_id** | **int**| Return only budgets that pay for a given campaign. | [optional] |
| **end_after_date** | **\DateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.              If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **start_before_date** | **\DateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **string**| Return only budgets with the given status. | [optional] |
| **type** | **string**| Return only budgets with the given budget type. | [optional] |
| **with_balance** | **bool**| Return only budgets with the given status. | [optional] |
| **with_spend** | **bool**| Return budgets with any positive spend. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceBudgetsBySellerCampaign()`

```php
getMarketplaceBudgetsBySellerCampaign($seller_campaign_id, $end_after_date, $start_before_date, $status, $type, $with_balance, $with_spend): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}/budgets

Return a collection of budgets for this seller campaign filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned, except those whose endDate is in the past. Returned budgets must satisfy all supplied filter  criteria if multiple parameters are used.                See the budgets endpoint for additional details.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_campaign_id = 'seller_campaign_id_example'; // string | Return only budgets belonging to the given seller campaign. Format: `{sellerId}.{campaignId}`, e.g. `2578464.187625`.
$end_after_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended.
$start_before_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
$status = 'status_example'; // string | Return only budgets with the given status.
$type = 'type_example'; // string | Return only budgets with the given budget type.
$with_balance = True; // bool | Return only budgets with a positive balance.
$with_spend = True; // bool | Return budgets with a positive spend.

try {
    $result = $apiInstance->getMarketplaceBudgetsBySellerCampaign($seller_campaign_id, $end_after_date, $start_before_date, $status, $type, $with_balance, $with_spend);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceBudgetsBySellerCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_campaign_id** | **string**| Return only budgets belonging to the given seller campaign. Format: &#x60;{sellerId}.{campaignId}&#x60;, e.g. &#x60;2578464.187625&#x60;. | |
| **end_after_date** | **\DateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **start_before_date** | **\DateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **string**| Return only budgets with the given status. | [optional] |
| **type** | **string**| Return only budgets with the given budget type. | [optional] |
| **with_balance** | **bool**| Return only budgets with a positive balance. | [optional] |
| **with_spend** | **bool**| Return budgets with a positive spend. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceCampaignsByAdvertiser()`

```php
getMarketplaceCampaignsByAdvertiser($advertiser_id): \criteo\api\marketingsolutions\v2026_01\Model\AdvertiserCampaignMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/campaigns

Get the collection of CRP campaigns associated with the advertiserId.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser

try {
    $result = $apiInstance->getMarketplaceCampaignsByAdvertiser($advertiser_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceCampaignsByAdvertiser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdvertiserCampaignMessage[]**](../Model/AdvertiserCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceCampaignsStats()`

```php
getMarketplaceCampaignsStats($advertiser_id, $campaign_id, $click_attribution_policy, $count, $end_date, $interval_size, $start_date, $time_zone_id): \criteo\api\marketingsolutions\v2026_01\Model\StatsReportMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/stats/campaigns

## Dimensions                Get performance statistics aggregated for _campaigns_. The campaign id appears  in the output as the first column.                Aggregation can be done by `hour`, `day`, `month`, or `year` aligned with the user timezone  if provided. The aggregation interval size is controlled by `intervalSize`. The time  interval appears in the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by campaign, date or count.                Filtering the results to events associated with a specific campaign is done by setting  the `campaignId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {     \"columns\": [ \"campaignId\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\" ],     \"data\": [         [168423, \"2019-05-01\", 3969032, 13410, 1111.295, 985, 190758099, 0.073, 1.128, 0.000, 171653.880 ],         [168423, \"2019-06-01\", 8479603, 25619, 2190.705, 740, 152783656, 0.028, 2.960, 0.000, 69741.775 ]         ],     \"rows\": 2  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  column comes first and consists of the campaign id.  The interval column comes next and defines the aggregation period.  The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 56; // int | Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts.
$campaign_id = 'campaign_id_example'; // string | Show only metrics for this campaign (default all campaigns)
$click_attribution_policy = 'AnySeller'; // string | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS
$count = 56; // int | Return up to the first count rows of data (default is all rows)
$end_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Filter out all events that occur after date (default is today’s date)
$interval_size = 'Day'; // string | Specify the aggregation interval for events used to compute stats (default is \"day\")
$start_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Filter out all events that occur before date (default is the value of `endDate`)
$time_zone_id = 'time_zone_id_example'; // string | Specify the timezone used in the aggregations (IANA code).

try {
    $result = $apiInstance->getMarketplaceCampaignsStats($advertiser_id, $campaign_id, $click_attribution_policy, $count, $end_date, $interval_size, $start_date, $time_zone_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceCampaignsStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **int**| Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts. | [optional] |
| **campaign_id** | **string**| Show only metrics for this campaign (default all campaigns) | [optional] |
| **click_attribution_policy** | **string**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] [default to &#39;AnySeller&#39;] |
| **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional] |
| **end_date** | **\DateTime**| Filter out all events that occur after date (default is today’s date) | [optional] |
| **interval_size** | **string**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] [default to &#39;Day&#39;] |
| **start_date** | **\DateTime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] |
| **time_zone_id** | **string**| Specify the timezone used in the aggregations (IANA code). | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\StatsReportMessage**](../Model/StatsReportMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSeller()`

```php
getMarketplaceSeller($seller_id): \criteo\api\marketingsolutions\v2026_01\Model\SellerBase
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}

Return details for the selected seller. For example,                    {          \"id\" : \"123456\"          \"sellerName\": \"HBogart\",      }

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_id = 'seller_id_example'; // string | Id of the seller.

try {
    $result = $apiInstance->getMarketplaceSeller($seller_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSeller: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_id** | **string**| Id of the seller. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBase**](../Model/SellerBase.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerAdPreview()`

```php
getMarketplaceSellerAdPreview($advertiser_id, $seller_id, $campaign_id, $height, $width): string
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/ad-preview

Get a preview of an HTML ad with products belonging to the provided seller  • <b>advertiserId</b>: Valid crp advertiserId, seller belongs to provided advertiser<br />  • <b>sellerId</b>: Products from given SellerId will fill the ad preview, must be existing crp sellerId<br />  • <b>height</b>: height may be supplied to request a specific ad preview height. Default height: 250<br />  • <b>width</b>: width may be supplied to request a specific ad preview width. Default width: 300<br />                Ad preview api calls are capped to 1000 per day per advertiser by default. Current usage, limit, and period can be found using v2/crp/advertisers/preview-limit

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser
$seller_id = 56; // int | Id of the seller
$campaign_id = 56; // int | Seller CampaignId
$height = 56; // int | Height of the ad to display
$width = 56; // int | Width of the ad to display

try {
    $result = $apiInstance->getMarketplaceSellerAdPreview($advertiser_id, $seller_id, $campaign_id, $height, $width);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerAdPreview: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |
| **seller_id** | **int**| Id of the seller | |
| **campaign_id** | **int**| Seller CampaignId | [optional] |
| **height** | **int**| Height of the ad to display | [optional] |
| **width** | **int**| Width of the ad to display | [optional] |

### Return type

**string**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerBudget()`

```php
getMarketplaceSellerBudget($budget_id): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId}

Return a budget. For example,                    {          \"id\": \"1759183\",          \"sellerId\": \"321392\",          \"campaignIds\": [              143962          ],          \"budgetType\": \"Capped\",          \"amount\": 1000,          \"startDate\": \"2021-01-11\",          \"endDate\": \"2021-01-12\",          \"spend\": null,          \"status\": \"Active\"      }                A budget limits the spend of a seller for one or more campaigns.                There are three types of budget:<br /><b>Uncapped</b> budgets put no limit on the total amount of spend.<br /><b>Capped</b> budgets limit the total spend to a fixed amount.<br /><b>Daily</b> budgets limit daily spend to a fixed amount.<br />                In addition, budgets can limit the spend to a specific range of dates using  the start and end date attributes. Finally a budget must be active to be used.                <b>Spend</b> approximates the current spend against this budget. There may be a lag  between when an ad is clicked and the time it accrues to the spend. Daily budgets  show spend against the most recent day only.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$budget_id = 'budget_id_example'; // string | Id of the budget.

try {
    $result = $apiInstance->getMarketplaceSellerBudget($budget_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerBudget: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **budget_id** | **string**| Id of the budget. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerBudgets()`

```php
getMarketplaceSellerBudgets($advertiser_id, $campaign_id, $end_after_date, $seller_id, $start_before_date, $status, $type, $with_balance, $with_spend): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/budgets

Return a collection of budgets filtered by optional filter parameters, **including archived budgets**. This is the endpoint to use when investigating past budget history.                By default, budgets whose endDate is in the past are excluded. Use `endAfterDate` to retrieve archived budgets (e.g. `endAfterDate=2025-01-01` returns all budgets ending after that date). Use `sellerId` to filter to a specific seller — omitting it on large advertisers causes timeouts.                <b>Date filter.</b> To find budgets that were active on a specific date, set both `startBeforeDate` and `endAfterDate` to that day.                <b>Spend.</b> If `endAfterDate` is supplied, the spend excludes spend that happened after that date. For daily budgets, only the spend for the final day is displayed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 56; // int | Return only budgets belonging to the specified advertiser
$campaign_id = 56; // int | Return only budgets that pay for a given campaign.
$end_after_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that end after the given date using the `yyyy-MM-DD` format.               If param is not provided, default behavior is to only return budgets that have not yet ended.
$seller_id = 'seller_id_example'; // string | Return only budgets belonging to the given seller.
$start_before_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Return budgets that start on or before the given date using the `yyyy-MM-DD` format.
$status = 'status_example'; // string | Return only budgets with the given status.
$type = 'type_example'; // string | Return only budgets with the given budget type.
$with_balance = True; // bool | Return only budgets with the given status.
$with_spend = True; // bool | Return budgets with any positive spend.

try {
    $result = $apiInstance->getMarketplaceSellerBudgets($advertiser_id, $campaign_id, $end_after_date, $seller_id, $start_before_date, $status, $type, $with_balance, $with_spend);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerBudgets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **int**| Return only budgets belonging to the specified advertiser | [optional] |
| **campaign_id** | **int**| Return only budgets that pay for a given campaign. | [optional] |
| **end_after_date** | **\DateTime**| Return budgets that end after the given date using the &#x60;yyyy-MM-DD&#x60; format.               If param is not provided, default behavior is to only return budgets that have not yet ended. | [optional] |
| **seller_id** | **string**| Return only budgets belonging to the given seller. | [optional] |
| **start_before_date** | **\DateTime**| Return budgets that start on or before the given date using the &#x60;yyyy-MM-DD&#x60; format. | [optional] |
| **status** | **string**| Return only budgets with the given status. | [optional] |
| **type** | **string**| Return only budgets with the given budget type. | [optional] |
| **with_balance** | **bool**| Return only budgets with the given status. | [optional] |
| **with_spend** | **bool**| Return budgets with any positive spend. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerCampaign()`

```php
getMarketplaceSellerCampaign($seller_campaign_id): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}

Return details for a seller campaign. For example,                    {          \"id\": \"543210.123456\",          \"sellerId\": \"543210\",          \"campaignId\": 123456,          \"bid\": 1.55,          \"suspendedSince\": \"2018-07-30T15:15:24.813\",          \"suspensionReasons\": [              \"NoMoreBudget\"          ]      }                An active seller campaign is one for which the value of <b>suspendedSince</b> is null and  the <b>bid</b> is positive. The currency of the bid is the <b>bidCurrency</b> of the  associated campaign.                Any active seller campaign must also have an active total (capped or uncapped) budget.  It may optionally have an active daily budget as well to further limit spending.                Suspension reasons:  - ManuallyStopped: The Seller-Campaign has been manually paused. This is not related to the other suspension reasons.  - NoBudgetDefined: No valid budget has been linked to the Seller-Campaign.  - NoCpcDefined: No CPC has been set for the Seller-Campaign.  - NoMoreBudget: The current budget of the Seller-Campaign has been exhausted.  - RemovedFromCatalog: All the products of the Seller-Campaign have been deleted from the catalog.  - NotYetStarted: The Seller-Campaign has just been created and has not yet been processed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_campaign_id = 'seller_campaign_id_example'; // string | Composite id of the seller campaign in the format `{sellerId}.{campaignId}`, e.g. `2578464.187625`.

try {
    $result = $apiInstance->getMarketplaceSellerCampaign($seller_campaign_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_campaign_id** | **string**| Composite id of the seller campaign in the format &#x60;{sellerId}.{campaignId}&#x60;, e.g. &#x60;2578464.187625&#x60;. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerCampaigns()`

```php
getMarketplaceSellerCampaigns($advertiser_id, $budget_status, $campaign_id, $seller_id, $seller_status): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns

Return a collection of seller campaigns filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 56; // int | Return only seller belonging to the specified advertiser
$budget_status = 'budget_status_example'; // string | Return only seller campaigns whose budget has the given status.
$campaign_id = 56; // int | Return only seller campaigns associated with the given campaign.
$seller_id = 'seller_id_example'; // string | Return only seller campaigns belonging to the given seller.
$seller_status = 'seller_status_example'; // string | Return only seller campaigns for sellers with the given status.

try {
    $result = $apiInstance->getMarketplaceSellerCampaigns($advertiser_id, $budget_status, $campaign_id, $seller_id, $seller_status);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerCampaigns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **int**| Return only seller belonging to the specified advertiser | [optional] |
| **budget_status** | **string**| Return only seller campaigns whose budget has the given status. | [optional] |
| **campaign_id** | **int**| Return only seller campaigns associated with the given campaign. | [optional] |
| **seller_id** | **string**| Return only seller campaigns belonging to the given seller. | [optional] |
| **seller_status** | **string**| Return only seller campaigns for sellers with the given status. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerCampaignsByAdvertiser()`

```php
getMarketplaceSellerCampaignsByAdvertiser($advertiser_id): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/seller-campaigns

Get CRP seller campaigns for a specific advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser

try {
    $result = $apiInstance->getMarketplaceSellerCampaignsByAdvertiser($advertiser_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerCampaignsByAdvertiser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerCampaignsBySeller()`

```php
getMarketplaceSellerCampaignsBySeller($seller_id, $budget_status, $campaign_id, $seller_status): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/sellers/{sellerId}/seller-campaigns

Return a collection of seller campaigns for this seller filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used. See the seller campaigns endpoint for additional details.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_id = 'seller_id_example'; // string | Return only seller campaigns belonging to the given seller.
$budget_status = 'budget_status_example'; // string | Return only seller campaigns whose budget has the given status.
$campaign_id = 56; // int | Return only seller campaigns associated with the given campaign.
$seller_status = 'seller_status_example'; // string | Return only seller campaigns for sellers with the given status.

try {
    $result = $apiInstance->getMarketplaceSellerCampaignsBySeller($seller_id, $budget_status, $campaign_id, $seller_status);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerCampaignsBySeller: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_id** | **string**| Return only seller campaigns belonging to the given seller. | |
| **budget_status** | **string**| Return only seller campaigns whose budget has the given status. | [optional] |
| **campaign_id** | **int**| Return only seller campaigns associated with the given campaign. | [optional] |
| **seller_status** | **string**| Return only seller campaigns for sellers with the given status. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellerCampaignsStats()`

```php
getMarketplaceSellerCampaignsStats($advertiser_id, $campaign_id, $click_attribution_policy, $count, $end_date, $interval_size, $seller_id, $start_date, $time_zone_id): \criteo\api\marketingsolutions\v2026_01\Model\StatsReportMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/stats/seller-campaigns

## Dimensions                Get performance statistics aggregated for _seller campaigns_.The campaign id, seller id, and  seller name appear in the first three columns of the output. These are followed by the interval  size column.                Aggregation can be done by `hour`, `day`, `month`, or `year` aligned with the user timezone if  provided. The aggregation interval size is controlled by `intervalSize`. The remaining columns  are metrics.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by date or count.                Filtering the results to events associated with a specific campaign is done by setting  the `campaignId` filter parameter to the desired value.                Filtering the results to events associated with a specific seller is done by setting  the `sellerId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {      \"columns\": [          \"campaignId\", \"sellerId\", \"sellerName\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\"      ],      \"data\": [          [168423, 1110222, \"118883955\", \"2019-05-01\", 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110222, \"118883955\", \"2019-06-01\", 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \"117980027\", \"2019-05-01\", 12502, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],          [168423, 1110225, \"117980027\", \"2019-06-01\", 20266, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0]      ],      \"rows\": 4  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the campaign id, seller id, and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 56; // int | Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts.
$campaign_id = 'campaign_id_example'; // string | Show only metrics for this campaign (default all campaigns)
$click_attribution_policy = 'AnySeller'; // string | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS
$count = 56; // int | Return up to the first count rows of data (default is all rows)
$end_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Filter out all events that occur after date (default is today’s date)
$interval_size = 'Day'; // string | Specify the aggregation interval for events used to compute stats (default is \"day\")
$seller_id = 'seller_id_example'; // string | Show only metrics for this seller (default all sellers)
$start_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Filter out all events that occur before date (default is the value of `endDate`)
$time_zone_id = 'time_zone_id_example'; // string | Specify the timezone used in the aggregations (IANA code).

try {
    $result = $apiInstance->getMarketplaceSellerCampaignsStats($advertiser_id, $campaign_id, $click_attribution_policy, $count, $end_date, $interval_size, $seller_id, $start_date, $time_zone_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellerCampaignsStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **int**| Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts. | [optional] |
| **campaign_id** | **string**| Show only metrics for this campaign (default all campaigns) | [optional] |
| **click_attribution_policy** | **string**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] [default to &#39;AnySeller&#39;] |
| **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional] |
| **end_date** | **\DateTime**| Filter out all events that occur after date (default is today’s date) | [optional] |
| **interval_size** | **string**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] [default to &#39;Day&#39;] |
| **seller_id** | **string**| Show only metrics for this seller (default all sellers) | [optional] |
| **start_date** | **\DateTime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] |
| **time_zone_id** | **string**| Specify the timezone used in the aggregations (IANA code). | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\StatsReportMessage**](../Model/StatsReportMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellers()`

```php
getMarketplaceSellers($advertiser_id, $campaign_id, $seller_name, $seller_status, $with_budget_status, $with_products): \criteo\api\marketingsolutions\v2026_01\Model\SellerBase[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/sellers

Return a collection of sellers filtered by optional filter parameters.  If all parameters are omitted the entire collection to which the user has  access is returned. Returned sellers must satisfy all supplied filter  criteria if multiple parameters are used.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 56; // int | Return only sellers belonging to the specified advertiser
$campaign_id = 56; // int | Return only sellers belonging to the specified campaign
$seller_name = 'seller_name_example'; // string | Return only sellers with the matching name.
$seller_status = 'seller_status_example'; // string | Return only sellers with specific status.
$with_budget_status = 'with_budget_status_example'; // string | Return only sellers with specific budget status.
$with_products = True; // bool | Return only sellers with or without products in catalog.

try {
    $result = $apiInstance->getMarketplaceSellers($advertiser_id, $campaign_id, $seller_name, $seller_status, $with_budget_status, $with_products);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **int**| Return only sellers belonging to the specified advertiser | [optional] |
| **campaign_id** | **int**| Return only sellers belonging to the specified campaign | [optional] |
| **seller_name** | **string**| Return only sellers with the matching name. | [optional] |
| **seller_status** | **string**| Return only sellers with specific status. | [optional] |
| **with_budget_status** | **string**| Return only sellers with specific budget status. | [optional] |
| **with_products** | **bool**| Return only sellers with or without products in catalog. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBase[]**](../Model/SellerBase.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellersByAdvertiser()`

```php
getMarketplaceSellersByAdvertiser($advertiser_id, $request_body, $partner_id): \criteo\api\marketingsolutions\v2026_01\Model\SellerBase[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/advertisers/{advertiserId}/sellers

Create new sellers for an advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | Id of the advertiser
$request_body = array('request_body_example'); // string[] | Names of the sellers to associate with new Ids
$partner_id = 56; // int | Id of the partner

try {
    $result = $apiInstance->getMarketplaceSellersByAdvertiser($advertiser_id, $request_body, $partner_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellersByAdvertiser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| Id of the advertiser | |
| **request_body** | [**string[]**](../Model/string.md)| Names of the sellers to associate with new Ids | |
| **partner_id** | **int**| Id of the partner | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBase[]**](../Model/SellerBase.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplaceSellersStats()`

```php
getMarketplaceSellersStats($advertiser_id, $click_attribution_policy, $count, $end_date, $interval_size, $seller_id, $start_date, $time_zone_id): \criteo\api\marketingsolutions\v2026_01\Model\StatsReportMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/stats/sellers

## Dimensions                Get performance statistics aggregated for _sellers_. The seller id appears  in the output in the first column and the seller name appears in the second.                Aggregation can be done by `hour`, `day`, `month`, or `year` aligned with the user timezone  if provided. The aggregation interval size is controlled by `intervalSize`. The time interval  appears in the output as the second column.                ## Metrics                The metrics reported by this endpoint are                .  | Metric Group | Description  ---|--------------|------------  A | impressions | Number of times product is shown in a banner  B | clicks | Number of clicks on product  C | cost | Amount spent for clicks on products  D | saleUnits | Number of products sold attributed to clicks  E | revenue | Revenue generated by sales  F | CR = Conversion Rate | salesUnits / clicks  G | CPO = Cost Per Order | cost / salesUnits  H | COS = Cost of Sale | cost / revenue  I | ROAS = Return On Add Spend | revenue / cost                The last six metrics can be computed in two ways depending on the policy to count only  the sales that result from clicks on the same sellers product in a banner  (same-seller) or not (any-seller).  Reporting can be controlled by `clickAttributionPolicy`.                The 9 (or 15) metric values appear in the output as the final 9 (or 15) columns.                ## Filtering                The results can be filtered by seller id, date or count.                Filtering the results to events associated with a specific seller is done by setting  the `sellerId` filter parameter to the desired value.                Filtering the results to events  that happened in a time interval is done by setting the `startDate` and  `endDate` filter parameters using the `yyyy-MM-DD` format. The start date  includes all events timestamped since the beginning of that day while the end  date includes events until the end of day. The maximum duration of the date  range is 1 year. If the aggregation interval is `hour`, then the maximum  duration of the date range is 31 days. Note that month and year aggregate values  may contain partial data for the interval if filtering by date.                Filtering the results to a maximum number of data rows is done by setting the  `count` filter parameter. When combined with startDate this can be used to perform  simple pagination.                ## Response Format                The representation format can be specified by MIME values in the Accept header.  For now the only supported values for the accept header is `application/json` and  `text/csv`.                ```json  {      \"columns\": [\"sellerId\", \"sellerName\", \"month\", \"impressions\", \"clicks\", \"cost\", \"saleUnits\", \"revenue\", \"cr\", \"cpo\", \"cos\", \"roas\"],      \"data\": [         [1200972, \"sellerA\", \"2019-05-01\", 14542, 48, 3.36, 0, 0.0, 0.0, null, null, 0.0],         [1200972, \"sellerA\", \"2019-06-01\", 16619, 53, 3.71, 0, 0.0, 0.0, null, null, 0.0],         [1200974, \"sellerB\", \"2019-05-01\", 10102, 47, 3.29, 3, 396000.0, 0.063, 1.096, 8.308E-6, 120364.741],         [1200974, \"sellerB\", \"2019-06-01\", 11576, 54, 3.78, 1, 132000.0, 0.018, 3.78, 2.863E-5, 34920.634]      ],      \"rows\": 4  }  ```                The JSON result is an object with three fields (`columns`, `data`, and `rows`). The  “columns” array acts as the header for the data rows. The categorical dimension  columns come first and include the seller id and seller name.  The interval column comes next and defines the aggregation period. The interval size is  determined by the `intervalSize` parameter. This is followed by either nine or  fifteen metrics columns. The first three metrics (impressions, clicks, and cost)  always appear. The remaining metrics depend on the `clickAttributionPolicy` parameter.                The “data” array contains data rows whose values match the entries in the  “columns” array. Id dimensions are numbers while name and date dimensions are strings. The metrics are JSON objects  whose type is number. Some of these are natural numbers (e.g. clicks and  impressions) whereas others are decimal values. A divide by zero yields null. The  currency is assumed to be the local currency established by the advertiser.                The “row” value is a count of the number of rows in the data array, and can be  used to check the integrity of the data.                Further information on the campaign or seller (e.g. the seller name) can be  obtained from the existing V1 or V2 endpoints using the campaign and/or seller  ID values.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 56; // int | Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts.
$click_attribution_policy = 'AnySeller'; // string | Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS
$count = 56; // int | Return up to the first count rows of data (default is all rows)
$end_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Filter out all events that occur after date (default is today’s date)
$interval_size = 'Day'; // string | Specify the aggregation interval for events used to compute stats (default is \"day\")
$seller_id = 'seller_id_example'; // string | Show only metrics for this seller (default all sellers)
$start_date = new \DateTime("2013-10-20T19:20:30+01:00"); // \DateTime | Filter out all events that occur before date (default is the value of `endDate`)
$time_zone_id = 'time_zone_id_example'; // string | Specify the timezone used in the aggregations (IANA code).

try {
    $result = $apiInstance->getMarketplaceSellersStats($advertiser_id, $click_attribution_policy, $count, $end_date, $interval_size, $seller_id, $start_date, $time_zone_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getMarketplaceSellersStats: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **int**| Filter metrics to this advertiser. Strongly recommended — omitting this on large accounts causes timeouts. | [optional] |
| **click_attribution_policy** | **string**| Specify the click attribution policy for salesUnits, revenue, CR, CPO, COS, and ROAS | [optional] [default to &#39;AnySeller&#39;] |
| **count** | **int**| Return up to the first count rows of data (default is all rows) | [optional] |
| **end_date** | **\DateTime**| Filter out all events that occur after date (default is today’s date) | [optional] |
| **interval_size** | **string**| Specify the aggregation interval for events used to compute stats (default is \&quot;day\&quot;) | [optional] [default to &#39;Day&#39;] |
| **seller_id** | **string**| Show only metrics for this seller (default all sellers) | [optional] |
| **start_date** | **\DateTime**| Filter out all events that occur before date (default is the value of &#x60;endDate&#x60;) | [optional] |
| **time_zone_id** | **string**| Specify the timezone used in the aggregations (IANA code). | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\StatsReportMessage**](../Model/StatsReportMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `patchAdSetCategoryBids()`

```php
patchAdSetCategoryBids($ad_set_id, $patch_ad_set_category_bid_list_request): \criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetCategoryBidResultListResponse
```

/2026-01/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Update the Category Bids for given Categories associated to an Ad Set  Patch Category Bids for one or more Categories in a single request. Partial success policy is followed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set
$patch_ad_set_category_bid_list_request = new \criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetCategoryBidListRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetCategoryBidListRequest | Collection of category bids to update

try {
    $result = $apiInstance->patchAdSetCategoryBids($ad_set_id, $patch_ad_set_category_bid_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->patchAdSetCategoryBids: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |
| **patch_ad_set_category_bid_list_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetCategoryBidListRequest**](../Model/PatchAdSetCategoryBidListRequest.md)| Collection of category bids to update | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetCategoryBidResultListResponse**](../Model/PatchAdSetCategoryBidResultListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `patchAdSets()`

```php
patchAdSets($requests_patch_ad_set_v24_q3): \criteo\api\marketingsolutions\v2026_01\Model\ResponsesAdSetIdV24Q3
```

/2026-01/marketing-solutions/ad-sets

Patch a list of AdSets.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requests_patch_ad_set_v24_q3 = new \criteo\api\marketingsolutions\v2026_01\Model\RequestsPatchAdSetV24Q3(); // \criteo\api\marketingsolutions\v2026_01\Model\RequestsPatchAdSetV24Q3 | List of adsets to patch.

try {
    $result = $apiInstance->patchAdSets($requests_patch_ad_set_v24_q3);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->patchAdSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **requests_patch_ad_set_v24_q3** | [**\criteo\api\marketingsolutions\v2026_01\Model\RequestsPatchAdSetV24Q3**](../Model/RequestsPatchAdSetV24Q3.md)| List of adsets to patch. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResponsesAdSetIdV24Q3**](../Model/ResponsesAdSetIdV24Q3.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `patchCampaigns()`

```php
patchCampaigns($patch_campaign_list_request): \criteo\api\marketingsolutions\v2026_01\Model\PatchResultCampaignListResponse
```

/2026-01/marketing-solutions/campaigns

Patch a list of Campaigns.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$patch_campaign_list_request = new \criteo\api\marketingsolutions\v2026_01\Model\PatchCampaignListRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\PatchCampaignListRequest | List of campaigns to patch.

try {
    $result = $apiInstance->patchCampaigns($patch_campaign_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->patchCampaigns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **patch_campaign_list_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\PatchCampaignListRequest**](../Model/PatchCampaignListRequest.md)| List of campaigns to patch. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\PatchResultCampaignListResponse**](../Model/PatchResultCampaignListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `patchDisplayMultipliers()`

```php
patchDisplayMultipliers($ad_set_id, $patch_ad_set_display_multiplier_list_request): \criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetDisplayMultiplierResultListResponse
```

/2026-01/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Update the Display Multipliers for given Categories associated to an Ad Set  Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set
$patch_ad_set_display_multiplier_list_request = new \criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetDisplayMultiplierListRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetDisplayMultiplierListRequest | List of display multiplier values to change

try {
    $result = $apiInstance->patchDisplayMultipliers($ad_set_id, $patch_ad_set_display_multiplier_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->patchDisplayMultipliers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |
| **patch_ad_set_display_multiplier_list_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetDisplayMultiplierListRequest**](../Model/PatchAdSetDisplayMultiplierListRequest.md)| List of display multiplier values to change | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\PatchAdSetDisplayMultiplierResultListResponse**](../Model/PatchAdSetDisplayMultiplierResultListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAdSets()`

```php
searchAdSets($ad_set_search_request_v24_q3): \criteo\api\marketingsolutions\v2026_01\Model\ResponsesReadAdSetV24Q3
```

/2026-01/marketing-solutions/ad-sets/search

Search for ad sets

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_search_request_v24_q3 = new \criteo\api\marketingsolutions\v2026_01\Model\AdSetSearchRequestV24Q3(); // \criteo\api\marketingsolutions\v2026_01\Model\AdSetSearchRequestV24Q3

try {
    $result = $apiInstance->searchAdSets($ad_set_search_request_v24_q3);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchAdSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_search_request_v24_q3** | [**\criteo\api\marketingsolutions\v2026_01\Model\AdSetSearchRequestV24Q3**](../Model/AdSetSearchRequestV24Q3.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResponsesReadAdSetV24Q3**](../Model/ResponsesReadAdSetV24Q3.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchCampaigns()`

```php
searchCampaigns($campaign_search_request_v23_q1): \criteo\api\marketingsolutions\v2026_01\Model\CampaignV23Q1ListResponse
```

/2026-01/marketing-solutions/campaigns/search

Search endpoint for campaigns                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_search_request_v23_q1 = new \criteo\api\marketingsolutions\v2026_01\Model\CampaignSearchRequestV23Q1(); // \criteo\api\marketingsolutions\v2026_01\Model\CampaignSearchRequestV23Q1 | Filters for searching for campaigns

try {
    $result = $apiInstance->searchCampaigns($campaign_search_request_v23_q1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchCampaigns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_search_request_v23_q1** | [**\criteo\api\marketingsolutions\v2026_01\Model\CampaignSearchRequestV23Q1**](../Model/CampaignSearchRequestV23Q1.md)| Filters for searching for campaigns | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\CampaignV23Q1ListResponse**](../Model/CampaignV23Q1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `startAdSets()`

```php
startAdSets($requests_ad_set_id): \criteo\api\marketingsolutions\v2026_01\Model\ResponsesAdSetId
```

/2026-01/marketing-solutions/ad-sets/start

Start the specified list of ad sets

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requests_ad_set_id = new \criteo\api\marketingsolutions\v2026_01\Model\RequestsAdSetId(); // \criteo\api\marketingsolutions\v2026_01\Model\RequestsAdSetId | All the ad sets to start

try {
    $result = $apiInstance->startAdSets($requests_ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->startAdSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **requests_ad_set_id** | [**\criteo\api\marketingsolutions\v2026_01\Model\RequestsAdSetId**](../Model/RequestsAdSetId.md)| All the ad sets to start | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResponsesAdSetId**](../Model/ResponsesAdSetId.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `stopAdSets()`

```php
stopAdSets($requests_ad_set_id): \criteo\api\marketingsolutions\v2026_01\Model\ResponsesAdSetId
```

/2026-01/marketing-solutions/ad-sets/stop

Stop the specified list of ad sets

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requests_ad_set_id = new \criteo\api\marketingsolutions\v2026_01\Model\RequestsAdSetId(); // \criteo\api\marketingsolutions\v2026_01\Model\RequestsAdSetId | All the ad sets to stop

try {
    $result = $apiInstance->stopAdSets($requests_ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->stopAdSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **requests_ad_set_id** | [**\criteo\api\marketingsolutions\v2026_01\Model\RequestsAdSetId**](../Model/RequestsAdSetId.md)| All the ad sets to stop | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResponsesAdSetId**](../Model/ResponsesAdSetId.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateAdSetAudience()`

```php
updateAdSetAudience($ad_set_id, $ad_set_audience_link_input_entity_v1): \criteo\api\marketingsolutions\v2026_01\Model\AdSetAudienceLinkEntityV1Response
```

/2026-01/marketing-solutions/ad-sets/{ad-set-id}/audience

Link or unlink an audience with an ad set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | The ad set ID.
$ad_set_audience_link_input_entity_v1 = new \criteo\api\marketingsolutions\v2026_01\Model\AdSetAudienceLinkInputEntityV1(); // \criteo\api\marketingsolutions\v2026_01\Model\AdSetAudienceLinkInputEntityV1 | Ad set-Audience update request.

try {
    $result = $apiInstance->updateAdSetAudience($ad_set_id, $ad_set_audience_link_input_entity_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateAdSetAudience: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| The ad set ID. | |
| **ad_set_audience_link_input_entity_v1** | [**\criteo\api\marketingsolutions\v2026_01\Model\AdSetAudienceLinkInputEntityV1**](../Model/AdSetAudienceLinkInputEntityV1.md)| Ad set-Audience update request. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\AdSetAudienceLinkEntityV1Response**](../Model/AdSetAudienceLinkEntityV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateMarketplaceSellerBudget()`

```php
updateMarketplaceSellerBudget($budget_id, $update_seller_budget_message_base): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/budgets/{budgetId}

Modify an existing active budget to change its limitations or status.  All three types of budgets can be modified.                See the additional restrictions listed in the PATCH budgets endpoint.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$budget_id = 'budget_id_example'; // string | Id of the budget
$update_seller_budget_message_base = new \criteo\api\marketingsolutions\v2026_01\Model\UpdateSellerBudgetMessageBase(); // \criteo\api\marketingsolutions\v2026_01\Model\UpdateSellerBudgetMessageBase | 

try {
    $result = $apiInstance->updateMarketplaceSellerBudget($budget_id, $update_seller_budget_message_base);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateMarketplaceSellerBudget: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **budget_id** | **string**| Id of the budget | |
| **update_seller_budget_message_base** | [**\criteo\api\marketingsolutions\v2026_01\Model\UpdateSellerBudgetMessageBase**](../Model/UpdateSellerBudgetMessageBase.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateMarketplaceSellerBudgets()`

```php
updateMarketplaceSellerBudgets($update_seller_budget_message): \criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/budgets

Modify one or more existing active budgets to change their limitations or status.  All three types of budgets can be modified.                The following constraints apply when modifying an existing budget.                • <b>campaignIds</b>: a non-empty subset of the original campaign ids MAY be supplied<br />  • <b>amount</b>: an amount MAY be supplied only if the type is not Uncapped and if supplied it MUST be non-negative<br />  • <b>startDate</b>: a future start date MAY be supplied for budgets that have not yet started<br />  • <b>endDate</b>: an end date MAY be supplied and if supplied MUST be a future date greater than the start date<br />                Other attributes MUST NOT be supplied.                Adding new campaigns to a budget is not allowed. In addition, reducing the amount for  a Capped budget to a value less than the current spend not allowed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$update_seller_budget_message = array(new \criteo\api\marketingsolutions\v2026_01\Model\UpdateSellerBudgetMessage()); // \criteo\api\marketingsolutions\v2026_01\Model\UpdateSellerBudgetMessage[] | 

try {
    $result = $apiInstance->updateMarketplaceSellerBudgets($update_seller_budget_message);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateMarketplaceSellerBudgets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **update_seller_budget_message** | [**\criteo\api\marketingsolutions\v2026_01\Model\UpdateSellerBudgetMessage[]**](../Model/UpdateSellerBudgetMessage.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerBudgetMessage[]**](../Model/SellerBudgetMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateMarketplaceSellerCampaign()`

```php
updateMarketplaceSellerCampaign($seller_campaign_id, $bid): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns/{sellerCampaignId}

Patching a seller campaign allows the bid to be modified. The bid must be a non-negative value.  Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_campaign_id = 'seller_campaign_id_example'; // string | Composite id of the seller campaign to update in the format `{sellerId}.{campaignId}`, e.g. `2578464.187625`.
$bid = 3.4; // float | The new bid for the seller campaign.

try {
    $result = $apiInstance->updateMarketplaceSellerCampaign($seller_campaign_id, $bid);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateMarketplaceSellerCampaign: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_campaign_id** | **string**| Composite id of the seller campaign to update in the format &#x60;{sellerId}.{campaignId}&#x60;, e.g. &#x60;2578464.187625&#x60;. | |
| **bid** | **float**| The new bid for the seller campaign. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateMarketplaceSellerCampaigns()`

```php
updateMarketplaceSellerCampaigns($seller_campaign_update): \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]
```

/2026-01/marketing-solutions/marketplace-performance-outcomes/seller-campaigns

Patching a collection of seller campaigns allows their bids to be modified.  Each bid must be a non-negative value. Setting the bid to zero will make a seller campaign inactive.                The currency used for bids will be the default currency of the campaign.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$seller_campaign_update = array(new \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignUpdate()); // \criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignUpdate[] | 

try {
    $result = $apiInstance->updateMarketplaceSellerCampaigns($seller_campaign_update);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->updateMarketplaceSellerCampaigns: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **seller_campaign_update** | [**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignUpdate[]**](../Model/SellerCampaignUpdate.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\SellerCampaignMessage[]**](../Model/SellerCampaignMessage.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
