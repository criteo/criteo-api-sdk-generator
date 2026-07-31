# criteo\api\marketingsolutions\v2026_01\RecoApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createProductSet()**](RecoApi.md#createProductSet) | **POST** /2026-01/marketing-solutions/product-sets | /2026-01/marketing-solutions/product-sets |
| [**disableProductFiltering()**](RecoApi.md#disableProductFiltering) | **DELETE** /2026-01/marketing-solutions/ads/{ad-id}/product-filter | /2026-01/marketing-solutions/ads/{ad-id}/product-filter |
| [**enableProductFiltering()**](RecoApi.md#enableProductFiltering) | **POST** /2026-01/marketing-solutions/ads/{ad-id}/product-filter | /2026-01/marketing-solutions/ads/{ad-id}/product-filter |
| [**fetchProductFilteringConfig()**](RecoApi.md#fetchProductFilteringConfig) | **GET** /2026-01/marketing-solutions/ads/{ad-id}/product-filter | /2026-01/marketing-solutions/ads/{ad-id}/product-filter |
| [**fetchProductFilteringUsages()**](RecoApi.md#fetchProductFilteringUsages) | **GET** /2026-01/marketing-solutions/product-sets/{product-set-id}/product-filters | /2026-01/marketing-solutions/product-sets/{product-set-id}/product-filters |
| [**fetchProductSet()**](RecoApi.md#fetchProductSet) | **GET** /2026-01/marketing-solutions/product-sets/{product-set-id} | /2026-01/marketing-solutions/product-sets/{product-set-id} |
| [**fetchProductSets()**](RecoApi.md#fetchProductSets) | **GET** /2026-01/marketing-solutions/product-sets/dataset/{dataset-id} | /2026-01/marketing-solutions/product-sets/dataset/{dataset-id} |
| [**patchProductSet()**](RecoApi.md#patchProductSet) | **PATCH** /2026-01/marketing-solutions/product-sets/{product-set-id} | /2026-01/marketing-solutions/product-sets/{product-set-id} |
| [**removeProductSet()**](RecoApi.md#removeProductSet) | **DELETE** /2026-01/marketing-solutions/product-sets/{product-set-id} | /2026-01/marketing-solutions/product-sets/{product-set-id} |


## `createProductSet()`

```php
createProductSet($value_resource_input_of_create_product_set_request): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfProductSet
```

/2026-01/marketing-solutions/product-sets

Create a new product set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$value_resource_input_of_create_product_set_request = new \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfCreateProductSetRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfCreateProductSetRequest

try {
    $result = $apiInstance->createProductSet($value_resource_input_of_create_product_set_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->createProductSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **value_resource_input_of_create_product_set_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfCreateProductSetRequest**](../Model/ValueResourceInputOfCreateProductSetRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfProductSet**](../Model/ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `disableProductFiltering()`

```php
disableProductFiltering($ad_id): \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceOutcomeOfProductFilterConfig
```

/2026-01/marketing-solutions/ads/{ad-id}/product-filter

Disable product filtering for a given ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_id = 'ad_id_example'; // string | ID of the ad

try {
    $result = $apiInstance->disableProductFiltering($ad_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->disableProductFiltering: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_id** | **string**| ID of the ad | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceOutcomeOfProductFilterConfig**](../Model/ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `enableProductFiltering()`

```php
enableProductFiltering($ad_id, $value_resource_input_of_create_product_filter_request): \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceOutcomeOfProductFilterConfig
```

/2026-01/marketing-solutions/ads/{ad-id}/product-filter

Enable product filtering for a given ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_id = 'ad_id_example'; // string | ID of the ad
$value_resource_input_of_create_product_filter_request = new \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfCreateProductFilterRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfCreateProductFilterRequest

try {
    $result = $apiInstance->enableProductFiltering($ad_id, $value_resource_input_of_create_product_filter_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->enableProductFiltering: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_id** | **string**| ID of the ad | |
| **value_resource_input_of_create_product_filter_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfCreateProductFilterRequest**](../Model/ValueResourceInputOfCreateProductFilterRequest.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceOutcomeOfProductFilterConfig**](../Model/ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `fetchProductFilteringConfig()`

```php
fetchProductFilteringConfig($ad_id): \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceOutcomeOfProductFilterConfig
```

/2026-01/marketing-solutions/ads/{ad-id}/product-filter

Fetch product filtering configuration for a given ad

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$ad_id = 'ad_id_example'; // string | ID of the ad

try {
    $result = $apiInstance->fetchProductFilteringConfig($ad_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->fetchProductFilteringConfig: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ad_id** | **string**| ID of the ad | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceOutcomeOfProductFilterConfig**](../Model/ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `fetchProductFilteringUsages()`

```php
fetchProductFilteringUsages($product_set_id): \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceCollectionOutcomeOfProductFilterConfig
```

/2026-01/marketing-solutions/product-sets/{product-set-id}/product-filters

Fetch product filtering usages for a given product set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_set_id = 'product_set_id_example'; // string | ID of the product set

try {
    $result = $apiInstance->fetchProductFilteringUsages($product_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->fetchProductFilteringUsages: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **product_set_id** | **string**| ID of the product set | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceCollectionOutcomeOfProductFilterConfig**](../Model/ValueResourceCollectionOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `fetchProductSet()`

```php
fetchProductSet($product_set_id): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfProductSet
```

/2026-01/marketing-solutions/product-sets/{product-set-id}

Fetch an existing product set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_set_id = 'product_set_id_example'; // string | ID of the product set

try {
    $result = $apiInstance->fetchProductSet($product_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->fetchProductSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **product_set_id** | **string**| ID of the product set | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfProductSet**](../Model/ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `fetchProductSets()`

```php
fetchProductSets($dataset_id): \criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfProductSet
```

/2026-01/marketing-solutions/product-sets/dataset/{dataset-id}

Fetch product sets of a given dataset

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$dataset_id = 'dataset_id_example'; // string | The ID of the dataset that should be used for product set retrieval

try {
    $result = $apiInstance->fetchProductSets($dataset_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->fetchProductSets: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **dataset_id** | **string**| The ID of the dataset that should be used for product set retrieval | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceCollectionOutcomeOfProductSet**](../Model/ResourceCollectionOutcomeOfProductSet.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `patchProductSet()`

```php
patchProductSet($product_set_id, $value_resource_input_of_patch_product_set_request): \criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfProductSet
```

/2026-01/marketing-solutions/product-sets/{product-set-id}

Patch an existing product set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_set_id = 'product_set_id_example'; // string | ID of the product set
$value_resource_input_of_patch_product_set_request = new \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfPatchProductSetRequest(); // \criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfPatchProductSetRequest

try {
    $result = $apiInstance->patchProductSet($product_set_id, $value_resource_input_of_patch_product_set_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->patchProductSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **product_set_id** | **string**| ID of the product set | |
| **value_resource_input_of_patch_product_set_request** | [**\criteo\api\marketingsolutions\v2026_01\Model\ValueResourceInputOfPatchProductSetRequest**](../Model/ValueResourceInputOfPatchProductSetRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\ResourceOutcomeOfProductSet**](../Model/ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `removeProductSet()`

```php
removeProductSet($product_set_id): \criteo\api\marketingsolutions\v2026_01\Model\Outcome
```

/2026-01/marketing-solutions/product-sets/{product-set-id}

Remove a product set

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_01\Api\RecoApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$product_set_id = 'product_set_id_example'; // string | ID of the product set to remove

try {
    $result = $apiInstance->removeProductSet($product_set_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecoApi->removeProductSet: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **product_set_id** | **string**| ID of the product set to remove | |

### Return type

[**\criteo\api\marketingsolutions\v2026_01\Model\Outcome**](../Model/Outcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
