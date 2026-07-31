# criteo\api\commercegrid\experimental\SegmentApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addRemoveContactListByAudienceSegment()**](SegmentApi.md#addRemoveContactListByAudienceSegment) | **POST** /experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove | /experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove |
| [**bulkCreateAudienceSegments()**](SegmentApi.md#bulkCreateAudienceSegments) | **POST** /experimental/commerce-grid/audience-segments/create | /experimental/commerce-grid/audience-segments/create |
| [**bulkDeleteAudienceSegments()**](SegmentApi.md#bulkDeleteAudienceSegments) | **POST** /experimental/commerce-grid/audience-segments/delete | /experimental/commerce-grid/audience-segments/delete |
| [**bulkUpdateAudienceSegments()**](SegmentApi.md#bulkUpdateAudienceSegments) | **PATCH** /experimental/commerce-grid/audience-segments | /experimental/commerce-grid/audience-segments |
| [**clearContactListByAudienceSegment()**](SegmentApi.md#clearContactListByAudienceSegment) | **POST** /experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear | /experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear |
| [**getAudienceSegmentContactListStatistics()**](SegmentApi.md#getAudienceSegmentContactListStatistics) | **GET** /experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics | /experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics |
| [**searchAudienceSegments()**](SegmentApi.md#searchAudienceSegments) | **POST** /experimental/commerce-grid/audience-segments/search | /experimental/commerce-grid/audience-segments/search |


## `addRemoveContactListByAudienceSegment()`

```php
addRemoveContactListByAudienceSegment($audience_segment_id, $commerce_grid_contactlist_amendment_request): \criteo\api\commercegrid\experimental\Model\CommerceGridContactlistOperation
```

/experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/add-remove

Add/remove identifiers to or from a Commerce Grid audience segment of type Contact List.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The ID of the audience segment of type contact list to amend
$commerce_grid_contactlist_amendment_request = new \criteo\api\commercegrid\experimental\Model\CommerceGridContactlistAmendmentRequest(); // \criteo\api\commercegrid\experimental\Model\CommerceGridContactlistAmendmentRequest

try {
    $result = $apiInstance->addRemoveContactListByAudienceSegment($audience_segment_id, $commerce_grid_contactlist_amendment_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->addRemoveContactListByAudienceSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The ID of the audience segment of type contact list to amend | |
| **commerce_grid_contactlist_amendment_request** | [**\criteo\api\commercegrid\experimental\Model\CommerceGridContactlistAmendmentRequest**](../Model/CommerceGridContactlistAmendmentRequest.md)|  | |

### Return type

[**\criteo\api\commercegrid\experimental\Model\CommerceGridContactlistOperation**](../Model/CommerceGridContactlistOperation.md)

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
bulkCreateAudienceSegments($cg_audience_segment_bulk_create_input_v1): \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentEntityV1ListResponse
```

/experimental/commerce-grid/audience-segments/create

Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cg_audience_segment_bulk_create_input_v1 = new \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkCreateInputV1(); // \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkCreateInputV1 | Segment creation parameter

try {
    $result = $apiInstance->bulkCreateAudienceSegments($cg_audience_segment_bulk_create_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->bulkCreateAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cg_audience_segment_bulk_create_input_v1** | [**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkCreateInputV1**](../Model/CgAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentEntityV1ListResponse**](../Model/CgAudienceSegmentEntityV1ListResponse.md)

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
bulkDeleteAudienceSegments($cg_audience_segment_bulk_delete_input_v1): \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentIdEntityV1ListResponse
```

/experimental/commerce-grid/audience-segments/delete

Delete the segments associated to the given IDs.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cg_audience_segment_bulk_delete_input_v1 = new \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkDeleteInputV1(); // \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkDeleteInputV1 | Segment delete request.

try {
    $result = $apiInstance->bulkDeleteAudienceSegments($cg_audience_segment_bulk_delete_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->bulkDeleteAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cg_audience_segment_bulk_delete_input_v1** | [**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkDeleteInputV1**](../Model/CgAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentIdEntityV1ListResponse**](../Model/CgAudienceSegmentIdEntityV1ListResponse.md)

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
bulkUpdateAudienceSegments($cg_audience_segment_bulk_update_input_v1): \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentEntityV1ListResponse
```

/experimental/commerce-grid/audience-segments

Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cg_audience_segment_bulk_update_input_v1 = new \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkUpdateInputV1(); // \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkUpdateInputV1 | Segment Update request

try {
    $result = $apiInstance->bulkUpdateAudienceSegments($cg_audience_segment_bulk_update_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->bulkUpdateAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cg_audience_segment_bulk_update_input_v1** | [**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentBulkUpdateInputV1**](../Model/CgAudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentEntityV1ListResponse**](../Model/CgAudienceSegmentEntityV1ListResponse.md)

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

/experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/clear

Delete all identifiers from a Commerce Grid audience segment of type Contact List.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The ID of the audience segment of type contact list to amend

try {
    $apiInstance->clearContactListByAudienceSegment($audience_segment_id);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->clearContactListByAudienceSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The ID of the audience segment of type contact list to amend | |

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
getAudienceSegmentContactListStatistics($audience_segment_id): \criteo\api\commercegrid\experimental\Model\CgContactListStatisticsEntityV1Response
```

/experimental/commerce-grid/audience-segments/{audience-segment-id}/contact-list/statistics

Returns the statistics of a contact list segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The segment ID.

try {
    $result = $apiInstance->getAudienceSegmentContactListStatistics($audience_segment_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->getAudienceSegmentContactListStatistics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The segment ID. | |

### Return type

[**\criteo\api\commercegrid\experimental\Model\CgContactListStatisticsEntityV1Response**](../Model/CgContactListStatisticsEntityV1Response.md)

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
searchAudienceSegments($cg_audience_segment_search_input_v1, $limit, $offset): \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse
```

/experimental/commerce-grid/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\commercegrid\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\commercegrid\experimental\Api\SegmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$cg_audience_segment_search_input_v1 = new \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentSearchInputV1(); // \criteo\api\commercegrid\experimental\Model\CgAudienceSegmentSearchInputV1 | 
$limit = 50; // int | The number of elements to be returned. The default is 50 and the maximum is 100.
$offset = 0; // int | The (zero-based) offset into the collection. The default is 0.

try {
    $result = $apiInstance->searchAudienceSegments($cg_audience_segment_search_input_v1, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling SegmentApi->searchAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **cg_audience_segment_search_input_v1** | [**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentSearchInputV1**](../Model/CgAudienceSegmentSearchInputV1.md)|  | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\commercegrid\experimental\Model\CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse**](../Model/CgAudienceSegmentEntityV1CgAudienceSegmentSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
