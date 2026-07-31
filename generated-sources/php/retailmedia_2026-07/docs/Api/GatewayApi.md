# criteo\api\retailmedia\v2026_07\GatewayApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getCurrentApplication()**](GatewayApi.md#getCurrentApplication) | **GET** /2026-07/retail-media/me | /2026-07/retail-media/me |


## `getCurrentApplication()`

```php
getCurrentApplication(): \criteo\api\retailmedia\v2026_07\Model\ApplicationSummaryModelResponse
```

/2026-07/retail-media/me

Get information about the currently logged application

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_07\Api\GatewayApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $result = $apiInstance->getCurrentApplication();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling GatewayApi->getCurrentApplication: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**\criteo\api\retailmedia\v2026_07\Model\ApplicationSummaryModelResponse**](../Model/ApplicationSummaryModelResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
