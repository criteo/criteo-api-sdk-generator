# criteo\api\retailmedia\v2027_01\AnalyticsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**generateAsyncAttributedTransactionsReport()**](AnalyticsApi.md#generateAsyncAttributedTransactionsReport) | **POST** /2027-01/retail-media/reports/attributed-transactions | /2027-01/retail-media/reports/attributed-transactions |
| [**generateAsyncFillRateReport()**](AnalyticsApi.md#generateAsyncFillRateReport) | **POST** /2027-01/retail-media/reports/fillrate | /2027-01/retail-media/reports/fillrate |
| [**generateAsyncMissedOpportunitiesReport()**](AnalyticsApi.md#generateAsyncMissedOpportunitiesReport) | **POST** /2027-01/retail-media/reports/missed-opportunities | /2027-01/retail-media/reports/missed-opportunities |
| [**generateAsyncPerformanceReport()**](AnalyticsApi.md#generateAsyncPerformanceReport) | **POST** /2027-01/retail-media/reports/performance | /2027-01/retail-media/reports/performance |
| [**generateAsyncRevenueReport()**](AnalyticsApi.md#generateAsyncRevenueReport) | **POST** /2027-01/retail-media/reports/revenue | /2027-01/retail-media/reports/revenue |
| [**generateAsyncUnfilledPlacementsReport()**](AnalyticsApi.md#generateAsyncUnfilledPlacementsReport) | **POST** /2027-01/retail-media/reports/unfilled-placements | /2027-01/retail-media/reports/unfilled-placements |
| [**generateSyncAttributedTransactionsReport()**](AnalyticsApi.md#generateSyncAttributedTransactionsReport) | **POST** /2027-01/retail-media/reports/sync/attributed-transactions | /2027-01/retail-media/reports/sync/attributed-transactions |
| [**generateSyncCampaignsReport()**](AnalyticsApi.md#generateSyncCampaignsReport) | **POST** /2027-01/retail-media/reports/sync/campaigns | /2027-01/retail-media/reports/sync/campaigns |
| [**generateSyncLineItemsReport()**](AnalyticsApi.md#generateSyncLineItemsReport) | **POST** /2027-01/retail-media/reports/sync/line-items | /2027-01/retail-media/reports/sync/line-items |
| [**generateSyncRealTimePerformanceReport()**](AnalyticsApi.md#generateSyncRealTimePerformanceReport) | **POST** /2027-01/retail-media/reports/sync/real-time-performance | /2027-01/retail-media/reports/sync/real-time-performance |
| [**getAsyncExportOutput()**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /2027-01/retail-media/reports/{reportId}/output | /2027-01/retail-media/reports/{reportId}/output |
| [**getAsyncExportStatus()**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /2027-01/retail-media/reports/{reportId}/status | /2027-01/retail-media/reports/{reportId}/status |


## `generateAsyncAttributedTransactionsReport()`

```php
generateAsyncAttributedTransactionsReport($async_attributed_transactions_report_request): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/attributed-transactions

Creates an attributed-transactions async report. The request accepts explicit attributed-transaction dimensions, metrics, and filters.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_attributed_transactions_report_request = new \criteo\api\retailmedia\v2027_01\Model\AsyncAttributedTransactionsReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\AsyncAttributedTransactionsReportRequest

try {
    $result = $apiInstance->generateAsyncAttributedTransactionsReport($async_attributed_transactions_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncAttributedTransactionsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_attributed_transactions_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\AsyncAttributedTransactionsReportRequest**](../Model/AsyncAttributedTransactionsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncFillRateReport($async_fill_rate_report_request): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_fill_rate_report_request = new \criteo\api\retailmedia\v2027_01\Model\AsyncFillRateReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\AsyncFillRateReportRequest

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
| **async_fill_rate_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\AsyncFillRateReportRequest**](../Model/AsyncFillRateReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncMissedOpportunitiesReport()`

```php
generateAsyncMissedOpportunitiesReport($async_missed_opportunities_report_request): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/missed-opportunities

Creates a missed-opportunities async report. The request accepts explicit missed-opportunities dimensions, metrics, and filters.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_missed_opportunities_report_request = new \criteo\api\retailmedia\v2027_01\Model\AsyncMissedOpportunitiesReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\AsyncMissedOpportunitiesReportRequest

try {
    $result = $apiInstance->generateAsyncMissedOpportunitiesReport($async_missed_opportunities_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncMissedOpportunitiesReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_missed_opportunities_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\AsyncMissedOpportunitiesReportRequest**](../Model/AsyncMissedOpportunitiesReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncPerformanceReport()`

```php
generateAsyncPerformanceReport($async_performance_report_request): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/performance

Creates a performance DSP analytics async report. Dimensions and metrics select the output schema, and filters constrain eligible data.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_performance_report_request = new \criteo\api\retailmedia\v2027_01\Model\AsyncPerformanceReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\AsyncPerformanceReportRequest

try {
    $result = $apiInstance->generateAsyncPerformanceReport($async_performance_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncPerformanceReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_performance_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\AsyncPerformanceReportRequest**](../Model/AsyncPerformanceReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncRevenueReport($async_revenue_report_request): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/revenue

Returns an asynchronous Revenue Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_revenue_report_request = new \criteo\api\retailmedia\v2027_01\Model\AsyncRevenueReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\AsyncRevenueReportRequest

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
| **async_revenue_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\AsyncRevenueReportRequest**](../Model/AsyncRevenueReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncUnfilledPlacementsReport($async_unfilled_placements_report_request): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_unfilled_placements_report_request = new \criteo\api\retailmedia\v2027_01\Model\AsyncUnfilledPlacementsReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\AsyncUnfilledPlacementsReportRequest

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
| **async_unfilled_placements_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\AsyncUnfilledPlacementsReportRequest**](../Model/AsyncUnfilledPlacementsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateSyncAttributedTransactionsReport()`

```php
generateSyncAttributedTransactionsReport($sync_attributed_transactions_report_request): \criteo\api\retailmedia\v2027_01\Model\ReportResponse
```

/2027-01/retail-media/reports/sync/attributed-transactions

Returns a synchronous Attributed Transactions Report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_attributed_transactions_report_request = new \criteo\api\retailmedia\v2027_01\Model\SyncAttributedTransactionsReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\SyncAttributedTransactionsReportRequest

try {
    $result = $apiInstance->generateSyncAttributedTransactionsReport($sync_attributed_transactions_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateSyncAttributedTransactionsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sync_attributed_transactions_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\SyncAttributedTransactionsReportRequest**](../Model/SyncAttributedTransactionsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\ReportResponse**](../Model/ReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateSyncCampaignsReport()`

```php
generateSyncCampaignsReport($sync_campaigns_report_request): \criteo\api\retailmedia\v2027_01\Model\ReportResponse
```

/2027-01/retail-media/reports/sync/campaigns

Returns a synchronous Campaigns Report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_campaigns_report_request = new \criteo\api\retailmedia\v2027_01\Model\SyncCampaignsReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\SyncCampaignsReportRequest

try {
    $result = $apiInstance->generateSyncCampaignsReport($sync_campaigns_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateSyncCampaignsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sync_campaigns_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\SyncCampaignsReportRequest**](../Model/SyncCampaignsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\ReportResponse**](../Model/ReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateSyncLineItemsReport()`

```php
generateSyncLineItemsReport($sync_line_items_report_request): \criteo\api\retailmedia\v2027_01\Model\ReportResponse
```

/2027-01/retail-media/reports/sync/line-items

Returns a synchronous Line Items Report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_line_items_report_request = new \criteo\api\retailmedia\v2027_01\Model\SyncLineItemsReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\SyncLineItemsReportRequest

try {
    $result = $apiInstance->generateSyncLineItemsReport($sync_line_items_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateSyncLineItemsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sync_line_items_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\SyncLineItemsReportRequest**](../Model/SyncLineItemsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\ReportResponse**](../Model/ReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateSyncRealTimePerformanceReport()`

```php
generateSyncRealTimePerformanceReport($sync_real_time_performance_report_request): \criteo\api\retailmedia\v2027_01\Model\ReportResponse
```

/2027-01/retail-media/reports/sync/real-time-performance

Returns a synchronous Real Time Performance Report. Returns empty rows; metadata includes dataCompleteThrough (latest time from streaming table in the request timezone).  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_real_time_performance_report_request = new \criteo\api\retailmedia\v2027_01\Model\SyncRealTimePerformanceReportRequest(); // \criteo\api\retailmedia\v2027_01\Model\SyncRealTimePerformanceReportRequest

try {
    $result = $apiInstance->generateSyncRealTimePerformanceReport($sync_real_time_performance_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateSyncRealTimePerformanceReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sync_real_time_performance_report_request** | [**\criteo\api\retailmedia\v2027_01\Model\SyncRealTimePerformanceReportRequest**](../Model/SyncRealTimePerformanceReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2027_01\Model\ReportResponse**](../Model/ReportResponse.md)

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

/2027-01/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
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
getAsyncExportStatus($report_id): \criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse
```

/2027-01/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2027_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2027_01\Api\AnalyticsApi(
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

[**\criteo\api\retailmedia\v2027_01\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
