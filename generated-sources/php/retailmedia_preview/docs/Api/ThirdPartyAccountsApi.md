# criteo\api\retailmedia\preview\ThirdPartyAccountsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addThirdPartyAccountBrands()**](ThirdPartyAccountsApi.md#addThirdPartyAccountBrands) | **POST** /preview/retail-media/third-party-accounts/{accountId}/brands/add | /preview/retail-media/third-party-accounts/{accountId}/brands/add |
| [**createThirdPartyBrandAccount()**](ThirdPartyAccountsApi.md#createThirdPartyBrandAccount) | **POST** /preview/retail-media/third-party-accounts/{accountId}/create-brand-account | /preview/retail-media/third-party-accounts/{accountId}/create-brand-account |
| [**createThirdPartySellerAccount()**](ThirdPartyAccountsApi.md#createThirdPartySellerAccount) | **POST** /preview/retail-media/third-party-accounts/{accountId}/create-seller-account | /preview/retail-media/third-party-accounts/{accountId}/create-seller-account |
| [**grantThirdPartyConsent()**](ThirdPartyAccountsApi.md#grantThirdPartyConsent) | **POST** /preview/retail-media/accounts/{accountId}/grant-third-party-consent | /preview/retail-media/accounts/{accountId}/grant-third-party-consent |
| [**removeThirdPartyAccountBrand()**](ThirdPartyAccountsApi.md#removeThirdPartyAccountBrand) | **POST** /preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove | /preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove |
| [**updateThirdPartyAccountSellers()**](ThirdPartyAccountsApi.md#updateThirdPartyAccountSellers) | **PUT** /preview/retail-media/third-party-accounts/{accountId}/sellers | /preview/retail-media/third-party-accounts/{accountId}/sellers |


## `addThirdPartyAccountBrands()`

```php
addThirdPartyAccountBrands($account_id, $value_resource_input_of_retail_media_brands): \criteo\api\retailmedia\preview\Model\ValueResourceOutcomeOfRetailMediaBrands
```

/preview/retail-media/third-party-accounts/{accountId}/brands/add

add the provided brands to an account. This will not remove any existing brands.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\ThirdPartyAccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | account to add brands to
$value_resource_input_of_retail_media_brands = new \criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaBrands(); // \criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaBrands | list of bands to add to an account

try {
    $result = $apiInstance->addThirdPartyAccountBrands($account_id, $value_resource_input_of_retail_media_brands);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ThirdPartyAccountsApi->addThirdPartyAccountBrands: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| account to add brands to | |
| **value_resource_input_of_retail_media_brands** | [**\criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaBrands**](../Model/ValueResourceInputOfRetailMediaBrands.md)| list of bands to add to an account | [optional] |

### Return type

[**\criteo\api\retailmedia\preview\Model\ValueResourceOutcomeOfRetailMediaBrands**](../Model/ValueResourceOutcomeOfRetailMediaBrands.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createThirdPartyBrandAccount()`

```php
createThirdPartyBrandAccount($account_id, $value_resource_input_of_retail_media_brand_account_creation_v2): \criteo\api\retailmedia\preview\Model\EntityResourceOutcomeOfRetailMediaAccountV2
```

/preview/retail-media/third-party-accounts/{accountId}/create-brand-account

Create a private market demand brand account under a given parent account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\ThirdPartyAccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | parent supply account to create account under
$value_resource_input_of_retail_media_brand_account_creation_v2 = new \criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaBrandAccountCreationV2(); // \criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaBrandAccountCreationV2 | 

try {
    $result = $apiInstance->createThirdPartyBrandAccount($account_id, $value_resource_input_of_retail_media_brand_account_creation_v2);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ThirdPartyAccountsApi->createThirdPartyBrandAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| parent supply account to create account under | |
| **value_resource_input_of_retail_media_brand_account_creation_v2** | [**\criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaBrandAccountCreationV2**](../Model/ValueResourceInputOfRetailMediaBrandAccountCreationV2.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\preview\Model\EntityResourceOutcomeOfRetailMediaAccountV2**](../Model/EntityResourceOutcomeOfRetailMediaAccountV2.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createThirdPartySellerAccount()`

```php
createThirdPartySellerAccount($account_id, $value_resource_input_of_retail_media_seller_account_creation_v2): \criteo\api\retailmedia\preview\Model\EntityResourceOutcomeOfRetailMediaAccountV2
```

/preview/retail-media/third-party-accounts/{accountId}/create-seller-account

Create a private market demand seller account under a given parent account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\ThirdPartyAccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | parent supply account to create account under
$value_resource_input_of_retail_media_seller_account_creation_v2 = new \criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaSellerAccountCreationV2(); // \criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaSellerAccountCreationV2 | 

try {
    $result = $apiInstance->createThirdPartySellerAccount($account_id, $value_resource_input_of_retail_media_seller_account_creation_v2);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ThirdPartyAccountsApi->createThirdPartySellerAccount: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| parent supply account to create account under | |
| **value_resource_input_of_retail_media_seller_account_creation_v2** | [**\criteo\api\retailmedia\preview\Model\ValueResourceInputOfRetailMediaSellerAccountCreationV2**](../Model/ValueResourceInputOfRetailMediaSellerAccountCreationV2.md)|  | [optional] |

### Return type

[**\criteo\api\retailmedia\preview\Model\EntityResourceOutcomeOfRetailMediaAccountV2**](../Model/EntityResourceOutcomeOfRetailMediaAccountV2.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `grantThirdPartyConsent()`

```php
grantThirdPartyConsent($account_id, $grant_consent_input)
```

/preview/retail-media/accounts/{accountId}/grant-third-party-consent

Grant third-party consent to a business application on behalf of a Private Market demand account

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\ThirdPartyAccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | The demand account ID on which to grant consent
$grant_consent_input = new \criteo\api\retailmedia\preview\Model\GrantConsentInput(); // \criteo\api\retailmedia\preview\Model\GrantConsentInput | The request input containing clientId, callbackURL, and callbackState

try {
    $apiInstance->grantThirdPartyConsent($account_id, $grant_consent_input);
} catch (Exception $e) {
    echo 'Exception when calling ThirdPartyAccountsApi->grantThirdPartyConsent: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| The demand account ID on which to grant consent | |
| **grant_consent_input** | [**\criteo\api\retailmedia\preview\Model\GrantConsentInput**](../Model/GrantConsentInput.md)| The request input containing clientId, callbackURL, and callbackState | [optional] |

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

## `removeThirdPartyAccountBrand()`

```php
removeThirdPartyAccountBrand($account_id, $brand_id): \criteo\api\retailmedia\preview\Model\ValueResourceOutcomeOfRetailMediaBrands
```

/preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove

Attempt to remove the provided brand from the account.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\ThirdPartyAccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | account id to remove brand from
$brand_id = 'brand_id_example'; // string | brand to remove

try {
    $result = $apiInstance->removeThirdPartyAccountBrand($account_id, $brand_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ThirdPartyAccountsApi->removeThirdPartyAccountBrand: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| account id to remove brand from | |
| **brand_id** | **string**| brand to remove | |

### Return type

[**\criteo\api\retailmedia\preview\Model\ValueResourceOutcomeOfRetailMediaBrands**](../Model/ValueResourceOutcomeOfRetailMediaBrands.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateThirdPartyAccountSellers()`

```php
updateThirdPartyAccountSellers($account_id, $value_resource_collection_input_of_retail_media_seller): \criteo\api\retailmedia\preview\Model\ValueResourceCollectionOutcomeOfRetailMediaSeller
```

/preview/retail-media/third-party-accounts/{accountId}/sellers

Update the list of sellers mapped to the account. This will override any existing mappings.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\ThirdPartyAccountsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | accountId to update sellers for
$value_resource_collection_input_of_retail_media_seller = new \criteo\api\retailmedia\preview\Model\ValueResourceCollectionInputOfRetailMediaSeller(); // \criteo\api\retailmedia\preview\Model\ValueResourceCollectionInputOfRetailMediaSeller | 

try {
    $result = $apiInstance->updateThirdPartyAccountSellers($account_id, $value_resource_collection_input_of_retail_media_seller);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ThirdPartyAccountsApi->updateThirdPartyAccountSellers: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| accountId to update sellers for | |
| **value_resource_collection_input_of_retail_media_seller** | [**\criteo\api\retailmedia\preview\Model\ValueResourceCollectionInputOfRetailMediaSeller**](../Model/ValueResourceCollectionInputOfRetailMediaSeller.md)|  | |

### Return type

[**\criteo\api\retailmedia\preview\Model\ValueResourceCollectionOutcomeOfRetailMediaSeller**](../Model/ValueResourceCollectionOutcomeOfRetailMediaSeller.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
