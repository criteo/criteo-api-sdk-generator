# criteo\api\marketingsolutions\v2026_07\AnalyticsApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAdsetReport()**](AnalyticsApi.md#getAdsetReport) | **POST** /2026-07/statistics/report | /2026-07/statistics/report |
| [**getPlacementsReport()**](AnalyticsApi.md#getPlacementsReport) | **POST** /2026-07/placements/report | /2026-07/placements/report |
| [**getTransactionsReport()**](AnalyticsApi.md#getTransactionsReport) | **POST** /2026-07/transactions/report | /2026-07/transactions/report |
| [**getTransparencyReport()**](AnalyticsApi.md#getTransparencyReport) | **POST** /2026-07/log-level/advertisers/{advertiser-id}/report | /2026-07/log-level/advertisers/{advertiser-id}/report |


## `getAdsetReport()`

```php
getAdsetReport($statistics_report_query_message): \SplFileObject
```

/2026-07/statistics/report

This Statistics endpoint provides ad set related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.  <br/><br/>  This endpoint supports data retrieval for up to two years in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_07\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$statistics_report_query_message = {"advertiserIds":"123,456,789","adSetIds":["12345","54321"],"adSetNames":["myAdSet1","myAdSet2"],"adSetStatus":["Active"],"dimensions":["CampaignId","Campaign","AdsetId","Adset","AdvertiserId","Advertiser","AdId","Ad","CouponId","Coupon","CategoryId","Category","Hour","Day","Week","Month","Year","Os","Device"],"metrics":["Clicks","Displays","Cpc","Visits"],"currency":"EUR","format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}; // \criteo\api\marketingsolutions\v2026_07\Model\StatisticsReportQueryMessage

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
| **statistics_report_query_message** | [**\criteo\api\marketingsolutions\v2026_07\Model\StatisticsReportQueryMessage**](../Model/StatisticsReportQueryMessage.md)|  | [optional] |

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

## `getPlacementsReport()`

```php
getPlacementsReport($placements_report_query_message_list_request): \SplFileObject
```

/2026-07/placements/report

Your ads are placed in different domains (publishers) and environments (websites and apps). Thanks to the placements endpoint, you can analyse the performances for each publisher, comparing displays, clicks and sales generated.  <br/><br/>  This endpoint supports data retrieval for up to three months in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_07\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$placements_report_query_message_list_request = {"data":[{"type":"report","attributes":{"advertiserIds":"123,456,789","campaignIds":"111,222,333,444","adsetIds":"135,246,357,468","environment":"Web","placement":"MyPlacement","dimensions":["AdsetId","AdvertiserId","Placement"],"metrics":["Clicks","Displays","Cost"],"currency":"EUR","disclosed":false,"format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}}]}; // \criteo\api\marketingsolutions\v2026_07\Model\PlacementsReportQueryMessageListRequest

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
| **placements_report_query_message_list_request** | [**\criteo\api\marketingsolutions\v2026_07\Model\PlacementsReportQueryMessageListRequest**](../Model/PlacementsReportQueryMessageListRequest.md)|  | [optional] |

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

## `getTransactionsReport()`

```php
getTransactionsReport($transactions_report_query_message_list_request): \SplFileObject
```

/2026-07/transactions/report

This Transactions endpoint provides transactions id related data.  <br/><br/>  This endpoint supports data retrieval for up to two years in the past.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_07\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$transactions_report_query_message_list_request = {"data":[{"type":"report","attributes":{"advertiserIds":"123,456,789","eventType":"Display","currency":"EUR","format":"csv","timezone":"Europe/Paris","startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}}]}; // \criteo\api\marketingsolutions\v2026_07\Model\TransactionsReportQueryMessageListRequest

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
| **transactions_report_query_message_list_request** | [**\criteo\api\marketingsolutions\v2026_07\Model\TransactionsReportQueryMessageListRequest**](../Model/TransactionsReportQueryMessageListRequest.md)|  | [optional] |

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
getTransparencyReport($advertiser_id, $transparency_query_message): \criteo\api\marketingsolutions\v2026_07\Model\TransparencyReportListResponse
```

/2026-07/log-level/advertisers/{advertiser-id}/report

This Statistics endpoint provides publisher data.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\v2026_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\v2026_07\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser ID to fetch the transparency data for. The advertiser must already exist. Must be greater than 0.
$transparency_query_message = {"shouldDisplayProductIds":false,"startDate":"2024-01-01T00:00:00.0000000+00:00","endDate":"2024-01-04T00:00:00.0000000+00:00"}; // \criteo\api\marketingsolutions\v2026_07\Model\TransparencyQueryMessage | The query message.

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
| **transparency_query_message** | [**\criteo\api\marketingsolutions\v2026_07\Model\TransparencyQueryMessage**](../Model/TransparencyQueryMessage.md)| The query message. | [optional] |

### Return type

[**\criteo\api\marketingsolutions\v2026_07\Model\TransparencyReportListResponse**](../Model/TransparencyReportListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `text/xml`, `application/*+xml`
- **Accept**: `application/json`, `application/xml`, `text/xml`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
