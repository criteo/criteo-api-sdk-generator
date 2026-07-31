# criteo\api\retailmedia\v2026_07\BalanceApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addFundsByAccountAndBalanceId()**](BalanceApi.md#addFundsByAccountAndBalanceId) | **POST** /2026-07/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds | /2026-07/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds |
| [**changeDatesByAccountAndBalanceId()**](BalanceApi.md#changeDatesByAccountAndBalanceId) | **POST** /2026-07/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates | /2026-07/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates |
| [**createBalanceByAccountId()**](BalanceApi.md#createBalanceByAccountId) | **POST** /2026-07/retail-media/accounts/{account-id}/balances | /2026-07/retail-media/accounts/{account-id}/balances |
| [**getBalanceByAccountAndBalanceId()**](BalanceApi.md#getBalanceByAccountAndBalanceId) | **GET** /2026-07/retail-media/accounts/{account-id}/balances/{balance-id} | /2026-07/retail-media/accounts/{account-id}/balances/{balance-id} |
| [**getBalanceHistoryV1()**](BalanceApi.md#getBalanceHistoryV1) | **GET** /2026-07/retail-media/balances/{balanceId}/history | /2026-07/retail-media/balances/{balanceId}/history |
| [**getBalanceV1()**](BalanceApi.md#getBalanceV1) | **GET** /2026-07/retail-media/balances/{balanceId} | /2026-07/retail-media/balances/{balanceId} |
| [**getCampaignsByBalanceId()**](BalanceApi.md#getCampaignsByBalanceId) | **GET** /2026-07/retail-media/balances/{balance-id}/campaigns | /2026-07/retail-media/balances/{balance-id}/campaigns |
| [**getPageOfBalancesV1()**](BalanceApi.md#getPageOfBalancesV1) | **GET** /2026-07/retail-media/accounts/{accountId}/balances | /2026-07/retail-media/accounts/{accountId}/balances |
| [**updateBalanceV1()**](BalanceApi.md#updateBalanceV1) | **PATCH** /2026-07/retail-media/accounts/{account-id}/balances/{balance-id} | /2026-07/retail-media/accounts/{account-id}/balances/{balance-id} |


## `addFundsByAccountAndBalanceId()`

```php
addFundsByAccountAndBalanceId($account_id, $balance_id, $add_funds_to_balance_v3_request): \criteo\api\retailmedia\v2026_07\Model\BalanceResponseV3Response
```

/2026-07/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds

Add funds to a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to add funds to
$add_funds_to_balance_v3_request = new \criteo\api\retailmedia\v2026_07\Model\AddFundsToBalanceV3Request(); // \criteo\api\retailmedia\v2026_07\Model\AddFundsToBalanceV3Request | An object that represents the available options of adding funds to a balance.

try {
    $result = $apiInstance->addFundsByAccountAndBalanceId($account_id, $balance_id, $add_funds_to_balance_v3_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->addFundsByAccountAndBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account of the balance | |
| **balance_id** | **string**| The balance to add funds to | |
| **add_funds_to_balance_v3_request** | [**\criteo\api\retailmedia\v2026_07\Model\AddFundsToBalanceV3Request**](../Model/AddFundsToBalanceV3Request.md)| An object that represents the available options of adding funds to a balance. | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\BalanceResponseV3Response**](../Model/BalanceResponseV3Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `changeDatesByAccountAndBalanceId()`

```php
changeDatesByAccountAndBalanceId($account_id, $balance_id, $change_dates_of_balance_v2_request): \criteo\api\retailmedia\v2026_07\Model\BalanceResponseV2Response
```

/2026-07/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates

Change dates of a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to change the dates
$change_dates_of_balance_v2_request = new \criteo\api\retailmedia\v2026_07\Model\ChangeDatesOfBalanceV2Request(); // \criteo\api\retailmedia\v2026_07\Model\ChangeDatesOfBalanceV2Request | An object that represents the available options to modify schedule of a balance.

try {
    $result = $apiInstance->changeDatesByAccountAndBalanceId($account_id, $balance_id, $change_dates_of_balance_v2_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->changeDatesByAccountAndBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account of the balance | |
| **balance_id** | **string**| The balance to change the dates | |
| **change_dates_of_balance_v2_request** | [**\criteo\api\retailmedia\v2026_07\Model\ChangeDatesOfBalanceV2Request**](../Model/ChangeDatesOfBalanceV2Request.md)| An object that represents the available options to modify schedule of a balance. | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createBalanceByAccountId()`

```php
createBalanceByAccountId($account_id, $create_balance_v3_request): \criteo\api\retailmedia\v2026_07\Model\BalanceResponseV3Response
```

/2026-07/retail-media/accounts/{account-id}/balances

Create balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to create balances for
$create_balance_v3_request = new \criteo\api\retailmedia\v2026_07\Model\CreateBalanceV3Request(); // \criteo\api\retailmedia\v2026_07\Model\CreateBalanceV3Request | An object that represents the available options to set when creating a Retail Media Balance

try {
    $result = $apiInstance->createBalanceByAccountId($account_id, $create_balance_v3_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->createBalanceByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to create balances for | |
| **create_balance_v3_request** | [**\criteo\api\retailmedia\v2026_07\Model\CreateBalanceV3Request**](../Model/CreateBalanceV3Request.md)| An object that represents the available options to set when creating a Retail Media Balance | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\BalanceResponseV3Response**](../Model/BalanceResponseV3Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBalanceByAccountAndBalanceId()`

```php
getBalanceByAccountAndBalanceId($account_id, $balance_id): \criteo\api\retailmedia\v2026_07\Model\BalanceResponseV2Response
```

/2026-07/retail-media/accounts/{account-id}/balances/{balance-id}

Get a balance for the given account id and balance id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance id

try {
    $result = $apiInstance->getBalanceByAccountAndBalanceId($account_id, $balance_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getBalanceByAccountAndBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account of the balance | |
| **balance_id** | **string**| The balance id | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBalanceHistoryV1()`

```php
getBalanceHistoryV1($balance_id, $limit, $limit_to_change_types, $offset): \criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata
```

/2026-07/retail-media/balances/{balanceId}/history

Gets the balance's historical change data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
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

[**\criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata**](../Model/ValueResourceCollectionOutcomeBalanceHistoryChangeDataCaptureV1AndMetadata.md)

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
getBalanceV1($balance_id): \criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeBalanceV1
```

/2026-07/retail-media/balances/{balanceId}

Get a balance for the given balance id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
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

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeBalanceV1**](../Model/EntityResourceOutcomeBalanceV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCampaignsByBalanceId()`

```php
getCampaignsByBalanceId($balance_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_07\Model\BalanceCampaign202110PagedListResponse
```

/2026-07/retail-media/balances/{balance-id}/campaigns

Gets page of campaigns for the given balanceId

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$balance_id = 'balance_id_example'; // string | The balance to get campaigns from
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getCampaignsByBalanceId($balance_id, $limit_to_id, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getCampaignsByBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **balance_id** | **string**| The balance to get campaigns from | |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\BalanceCampaign202110PagedListResponse**](../Model/BalanceCampaign202110PagedListResponse.md)

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
getPageOfBalancesV1($account_id, $limit, $limit_to_id, $offset): \criteo\api\retailmedia\v2026_07\Model\EntityResourceCollectionOutcomeBalanceV1AndMetadata
```

/2026-07/retail-media/accounts/{accountId}/balances

Gets page of balance objects for the given account id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
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

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceCollectionOutcomeBalanceV1AndMetadata**](../Model/EntityResourceCollectionOutcomeBalanceV1AndMetadata.md)

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
updateBalanceV1($account_id, $balance_id, $value_resource_input_of_update_balance_model_v1): \criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeOfBalanceResponseV1
```

/2026-07/retail-media/accounts/{account-id}/balances/{balance-id}

Modify a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to change the dates
$value_resource_input_of_update_balance_model_v1 = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfUpdateBalanceModelV1(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfUpdateBalanceModelV1 | An object that represents the available options to modify a balance.

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
| **value_resource_input_of_update_balance_model_v1** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfUpdateBalanceModelV1**](../Model/ValueResourceInputOfUpdateBalanceModelV1.md)| An object that represents the available options to modify a balance. | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeOfBalanceResponseV1**](../Model/EntityResourceOutcomeOfBalanceResponseV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
