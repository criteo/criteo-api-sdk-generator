# criteo\api\retailmedia\preview\CatalogApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteStoreInventoryPerMerchantId()**](CatalogApi.md#deleteStoreInventoryPerMerchantId) | **POST** /preview/retail-media/catalog/merchants/{merchantId}/store-inventory/delete | /preview/retail-media/catalog/merchants/{merchantId}/store-inventory/delete |
| [**getCatalogProductsBatchReport()**](CatalogApi.md#getCatalogProductsBatchReport) | **GET** /preview/retail-media/catalog/products/batch/report/{operation-token} | /preview/retail-media/catalog/products/batch/report/{operation-token} |
| [**offerSetBbwV1()**](CatalogApi.md#offerSetBbwV1) | **POST** /preview/retail-media/retailers/{retailer-id}/products/set-buy-box-winners | /preview/retail-media/retailers/{retailer-id}/products/set-buy-box-winners |
| [**offerUpdateV1()**](CatalogApi.md#offerUpdateV1) | **POST** /preview/retail-media/retailers/{retailer-id}/offers/update | /preview/retail-media/retailers/{retailer-id}/offers/update |
| [**submitCatalogProductsBatch()**](CatalogApi.md#submitCatalogProductsBatch) | **POST** /preview/retail-media/catalog/products/batch | /preview/retail-media/catalog/products/batch |
| [**upsertStoreInventoryPerMerchantId()**](CatalogApi.md#upsertStoreInventoryPerMerchantId) | **POST** /preview/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert | /preview/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert |


## `deleteStoreInventoryPerMerchantId()`

```php
deleteStoreInventoryPerMerchantId($merchant_id, $batch_store_inventory_delete_request)
```

/preview/retail-media/catalog/merchants/{merchantId}/store-inventory/delete

Used to publish a batch of store inventories to delete. The batch is processed asynchronously.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$merchant_id = 'merchant_id_example'; // string | Identifies the merchant, can also be called partnerId
$batch_store_inventory_delete_request = new \criteo\api\retailmedia\preview\Model\BatchStoreInventoryDeleteRequest(); // \criteo\api\retailmedia\preview\Model\BatchStoreInventoryDeleteRequest

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
| **batch_store_inventory_delete_request** | [**\criteo\api\retailmedia\preview\Model\BatchStoreInventoryDeleteRequest**](../Model/BatchStoreInventoryDeleteRequest.md)|  | |

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

## `getCatalogProductsBatchReport()`

```php
getCatalogProductsBatchReport($operation_token): \criteo\api\retailmedia\preview\Model\ReportOkResponse
```

/preview/retail-media/catalog/products/batch/report/{operation-token}

Get the report of an asynchronous batch operation previously requested

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$operation_token = 'operation_token_example'; // string | The token returned by the batch endpoint.

try {
    $result = $apiInstance->getCatalogProductsBatchReport($operation_token);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogApi->getCatalogProductsBatchReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **operation_token** | **string**| The token returned by the batch endpoint. | |

### Return type

[**\criteo\api\retailmedia\preview\Model\ReportOkResponse**](../Model/ReportOkResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `offerSetBbwV1()`

```php
offerSetBbwV1($retailer_id, $value_resource_input_set_product_buy_box_winners_request): \criteo\api\retailmedia\preview\Model\Outcome
```

/preview/retail-media/retailers/{retailer-id}/products/set-buy-box-winners

Update the buy box winner for one or more products

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | The retailer for which these buy box winners will be set
$value_resource_input_set_product_buy_box_winners_request = new \criteo\api\retailmedia\preview\Model\ValueResourceInputSetProductBuyBoxWinnersRequest(); // \criteo\api\retailmedia\preview\Model\ValueResourceInputSetProductBuyBoxWinnersRequest | Updated buy box winners for one or more products

try {
    $result = $apiInstance->offerSetBbwV1($retailer_id, $value_resource_input_set_product_buy_box_winners_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogApi->offerSetBbwV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| The retailer for which these buy box winners will be set | |
| **value_resource_input_set_product_buy_box_winners_request** | [**\criteo\api\retailmedia\preview\Model\ValueResourceInputSetProductBuyBoxWinnersRequest**](../Model/ValueResourceInputSetProductBuyBoxWinnersRequest.md)| Updated buy box winners for one or more products | |

### Return type

[**\criteo\api\retailmedia\preview\Model\Outcome**](../Model/Outcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `offerUpdateV1()`

```php
offerUpdateV1($retailer_id, $value_resource_input_update_offers_request): \criteo\api\retailmedia\preview\Model\Outcome
```

/preview/retail-media/retailers/{retailer-id}/offers/update

Update one or more offers by replacing each offer's price and availability with the given values

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$retailer_id = 'retailer_id_example'; // string | The retailer for which these offers will be updated
$value_resource_input_update_offers_request = new \criteo\api\retailmedia\preview\Model\ValueResourceInputUpdateOffersRequest(); // \criteo\api\retailmedia\preview\Model\ValueResourceInputUpdateOffersRequest | Collection of offer price and availability updates to be applied.

try {
    $result = $apiInstance->offerUpdateV1($retailer_id, $value_resource_input_update_offers_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogApi->offerUpdateV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **retailer_id** | **string**| The retailer for which these offers will be updated | |
| **value_resource_input_update_offers_request** | [**\criteo\api\retailmedia\preview\Model\ValueResourceInputUpdateOffersRequest**](../Model/ValueResourceInputUpdateOffersRequest.md)| Collection of offer price and availability updates to be applied. | |

### Return type

[**\criteo\api\retailmedia\preview\Model\Outcome**](../Model/Outcome.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `submitCatalogProductsBatch()`

```php
submitCatalogProductsBatch($products_custom_batch_request): \criteo\api\retailmedia\preview\Model\BatchAcceptedResponse
```

/preview/retail-media/catalog/products/batch

Used to publish a batch of operations to insert, update and deletes products.  The batch is processed asynchronously.The response provides an operationToken which can be used to track  the status of the report of the operation.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$products_custom_batch_request = new \criteo\api\retailmedia\preview\Model\ProductsCustomBatchRequest(); // \criteo\api\retailmedia\preview\Model\ProductsCustomBatchRequest

try {
    $result = $apiInstance->submitCatalogProductsBatch($products_custom_batch_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CatalogApi->submitCatalogProductsBatch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **products_custom_batch_request** | [**\criteo\api\retailmedia\preview\Model\ProductsCustomBatchRequest**](../Model/ProductsCustomBatchRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\preview\Model\BatchAcceptedResponse**](../Model/BatchAcceptedResponse.md)

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

/preview/retail-media/catalog/merchants/{merchantId}/store-inventory/upsert

Used to publish a batch of store inventories to upsert. The batch is processed asynchronously.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\CatalogApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$merchant_id = 'merchant_id_example'; // string | Identifies the merchant, can also be called partnerId
$batch_store_inventory_request = new \criteo\api\retailmedia\preview\Model\BatchStoreInventoryRequest(); // \criteo\api\retailmedia\preview\Model\BatchStoreInventoryRequest

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
| **batch_store_inventory_request** | [**\criteo\api\retailmedia\preview\Model\BatchStoreInventoryRequest**](../Model/BatchStoreInventoryRequest.md)|  | |

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
