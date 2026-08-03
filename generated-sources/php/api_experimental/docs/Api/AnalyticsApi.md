# criteo\api\api\experimental\AnalyticsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**postInheritance()**](AnalyticsApi.md#postInheritance) | **POST** /experimental/sample/testing/inheritance | /experimental/sample/testing/inheritance |
| [**postPolymorphicList()**](AnalyticsApi.md#postPolymorphicList) | **POST** /experimental/sample/testing/polymorphic-list | /experimental/sample/testing/polymorphic-list |
| [**postPolymorphism()**](AnalyticsApi.md#postPolymorphism) | **POST** /experimental/sample/testing/polymorphism | /experimental/sample/testing/polymorphism |


## `postInheritance()`

```php
postInheritance($derived_type_one_request): \criteo\api\api\experimental\Model\DerivedTypeOneResponse
```

/experimental/sample/testing/inheritance

Echoes a concrete derived type (plain inheritance / allOf).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\api\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\api\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\api\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$derived_type_one_request = new \criteo\api\api\experimental\Model\DerivedTypeOneRequest(); // \criteo\api\api\experimental\Model\DerivedTypeOneRequest

try {
    $result = $apiInstance->postInheritance($derived_type_one_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->postInheritance: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **derived_type_one_request** | [**\criteo\api\api\experimental\Model\DerivedTypeOneRequest**](../Model/DerivedTypeOneRequest.md)|  | [optional] |

### Return type

[**\criteo\api\api\experimental\Model\DerivedTypeOneResponse**](../Model/DerivedTypeOneResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postPolymorphicList()`

```php
postPolymorphicList($base_type_list_request): \criteo\api\api\experimental\Model\BaseTypeListResponse
```

/experimental/sample/testing/polymorphic-list

Echoes a list of the polymorphic types.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\api\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\api\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\api\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$base_type_list_request = new \criteo\api\api\experimental\Model\BaseTypeListRequest(); // \criteo\api\api\experimental\Model\BaseTypeListRequest

try {
    $result = $apiInstance->postPolymorphicList($base_type_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->postPolymorphicList: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_type_list_request** | [**\criteo\api\api\experimental\Model\BaseTypeListRequest**](../Model/BaseTypeListRequest.md)|  | [optional] |

### Return type

[**\criteo\api\api\experimental\Model\BaseTypeListResponse**](../Model/BaseTypeListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `postPolymorphism()`

```php
postPolymorphism($base_type_request): \criteo\api\api\experimental\Model\BaseTypeResponse
```

/experimental/sample/testing/polymorphism

Echoes a polymorphic type (allOf + discriminator).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\api\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\api\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\api\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$base_type_request = new \criteo\api\api\experimental\Model\BaseTypeRequest(); // \criteo\api\api\experimental\Model\BaseTypeRequest

try {
    $result = $apiInstance->postPolymorphism($base_type_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->postPolymorphism: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **base_type_request** | [**\criteo\api\api\experimental\Model\BaseTypeRequest**](../Model/BaseTypeRequest.md)|  | [optional] |

### Return type

[**\criteo\api\api\experimental\Model\BaseTypeResponse**](../Model/BaseTypeResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
