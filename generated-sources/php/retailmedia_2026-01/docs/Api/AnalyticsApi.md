# criteo\api\retailmedia\v2026_01\AnalyticsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**generateAsyncAccountsReportV2()**](AnalyticsApi.md#generateAsyncAccountsReportV2) | **POST** /2026-01/retail-media/reports/accounts | /2026-01/retail-media/reports/accounts |
| [**generateAsyncCampaignsReportV2()**](AnalyticsApi.md#generateAsyncCampaignsReportV2) | **POST** /2026-01/retail-media/reports/campaigns | /2026-01/retail-media/reports/campaigns |
| [**generateAsyncFillRateReport()**](AnalyticsApi.md#generateAsyncFillRateReport) | **POST** /2026-01/retail-media/reports/fillrate | /2026-01/retail-media/reports/fillrate |
| [**generateAsyncLineItemsReportV2()**](AnalyticsApi.md#generateAsyncLineItemsReportV2) | **POST** /2026-01/retail-media/reports/line-items | /2026-01/retail-media/reports/line-items |
| [**generateAsyncRevenueReport()**](AnalyticsApi.md#generateAsyncRevenueReport) | **POST** /2026-01/retail-media/reports/revenue | /2026-01/retail-media/reports/revenue |
| [**generateAsyncUnfilledPlacementsReport()**](AnalyticsApi.md#generateAsyncUnfilledPlacementsReport) | **POST** /2026-01/retail-media/reports/unfilled-placements | /2026-01/retail-media/reports/unfilled-placements |
| [**getAsyncExportOutput()**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /2026-01/retail-media/reports/{reportId}/output | /2026-01/retail-media/reports/{reportId}/output |
| [**getAsyncExportStatus()**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /2026-01/retail-media/reports/{reportId}/status | /2026-01/retail-media/reports/{reportId}/status |


## `generateAsyncAccountsReportV2()`

```php
generateAsyncAccountsReportV2($async_accounts_report_request): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/accounts

Returns an asynchronous Accounts Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_accounts_report_request = new \criteo\api\retailmedia\v2026_01\Model\AsyncAccountsReportRequest(); // \criteo\api\retailmedia\v2026_01\Model\AsyncAccountsReportRequest

try {
    $result = $apiInstance->generateAsyncAccountsReportV2($async_accounts_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncAccountsReportV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_accounts_report_request** | [**\criteo\api\retailmedia\v2026_01\Model\AsyncAccountsReportRequest**](../Model/AsyncAccountsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncCampaignsReportV2()`

```php
generateAsyncCampaignsReportV2($async_campaigns_report_request): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/campaigns

Return an asynchronous Campaigns Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_campaigns_report_request = new \criteo\api\retailmedia\v2026_01\Model\AsyncCampaignsReportRequest(); // \criteo\api\retailmedia\v2026_01\Model\AsyncCampaignsReportRequest

try {
    $result = $apiInstance->generateAsyncCampaignsReportV2($async_campaigns_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncCampaignsReportV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_campaigns_report_request** | [**\criteo\api\retailmedia\v2026_01\Model\AsyncCampaignsReportRequest**](../Model/AsyncCampaignsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncFillRateReport()`

```php
generateAsyncFillRateReport($async_fill_rate_report_request): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_fill_rate_report_request = new \criteo\api\retailmedia\v2026_01\Model\AsyncFillRateReportRequest(); // \criteo\api\retailmedia\v2026_01\Model\AsyncFillRateReportRequest

try {
    $result = $apiInstance->generateAsyncFillRateReport($async_fill_rate_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncFillRateReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_fill_rate_report_request** | [**\criteo\api\retailmedia\v2026_01\Model\AsyncFillRateReportRequest**](../Model/AsyncFillRateReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncLineItemsReportV2()`

```php
generateAsyncLineItemsReportV2($async_line_items_report_request): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/line-items

Returns an asynchronous Line Items Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_line_items_report_request = new \criteo\api\retailmedia\v2026_01\Model\AsyncLineItemsReportRequest(); // \criteo\api\retailmedia\v2026_01\Model\AsyncLineItemsReportRequest

try {
    $result = $apiInstance->generateAsyncLineItemsReportV2($async_line_items_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncLineItemsReportV2: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_line_items_report_request** | [**\criteo\api\retailmedia\v2026_01\Model\AsyncLineItemsReportRequest**](../Model/AsyncLineItemsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncRevenueReport()`

```php
generateAsyncRevenueReport($async_revenue_report_request): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/revenue

Returns an asynchronous Revenue Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_revenue_report_request = new \criteo\api\retailmedia\v2026_01\Model\AsyncRevenueReportRequest(); // \criteo\api\retailmedia\v2026_01\Model\AsyncRevenueReportRequest

try {
    $result = $apiInstance->generateAsyncRevenueReport($async_revenue_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncRevenueReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_revenue_report_request** | [**\criteo\api\retailmedia\v2026_01\Model\AsyncRevenueReportRequest**](../Model/AsyncRevenueReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncUnfilledPlacementsReport()`

```php
generateAsyncUnfilledPlacementsReport($async_unfilled_placements_report_request): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_unfilled_placements_report_request = new \criteo\api\retailmedia\v2026_01\Model\AsyncUnfilledPlacementsReportRequest(); // \criteo\api\retailmedia\v2026_01\Model\AsyncUnfilledPlacementsReportRequest

try {
    $result = $apiInstance->generateAsyncUnfilledPlacementsReport($async_unfilled_placements_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncUnfilledPlacementsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_unfilled_placements_report_request** | [**\criteo\api\retailmedia\v2026_01\Model\AsyncUnfilledPlacementsReportRequest**](../Model/AsyncUnfilledPlacementsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAsyncExportOutput()`

```php
getAsyncExportOutput($report_id): \SplFileObject
```

/2026-01/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | The ID of the report to retrieve

try {
    $result = $apiInstance->getAsyncExportOutput($report_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAsyncExportOutput: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **report_id** | **string**| The ID of the report to retrieve | |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAsyncExportStatus()`

```php
getAsyncExportStatus($report_id): \criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse
```

/2026-01/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | The ID of the report to retrieve

try {
    $result = $apiInstance->getAsyncExportStatus($report_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAsyncExportStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **report_id** | **string**| The ID of the report to retrieve | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
