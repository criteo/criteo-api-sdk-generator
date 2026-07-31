# criteo\api\retailmedia\experimental\AnalyticsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**generateAsyncAccountsReportV2()**](AnalyticsApi.md#generateAsyncAccountsReportV2) | **POST** /experimental/retail-media/reports/accounts | /experimental/retail-media/reports/accounts |
| [**generateAsyncCampaignsReportV2()**](AnalyticsApi.md#generateAsyncCampaignsReportV2) | **POST** /experimental/retail-media/reports/campaigns | /experimental/retail-media/reports/campaigns |
| [**generateAsyncFillRateReport()**](AnalyticsApi.md#generateAsyncFillRateReport) | **POST** /experimental/retail-media/reports/fillrate | /experimental/retail-media/reports/fillrate |
| [**generateAsyncLineItemsReportV2()**](AnalyticsApi.md#generateAsyncLineItemsReportV2) | **POST** /experimental/retail-media/reports/line-items | /experimental/retail-media/reports/line-items |
| [**generateAsyncOffsiteReport()**](AnalyticsApi.md#generateAsyncOffsiteReport) | **POST** /experimental/retail-media/reports/offsite | /experimental/retail-media/reports/offsite |
| [**generateAsyncUnfilledPlacementsReport()**](AnalyticsApi.md#generateAsyncUnfilledPlacementsReport) | **POST** /experimental/retail-media/reports/unfilled-placements | /experimental/retail-media/reports/unfilled-placements |
| [**generateDigitalShelfIntelligenceInsight()**](AnalyticsApi.md#generateDigitalShelfIntelligenceInsight) | **POST** /experimental/retail-media/insights/digital-shelf-intelligence | /experimental/retail-media/insights/digital-shelf-intelligence |
| [**generateShareOfVoiceInsight()**](AnalyticsApi.md#generateShareOfVoiceInsight) | **POST** /experimental/retail-media/insights/share-of-voice | /experimental/retail-media/insights/share-of-voice |
| [**generateSyncAttributedTransactionsReport()**](AnalyticsApi.md#generateSyncAttributedTransactionsReport) | **POST** /experimental/retail-media/reports/sync/attributed-transactions | /experimental/retail-media/reports/sync/attributed-transactions |
| [**generateSyncCampaignsReport()**](AnalyticsApi.md#generateSyncCampaignsReport) | **POST** /experimental/retail-media/reports/sync/campaigns | /experimental/retail-media/reports/sync/campaigns |
| [**generateSyncLineItemsReport()**](AnalyticsApi.md#generateSyncLineItemsReport) | **POST** /experimental/retail-media/reports/sync/line-items | /experimental/retail-media/reports/sync/line-items |
| [**generateSyncRealTimePerformanceReport()**](AnalyticsApi.md#generateSyncRealTimePerformanceReport) | **POST** /experimental/retail-media/reports/sync/real-time-performance | /experimental/retail-media/reports/sync/real-time-performance |
| [**getAsyncExportOutput()**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /experimental/retail-media/reports/{reportId}/output | /experimental/retail-media/reports/{reportId}/output |
| [**getAsyncExportStatus()**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /experimental/retail-media/reports/{reportId}/status | /experimental/retail-media/reports/{reportId}/status |
| [**getInsightReportOutput()**](AnalyticsApi.md#getInsightReportOutput) | **GET** /experimental/retail-media/insights/{insightId}/output | /experimental/retail-media/insights/{insightId}/output |
| [**getInsightReportStatus()**](AnalyticsApi.md#getInsightReportStatus) | **GET** /experimental/retail-media/insights/{insightId}/status | /experimental/retail-media/insights/{insightId}/status |


## `generateAsyncAccountsReportV2()`

```php
generateAsyncAccountsReportV2($async_accounts_report_request): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/accounts

Returns an asynchronous Accounts Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_accounts_report_request = new \criteo\api\retailmedia\experimental\Model\AsyncAccountsReportRequest(); // \criteo\api\retailmedia\experimental\Model\AsyncAccountsReportRequest

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
| **async_accounts_report_request** | [**\criteo\api\retailmedia\experimental\Model\AsyncAccountsReportRequest**](../Model/AsyncAccountsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncCampaignsReportV2($async_campaigns_report_request): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/campaigns

Return an asynchronous Campaigns Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_campaigns_report_request = new \criteo\api\retailmedia\experimental\Model\AsyncCampaignsReportRequest(); // \criteo\api\retailmedia\experimental\Model\AsyncCampaignsReportRequest

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
| **async_campaigns_report_request** | [**\criteo\api\retailmedia\experimental\Model\AsyncCampaignsReportRequest**](../Model/AsyncCampaignsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncFillRateReport($async_fill_rate_report_request): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/fillrate

Returns an asynchronous Fill Rate Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_fill_rate_report_request = new \criteo\api\retailmedia\experimental\Model\AsyncFillRateReportRequest(); // \criteo\api\retailmedia\experimental\Model\AsyncFillRateReportRequest

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
| **async_fill_rate_report_request** | [**\criteo\api\retailmedia\experimental\Model\AsyncFillRateReportRequest**](../Model/AsyncFillRateReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncLineItemsReportV2($async_line_items_report_request): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/line-items

Returns an asynchronous Line Items Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_line_items_report_request = new \criteo\api\retailmedia\experimental\Model\AsyncLineItemsReportRequest(); // \criteo\api\retailmedia\experimental\Model\AsyncLineItemsReportRequest

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
| **async_line_items_report_request** | [**\criteo\api\retailmedia\experimental\Model\AsyncLineItemsReportRequest**](../Model/AsyncLineItemsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateAsyncOffsiteReport()`

```php
generateAsyncOffsiteReport($async_offsite_report_request): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/offsite

Returns an asynchronous Offsite Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_offsite_report_request = new \criteo\api\retailmedia\experimental\Model\AsyncOffsiteReportRequest(); // \criteo\api\retailmedia\experimental\Model\AsyncOffsiteReportRequest

try {
    $result = $apiInstance->generateAsyncOffsiteReport($async_offsite_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateAsyncOffsiteReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **async_offsite_report_request** | [**\criteo\api\retailmedia\experimental\Model\AsyncOffsiteReportRequest**](../Model/AsyncOffsiteReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

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
generateAsyncUnfilledPlacementsReport($async_unfilled_placements_report_request): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/unfilled-placements

Returns an asynchronous Unfilled Placements Report  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$async_unfilled_placements_report_request = new \criteo\api\retailmedia\experimental\Model\AsyncUnfilledPlacementsReportRequest(); // \criteo\api\retailmedia\experimental\Model\AsyncUnfilledPlacementsReportRequest

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
| **async_unfilled_placements_report_request** | [**\criteo\api\retailmedia\experimental\Model\AsyncUnfilledPlacementsReportRequest**](../Model/AsyncUnfilledPlacementsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateDigitalShelfIntelligenceInsight()`

```php
generateDigitalShelfIntelligenceInsight($digital_shelf_intelligence_insight_request): \criteo\api\retailmedia\experimental\Model\AsyncInsightResponse
```

/experimental/retail-media/insights/digital-shelf-intelligence

Generate a Digital Shelf Intelligence insight

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$digital_shelf_intelligence_insight_request = new \criteo\api\retailmedia\experimental\Model\DigitalShelfIntelligenceInsightRequest(); // \criteo\api\retailmedia\experimental\Model\DigitalShelfIntelligenceInsightRequest

try {
    $result = $apiInstance->generateDigitalShelfIntelligenceInsight($digital_shelf_intelligence_insight_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateDigitalShelfIntelligenceInsight: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **digital_shelf_intelligence_insight_request** | [**\criteo\api\retailmedia\experimental\Model\DigitalShelfIntelligenceInsightRequest**](../Model/DigitalShelfIntelligenceInsightRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncInsightResponse**](../Model/AsyncInsightResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `generateShareOfVoiceInsight()`

```php
generateShareOfVoiceInsight($share_of_voice_insight_request): \criteo\api\retailmedia\experimental\Model\AsyncInsightResponse
```

/experimental/retail-media/insights/share-of-voice

Generate a share of voice insight

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$share_of_voice_insight_request = new \criteo\api\retailmedia\experimental\Model\ShareOfVoiceInsightRequest(); // \criteo\api\retailmedia\experimental\Model\ShareOfVoiceInsightRequest

try {
    $result = $apiInstance->generateShareOfVoiceInsight($share_of_voice_insight_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->generateShareOfVoiceInsight: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **share_of_voice_insight_request** | [**\criteo\api\retailmedia\experimental\Model\ShareOfVoiceInsightRequest**](../Model/ShareOfVoiceInsightRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncInsightResponse**](../Model/AsyncInsightResponse.md)

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
generateSyncAttributedTransactionsReport($sync_attributed_transactions_report_request): \criteo\api\retailmedia\experimental\Model\ReportResponse
```

/experimental/retail-media/reports/sync/attributed-transactions

Returns a synchronous Attributed Transactions Report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_attributed_transactions_report_request = new \criteo\api\retailmedia\experimental\Model\SyncAttributedTransactionsReportRequest(); // \criteo\api\retailmedia\experimental\Model\SyncAttributedTransactionsReportRequest

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
| **sync_attributed_transactions_report_request** | [**\criteo\api\retailmedia\experimental\Model\SyncAttributedTransactionsReportRequest**](../Model/SyncAttributedTransactionsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ReportResponse**](../Model/ReportResponse.md)

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
generateSyncCampaignsReport($sync_campaigns_report_request): \criteo\api\retailmedia\experimental\Model\ReportResponse
```

/experimental/retail-media/reports/sync/campaigns

Returns a synchronous Campaigns Report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_campaigns_report_request = new \criteo\api\retailmedia\experimental\Model\SyncCampaignsReportRequest(); // \criteo\api\retailmedia\experimental\Model\SyncCampaignsReportRequest

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
| **sync_campaigns_report_request** | [**\criteo\api\retailmedia\experimental\Model\SyncCampaignsReportRequest**](../Model/SyncCampaignsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ReportResponse**](../Model/ReportResponse.md)

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
generateSyncLineItemsReport($sync_line_items_report_request): \criteo\api\retailmedia\experimental\Model\ReportResponse
```

/experimental/retail-media/reports/sync/line-items

Returns a synchronous Line Items Report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_line_items_report_request = new \criteo\api\retailmedia\experimental\Model\SyncLineItemsReportRequest(); // \criteo\api\retailmedia\experimental\Model\SyncLineItemsReportRequest

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
| **sync_line_items_report_request** | [**\criteo\api\retailmedia\experimental\Model\SyncLineItemsReportRequest**](../Model/SyncLineItemsReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ReportResponse**](../Model/ReportResponse.md)

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
generateSyncRealTimePerformanceReport($sync_real_time_performance_report_request): \criteo\api\retailmedia\experimental\Model\ReportResponse
```

/experimental/retail-media/reports/sync/real-time-performance

Returns a synchronous Real Time Performance Report. Returns empty rows; metadata includes dataCompleteThrough (latest time from streaming table in the request timezone).  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$sync_real_time_performance_report_request = new \criteo\api\retailmedia\experimental\Model\SyncRealTimePerformanceReportRequest(); // \criteo\api\retailmedia\experimental\Model\SyncRealTimePerformanceReportRequest

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
| **sync_real_time_performance_report_request** | [**\criteo\api\retailmedia\experimental\Model\SyncRealTimePerformanceReportRequest**](../Model/SyncRealTimePerformanceReportRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\ReportResponse**](../Model/ReportResponse.md)

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

/experimental/retail-media/reports/{reportId}/output

Returns the output of an async report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
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
getAsyncExportStatus($report_id): \criteo\api\retailmedia\experimental\Model\AsyncReportResponse
```

/experimental/retail-media/reports/{reportId}/status

Returns the status of an async report

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
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

[**\criteo\api\retailmedia\experimental\Model\AsyncReportResponse**](../Model/AsyncReportResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getInsightReportOutput()`

```php
getInsightReportOutput($insight_id): \SplFileObject
```

/experimental/retail-media/insights/{insightId}/output

Returns the output of an async insight

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$insight_id = 'insight_id_example'; // string | The ID of the asynchronous insight report. Must be a valid ID format.

try {
    $result = $apiInstance->getInsightReportOutput($insight_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getInsightReportOutput: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **insight_id** | **string**| The ID of the asynchronous insight report. Must be a valid ID format. | |

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

## `getInsightReportStatus()`

```php
getInsightReportStatus($insight_id): \criteo\api\retailmedia\experimental\Model\AsyncInsightResponse
```

/experimental/retail-media/insights/{insightId}/status

Returns the status of an async insight

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$insight_id = 'insight_id_example'; // string | The ID of the asynchronous insight report. Must be a valid ID format.

try {
    $result = $apiInstance->getInsightReportStatus($insight_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getInsightReportStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **insight_id** | **string**| The ID of the asynchronous insight report. Must be a valid ID format. | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\AsyncInsightResponse**](../Model/AsyncInsightResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
