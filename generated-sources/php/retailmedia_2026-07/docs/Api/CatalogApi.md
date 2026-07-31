# criteo\api\retailmedia\v2026_07\CatalogApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteStoreInventoryPerMerchantId()**](CatalogApi.md#deleteStoreInventoryPerMerchantId) | **POST** /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/delete | /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/delete |
| [**upsertStoreInventoryPerMerchantId()**](CatalogApi.md#upsertStoreInventoryPerMerchantId) | **POST** /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert | /2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert |


## `deleteStoreInventoryPerMerchantId()`

```php
deleteStoreInventoryPerMerchantId($merchant_id, $batch_store_inventory_delete_request)
```

/2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/delete

Used to publish a batch of store inventories to delete. The batch is processed asynchronously.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$merchant_id = 'merchant_id_example'; // string | Identifies the merchant, can also be called partnerId
$batch_store_inventory_delete_request = new \criteo\api\retailmedia\v2026_07\Model\BatchStoreInventoryDeleteRequest(); // \criteo\api\retailmedia\v2026_07\Model\BatchStoreInventoryDeleteRequest

try {
    $apiInstance->deleteStoreInventoryPerMerchantId($merchant_id, $batch_store_inventory_delete_request);
} catch (Exception $e) {
    echo 'Exception when calling CatalogApi->deleteStoreInventoryPerMerchantId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **merchant_id** | **string**| Identifies the merchant, can also be called partnerId | |
| **batch_store_inventory_delete_request** | [**\criteo\api\retailmedia\v2026_07\Model\BatchStoreInventoryDeleteRequest**](../Model/BatchStoreInventoryDeleteRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `upsertStoreInventoryPerMerchantId()`

```php
upsertStoreInventoryPerMerchantId($merchant_id, $batch_store_inventory_request)
```

/2026-07/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert

Used to publish a batch of store inventories to upsert. The batch is processed asynchronously.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$merchant_id = 'merchant_id_example'; // string | Identifies the merchant, can also be called partnerId
$batch_store_inventory_request = new \criteo\api\retailmedia\v2026_07\Model\BatchStoreInventoryRequest(); // \criteo\api\retailmedia\v2026_07\Model\BatchStoreInventoryRequest

try {
    $apiInstance->upsertStoreInventoryPerMerchantId($merchant_id, $batch_store_inventory_request);
} catch (Exception $e) {
    echo 'Exception when calling CatalogApi->upsertStoreInventoryPerMerchantId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **merchant_id** | **string**| Identifies the merchant, can also be called partnerId | |
| **batch_store_inventory_request** | [**\criteo\api\retailmedia\v2026_07\Model\BatchStoreInventoryRequest**](../Model/BatchStoreInventoryRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
