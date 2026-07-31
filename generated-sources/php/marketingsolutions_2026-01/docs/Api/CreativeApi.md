# criteo\api\marketingsolutions\v2026_01\CreativeApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createAdvertiserAd()**](CreativeApi.md#createAdvertiserAd) | **POST** /2026-01/marketing-solutions/advertisers/{advertiser-id}/ads | /2026-01/marketing-solutions/advertisers/{advertiser-id}/ads |
| [**createAdvertiserCoupon()**](CreativeApi.md#createAdvertiserCoupon) | **POST** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons |
| [**createAdvertiserCreative()**](CreativeApi.md#createAdvertiserCreative) | **POST** /2026-01/marketing-solutions/advertisers/{advertiser-id}/creatives | /2026-01/marketing-solutions/advertisers/{advertiser-id}/creatives |
| [**deleteAd()**](CreativeApi.md#deleteAd) | **DELETE** /2026-01/marketing-solutions/ads/{id} | /2026-01/marketing-solutions/ads/{id} |
| [**deleteAdvertiserCoupon()**](CreativeApi.md#deleteAdvertiserCoupon) | **DELETE** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} |
| [**deleteCreative()**](CreativeApi.md#deleteCreative) | **DELETE** /2026-01/marketing-solutions/creatives/{id} | /2026-01/marketing-solutions/creatives/{id} |
| [**editAdvertiserCoupon()**](CreativeApi.md#editAdvertiserCoupon) | **PUT** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} |
| [**editCreative()**](CreativeApi.md#editCreative) | **PUT** /2026-01/marketing-solutions/creatives/{id} | /2026-01/marketing-solutions/creatives/{id} |
| [**generateCreativePreview()**](CreativeApi.md#generateCreativePreview) | **POST** /2026-01/marketing-solutions/creatives/{id}/preview | /2026-01/marketing-solutions/creatives/{id}/preview |
| [**getAd()**](CreativeApi.md#getAd) | **GET** /2026-01/marketing-solutions/ads/{id} | /2026-01/marketing-solutions/ads/{id} |
| [**getAdvertiserAds()**](CreativeApi.md#getAdvertiserAds) | **GET** /2026-01/marketing-solutions/advertisers/{advertiser-id}/ads | /2026-01/marketing-solutions/advertisers/{advertiser-id}/ads |
| [**getAdvertiserCoupon()**](CreativeApi.md#getAdvertiserCoupon) | **GET** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id} |
| [**getAdvertiserCouponPreview()**](CreativeApi.md#getAdvertiserCouponPreview) | **GET** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}/preview | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}/preview |
| [**getAdvertiserCouponSupportedSizes()**](CreativeApi.md#getAdvertiserCouponSupportedSizes) | **GET** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons-supported-sizes | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons-supported-sizes |
| [**getAdvertiserCoupons()**](CreativeApi.md#getAdvertiserCoupons) | **GET** /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons | /2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons |
| [**getAdvertiserCreatives()**](CreativeApi.md#getAdvertiserCreatives) | **GET** /2026-01/marketing-solutions/advertisers/{advertiser-id}/creatives | /2026-01/marketing-solutions/advertisers/{advertiser-id}/creatives |
| [**getCreative()**](CreativeApi.md#getCreative) | **GET** /2026-01/marketing-solutions/creatives/{id} | /2026-01/marketing-solutions/creatives/{id} |


## `createAdvertiserAd()`

```php
createAdvertiserAd($advertiser_id, $resource_input_of_ad_write): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfAd
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/ads

Create an Ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$resource_input_of_ad_write = new \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfAdWrite(); // \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfAdWrite

try {
    $result = $apiInstance->createAdvertiserAd($advertiser_id, $resource_input_of_ad_write);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->createAdvertiserAd: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **resource_input_of_ad_write** | [**\criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfAdWrite**](../Model/ResourceInputOfAdWrite.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfAd**](../Model/ResourceOutcomeOfAd.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAdvertiserCoupon()`

```php
createAdvertiserCoupon($advertiser_id, $resource_input_of_create_coupon): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCoupon
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons

Create a Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$resource_input_of_create_coupon = new \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreateCoupon(); // \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreateCoupon

try {
    $result = $apiInstance->createAdvertiserCoupon($advertiser_id, $resource_input_of_create_coupon);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->createAdvertiserCoupon: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **resource_input_of_create_coupon** | [**\criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreateCoupon**](../Model/ResourceInputOfCreateCoupon.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCoupon**](../Model/ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAdvertiserCreative()`

```php
createAdvertiserCreative($advertiser_id, $resource_input_of_creative_write): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCreative
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/creatives

Create a Creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$resource_input_of_creative_write = new \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreativeWrite(); // \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreativeWrite

try {
    $result = $apiInstance->createAdvertiserCreative($advertiser_id, $resource_input_of_creative_write);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->createAdvertiserCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **resource_input_of_creative_write** | [**\criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreativeWrite**](../Model/ResourceInputOfCreativeWrite.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCreative**](../Model/ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAd()`

```php
deleteAd($id)
```

/2026-01/marketing-solutions/ads/{id}

Delete an Ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The ad identifier to delete.

try {
    $apiInstance->deleteAd($id);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->deleteAd: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The ad identifier to delete. | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAdvertiserCoupon()`

```php
deleteAdvertiserCoupon($advertiser_id, $id)
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}

Delete a Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$id = 'id_example'; // string | The Coupon identifier to delete.

try {
    $apiInstance->deleteAdvertiserCoupon($advertiser_id, $id);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->deleteAdvertiserCoupon: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **id** | **string**| The Coupon identifier to delete. | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteCreative()`

```php
deleteCreative($id)
```

/2026-01/marketing-solutions/creatives/{id}

Delete a Creative if there are no ads binded to it

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The creative identifier to delete.

try {
    $apiInstance->deleteCreative($id);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->deleteCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The creative identifier to delete. | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `editAdvertiserCoupon()`

```php
editAdvertiserCoupon($advertiser_id, $id, $resource_input_of_update_coupon): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCoupon
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}

Edit a specific Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$id = 'id_example'; // string | The Coupon identifier to edit.
$resource_input_of_update_coupon = new \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfUpdateCoupon(); // \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfUpdateCoupon

try {
    $result = $apiInstance->editAdvertiserCoupon($advertiser_id, $id, $resource_input_of_update_coupon);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->editAdvertiserCoupon: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **id** | **string**| The Coupon identifier to edit. | |
| **resource_input_of_update_coupon** | [**\criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfUpdateCoupon**](../Model/ResourceInputOfUpdateCoupon.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCoupon**](../Model/ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `editCreative()`

```php
editCreative($id, $resource_input_of_creative_write): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCreative
```

/2026-01/marketing-solutions/creatives/{id}

Edit a specific Creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The creative identifier to edit.
$resource_input_of_creative_write = new \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreativeWrite(); // \criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreativeWrite

try {
    $result = $apiInstance->editCreative($id, $resource_input_of_creative_write);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->editCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The creative identifier to edit. | |
| **resource_input_of_creative_write** | [**\criteo\api\marketingsolutions\v2026_01\Model\ResourceInputOfCreativeWrite**](../Model/ResourceInputOfCreativeWrite.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCreative**](../Model/ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateCreativePreview()`

```php
generateCreativePreview($id, $height, $width): string
```

/2026-01/marketing-solutions/creatives/{id}/preview

Get the preview of a specific Creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The Creative identifier to preview.
$height = 56; // int | The height of the Creative to preview.
$width = 56; // int | The width of the Creative to preview.

try {
    $result = $apiInstance->generateCreativePreview($id, $height, $width);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->generateCreativePreview: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The Creative identifier to preview. | |
| **height** | **int**| The height of the Creative to preview. | [optional] |
| **width** | **int**| The width of the Creative to preview. | [optional] |

### Return type

**string**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAd()`

```php
getAd($id): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfAd
```

/2026-01/marketing-solutions/ads/{id}

Get an Ad with its id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The ad identifier to retrieve.

try {
    $result = $apiInstance->getAd($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAd: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The ad identifier to retrieve. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfAd**](../Model/ResourceOutcomeOfAd.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserAds()`

```php
getAdvertiserAds($advertiser_id, $limit, $offset): \criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfAd
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/ads

Get the list of self-services Ads for a given advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$limit = 56; // int | The number of ads to be returned. The default is 50.
$offset = 56; // int | The (zero-based) offset into the collection of ads. The default is 0.

try {
    $result = $apiInstance->getAdvertiserAds($advertiser_id, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdvertiserAds: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **limit** | **int**| The number of ads to be returned. The default is 50. | [optional] |
| **offset** | **int**| The (zero-based) offset into the collection of ads. The default is 0. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfAd**](../Model/ResourceCollectionOutcomeOfAd.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserCoupon()`

```php
getAdvertiserCoupon($advertiser_id, $id): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCoupon
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}

Get a Coupon with its id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$id = 'id_example'; // string | The Coupon identifier to retrieve.

try {
    $result = $apiInstance->getAdvertiserCoupon($advertiser_id, $id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdvertiserCoupon: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **id** | **string**| The Coupon identifier to retrieve. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCoupon**](../Model/ResourceOutcomeOfCoupon.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserCouponPreview()`

```php
getAdvertiserCouponPreview($advertiser_id, $id, $height, $width): string
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons/{id}/preview

Get the preview of a specific Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$id = 'id_example'; // string | The Coupon identifier to preview.
$height = 56; // int | The height of the coupon to preview.
$width = 56; // int | The width of the coupon to preview.

try {
    $result = $apiInstance->getAdvertiserCouponPreview($advertiser_id, $id, $height, $width);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdvertiserCouponPreview: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **id** | **string**| The Coupon identifier to preview. | |
| **height** | **int**| The height of the coupon to preview. | [optional] |
| **width** | **int**| The width of the coupon to preview. | [optional] |

### Return type

**string**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `text/html`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserCouponSupportedSizes()`

```php
getAdvertiserCouponSupportedSizes($advertiser_id, $ad_set_id): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCouponSupportedSizes
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons-supported-sizes

Get the list of Coupon supported sizes

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$ad_set_id = 'ad_set_id_example'; // string | The ad set id on which you want to check the Coupon supported sizes.

try {
    $result = $apiInstance->getAdvertiserCouponSupportedSizes($advertiser_id, $ad_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdvertiserCouponSupportedSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **ad_set_id** | **string**| The ad set id on which you want to check the Coupon supported sizes. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCouponSupportedSizes**](../Model/ResourceOutcomeOfCouponSupportedSizes.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserCoupons()`

```php
getAdvertiserCoupons($advertiser_id, $limit, $offset): \criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfCoupon
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/coupons

Get the list of self-services Coupons for a given advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$limit = 56; // int | The number of coupons to be returned. The default is 50.
$offset = 56; // int | The (zero-based) offset into the collection of coupons. The default is 0.

try {
    $result = $apiInstance->getAdvertiserCoupons($advertiser_id, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdvertiserCoupons: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **limit** | **int**| The number of coupons to be returned. The default is 50. | [optional] |
| **offset** | **int**| The (zero-based) offset into the collection of coupons. The default is 0. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfCoupon**](../Model/ResourceCollectionOutcomeOfCoupon.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdvertiserCreatives()`

```php
getAdvertiserCreatives($advertiser_id, $limit, $offset): \criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfCreativeRead
```

/2026-01/marketing-solutions/advertisers/{advertiser-id}/creatives

Get the list of self-services Creatives for a given advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$limit = 56; // int | The number of creatives to be returned. The default is 50.
$offset = 56; // int | The (zero-based) offset into the collection of creatives. The default is 0.

try {
    $result = $apiInstance->getAdvertiserCreatives($advertiser_id, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdvertiserCreatives: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser identifier. | |
| **limit** | **int**| The number of creatives to be returned. The default is 50. | [optional] |
| **offset** | **int**| The (zero-based) offset into the collection of creatives. The default is 0. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfCreativeRead**](../Model/ResourceCollectionOutcomeOfCreativeRead.md)

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
getCreative($id): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCreative
```

/2026-01/marketing-solutions/creatives/{id}

Get a Creative with its id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The creative identifier to retrieve.

try {
    $result = $apiInstance->getCreative($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getCreative: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| The creative identifier to retrieve. | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfCreative**](../Model/ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
