# criteo\api\retailmedia\v2026_07\AccountsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**accountFeesSearch()**](AccountsApi.md#accountFeesSearch) | **POST** /2026-07/retail-media/accounts/fees/search | /2026-07/retail-media/accounts/fees/search |
| [**addBrands()**](AccountsApi.md#addBrands) | **POST** /2026-07/retail-media/account-management/accounts/{accountId}/brands/add | /2026-07/retail-media/account-management/accounts/{accountId}/brands/add |
| [**createPrivateMarketDemandBrandAccount()**](AccountsApi.md#createPrivateMarketDemandBrandAccount) | **POST** /2026-07/retail-media/account-management/accounts/{accountId}/create-brand-account | /2026-07/retail-media/account-management/accounts/{accountId}/create-brand-account |
| [**createPrivateMarketDemandSellerAccount()**](AccountsApi.md#createPrivateMarketDemandSellerAccount) | **POST** /2026-07/retail-media/account-management/accounts/{accountId}/create-seller-account | /2026-07/retail-media/account-management/accounts/{accountId}/create-seller-account |
| [**getAccounts()**](AccountsApi.md#getAccounts) | **GET** /2026-07/retail-media/accounts | /2026-07/retail-media/accounts |
| [**getPrivateMarketChildAccountsByAccountId()**](AccountsApi.md#getPrivateMarketChildAccountsByAccountId) | **GET** /2026-07/retail-media/account-management/accounts/{accountId}/private-market-child-accounts | /2026-07/retail-media/account-management/accounts/{accountId}/private-market-child-accounts |
| [**grantConsent()**](AccountsApi.md#grantConsent) | **POST** /2026-07/retail-media/accounts/{accountId}/grant-consent | /2026-07/retail-media/accounts/{accountId}/grant-consent |
| [**removeBrands()**](AccountsApi.md#removeBrands) | **POST** /2026-07/retail-media/account-management/accounts/{accountId}/brands/remove | /2026-07/retail-media/account-management/accounts/{accountId}/brands/remove |
| [**searchBrands()**](AccountsApi.md#searchBrands) | **POST** /2026-07/retail-media/brands/search | /2026-07/retail-media/brands/search |
| [**searchSellers()**](AccountsApi.md#searchSellers) | **POST** /2026-07/retail-media/accounts/sellers/search | /2026-07/retail-media/accounts/sellers/search |
| [**updateAccountFees()**](AccountsApi.md#updateAccountFees) | **POST** /2026-07/retail-media/accounts/fees/update | /2026-07/retail-media/accounts/fees/update |
| [**updateSellers()**](AccountsApi.md#updateSellers) | **PUT** /2026-07/retail-media/account-management/accounts/{accountId}/sellers | /2026-07/retail-media/account-management/accounts/{accountId}/sellers |


## `accountFeesSearch()`

```php
accountFeesSearch($value_resource_input_account_fees_search_request, $limit, $offset): \criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata
```

/2026-07/retail-media/accounts/fees/search

Get fees for provided accounts

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$value_resource_input_account_fees_search_request = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputAccountFeesSearchRequest(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputAccountFeesSearchRequest
$limit = 50; // int | used for paging, number of results returned per request, Maximum of 500
$offset = 0; // int | used for paging, number of records to skip

try {
    $result = $apiInstance->accountFeesSearch($value_resource_input_account_fees_search_request, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->accountFeesSearch: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **value_resource_input_account_fees_search_request** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputAccountFeesSearchRequest**](../Model/ValueResourceInputAccountFeesSearchRequest.md)|  | |
| **limit** | **int**| used for paging, number of results returned per request, Maximum of 500 | [optional] [default to 50] |
| **offset** | **int**| used for paging, number of records to skip | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata**](../Model/ValueResourceCollectionOutcomePrivateMarketAccountFeesAndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `addBrands()`

```php
addBrands($account_id, $value_resource_input_of_retail_media_brands): \criteo\api\retailmedia\v2026_07\Model\ValueResourceOutcomeOfRetailMediaBrands
```

/2026-07/retail-media/account-management/accounts/{accountId}/brands/add

Add brands to an account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | the account id to update
$value_resource_input_of_retail_media_brands = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrands(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrands

try {
    $result = $apiInstance->addBrands($account_id, $value_resource_input_of_retail_media_brands);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->addBrands: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| the account id to update | |
| **value_resource_input_of_retail_media_brands** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrands**](../Model/ValueResourceInputOfRetailMediaBrands.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\ValueResourceOutcomeOfRetailMediaBrands**](../Model/ValueResourceOutcomeOfRetailMediaBrands.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createPrivateMarketDemandBrandAccount()`

```php
createPrivateMarketDemandBrandAccount($account_id, $value_resource_input_of_retail_media_brand_account_creation): \criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeOfRetailMediaAccount
```

/2026-07/retail-media/account-management/accounts/{accountId}/create-brand-account

Creates a new child Demand Brand account for the provided parent Private Market account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$value_resource_input_of_retail_media_brand_account_creation = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrandAccountCreation(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrandAccountCreation

try {
    $result = $apiInstance->createPrivateMarketDemandBrandAccount($account_id, $value_resource_input_of_retail_media_brand_account_creation);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->createPrivateMarketDemandBrandAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **value_resource_input_of_retail_media_brand_account_creation** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrandAccountCreation**](../Model/ValueResourceInputOfRetailMediaBrandAccountCreation.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeOfRetailMediaAccount**](../Model/EntityResourceOutcomeOfRetailMediaAccount.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createPrivateMarketDemandSellerAccount()`

```php
createPrivateMarketDemandSellerAccount($account_id, $value_resource_input_of_retail_media_seller_account_creation): \criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeOfRetailMediaAccount
```

/2026-07/retail-media/account-management/accounts/{accountId}/create-seller-account

Creates a new child Demand Seller account for the provided parent Private Market account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$value_resource_input_of_retail_media_seller_account_creation = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaSellerAccountCreation(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaSellerAccountCreation

try {
    $result = $apiInstance->createPrivateMarketDemandSellerAccount($account_id, $value_resource_input_of_retail_media_seller_account_creation);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->createPrivateMarketDemandSellerAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **value_resource_input_of_retail_media_seller_account_creation** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaSellerAccountCreation**](../Model/ValueResourceInputOfRetailMediaSellerAccountCreation.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceOutcomeOfRetailMediaAccount**](../Model/EntityResourceOutcomeOfRetailMediaAccount.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAccounts()`

```php
getAccounts($limit_to_id, $page_index, $page_size): \criteo\api\retailmedia\v2026_07\Model\JsonApiPageResponseOfAccount
```

/2026-07/retail-media/accounts

Gets page of account objects that the current user can access

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit_to_id = array('limit_to_id_example'); // string[] | The ids that you would like to limit your result set to
$page_index = 0; // int | The 0 indexed page index you would like to receive given the page size
$page_size = 25; // int | The maximum number of items you would like to receive in this request

try {
    $result = $apiInstance->getAccounts($limit_to_id, $page_index, $page_size);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->getAccounts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit_to_id** | [**string[]**](../Model/string.md)| The ids that you would like to limit your result set to | [optional] |
| **page_index** | **int**| The 0 indexed page index you would like to receive given the page size | [optional] [default to 0] |
| **page_size** | **int**| The maximum number of items you would like to receive in this request | [optional] [default to 25] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\JsonApiPageResponseOfAccount**](../Model/JsonApiPageResponseOfAccount.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPrivateMarketChildAccountsByAccountId()`

```php
getPrivateMarketChildAccountsByAccountId($account_id, $limit, $offset): \criteo\api\retailmedia\v2026_07\Model\EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata
```

/2026-07/retail-media/account-management/accounts/{accountId}/private-market-child-accounts

Gets Private Market child accounts that are associated with the given account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$limit = 25; // int | The number of accounts to be returned. The default is 25.
$offset = 0; // int | The (zero-based) offset into the collection of accounts. The default is 0.

try {
    $result = $apiInstance->getPrivateMarketChildAccountsByAccountId($account_id, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->getPrivateMarketChildAccountsByAccountId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **limit** | **int**| The number of accounts to be returned. The default is 25. | [optional] [default to 25] |
| **offset** | **int**| The (zero-based) offset into the collection of accounts. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata**](../Model/EntityResourceCollectionOutcomeOfRetailMediaChildAccountAndMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `grantConsent()`

```php
grantConsent($account_id, $grant_consent_input)
```

/2026-07/retail-media/accounts/{accountId}/grant-consent

Grant consent to a business application on behalf of a Private Market demand account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The demand account ID on which to grant consent
$grant_consent_input = new \criteo\api\retailmedia\v2026_07\Model\GrantConsentInput(); // \criteo\api\retailmedia\v2026_07\Model\GrantConsentInput

try {
    $apiInstance->grantConsent($account_id, $grant_consent_input);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->grantConsent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The demand account ID on which to grant consent | |
| **grant_consent_input** | [**\criteo\api\retailmedia\v2026_07\Model\GrantConsentInput**](../Model/GrantConsentInput.md)|  | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `removeBrands()`

```php
removeBrands($account_id, $value_resource_input_of_retail_media_brands): \criteo\api\retailmedia\v2026_07\Model\ValueResourceOutcomeOfRetailMediaBrands
```

/2026-07/retail-media/account-management/accounts/{accountId}/brands/remove

Remove brands from an account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | the account id to update
$value_resource_input_of_retail_media_brands = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrands(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrands

try {
    $result = $apiInstance->removeBrands($account_id, $value_resource_input_of_retail_media_brands);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->removeBrands: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| the account id to update | |
| **value_resource_input_of_retail_media_brands** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfRetailMediaBrands**](../Model/ValueResourceInputOfRetailMediaBrands.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\ValueResourceOutcomeOfRetailMediaBrands**](../Model/ValueResourceOutcomeOfRetailMediaBrands.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchBrands()`

```php
searchBrands($limit, $offset, $value_resource_input_brand_id_search_request): \criteo\api\retailmedia\v2026_07\Model\EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata
```

/2026-07/retail-media/brands/search

Search for brands given a retailer ID and search term.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$limit = 25; // int | the number of brands to return
$offset = 0; // int | offset of paginated results
$value_resource_input_brand_id_search_request = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputBrandIdSearchRequest(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputBrandIdSearchRequest | BrandIdSearchRequest which contains the request parameters

try {
    $result = $apiInstance->searchBrands($limit, $offset, $value_resource_input_brand_id_search_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->searchBrands: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **int**| the number of brands to return | [optional] [default to 25] |
| **offset** | **int**| offset of paginated results | [optional] [default to 0] |
| **value_resource_input_brand_id_search_request** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputBrandIdSearchRequest**](../Model/ValueResourceInputBrandIdSearchRequest.md)| BrandIdSearchRequest which contains the request parameters | [optional] |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata**](../Model/EntityResourceCollectionOutcomeBrandIdSearchResultPagingOffsetLimitMetadata.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchSellers()`

```php
searchSellers($value_resource_input_of_seller_search): \criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomeOfSellerSearchResult
```

/2026-07/retail-media/accounts/sellers/search

Get the sellers mapped to provided accounts

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$value_resource_input_of_seller_search = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfSellerSearch(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfSellerSearch | 

try {
    $result = $apiInstance->searchSellers($value_resource_input_of_seller_search);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->searchSellers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **value_resource_input_of_seller_search** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputOfSellerSearch**](../Model/ValueResourceInputOfSellerSearch.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomeOfSellerSearchResult**](../Model/ValueResourceCollectionOutcomeOfSellerSearchResult.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateAccountFees()`

```php
updateAccountFees($value_resource_input_account_fees_update_request)
```

/2026-07/retail-media/accounts/fees/update

Set fees for provided accounts

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$value_resource_input_account_fees_update_request = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputAccountFeesUpdateRequest(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceInputAccountFeesUpdateRequest

try {
    $apiInstance->updateAccountFees($value_resource_input_account_fees_update_request);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->updateAccountFees: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **value_resource_input_account_fees_update_request** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceInputAccountFeesUpdateRequest**](../Model/ValueResourceInputAccountFeesUpdateRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateSellers()`

```php
updateSellers($account_id, $value_resource_collection_input_of_retail_media_seller): \criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomeOfRetailMediaSeller
```

/2026-07/retail-media/account-management/accounts/{accountId}/sellers

Replace the sellers associated with an account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\AccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The given account id
$value_resource_collection_input_of_retail_media_seller = new \criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionInputOfRetailMediaSeller(); // \criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionInputOfRetailMediaSeller

try {
    $result = $apiInstance->updateSellers($account_id, $value_resource_collection_input_of_retail_media_seller);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccountsApi->updateSellers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The given account id | |
| **value_resource_collection_input_of_retail_media_seller** | [**\criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionInputOfRetailMediaSeller**](../Model/ValueResourceCollectionInputOfRetailMediaSeller.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\ValueResourceCollectionOutcomeOfRetailMediaSeller**](../Model/ValueResourceCollectionOutcomeOfRetailMediaSeller.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
