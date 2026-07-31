# criteo\api\marketingsolutions\preview\AnalyticsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**createAllProductsExport()**](AnalyticsApi.md#createAllProductsExport) | **POST** /preview/marketing-solutions/report/products/export | /preview/marketing-solutions/report/products/export |
| [**createRealtimeProductReport()**](AnalyticsApi.md#createRealtimeProductReport) | **POST** /preview/marketing-solutions/marketplace-performance-outcomes/stats/realtime-reports/export | /preview/marketing-solutions/marketplace-performance-outcomes/stats/realtime-reports/export |
| [**downloadAllProductsExport()**](AnalyticsApi.md#downloadAllProductsExport) | **GET** /preview/marketing-solutions/report/products/{reportId} | /preview/marketing-solutions/report/products/{reportId} |
| [**getAdsetReport()**](AnalyticsApi.md#getAdsetReport) | **POST** /preview/statistics/report | /preview/statistics/report |
| [**getAsyncAdsetReport()**](AnalyticsApi.md#getAsyncAdsetReport) | **POST** /preview/reports/async-statistics | /preview/reports/async-statistics |
| [**getAsyncAudienceReport()**](AnalyticsApi.md#getAsyncAudienceReport) | **POST** /preview/reports/async-audience-performance | /preview/reports/async-audience-performance |
| [**getAsyncExportOutput()**](AnalyticsApi.md#getAsyncExportOutput) | **GET** /preview/reports/{report-id}/output | /preview/reports/{report-id}/output |
| [**getAsyncExportStatus()**](AnalyticsApi.md#getAsyncExportStatus) | **GET** /preview/reports/{report-id}/status | /preview/reports/{report-id}/status |
| [**getCategoriesReport()**](AnalyticsApi.md#getCategoriesReport) | **POST** /preview/categories/report | /preview/categories/report |
| [**getCreativesReport()**](AnalyticsApi.md#getCreativesReport) | **POST** /preview/reports/creatives | /preview/reports/creatives |
| [**getExportStatus()**](AnalyticsApi.md#getExportStatus) | **GET** /preview/marketing-solutions/report-jobs/{reportId} | /preview/marketing-solutions/report-jobs/{reportId} |
| [**getMarketplacePerformanceOutcomesExportStatus()**](AnalyticsApi.md#getMarketplacePerformanceOutcomesExportStatus) | **GET** /preview/marketing-solutions/marketplace-performance-outcomes/stats/report-jobs/{reportId} | /preview/marketing-solutions/marketplace-performance-outcomes/stats/report-jobs/{reportId} |
| [**getPlacementsReport()**](AnalyticsApi.md#getPlacementsReport) | **POST** /preview/placements/report | /preview/placements/report |
| [**getRealtimeProduct()**](AnalyticsApi.md#getRealtimeProduct) | **GET** /preview/marketing-solutions/marketplace-performance-outcomes/stats/realtime-reports/{reportId} | /preview/marketing-solutions/marketplace-performance-outcomes/stats/realtime-reports/{reportId} |
| [**getRealtimeStatisticsReport()**](AnalyticsApi.md#getRealtimeStatisticsReport) | **POST** /preview/reports/realtime | /preview/reports/realtime |
| [**getTopProductsReport()**](AnalyticsApi.md#getTopProductsReport) | **POST** /preview/reports/top-products | /preview/reports/top-products |
| [**getTransactionsReport()**](AnalyticsApi.md#getTransactionsReport) | **POST** /preview/transactions/report | /preview/transactions/report |
| [**getTransparencyReport()**](AnalyticsApi.md#getTransparencyReport) | **POST** /preview/log-level/advertisers/{advertiser-id}/report | /preview/log-level/advertisers/{advertiser-id}/report |


## `createAllProductsExport()`

```php
createAllProductsExport($generate_all_products_report_request_attributes_request): \criteo\api\marketingsolutions\preview\Model\ExportStatusModelResponse
```

/preview/marketing-solutions/report/products/export

Creates an all-products report export job.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_all_products_report_request_attributes_request = new \criteo\api\marketingsolutions\preview\Model\GenerateAllProductsReportRequestAttributesRequest(); // \criteo\api\marketingsolutions\preview\Model\GenerateAllProductsReportRequestAttributesRequest | The all-products report export request.

try {
    $result = $apiInstance->createAllProductsExport($generate_all_products_report_request_attributes_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->createAllProductsExport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_all_products_report_request_attributes_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateAllProductsReportRequestAttributesRequest**](../Model/GenerateAllProductsReportRequestAttributesRequest.md)| The all-products report export request. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ExportStatusModelResponse**](../Model/ExportStatusModelResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createRealtimeProductReport()`

```php
createRealtimeProductReport($real_time_product_report_job_request): \criteo\api\marketingsolutions\preview\Model\RealTimeProductReportJobStatusResponse
```

/preview/marketing-solutions/marketplace-performance-outcomes/stats/realtime-reports/export

Creates a marketplace performance outcomes realtime report export.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$real_time_product_report_job_request = new \criteo\api\marketingsolutions\preview\Model\RealTimeProductReportJobRequest(); // \criteo\api\marketingsolutions\preview\Model\RealTimeProductReportJobRequest | The realtime report export request.

try {
    $result = $apiInstance->createRealtimeProductReport($real_time_product_report_job_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->createRealtimeProductReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **real_time_product_report_job_request** | [**\criteo\api\marketingsolutions\preview\Model\RealTimeProductReportJobRequest**](../Model/RealTimeProductReportJobRequest.md)| The realtime report export request. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\RealTimeProductReportJobStatusResponse**](../Model/RealTimeProductReportJobStatusResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `downloadAllProductsExport()`

```php
downloadAllProductsExport($report_id): \SplFileObject
```

/preview/marketing-solutions/report/products/{reportId}

Downloads the generated all-products report export.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | The identifier of the all-products report export.

try {
    $result = $apiInstance->downloadAllProductsExport($report_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->downloadAllProductsExport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **report_id** | **string**| The identifier of the all-products report export. | |

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

## `getAdsetReport()`

```php
getAdsetReport($statistics_report_query_message): \SplFileObject
```

/preview/statistics/report

This Statistics endpoint provides ad set related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.  <br/><br/>  This endpoint supports data retrieval for up to two years in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$statistics_report_query_message = {"advertiserIds":"123,456,789","adSetIds":["12345","54321"],"adSetNames":["myAdSet1","myAdSet2"],"adSetStatus":["Active"],"dimensions":["CampaignId","Campaign","AdsetId","Adset","AdvertiserId","Advertiser","AdId","Ad","CouponId","Coupon","CategoryId","Category","Hour","Day","Week","Month","Year","Os","Device"],"metrics":["Clicks","Displays","Cpc","Visits"],"currency":"EUR","format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}; // \criteo\api\marketingsolutions\preview\Model\StatisticsReportQueryMessage

try {
    $result = $apiInstance->getAdsetReport($statistics_report_query_message);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAdsetReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **statistics_report_query_message** | [**\criteo\api\marketingsolutions\preview\Model\StatisticsReportQueryMessage**](../Model/StatisticsReportQueryMessage.md)|  | [optional] |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/csv`, `text/xml`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAsyncAdsetReport()`

```php
getAsyncAdsetReport($generate_statistics_report_request): \criteo\api\marketingsolutions\preview\Model\MarketingSolutionsReportStatusResponse
```

/preview/reports/async-statistics

This Statistics endpoint provides an export Id that let you retrieve data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_statistics_report_request = new \criteo\api\marketingsolutions\preview\Model\GenerateStatisticsReportRequest(); // \criteo\api\marketingsolutions\preview\Model\GenerateStatisticsReportRequest

try {
    $result = $apiInstance->getAsyncAdsetReport($generate_statistics_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAsyncAdsetReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_statistics_report_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateStatisticsReportRequest**](../Model/GenerateStatisticsReportRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\MarketingSolutionsReportStatusResponse**](../Model/MarketingSolutionsReportStatusResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAsyncAudienceReport()`

```php
getAsyncAudienceReport($generate_audience_performance_report_request): \criteo\api\marketingsolutions\preview\Model\MarketingSolutionsReportStatusResponse
```

/preview/reports/async-audience-performance

This Statistics endpoint provides an export Id that lets you retrieve data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_audience_performance_report_request = new \criteo\api\marketingsolutions\preview\Model\GenerateAudiencePerformanceReportRequest(); // \criteo\api\marketingsolutions\preview\Model\GenerateAudiencePerformanceReportRequest

try {
    $result = $apiInstance->getAsyncAudienceReport($generate_audience_performance_report_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAsyncAudienceReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_audience_performance_report_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateAudiencePerformanceReportRequest**](../Model/GenerateAudiencePerformanceReportRequest.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\MarketingSolutionsReportStatusResponse**](../Model/MarketingSolutionsReportStatusResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAsyncExportOutput()`

```php
getAsyncExportOutput($report_id): \criteo\api\marketingsolutions\preview\Model\ExportResult
```

/preview/reports/{report-id}/output

This endpoint gives you the output of the report.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | Id of the report

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
| **report_id** | **string**| Id of the report | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ExportResult**](../Model/ExportResult.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAsyncExportStatus()`

```php
getAsyncExportStatus($report_id): \criteo\api\marketingsolutions\preview\Model\MarketingSolutionsReportStatusResponse
```

/preview/reports/{report-id}/status

This endpoint gives you the status of the report.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | Id of the report

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
| **report_id** | **string**| Id of the report | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\MarketingSolutionsReportStatusResponse**](../Model/MarketingSolutionsReportStatusResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCategoriesReport()`

```php
getCategoriesReport($generate_categories_report_request_attributes_request): \SplFileObject
```

/preview/categories/report

With this endpoint you can analyse what are the categories of the placements' domains your ads are placed in.  <br/><br/>  This endpoint supports data retrieval for up to three months in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_categories_report_request_attributes_request = {"data":{"type":"GenerateCategoriesReport","attributes":{"advertiserIds":["123","456","789"],"campaignId":"111","adsetId":"135","domain":"example.com","category":"Example","shouldDisplayDomainDimension":true,"format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}}}; // \criteo\api\marketingsolutions\preview\Model\GenerateCategoriesReportRequestAttributesRequest

try {
    $result = $apiInstance->getCategoriesReport($generate_categories_report_request_attributes_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getCategoriesReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_categories_report_request_attributes_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateCategoriesReportRequestAttributesRequest**](../Model/GenerateCategoriesReportRequestAttributesRequest.md)|  | [optional] |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `text/csv`, `text/xml`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCreativesReport()`

```php
getCreativesReport($generate_creatives_report_request_attributes_request): \criteo\api\marketingsolutions\preview\Model\JsonReportRowsListResponse
```

/preview/reports/creatives

With Creatives endpoint, you can analyse the daily performances of your creatives on the main metrics: clicks, ctr, displays.  <br/><br/>  This endpoint supports data retrieval for up to two years in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_creatives_report_request_attributes_request = {"data":{"type":"GenerateCreativesReport","attributes":{"startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00","advertiserIds":["6666","7777"],"metrics":["Clicks","Ctr","Displays"],"dimensions":["SizeCategory","DisplaySize","AdFormat","Coupon","CouponId","Ad","AdId","Day","Hour"],"timezone":"Europe/Paris","adFormats":["Dynamic","Other formats"],"displaySizes":["LeaderBoard","LargeBanner"],"couponNames":["a coupon name"],"couponIds":["3333","5555"],"adNames":["Ad by Criteo team"],"adIds":["2222"],"campaignIds":["1111"],"adSetIds":["2222","3333"],"adSetStatus":["Active","NotRunning"]}}}; // \criteo\api\marketingsolutions\preview\Model\GenerateCreativesReportRequestAttributesRequest

try {
    $result = $apiInstance->getCreativesReport($generate_creatives_report_request_attributes_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getCreativesReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_creatives_report_request_attributes_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateCreativesReportRequestAttributesRequest**](../Model/GenerateCreativesReportRequestAttributesRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\JsonReportRowsListResponse**](../Model/JsonReportRowsListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getExportStatus()`

```php
getExportStatus($report_id): \criteo\api\marketingsolutions\preview\Model\ExportStatusModelResponse
```

/preview/marketing-solutions/report-jobs/{reportId}

Gets the status of  report export job.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | The identifier of the report export job.

try {
    $result = $apiInstance->getExportStatus($report_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getExportStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **report_id** | **string**| The identifier of the report export job. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ExportStatusModelResponse**](../Model/ExportStatusModelResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getMarketplacePerformanceOutcomesExportStatus()`

```php
getMarketplacePerformanceOutcomesExportStatus($report_id): \criteo\api\marketingsolutions\preview\Model\ExportStatusModelResponse
```

/preview/marketing-solutions/marketplace-performance-outcomes/stats/report-jobs/{reportId}

Gets the status of  report export job.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | The identifier of the report export job.

try {
    $result = $apiInstance->getMarketplacePerformanceOutcomesExportStatus($report_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getMarketplacePerformanceOutcomesExportStatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **report_id** | **string**| The identifier of the report export job. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ExportStatusModelResponse**](../Model/ExportStatusModelResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getPlacementsReport()`

```php
getPlacementsReport($placements_report_query_message_list_request): \SplFileObject
```

/preview/placements/report

Your ads are placed in different domains (publishers) and environments (websites and apps). Thanks to the placements endpoint, you can analyse the performances for each publisher, comparing displays, clicks and sales generated.  <br/><br/>  This endpoint supports data retrieval for up to three months in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$placements_report_query_message_list_request = {"data":[{"type":"report","attributes":{"advertiserIds":"123,456,789","campaignIds":"111,222,333,444","adsetIds":"135,246,357,468","environment":"Web","placement":"MyPlacement","dimensions":["AdsetId","AdvertiserId","Placement"],"metrics":["Clicks","Displays","Cost"],"currency":"EUR","disclosed":false,"format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}}]}; // \criteo\api\marketingsolutions\preview\Model\PlacementsReportQueryMessageListRequest

try {
    $result = $apiInstance->getPlacementsReport($placements_report_query_message_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getPlacementsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **placements_report_query_message_list_request** | [**\criteo\api\marketingsolutions\preview\Model\PlacementsReportQueryMessageListRequest**](../Model/PlacementsReportQueryMessageListRequest.md)|  | [optional] |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `text/csv`, `text/xml`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRealtimeProduct()`

```php
getRealtimeProduct($report_id): \criteo\api\marketingsolutions\preview\Model\FileStreamResultResponse
```

/preview/marketing-solutions/marketplace-performance-outcomes/stats/realtime-reports/{reportId}

Downloads the generated marketplace performance outcomes realtime report export.  <br />  This endpoint is subject to specific rate limits.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$report_id = 'report_id_example'; // string | The identifier of the realtime report export.

try {
    $result = $apiInstance->getRealtimeProduct($report_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getRealtimeProduct: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **report_id** | **string**| The identifier of the realtime report export. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\FileStreamResultResponse**](../Model/FileStreamResultResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getRealtimeStatisticsReport()`

```php
getRealtimeStatisticsReport($generate_realtime_statistics_report_request_attributes_request): \criteo\api\marketingsolutions\preview\Model\JsonReportRowsListResponse
```

/preview/reports/realtime

With Realtime endpoint, you can analyse the realtime values of the main metrics: displays, clicks, cost.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_realtime_statistics_report_request_attributes_request = {"data":{"type":"GenerateRealtimeStatisticsReport","attributes":{"advertiserIds":["123","456"],"campaignIds":["111"],"adsetIds":["135"],"dimensions":["AdvertiserId","Advertiser","CampaignId","Campaign","AdsetId","Adset","Day","Hour"],"metrics":["Displays","Clicks","Cost"],"lookbackWindow":12,"currency":"EUR","timezone":"Europe/Paris"}}}; // \criteo\api\marketingsolutions\preview\Model\GenerateRealtimeStatisticsReportRequestAttributesRequest

try {
    $result = $apiInstance->getRealtimeStatisticsReport($generate_realtime_statistics_report_request_attributes_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getRealtimeStatisticsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_realtime_statistics_report_request_attributes_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateRealtimeStatisticsReportRequestAttributesRequest**](../Model/GenerateRealtimeStatisticsReportRequestAttributesRequest.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\JsonReportRowsListResponse**](../Model/JsonReportRowsListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTopProductsReport()`

```php
getTopProductsReport($generate_top_products_report_request_attributes_request): \criteo\api\marketingsolutions\preview\Model\JsonReportRowsListResponse
```

/preview/reports/top-products

With the topProducts endpoint, you can analyse the performances for each publisher, by top displays, top clicks or top sales.  <br/><br/>  This endpoint supports data retrieval for up to one year in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$generate_top_products_report_request_attributes_request = {"data":{"type":"GenerateTopProductsReport","attributes":{"timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00","advertiserId":"1234","limit":200,"rankProductsBy":"Clicks","dimensions":["CampaignId","Campaign","AdSetId","AdSet","ProductId","Product","ProductUrl","Brand","Category"],"metrics":["Clicks","Ctr","Visits","Sales","Cost","Revenue","Displays"],"currency":"EUR","brands":["Brand1","Brand2"],"categoryIds":["6666","7777"],"campaignIds":["9999"],"adSetIds":["11111","22222"],"adSetStatus":["Active","NotRunning"]}}}; // \criteo\api\marketingsolutions\preview\Model\GenerateTopProductsReportRequestAttributesRequest

try {
    $result = $apiInstance->getTopProductsReport($generate_top_products_report_request_attributes_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getTopProductsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **generate_top_products_report_request_attributes_request** | [**\criteo\api\marketingsolutions\preview\Model\GenerateTopProductsReportRequestAttributesRequest**](../Model/GenerateTopProductsReportRequestAttributesRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\JsonReportRowsListResponse**](../Model/JsonReportRowsListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTransactionsReport()`

```php
getTransactionsReport($transactions_report_query_message_list_request): \SplFileObject
```

/preview/transactions/report

This Transactions endpoint provides transactions id related data.  <br/><br/>  This endpoint supports data retrieval for up to two years in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$transactions_report_query_message_list_request = {"data":[{"type":"report","attributes":{"advertiserIds":"123,456,789","eventType":"Display","currency":"EUR","format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}}]}; // \criteo\api\marketingsolutions\preview\Model\TransactionsReportQueryMessageListRequest

try {
    $result = $apiInstance->getTransactionsReport($transactions_report_query_message_list_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getTransactionsReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **transactions_report_query_message_list_request** | [**\criteo\api\marketingsolutions\preview\Model\TransactionsReportQueryMessageListRequest**](../Model/TransactionsReportQueryMessageListRequest.md)|  | [optional] |

### Return type

**\SplFileObject**

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `text/csv`, `text/xml`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getTransparencyReport()`

```php
getTransparencyReport($advertiser_id, $transparency_query_message): \criteo\api\marketingsolutions\preview\Model\TransparencyReportListResponse
```

/preview/log-level/advertisers/{advertiser-id}/report

This Statistics endpoint provides publisher data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser ID to fetch the transparency data for. The advertiser must already exist. Must be greater than 0.
$transparency_query_message = {"shouldDisplayProductIds":false,"startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}; // \criteo\api\marketingsolutions\preview\Model\TransparencyQueryMessage | The query message.

try {
    $result = $apiInstance->getTransparencyReport($advertiser_id, $transparency_query_message);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getTransparencyReport: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser ID to fetch the transparency data for. The advertiser must already exist. Must be greater than 0. | |
| **transparency_query_message** | [**\criteo\api\marketingsolutions\preview\Model\TransparencyQueryMessage**](../Model/TransparencyQueryMessage.md)| The query message. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\TransparencyReportListResponse**](../Model/TransparencyReportListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
