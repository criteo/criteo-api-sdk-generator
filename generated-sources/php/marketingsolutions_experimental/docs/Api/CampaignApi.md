# criteo\api\marketingsolutions\experimental\CampaignApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createAdSet()**](CampaignApi.md#createAdSet) | **POST** /experimental/marketing-solutions/ad-sets | /experimental/marketing-solutions/ad-sets |
| [**createCampaign()**](CampaignApi.md#createCampaign) | **POST** /experimental/marketing-solutions/campaigns | /experimental/marketing-solutions/campaigns |
| [**deleteAdvertiserBundleRules()**](CampaignApi.md#deleteAdvertiserBundleRules) | **DELETE** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**deleteAdvertiserDomainRules()**](CampaignApi.md#deleteAdvertiserDomainRules) | **DELETE** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**deleteCampaignBundleRules()**](CampaignApi.md#deleteCampaignBundleRules) | **DELETE** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**deleteCampaignDomainRules()**](CampaignApi.md#deleteCampaignDomainRules) | **DELETE** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**disableAdSetTargetingDealIds()**](CampaignApi.md#disableAdSetTargetingDealIds) | **POST** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable |
| [**disableAdSetTargetingVideoPositioning()**](CampaignApi.md#disableAdSetTargetingVideoPositioning) | **POST** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable |
| [**getAdSet()**](CampaignApi.md#getAdSet) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id} | /experimental/marketing-solutions/ad-sets/{ad-set-id} |
| [**getAdSetCategoryBids()**](CampaignApi.md#getAdSetCategoryBids) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**getAdSetTargetingDealIds()**](CampaignApi.md#getAdSetTargetingDealIds) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids |
| [**getAdSetTargetingVideoPositioning()**](CampaignApi.md#getAdSetTargetingVideoPositioning) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning |
| [**getAdvertiserBundleRules()**](CampaignApi.md#getAdvertiserBundleRules) | **GET** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**getAdvertiserDomainRules()**](CampaignApi.md#getAdvertiserDomainRules) | **GET** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**getCampaign()**](CampaignApi.md#getCampaign) | **GET** /experimental/marketing-solutions/campaigns/{campaign-id} | /experimental/marketing-solutions/campaigns/{campaign-id} |
| [**getCampaignBundleRules()**](CampaignApi.md#getCampaignBundleRules) | **GET** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**getCampaignDomainRules()**](CampaignApi.md#getCampaignDomainRules) | **GET** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**getDisplayMultipliers()**](CampaignApi.md#getDisplayMultipliers) | **GET** /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**getSupplyVendorList()**](CampaignApi.md#getSupplyVendorList) | **GET** /experimental/marketing-solutions/ad-sets/targeting/supply-vendors | /experimental/marketing-solutions/ad-sets/targeting/supply-vendors |
| [**patchAdSetCategoryBids()**](CampaignApi.md#patchAdSetCategoryBids) | **PATCH** /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids |
| [**patchAdSets()**](CampaignApi.md#patchAdSets) | **PATCH** /experimental/marketing-solutions/ad-sets | /experimental/marketing-solutions/ad-sets |
| [**patchCampaigns()**](CampaignApi.md#patchCampaigns) | **PATCH** /experimental/marketing-solutions/campaigns | /experimental/marketing-solutions/campaigns |
| [**patchDisplayMultipliers()**](CampaignApi.md#patchDisplayMultipliers) | **PATCH** /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers | /experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers |
| [**postAdvertiserBundleRules()**](CampaignApi.md#postAdvertiserBundleRules) | **POST** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**postAdvertiserDomainRules()**](CampaignApi.md#postAdvertiserDomainRules) | **POST** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**postCampaignBundleRules()**](CampaignApi.md#postCampaignBundleRules) | **POST** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**postCampaignDomainRules()**](CampaignApi.md#postCampaignDomainRules) | **POST** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**putAdvertiserBundleRules()**](CampaignApi.md#putAdvertiserBundleRules) | **PUT** /experimental/advertisers/{advertiserId}/targeting/bundle-rules | /experimental/advertisers/{advertiserId}/targeting/bundle-rules |
| [**putAdvertiserDomainRules()**](CampaignApi.md#putAdvertiserDomainRules) | **PUT** /experimental/advertisers/{advertiserId}/targeting/domain-rules | /experimental/advertisers/{advertiserId}/targeting/domain-rules |
| [**putCampaignBundleRules()**](CampaignApi.md#putCampaignBundleRules) | **PUT** /experimental/campaigns/{campaignId}/targeting/bundle-rules | /experimental/campaigns/{campaignId}/targeting/bundle-rules |
| [**putCampaignDomainRules()**](CampaignApi.md#putCampaignDomainRules) | **PUT** /experimental/campaigns/{campaignId}/targeting/domain-rules | /experimental/campaigns/{campaignId}/targeting/domain-rules |
| [**searchAdSets()**](CampaignApi.md#searchAdSets) | **POST** /experimental/marketing-solutions/ad-sets/search | /experimental/marketing-solutions/ad-sets/search |
| [**searchCampaigns()**](CampaignApi.md#searchCampaigns) | **POST** /experimental/marketing-solutions/campaigns/search | /experimental/marketing-solutions/campaigns/search |
| [**setAdSetTargetingDealIds()**](CampaignApi.md#setAdSetTargetingDealIds) | **PUT** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids |
| [**setAdSetTargetingVideoPositioning()**](CampaignApi.md#setAdSetTargetingVideoPositioning) | **PUT** /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning | /experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning |
| [**startAdSets()**](CampaignApi.md#startAdSets) | **POST** /experimental/marketing-solutions/ad-sets/start | /experimental/marketing-solutions/ad-sets/start |
| [**stopAdSets()**](CampaignApi.md#stopAdSets) | **POST** /experimental/marketing-solutions/ad-sets/stop | /experimental/marketing-solutions/ad-sets/stop |
| [**updateAdSetAudience()**](CampaignApi.md#updateAdSetAudience) | **PUT** /experimental/marketing-solutions/ad-sets/{ad-set-id}/audience | /experimental/marketing-solutions/ad-sets/{ad-set-id}/audience |


## `createAdSet()`

```php
createAdSet($create_ad_set_v26_q1_request): \criteo\api\marketingsolutions\experimental\Model\ResponseReadAdSetV26Q1
```

/experimental/marketing-solutions/ad-sets

Create an ad set with the provided parameters

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$create_ad_set_v26_q1_request = new \criteo\api\marketingsolutions\experimental\Model\CreateAdSetV26Q1Request(); // \criteo\api\marketingsolutions\experimental\Model\CreateAdSetV26Q1Request | the ad sets to create

try {
    $result = $apiInstance->createAdSet($create_ad_set_v26_q1_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->createAdSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **create_ad_set_v26_q1_request** | [**\criteo\api\marketingsolutions\experimental\Model\CreateAdSetV26Q1Request**](../Model/CreateAdSetV26Q1Request.md)| the ad sets to create | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResponseReadAdSetV26Q1**](../Model/ResponseReadAdSetV26Q1.md)

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
createCampaign($create_campaign_request): \criteo\api\marketingsolutions\experimental\Model\CampaignV23Q1Response
```

/experimental/marketing-solutions/campaigns

Create the specified campaign                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$create_campaign_request = new \criteo\api\marketingsolutions\experimental\Model\CreateCampaignRequest(); // \criteo\api\marketingsolutions\experimental\Model\CreateCampaignRequest | the campaigns to create

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
| **create_campaign_request** | [**\criteo\api\marketingsolutions\experimental\Model\CreateCampaignRequest**](../Model/CreateCampaignRequest.md)| the campaigns to create | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\CampaignV23Q1Response**](../Model/CampaignV23Q1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAdvertiserBundleRules()`

```php
deleteAdvertiserBundleRules($advertiser_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Removes some bundles from the current list of targeted bundles for a given advertiser.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to delete from the list

try {
    $result = $apiInstance->deleteAdvertiserBundleRules($advertiser_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteAdvertiserBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAdvertiserDomainRules()`

```php
deleteAdvertiserDomainRules($advertiser_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Removes some domains from the current list of targeted domains for a given advertiser.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to delete from the list

try {
    $result = $apiInstance->deleteAdvertiserDomainRules($advertiser_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteAdvertiserDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCampaignBundleRules()`

```php
deleteCampaignBundleRules($campaign_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Removes some bundles from the current list of targeted bundles for a given campaign.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to delete from the list

try {
    $result = $apiInstance->deleteCampaignBundleRules($campaign_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteCampaignBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCampaignDomainRules()`

```php
deleteCampaignDomainRules($campaign_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/domain-rules

Removes some domains from the current list of targeted domains for a given campaign.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to delete from the list

try {
    $result = $apiInstance->deleteCampaignDomainRules($campaign_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->deleteCampaignDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to delete from the list | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `disableAdSetTargetingDealIds()`

```php
disableAdSetTargetingDealIds($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\AdSetTargetingDealIdsDisableResultResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids/disable

Disable the Deal Id Targeting configuration for the ad set whose id is specified

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set

try {
    $result = $apiInstance->disableAdSetTargetingDealIds($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->disableAdSetTargetingDealIds: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetTargetingDealIdsDisableResultResponse**](../Model/AdSetTargetingDealIdsDisableResultResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `disableAdSetTargetingVideoPositioning()`

```php
disableAdSetTargetingVideoPositioning($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\AdSetTargetingVideoPositioningDisableResultResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positionings/disable

Disable the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set

try {
    $result = $apiInstance->disableAdSetTargetingVideoPositioning($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->disableAdSetTargetingVideoPositioning: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetTargetingVideoPositioningDisableResultResponse**](../Model/AdSetTargetingVideoPositioningDisableResultResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdSet()`

```php
getAdSet($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\ResponseReadAdSetV26Q1
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}

Get the data for the specified ad set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResponseReadAdSetV26Q1**](../Model/ResponseReadAdSetV26Q1.md)

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
getAdSetCategoryBids($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\AdSetCategoryBidListResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Get the Category Bids for all valid Categories associated to an Ad Set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\AdSetCategoryBidListResponse**](../Model/AdSetCategoryBidListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdSetTargetingDealIds()`

```php
getAdSetTargetingDealIds($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\AdSetTargetingDealIdsResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids

Get the Deal Id Targeting configuration for the ad set whose id is specified

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set

try {
    $result = $apiInstance->getAdSetTargetingDealIds($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAdSetTargetingDealIds: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetTargetingDealIdsResponse**](../Model/AdSetTargetingDealIdsResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdSetTargetingVideoPositioning()`

```php
getAdSetTargetingVideoPositioning($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\AdSetTargetingVideoPositioningResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning

Get the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set

try {
    $result = $apiInstance->getAdSetTargetingVideoPositioning($ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAdSetTargetingVideoPositioning: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetTargetingVideoPositioningResponse**](../Model/AdSetTargetingVideoPositioningResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserBundleRules()`

```php
getAdvertiserBundleRules($advertiser_id): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Returns a list of all targeted bundles for an advertiser.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id

try {
    $result = $apiInstance->getAdvertiserBundleRules($advertiser_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAdvertiserBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserDomainRules()`

```php
getAdvertiserDomainRules($advertiser_id): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Returns a list of all targeted domains for an advertiser.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id

try {
    $result = $apiInstance->getAdvertiserDomainRules($advertiser_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getAdvertiserDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

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
getCampaign($campaign_id): \criteo\api\marketingsolutions\experimental\Model\CampaignV23Q1Response
```

/experimental/marketing-solutions/campaigns/{campaign-id}

Get the data for the specified campaign.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\CampaignV23Q1Response**](../Model/CampaignV23Q1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaignBundleRules()`

```php
getCampaignBundleRules($campaign_id): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Returns a list of all targeted bundles for a campaign.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id

try {
    $result = $apiInstance->getCampaignBundleRules($campaign_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCampaignBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaignDomainRules()`

```php
getCampaignDomainRules($campaign_id): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/domain-rules

Returns a list of all targeted domains for a campaign.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id

try {
    $result = $apiInstance->getCampaignDomainRules($campaign_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getCampaignDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

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
getDisplayMultipliers($ad_set_id): \criteo\api\marketingsolutions\experimental\Model\AdSetDisplayMultiplierListResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Get the Display Multipliers for all valid Categories associated to an Ad Set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\AdSetDisplayMultiplierListResponse**](../Model/AdSetDisplayMultiplierListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getSupplyVendorList()`

```php
getSupplyVendorList(): \criteo\api\marketingsolutions\experimental\Model\SupplyVendorListResponse
```

/experimental/marketing-solutions/ad-sets/targeting/supply-vendors

Fetch the list of available supply vendors for any Ad Set targetings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getSupplyVendorList();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->getSupplyVendorList: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\SupplyVendorListResponse**](../Model/SupplyVendorListResponse.md)

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
patchAdSetCategoryBids($ad_set_id, $patch_ad_set_category_bid_list_request): \criteo\api\marketingsolutions\experimental\Model\PatchAdSetCategoryBidResultListResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/category-bids

Update the Category Bids for given Categories associated to an Ad Set  Patch Category Bids for one or more Categories in a single request. Partial success policy is followed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set
$patch_ad_set_category_bid_list_request = new \criteo\api\marketingsolutions\experimental\Model\PatchAdSetCategoryBidListRequest(); // \criteo\api\marketingsolutions\experimental\Model\PatchAdSetCategoryBidListRequest | Collection of category bids to update

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
| **patch_ad_set_category_bid_list_request** | [**\criteo\api\marketingsolutions\experimental\Model\PatchAdSetCategoryBidListRequest**](../Model/PatchAdSetCategoryBidListRequest.md)| Collection of category bids to update | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\PatchAdSetCategoryBidResultListResponse**](../Model/PatchAdSetCategoryBidResultListResponse.md)

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
patchAdSets($requests_patch_ad_set_v26_q1): \criteo\api\marketingsolutions\experimental\Model\ResponsesAdSetIdV26Q1
```

/experimental/marketing-solutions/ad-sets

Patch a list of AdSets.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requests_patch_ad_set_v26_q1 = new \criteo\api\marketingsolutions\experimental\Model\RequestsPatchAdSetV26Q1(); // \criteo\api\marketingsolutions\experimental\Model\RequestsPatchAdSetV26Q1 | List of adsets to patch.

try {
    $result = $apiInstance->patchAdSets($requests_patch_ad_set_v26_q1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->patchAdSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **requests_patch_ad_set_v26_q1** | [**\criteo\api\marketingsolutions\experimental\Model\RequestsPatchAdSetV26Q1**](../Model/RequestsPatchAdSetV26Q1.md)| List of adsets to patch. | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResponsesAdSetIdV26Q1**](../Model/ResponsesAdSetIdV26Q1.md)

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
patchCampaigns($patch_campaign_list_request): \criteo\api\marketingsolutions\experimental\Model\PatchResultCampaignListResponse
```

/experimental/marketing-solutions/campaigns

Patch a list of Campaigns.                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$patch_campaign_list_request = new \criteo\api\marketingsolutions\experimental\Model\PatchCampaignListRequest(); // \criteo\api\marketingsolutions\experimental\Model\PatchCampaignListRequest | List of campaigns to patch.

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
| **patch_campaign_list_request** | [**\criteo\api\marketingsolutions\experimental\Model\PatchCampaignListRequest**](../Model/PatchCampaignListRequest.md)| List of campaigns to patch. | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\PatchResultCampaignListResponse**](../Model/PatchResultCampaignListResponse.md)

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
patchDisplayMultipliers($ad_set_id, $patch_ad_set_display_multiplier_list_request): \criteo\api\marketingsolutions\experimental\Model\PatchAdSetDisplayMultiplierResultListResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/display-multipliers

Update the Display Multipliers for given Categories associated to an Ad Set  Patch Display Multipliers for one or more Categories in a single request. Partial success policy is followed.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set
$patch_ad_set_display_multiplier_list_request = new \criteo\api\marketingsolutions\experimental\Model\PatchAdSetDisplayMultiplierListRequest(); // \criteo\api\marketingsolutions\experimental\Model\PatchAdSetDisplayMultiplierListRequest | List of display multiplier values to change

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
| **patch_ad_set_display_multiplier_list_request** | [**\criteo\api\marketingsolutions\experimental\Model\PatchAdSetDisplayMultiplierListRequest**](../Model/PatchAdSetDisplayMultiplierListRequest.md)| List of display multiplier values to change | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\PatchAdSetDisplayMultiplierResultListResponse**](../Model/PatchAdSetDisplayMultiplierResultListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postAdvertiserBundleRules()`

```php
postAdvertiserBundleRules($advertiser_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Inserts a list of targeted bundles for an advertiser and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Description of the targeting rule to setup

try {
    $result = $apiInstance->postAdvertiserBundleRules($advertiser_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->postAdvertiserBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postAdvertiserDomainRules()`

```php
postAdvertiserDomainRules($advertiser_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Inserts a list of targeted domains for an advertiser and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Description of the targeting rule to setup

try {
    $result = $apiInstance->postAdvertiserDomainRules($advertiser_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->postAdvertiserDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postCampaignBundleRules()`

```php
postCampaignBundleRules($campaign_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Inserts a list of targeted bundles for a campaign and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Description of the targeting rule to setup

try {
    $result = $apiInstance->postCampaignBundleRules($campaign_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->postCampaignBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postCampaignDomainRules()`

```php
postCampaignDomainRules($campaign_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/domain-rules

Inserts a list of targeted domains for a campaign and sets the targeting mode : blocklisting or allowlisting.<br />  It will replace the current list if any.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Description of the targeting rule to setup

try {
    $result = $apiInstance->postCampaignDomainRules($campaign_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->postCampaignDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Description of the targeting rule to setup | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putAdvertiserBundleRules()`

```php
putAdvertiserBundleRules($advertiser_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/bundle-rules

Updates the targeted bundles for an advertiser by adding a list of bundles to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list

try {
    $result = $apiInstance->putAdvertiserBundleRules($advertiser_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putAdvertiserBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putAdvertiserDomainRules()`

```php
putAdvertiserDomainRules($advertiser_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/advertisers/{advertiserId}/targeting/domain-rules

Updates the targeted domains for an advertiser by adding a list of domains to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list

try {
    $result = $apiInstance->putAdvertiserDomainRules($advertiser_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putAdvertiserDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putCampaignBundleRules()`

```php
putCampaignBundleRules($campaign_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/bundle-rules

Updates the targeted bundles for a campaign by adding a list of bundles to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list

try {
    $result = $apiInstance->putCampaignBundleRules($campaign_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putCampaignBundleRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `putCampaignDomainRules()`

```php
putCampaignDomainRules($campaign_id, $api_request_of_targeting_entity): \criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity
```

/experimental/campaigns/{campaignId}/targeting/domain-rules

Updates the targeted domains for a campaign by adding a list of domains to the current list.<br />  The mode of targeting (allowlist/blocklist) cannot be updated through this method.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_id = 'campaign_id_example'; // string | The campaign id
$api_request_of_targeting_entity = new \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity(); // \criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity | Contains the list of items to add to the existing list

try {
    $result = $apiInstance->putCampaignDomainRules($campaign_id, $api_request_of_targeting_entity);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->putCampaignDomainRules: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **campaign_id** | **string**| The campaign id | |
| **api_request_of_targeting_entity** | [**\criteo\api\marketingsolutions\experimental\Model\ApiRequestOfTargetingEntity**](../Model/ApiRequestOfTargetingEntity.md)| Contains the list of items to add to the existing list | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ApiResponseOfTargetingEntity**](../Model/ApiResponseOfTargetingEntity.md)

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
searchAdSets($ad_set_search_request_v26_q1): \criteo\api\marketingsolutions\experimental\Model\ResponsesReadAdSetV26Q1
```

/experimental/marketing-solutions/ad-sets/search

Search for ad sets based on provided criteria.  This returns the full configuration of ad sets matching those criteria.  Field projection can be used if only a subset of fields is required, instead of the full configuration.                If specific fields are precised in the user prompt, use meta.fields field projection in order to query only the value of these fields, else, provide every field.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_search_request_v26_q1 = new \criteo\api\marketingsolutions\experimental\Model\AdSetSearchRequestV26Q1(); // \criteo\api\marketingsolutions\experimental\Model\AdSetSearchRequestV26Q1

try {
    $result = $apiInstance->searchAdSets($ad_set_search_request_v26_q1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->searchAdSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_search_request_v26_q1** | [**\criteo\api\marketingsolutions\experimental\Model\AdSetSearchRequestV26Q1**](../Model/AdSetSearchRequestV26Q1.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResponsesReadAdSetV26Q1**](../Model/ResponsesReadAdSetV26Q1.md)

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
searchCampaigns($campaign_search_request_v23_q1): \criteo\api\marketingsolutions\experimental\Model\CampaignV23Q1ListResponse
```

/experimental/marketing-solutions/campaigns/search

Search endpoint for campaigns                A campaign, or in other words a marketing campaign, is an entity that defines advertising objectives and success criteria.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$campaign_search_request_v23_q1 = new \criteo\api\marketingsolutions\experimental\Model\CampaignSearchRequestV23Q1(); // \criteo\api\marketingsolutions\experimental\Model\CampaignSearchRequestV23Q1 | Filters for searching for campaigns

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
| **campaign_search_request_v23_q1** | [**\criteo\api\marketingsolutions\experimental\Model\CampaignSearchRequestV23Q1**](../Model/CampaignSearchRequestV23Q1.md)| Filters for searching for campaigns | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\CampaignV23Q1ListResponse**](../Model/CampaignV23Q1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `setAdSetTargetingDealIds()`

```php
setAdSetTargetingDealIds($ad_set_id, $set_ad_set_targeting_deal_ids_request): \criteo\api\marketingsolutions\experimental\Model\AdSetTargetingDealIdsSetResultResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/deal-ids

Set the Deal Id Targeting configuration for the ad set whose id is specified

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set
$set_ad_set_targeting_deal_ids_request = new \criteo\api\marketingsolutions\experimental\Model\SetAdSetTargetingDealIdsRequest(); // \criteo\api\marketingsolutions\experimental\Model\SetAdSetTargetingDealIdsRequest | the new Deal Id Targeting configuration

try {
    $result = $apiInstance->setAdSetTargetingDealIds($ad_set_id, $set_ad_set_targeting_deal_ids_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->setAdSetTargetingDealIds: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |
| **set_ad_set_targeting_deal_ids_request** | [**\criteo\api\marketingsolutions\experimental\Model\SetAdSetTargetingDealIdsRequest**](../Model/SetAdSetTargetingDealIdsRequest.md)| the new Deal Id Targeting configuration | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetTargetingDealIdsSetResultResponse**](../Model/AdSetTargetingDealIdsSetResultResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `setAdSetTargetingVideoPositioning()`

```php
setAdSetTargetingVideoPositioning($ad_set_id, $set_ad_set_targeting_video_positioning_request): \criteo\api\marketingsolutions\experimental\Model\AdSetTargetingVideoPositioningSetResultResponse
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/targeting/video-positioning

Set the Video Positioning Targeting configuration for the ad set whose id is specified

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | Id of the Ad Set
$set_ad_set_targeting_video_positioning_request = new \criteo\api\marketingsolutions\experimental\Model\SetAdSetTargetingVideoPositioningRequest(); // \criteo\api\marketingsolutions\experimental\Model\SetAdSetTargetingVideoPositioningRequest | the new Video Positioning Targeting configuration

try {
    $result = $apiInstance->setAdSetTargetingVideoPositioning($ad_set_id, $set_ad_set_targeting_video_positioning_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CampaignApi->setAdSetTargetingVideoPositioning: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_set_id** | **string**| Id of the Ad Set | |
| **set_ad_set_targeting_video_positioning_request** | [**\criteo\api\marketingsolutions\experimental\Model\SetAdSetTargetingVideoPositioningRequest**](../Model/SetAdSetTargetingVideoPositioningRequest.md)| the new Video Positioning Targeting configuration | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetTargetingVideoPositioningSetResultResponse**](../Model/AdSetTargetingVideoPositioningSetResultResponse.md)

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
startAdSets($requests_ad_set_id): \criteo\api\marketingsolutions\experimental\Model\ResponsesAdSetId
```

/experimental/marketing-solutions/ad-sets/start

Start the specified list of ad sets

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requests_ad_set_id = new \criteo\api\marketingsolutions\experimental\Model\RequestsAdSetId(); // \criteo\api\marketingsolutions\experimental\Model\RequestsAdSetId | All the ad sets to start

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
| **requests_ad_set_id** | [**\criteo\api\marketingsolutions\experimental\Model\RequestsAdSetId**](../Model/RequestsAdSetId.md)| All the ad sets to start | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResponsesAdSetId**](../Model/ResponsesAdSetId.md)

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
stopAdSets($requests_ad_set_id): \criteo\api\marketingsolutions\experimental\Model\ResponsesAdSetId
```

/experimental/marketing-solutions/ad-sets/stop

Stop the specified list of ad sets

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$requests_ad_set_id = new \criteo\api\marketingsolutions\experimental\Model\RequestsAdSetId(); // \criteo\api\marketingsolutions\experimental\Model\RequestsAdSetId | All the ad sets to stop

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
| **requests_ad_set_id** | [**\criteo\api\marketingsolutions\experimental\Model\RequestsAdSetId**](../Model/RequestsAdSetId.md)| All the ad sets to stop | [optional] |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResponsesAdSetId**](../Model/ResponsesAdSetId.md)

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
updateAdSetAudience($ad_set_id, $ad_set_audience_link_input_entity_v1): \criteo\api\marketingsolutions\experimental\Model\AdSetAudienceLinkEntityV1Response
```

/experimental/marketing-solutions/ad-sets/{ad-set-id}/audience

Link or unlink an audience with an ad set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CampaignApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_set_id = 'ad_set_id_example'; // string | The ad set ID.
$ad_set_audience_link_input_entity_v1 = new \criteo\api\marketingsolutions\experimental\Model\AdSetAudienceLinkInputEntityV1(); // \criteo\api\marketingsolutions\experimental\Model\AdSetAudienceLinkInputEntityV1 | Ad set-Audience update request.

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
| **ad_set_audience_link_input_entity_v1** | [**\criteo\api\marketingsolutions\experimental\Model\AdSetAudienceLinkInputEntityV1**](../Model/AdSetAudienceLinkInputEntityV1.md)| Ad set-Audience update request. | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\AdSetAudienceLinkEntityV1Response**](../Model/AdSetAudienceLinkEntityV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
