# criteo\api\retailmedia\preview\BalanceApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getBalanceHistoryV1()**](BalanceApi.md#getBalanceHistoryV1) | **GET** /preview/retail-media/balances/{balanceId}/history | /preview/retail-media/balances/{balanceId}/history |
| [**getBalanceV1()**](BalanceApi.md#getBalanceV1) | **GET** /preview/retail-media/balances/{balanceId} | /preview/retail-media/balances/{balanceId} |
| [**getPageOfBalancesV1()**](BalanceApi.md#getPageOfBalancesV1) | **GET** /preview/retail-media/accounts/{accountId}/balances | /preview/retail-media/accounts/{accountId}/balances |
| [**updateBalanceV1()**](BalanceApi.md#updateBalanceV1) | **PATCH** /preview/retail-media/accounts/{account-id}/balances/{balance-id} | /preview/retail-media/accounts/{account-id}/balances/{balance-id} |


## `getBalanceHistoryV1()`

```php
getBalanceHistoryV1($balance_id, $limit, $limit_to_change_types, $offset): \criteo\api\retailmedia\preview\Model\ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata
```

/preview/retail-media/balances/{balanceId}/history

Gets the balance's historical change data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | Balance id.
$limit = 25; // int | The number of elements to be returned.
$limit_to_change_types = 'limit_to_change_types_example'; // string | Comma separated change types string that will be queried.
$offset = 0; // int | The (zero-based) starting offset in the collection.

try {
    $result = $apiInstance->getBalanceHistoryV1($balance_id, $limit, $limit_to_change_types, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getBalanceHistoryV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| Balance id. | |
| **limit** | **int**| The number of elements to be returned. | [optional] [default to 25] |
| **limit_to_change_types** | **string**| Comma separated change types string that will be queried. | [optional] |
| **offset** | **int**| The (zero-based) starting offset in the collection. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\preview\Model\ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata**](../Model/ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBalanceV1()`

```php
getBalanceV1($balance_id): \criteo\api\retailmedia\preview\Model\EntityResourceOutcomeBalanceV1
```

/preview/retail-media/balances/{balanceId}

Get a balance for the given balance id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | The balance id.

try {
    $result = $apiInstance->getBalanceV1($balance_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getBalanceV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| The balance id. | |

### Return type

[**\criteo\api\retailmedia\preview\Model\EntityResourceOutcomeBalanceV1**](../Model/EntityResourceOutcomeBalanceV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPageOfBalancesV1()`

```php
getPageOfBalancesV1($account_id, $limit, $limit_to_id, $offset): \criteo\api\retailmedia\preview\Model\EntityResourceCollectionOutcomeBalanceV1AndMetadata
```

/preview/retail-media/accounts/{accountId}/balances

Gets page of balance objects for the given account id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to get balances for.
$limit = 25; // int | The number of elements to be returned.
$limit_to_id = array('limit_to_id_example'); // string[] | The balance ids which the result is limited to.
$offset = 0; // int | The (zero-based) starting offset in the collection.

try {
    $result = $apiInstance->getPageOfBalancesV1($account_id, $limit, $limit_to_id, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getPageOfBalancesV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to get balances for. | |
| **limit** | **int**| The number of elements to be returned. | [optional] [default to 25] |
| **limit_to_id** | [**string[]**](../Model/string.md)| The balance ids which the result is limited to. | [optional] |
| **offset** | **int**| The (zero-based) starting offset in the collection. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\preview\Model\EntityResourceCollectionOutcomeBalanceV1AndMetadata**](../Model/EntityResourceCollectionOutcomeBalanceV1AndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateBalanceV1()`

```php
updateBalanceV1($account_id, $balance_id, $value_resource_input_of_update_balance_model_v1): \criteo\api\retailmedia\preview\Model\EntityResourceOutcomeOfBalanceResponseV1
```

/preview/retail-media/accounts/{account-id}/balances/{balance-id}

Modify a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to change the dates
$value_resource_input_of_update_balance_model_v1 = new \criteo\api\retailmedia\preview\Model\ValueResourceInputOfUpdateBalanceModelV1(); // \criteo\api\retailmedia\preview\Model\ValueResourceInputOfUpdateBalanceModelV1 | An object that represents the available options to modify a balance.

try {
    $result = $apiInstance->updateBalanceV1($account_id, $balance_id, $value_resource_input_of_update_balance_model_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->updateBalanceV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account of the balance | |
| **balance_id** | **string**| The balance to change the dates | |
| **value_resource_input_of_update_balance_model_v1** | [**\criteo\api\retailmedia\preview\Model\ValueResourceInputOfUpdateBalanceModelV1**](../Model/ValueResourceInputOfUpdateBalanceModelV1.md)| An object that represents the available options to modify a balance. | |

### Return type

[**\criteo\api\retailmedia\preview\Model\EntityResourceOutcomeOfBalanceResponseV1**](../Model/EntityResourceOutcomeOfBalanceResponseV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
