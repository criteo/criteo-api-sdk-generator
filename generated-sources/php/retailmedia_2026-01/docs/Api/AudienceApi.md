# criteo\api\retailmedia\v2026_01\AudienceApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addRemoveContactListByAudienceSegment()**](AudienceApi.md#addRemoveContactListByAudienceSegment) | **POST** /2026-01/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | /2026-01/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove |
| [**bulkCreateAudienceSegments()**](AudienceApi.md#bulkCreateAudienceSegments) | **POST** /2026-01/retail-media/accounts/{account-id}/audience-segments/create | /2026-01/retail-media/accounts/{account-id}/audience-segments/create |
| [**bulkDeleteAudienceSegments()**](AudienceApi.md#bulkDeleteAudienceSegments) | **POST** /2026-01/retail-media/accounts/{account-id}/audience-segments/delete | /2026-01/retail-media/accounts/{account-id}/audience-segments/delete |
| [**bulkUpdateAudienceSegments()**](AudienceApi.md#bulkUpdateAudienceSegments) | **PATCH** /2026-01/retail-media/accounts/{account-id}/audience-segments | /2026-01/retail-media/accounts/{account-id}/audience-segments |
| [**clearContactListByAudienceSegment()**](AudienceApi.md#clearContactListByAudienceSegment) | **POST** /2026-01/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | /2026-01/retail-media/audience-segments/{audience-segment-id}/contact-list/clear |
| [**getAudienceSegmentContactListStatistics()**](AudienceApi.md#getAudienceSegmentContactListStatistics) | **GET** /2026-01/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | /2026-01/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list |
| [**searchAudienceSegments()**](AudienceApi.md#searchAudienceSegments) | **POST** /2026-01/retail-media/accounts/{account-id}/audience-segments/search | /2026-01/retail-media/accounts/{account-id}/audience-segments/search |
| [**searchAudiences()**](AudienceApi.md#searchAudiences) | **POST** /2026-01/retail-media/accounts/{account-id}/audiences/search | /2026-01/retail-media/accounts/{account-id}/audiences/search |


## `addRemoveContactListByAudienceSegment()`

```php
addRemoveContactListByAudienceSegment($audience_segment_id, $retail_media_contactlist_amendment_request): \criteo\api\retailmedia\v2026_01\Model\RetailMediaContactlistOperation
```

/2026-01/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove

Add/remove identifiers to or from a retail-media contact list audience-segment, with external audience segment id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The id of the contact list audience-segment to amend, we only accept external Id here
$retail_media_contactlist_amendment_request = new \criteo\api\retailmedia\v2026_01\Model\RetailMediaContactlistAmendmentRequest(); // \criteo\api\retailmedia\v2026_01\Model\RetailMediaContactlistAmendmentRequest

try {
    $result = $apiInstance->addRemoveContactListByAudienceSegment($audience_segment_id, $retail_media_contactlist_amendment_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->addRemoveContactListByAudienceSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The id of the contact list audience-segment to amend, we only accept external Id here | |
| **retail_media_contactlist_amendment_request** | [**\criteo\api\retailmedia\v2026_01\Model\RetailMediaContactlistAmendmentRequest**](../Model/RetailMediaContactlistAmendmentRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RetailMediaContactlistOperation**](../Model/RetailMediaContactlistOperation.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkCreateAudienceSegments()`

```php
bulkCreateAudienceSegments($account_id, $rm_audience_segment_bulk_create_input_v1): \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentEntityV1ListResponse
```

/2026-01/retail-media/accounts/{account-id}/audience-segments/create

Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_segment_bulk_create_input_v1 = new \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkCreateInputV1(); // \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkCreateInputV1 | Segment creation parameter

try {
    $result = $apiInstance->bulkCreateAudienceSegments($account_id, $rm_audience_segment_bulk_create_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->bulkCreateAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_segment_bulk_create_input_v1** | [**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkCreateInputV1**](../Model/RmAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentEntityV1ListResponse**](../Model/RmAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkDeleteAudienceSegments()`

```php
bulkDeleteAudienceSegments($account_id, $rm_audience_segment_bulk_delete_input_v1): \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentIdEntityV1ListResponse
```

/2026-01/retail-media/accounts/{account-id}/audience-segments/delete

Delete the segments associated to the given IDs.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account id
$rm_audience_segment_bulk_delete_input_v1 = new \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkDeleteInputV1(); // \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkDeleteInputV1 | Segment delete request.

try {
    $result = $apiInstance->bulkDeleteAudienceSegments($account_id, $rm_audience_segment_bulk_delete_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->bulkDeleteAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account id | |
| **rm_audience_segment_bulk_delete_input_v1** | [**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkDeleteInputV1**](../Model/RmAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentIdEntityV1ListResponse**](../Model/RmAudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkUpdateAudienceSegments()`

```php
bulkUpdateAudienceSegments($account_id, $rm_audience_segment_bulk_update_input_v1): \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentEntityV1ListResponse
```

/2026-01/retail-media/accounts/{account-id}/audience-segments

Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account id
$rm_audience_segment_bulk_update_input_v1 = new \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkUpdateInputV1(); // \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkUpdateInputV1 | Segment Update request

try {
    $result = $apiInstance->bulkUpdateAudienceSegments($account_id, $rm_audience_segment_bulk_update_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->bulkUpdateAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account id | |
| **rm_audience_segment_bulk_update_input_v1** | [**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentBulkUpdateInputV1**](../Model/RmAudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentEntityV1ListResponse**](../Model/RmAudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `clearContactListByAudienceSegment()`

```php
clearContactListByAudienceSegment($audience_segment_id)
```

/2026-01/retail-media/audience-segments/{audience-segment-id}/contact-list/clear

Delete all identifiers from a retail-media contact list audience-segment, with external audience segment id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The id of the contact list audience-segment to amend, we only accept external Id here

try {
    $apiInstance->clearContactListByAudienceSegment($audience_segment_id);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->clearContactListByAudienceSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The id of the contact list audience-segment to amend, we only accept external Id here | |

### Return type

void (empty response body)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAudienceSegmentContactListStatistics()`

```php
getAudienceSegmentContactListStatistics($account_id, $audience_segment_id): \criteo\api\retailmedia\v2026_01\Model\RmContactListStatisticsEntityV1Response
```

/2026-01/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list

Returns the statistics of a contact list segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$audience_segment_id = 'audience_segment_id_example'; // string | Segment Id.

try {
    $result = $apiInstance->getAudienceSegmentContactListStatistics($account_id, $audience_segment_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->getAudienceSegmentContactListStatistics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **audience_segment_id** | **string**| Segment Id. | |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RmContactListStatisticsEntityV1Response**](../Model/RmContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAudienceSegments()`

```php
searchAudienceSegments($account_id, $rm_audience_segment_search_input_v1, $limit, $offset): \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse
```

/2026-01/retail-media/accounts/{account-id}/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_segment_search_input_v1 = new \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentSearchInputV1(); // \criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentSearchInputV1 | Segment search filters.
$limit = 50; // int | The number of elements to be returned. The default is 50 and the maximum is 500.
$offset = 0; // int | The (zero-based) offset into the collection. The default is 0.

try {
    $result = $apiInstance->searchAudienceSegments($account_id, $rm_audience_segment_search_input_v1, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->searchAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_segment_search_input_v1** | [**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentSearchInputV1**](../Model/RmAudienceSegmentSearchInputV1.md)| Segment search filters. | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse**](../Model/RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAudiences()`

```php
searchAudiences($account_id, $rm_audience_search_input_v1, $limit, $offset): \criteo\api\retailmedia\v2026_01\Model\RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse
```

/2026-01/retail-media/accounts/{account-id}/audiences/search

Returns a list of audiences that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\v2026_01\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\v2026_01\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_search_input_v1 = new \criteo\api\retailmedia\v2026_01\Model\RmAudienceSearchInputV1(); // \criteo\api\retailmedia\v2026_01\Model\RmAudienceSearchInputV1 | Audience search filters.
$limit = 50; // int | The number of elements to be returned. The default is 50 and the maximum is 500.
$offset = 0; // int | The (zero-based) offset into the collection. The default is 0.

try {
    $result = $apiInstance->searchAudiences($account_id, $rm_audience_search_input_v1, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->searchAudiences: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_search_input_v1** | [**\criteo\api\retailmedia\v2026_01\Model\RmAudienceSearchInputV1**](../Model/RmAudienceSearchInputV1.md)| Audience search filters. | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\v2026_01\Model\RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse**](../Model/RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
