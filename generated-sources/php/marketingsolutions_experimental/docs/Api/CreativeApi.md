# criteo\api\marketingsolutions\experimental\CreativeApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createAdvertiserAd()**](CreativeApi.md#createAdvertiserAd) | **POST** /experimental/advertisers/{advertiser-id}/ads | /experimental/advertisers/{advertiser-id}/ads |
| [**createAdvertiserCoupon()**](CreativeApi.md#createAdvertiserCoupon) | **POST** /experimental/advertisers/{advertiser-id}/coupons | /experimental/advertisers/{advertiser-id}/coupons |
| [**createAdvertiserCreative()**](CreativeApi.md#createAdvertiserCreative) | **POST** /experimental/advertisers/{advertiser-id}/creatives | /experimental/advertisers/{advertiser-id}/creatives |
| [**deleteAd()**](CreativeApi.md#deleteAd) | **DELETE** /experimental/ads/{id} | /experimental/ads/{id} |
| [**deleteAdSegmentLink()**](CreativeApi.md#deleteAdSegmentLink) | **DELETE** /experimental/marketing-solutions/ads/{ad-id}/audience-segment | /experimental/marketing-solutions/ads/{ad-id}/audience-segment |
| [**deleteAdvertiserCoupon()**](CreativeApi.md#deleteAdvertiserCoupon) | **DELETE** /experimental/advertisers/{advertiser-id}/coupons/{id} | /experimental/advertisers/{advertiser-id}/coupons/{id} |
| [**deleteCreative()**](CreativeApi.md#deleteCreative) | **DELETE** /experimental/creatives/{id} | /experimental/creatives/{id} |
| [**editAdvertiserCoupon()**](CreativeApi.md#editAdvertiserCoupon) | **PUT** /experimental/advertisers/{advertiser-id}/coupons/{id} | /experimental/advertisers/{advertiser-id}/coupons/{id} |
| [**editCreative()**](CreativeApi.md#editCreative) | **PUT** /experimental/creatives/{id} | /experimental/creatives/{id} |
| [**generateCreativePreview()**](CreativeApi.md#generateCreativePreview) | **POST** /experimental/creatives/{id}/preview | /experimental/creatives/{id}/preview |
| [**getAd()**](CreativeApi.md#getAd) | **GET** /experimental/ads/{id} | /experimental/ads/{id} |
| [**getAdSegmentLink()**](CreativeApi.md#getAdSegmentLink) | **GET** /experimental/marketing-solutions/ads/{ad-id}/audience-segment | /experimental/marketing-solutions/ads/{ad-id}/audience-segment |
| [**getAdvertiserAds()**](CreativeApi.md#getAdvertiserAds) | **GET** /experimental/advertisers/{advertiser-id}/ads | /experimental/advertisers/{advertiser-id}/ads |
| [**getAdvertiserCoupon()**](CreativeApi.md#getAdvertiserCoupon) | **GET** /experimental/advertisers/{advertiser-id}/coupons/{id} | /experimental/advertisers/{advertiser-id}/coupons/{id} |
| [**getAdvertiserCouponPreview()**](CreativeApi.md#getAdvertiserCouponPreview) | **GET** /experimental/advertisers/{advertiser-id}/coupons/{id}/preview | /experimental/advertisers/{advertiser-id}/coupons/{id}/preview |
| [**getAdvertiserCouponSupportedSizes()**](CreativeApi.md#getAdvertiserCouponSupportedSizes) | **GET** /experimental/advertisers/{advertiser-id}/coupons-supported-sizes | /experimental/advertisers/{advertiser-id}/coupons-supported-sizes |
| [**getAdvertiserCoupons()**](CreativeApi.md#getAdvertiserCoupons) | **GET** /experimental/advertisers/{advertiser-id}/coupons | /experimental/advertisers/{advertiser-id}/coupons |
| [**getAdvertiserCreatives()**](CreativeApi.md#getAdvertiserCreatives) | **GET** /experimental/advertisers/{advertiser-id}/creatives | /experimental/advertisers/{advertiser-id}/creatives |
| [**getCreative()**](CreativeApi.md#getCreative) | **GET** /experimental/creatives/{id} | /experimental/creatives/{id} |
| [**linkAdSegment()**](CreativeApi.md#linkAdSegment) | **PUT** /experimental/marketing-solutions/ads/{ad-id}/audience-segment | /experimental/marketing-solutions/ads/{ad-id}/audience-segment |


## `createAdvertiserAd()`

```php
createAdvertiserAd($advertiser_id, $resource_input_of_ad_write): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfAd
```

/experimental/advertisers/{advertiser-id}/ads

Create an Ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$resource_input_of_ad_write = new \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfAdWrite(); // \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfAdWrite

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
| **resource_input_of_ad_write** | [**\criteo\api\marketingsolutions\experimental\Model\ResourceInputOfAdWrite**](../Model/ResourceInputOfAdWrite.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfAd**](../Model/ResourceOutcomeOfAd.md)

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
createAdvertiserCoupon($advertiser_id, $resource_input_of_create_coupon): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCoupon
```

/experimental/advertisers/{advertiser-id}/coupons

Create a Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$resource_input_of_create_coupon = new \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreateCoupon(); // \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreateCoupon

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
| **resource_input_of_create_coupon** | [**\criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreateCoupon**](../Model/ResourceInputOfCreateCoupon.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCoupon**](../Model/ResourceOutcomeOfCoupon.md)

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
createAdvertiserCreative($advertiser_id, $resource_input_of_creative_write): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCreative
```

/experimental/advertisers/{advertiser-id}/creatives

Create a Creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$resource_input_of_creative_write = new \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreativeWrite(); // \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreativeWrite

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
| **resource_input_of_creative_write** | [**\criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreativeWrite**](../Model/ResourceInputOfCreativeWrite.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCreative**](../Model/ResourceOutcomeOfCreative.md)

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

/experimental/ads/{id}

Delete an Ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

## `deleteAdSegmentLink()`

```php
deleteAdSegmentLink($ad_id)
```

/experimental/marketing-solutions/ads/{ad-id}/audience-segment

Delete the link between an Ad and an Audience Segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_id = 'ad_id_example'; // string | The ad identifier.

try {
    $apiInstance->deleteAdSegmentLink($ad_id);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->deleteAdSegmentLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_id** | **string**| The ad identifier. | |

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

/experimental/advertisers/{advertiser-id}/coupons/{id}

Delete a Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

/experimental/creatives/{id}

Delete a Creative if there are no ads binded to it

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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
editAdvertiserCoupon($advertiser_id, $id, $resource_input_of_update_coupon): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCoupon
```

/experimental/advertisers/{advertiser-id}/coupons/{id}

Edit a specific Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser identifier.
$id = 'id_example'; // string | The Coupon identifier to edit.
$resource_input_of_update_coupon = new \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfUpdateCoupon(); // \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfUpdateCoupon

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
| **resource_input_of_update_coupon** | [**\criteo\api\marketingsolutions\experimental\Model\ResourceInputOfUpdateCoupon**](../Model/ResourceInputOfUpdateCoupon.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCoupon**](../Model/ResourceOutcomeOfCoupon.md)

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
editCreative($id, $resource_input_of_creative_write): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCreative
```

/experimental/creatives/{id}

Edit a specific Creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | The creative identifier to edit.
$resource_input_of_creative_write = new \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreativeWrite(); // \criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreativeWrite

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
| **resource_input_of_creative_write** | [**\criteo\api\marketingsolutions\experimental\Model\ResourceInputOfCreativeWrite**](../Model/ResourceInputOfCreativeWrite.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCreative**](../Model/ResourceOutcomeOfCreative.md)

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

/experimental/creatives/{id}/preview

Get the preview of a specific Creative

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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
getAd($id): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfAd
```

/experimental/ads/{id}

Get an Ad with its id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfAd**](../Model/ResourceOutcomeOfAd.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAdSegmentLink()`

```php
getAdSegmentLink($ad_id): \criteo\api\marketingsolutions\experimental\Model\ValueResourceOutcomeOfExamAdAudienceSegmentLink
```

/experimental/marketing-solutions/ads/{ad-id}/audience-segment

Retrieve the Ad audience segment link.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_id = 'ad_id_example'; // string | The ad identifier.

try {
    $result = $apiInstance->getAdSegmentLink($ad_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->getAdSegmentLink: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_id** | **string**| The ad identifier. | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ValueResourceOutcomeOfExamAdAudienceSegmentLink**](../Model/ValueResourceOutcomeOfExamAdAudienceSegmentLink.md)

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
getAdvertiserAds($advertiser_id, $limit, $offset): \criteo\api\marketingsolutions\experimental\Model\ResourceCollectionOutcomeOfAd
```

/experimental/advertisers/{advertiser-id}/ads

Get the list of self-services Ads for a given advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceCollectionOutcomeOfAd**](../Model/ResourceCollectionOutcomeOfAd.md)

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
getAdvertiserCoupon($advertiser_id, $id): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCoupon
```

/experimental/advertisers/{advertiser-id}/coupons/{id}

Get a Coupon with its id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCoupon**](../Model/ResourceOutcomeOfCoupon.md)

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

/experimental/advertisers/{advertiser-id}/coupons/{id}/preview

Get the preview of a specific Coupon

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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
getAdvertiserCouponSupportedSizes($advertiser_id, $ad_set_id): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCouponSupportedSizes
```

/experimental/advertisers/{advertiser-id}/coupons-supported-sizes

Get the list of Coupon supported sizes

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCouponSupportedSizes**](../Model/ResourceOutcomeOfCouponSupportedSizes.md)

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
getAdvertiserCoupons($advertiser_id, $limit, $offset): \criteo\api\marketingsolutions\experimental\Model\ResourceCollectionOutcomeOfCoupon
```

/experimental/advertisers/{advertiser-id}/coupons

Get the list of self-services Coupons for a given advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceCollectionOutcomeOfCoupon**](../Model/ResourceCollectionOutcomeOfCoupon.md)

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
getAdvertiserCreatives($advertiser_id, $limit, $offset): \criteo\api\marketingsolutions\experimental\Model\ResourceCollectionOutcomeOfCreativeRead
```

/experimental/advertisers/{advertiser-id}/creatives

Get the list of self-services Creatives for a given advertiser

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceCollectionOutcomeOfCreativeRead**](../Model/ResourceCollectionOutcomeOfCreativeRead.md)

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
getCreative($id): \criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCreative
```

/experimental/creatives/{id}

Get a Creative with its id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
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

[**\criteo\api\marketingsolutions\experimental\Model\ResourceOutcomeOfCreative**](../Model/ResourceOutcomeOfCreative.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `linkAdSegment()`

```php
linkAdSegment($ad_id, $exam_ad_audience_segment_link_input): \criteo\api\marketingsolutions\experimental\Model\ValueResourceOutcomeOfExamAdAudienceSegmentLink
```

/experimental/marketing-solutions/ads/{ad-id}/audience-segment

Link an Ad with an Audience Segment. If a link already exists, its segment ID will be updated.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\experimental\Api\CreativeApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_id = 'ad_id_example'; // string | The ad identifier.
$exam_ad_audience_segment_link_input = new \criteo\api\marketingsolutions\experimental\Model\ExamAdAudienceSegmentLinkInput(); // \criteo\api\marketingsolutions\experimental\Model\ExamAdAudienceSegmentLinkInput | The audience segment link information.

try {
    $result = $apiInstance->linkAdSegment($ad_id, $exam_ad_audience_segment_link_input);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CreativeApi->linkAdSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_id** | **string**| The ad identifier. | |
| **exam_ad_audience_segment_link_input** | [**\criteo\api\marketingsolutions\experimental\Model\ExamAdAudienceSegmentLinkInput**](../Model/ExamAdAudienceSegmentLinkInput.md)| The audience segment link information. | |

### Return type

[**\criteo\api\marketingsolutions\experimental\Model\ValueResourceOutcomeOfExamAdAudienceSegmentLink**](../Model/ValueResourceOutcomeOfExamAdAudienceSegmentLink.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
