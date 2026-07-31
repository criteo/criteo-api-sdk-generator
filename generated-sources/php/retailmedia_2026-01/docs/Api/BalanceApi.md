# criteo\api\retailmedia\v2026_01\BalanceApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addFundsByAccountAndBalanceId()**](BalanceApi.md#addFundsByAccountAndBalanceId) | **POST** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds |
| [**changeDatesByAccountAndBalanceId()**](BalanceApi.md#changeDatesByAccountAndBalanceId) | **POST** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates |
| [**createBalanceByAccountId()**](BalanceApi.md#createBalanceByAccountId) | **POST** /2026-01/retail-media/accounts/{account-id}/balances | /2026-01/retail-media/accounts/{account-id}/balances |
| [**getBalanceByAccountAndBalanceId()**](BalanceApi.md#getBalanceByAccountAndBalanceId) | **GET** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} |
| [**getBalanceHistory()**](BalanceApi.md#getBalanceHistory) | **GET** /2026-01/retail-media/balances/{balanceId}/history | /2026-01/retail-media/balances/{balanceId}/history |
| [**getBalancesByAccountId()**](BalanceApi.md#getBalancesByAccountId) | **GET** /2026-01/retail-media/accounts/{account-id}/balances | /2026-01/retail-media/accounts/{account-id}/balances |
| [**getCampaignsByBalanceId()**](BalanceApi.md#getCampaignsByBalanceId) | **GET** /2026-01/retail-media/balances/{balance-id}/campaigns | /2026-01/retail-media/balances/{balance-id}/campaigns |
| [**modifyBalanceByAccountAndBalanceId()**](BalanceApi.md#modifyBalanceByAccountAndBalanceId) | **PATCH** /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} | /2026-01/retail-media/accounts/{account-id}/balances/{balance-id} |


## `addFundsByAccountAndBalanceId()`

```php
addFundsByAccountAndBalanceId($account_id, $balance_id, $add_funds_to_balance_v2_request): \criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response
```

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/add-funds

Add funds to a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to add funds to
$add_funds_to_balance_v2_request = new \criteo\api\retailmedia\v2026_01\Model\AddFundsToBalanceV2Request(); // \criteo\api\retailmedia\v2026_01\Model\AddFundsToBalanceV2Request | An object that represents the available options of adding funds to a balance.

try {
    $result = $apiInstance->addFundsByAccountAndBalanceId($account_id, $balance_id, $add_funds_to_balance_v2_request);
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
| **add_funds_to_balance_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\AddFundsToBalanceV2Request**](../Model/AddFundsToBalanceV2Request.md)| An object that represents the available options of adding funds to a balance. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

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
changeDatesByAccountAndBalanceId($account_id, $balance_id, $change_dates_of_balance_v2_request): \criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response
```

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}/change-dates

Change dates of a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to change the dates
$change_dates_of_balance_v2_request = new \criteo\api\retailmedia\v2026_01\Model\ChangeDatesOfBalanceV2Request(); // \criteo\api\retailmedia\v2026_01\Model\ChangeDatesOfBalanceV2Request | An object that represents the available options to modify schedule of a balance.

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
| **change_dates_of_balance_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\ChangeDatesOfBalanceV2Request**](../Model/ChangeDatesOfBalanceV2Request.md)| An object that represents the available options to modify schedule of a balance. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

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
createBalanceByAccountId($account_id, $create_balance_v2_request): \criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response
```

/2026-01/retail-media/accounts/{account-id}/balances

Create balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to create balances for
$create_balance_v2_request = new \criteo\api\retailmedia\v2026_01\Model\CreateBalanceV2Request(); // \criteo\api\retailmedia\v2026_01\Model\CreateBalanceV2Request | An object that represents the available options to set when creating a Retail Media Balance

try {
    $result = $apiInstance->createBalanceByAccountId($account_id, $create_balance_v2_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->createBalanceByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to create balances for | |
| **create_balance_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\CreateBalanceV2Request**](../Model/CreateBalanceV2Request.md)| An object that represents the available options to set when creating a Retail Media Balance | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

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
getBalanceByAccountAndBalanceId($account_id, $balance_id): \criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response
```

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}

Get a balance for the given account id and balance id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
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

[**\criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBalanceHistory()`

```php
getBalanceHistory($balance_id, $limit, $limit_to_change_types, $offset): \criteo\api\retailmedia\v2026_01\Model\PageOfBalanceHistoryChangeDataCaptureV1
```

/2026-01/retail-media/balances/{balanceId}/history

Gets the balance's historical change data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
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
    $result = $apiInstance->getBalanceHistory($balance_id, $limit, $limit_to_change_types, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getBalanceHistory: ', $e->getMessage(), PHP_EOL;
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

[**\criteo\api\retailmedia\v2026_01\Model\PageOfBalanceHistoryChangeDataCaptureV1**](../Model/PageOfBalanceHistoryChangeDataCaptureV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getBalancesByAccountId()`

```php
getBalancesByAccountId($account_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2PagedListResponse
```

/2026-01/retail-media/accounts/{account-id}/balances

Gets page of balance objects for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account to get balances for
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getBalancesByAccountId($account_id, $limit_to_id, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->getBalancesByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account to get balances for | |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2PagedListResponse**](../Model/BalanceResponseV2PagedListResponse.md)

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
getCampaignsByBalanceId($balance_id, $limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110PagedListResponse
```

/2026-01/retail-media/balances/{balance-id}/campaigns

Gets page of campaigns for the given balanceId

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
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

[**\criteo\api\retailmedia\v2026_01\Model\BalanceCampaign202110PagedListResponse**](../Model/BalanceCampaign202110PagedListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `modifyBalanceByAccountAndBalanceId()`

```php
modifyBalanceByAccountAndBalanceId($account_id, $balance_id, $update_balance_model_v2_request): \criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response
```

/2026-01/retail-media/accounts/{account-id}/balances/{balance-id}

Modify a balance for the given account id

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BalanceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The account of the balance
$balance_id = 'balance_id_example'; // string | The balance to change the dates
$update_balance_model_v2_request = new \criteo\api\retailmedia\v2026_01\Model\UpdateBalanceModelV2Request(); // \criteo\api\retailmedia\v2026_01\Model\UpdateBalanceModelV2Request | An object that represents the available options to modify a balance.

try {
    $result = $apiInstance->modifyBalanceByAccountAndBalanceId($account_id, $balance_id, $update_balance_model_v2_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BalanceApi->modifyBalanceByAccountAndBalanceId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The account of the balance | |
| **balance_id** | **string**| The balance to change the dates | |
| **update_balance_model_v2_request** | [**\criteo\api\retailmedia\v2026_01\Model\UpdateBalanceModelV2Request**](../Model/UpdateBalanceModelV2Request.md)| An object that represents the available options to modify a balance. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\BalanceResponseV2Response**](../Model/BalanceResponseV2Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
