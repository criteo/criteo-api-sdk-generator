# criteo\api\retailmedia\v2026_01\BillingApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createPartnerBillingReportRequestV1()**](BillingApi.md#createPartnerBillingReportRequestV1) | **POST** /2026-01/retail-media/billing/partner-report | /2026-01/retail-media/billing/partner-report |
| [**getPartnerBillingReportOutputV1()**](BillingApi.md#getPartnerBillingReportOutputV1) | **GET** /2026-01/retail-media/billing/partner-report/{requestId}/output | /2026-01/retail-media/billing/partner-report/{requestId}/output |
| [**getPartnerBillingReportStatusV1()**](BillingApi.md#getPartnerBillingReportStatusV1) | **GET** /2026-01/retail-media/billing/partner-report/{requestId}/status | /2026-01/retail-media/billing/partner-report/{requestId}/status |


## `createPartnerBillingReportRequestV1()`

```php
createPartnerBillingReportRequestV1($value_resource_input_partner_billing_report_request_v1): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomePartnerBillingReportStatusV1
```

/2026-01/retail-media/billing/partner-report

Create a Partner Billing Report request.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BillingApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$value_resource_input_partner_billing_report_request_v1 = new \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputPartnerBillingReportRequestV1(); // \criteo\api\retailmedia\v2026_01\Model\ValueResourceInputPartnerBillingReportRequestV1 | Partner Billing Report request object.

try {
    $result = $apiInstance->createPartnerBillingReportRequestV1($value_resource_input_partner_billing_report_request_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BillingApi->createPartnerBillingReportRequestV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **value_resource_input_partner_billing_report_request_v1** | [**\criteo\api\retailmedia\v2026_01\Model\ValueResourceInputPartnerBillingReportRequestV1**](../Model/ValueResourceInputPartnerBillingReportRequestV1.md)| Partner Billing Report request object. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomePartnerBillingReportStatusV1**](../Model/EntityResourceOutcomePartnerBillingReportStatusV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPartnerBillingReportOutputV1()`

```php
getPartnerBillingReportOutputV1($request_id): \SplFileObject
```

/2026-01/retail-media/billing/partner-report/{requestId}/output

Get the output of an existing Partner Billing Report.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BillingApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$request_id = 'request_id_example'; // string | The id of a Partner Billing Report request.

try {
    $result = $apiInstance->getPartnerBillingReportOutputV1($request_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BillingApi->getPartnerBillingReportOutputV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **string**| The id of a Partner Billing Report request. | |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/csv`, `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPartnerBillingReportStatusV1()`

```php
getPartnerBillingReportStatusV1($request_id): \criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomePartnerBillingReportStatusV1
```

/2026-01/retail-media/billing/partner-report/{requestId}/status

Get the status of an existing Partner Billing Report.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\BillingApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$request_id = 'request_id_example'; // string | The id of a Partner Billing Report request.

try {
    $result = $apiInstance->getPartnerBillingReportStatusV1($request_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling BillingApi->getPartnerBillingReportStatusV1: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **request_id** | **string**| The id of a Partner Billing Report request. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\EntityResourceOutcomePartnerBillingReportStatusV1**](../Model/EntityResourceOutcomePartnerBillingReportStatusV1.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
