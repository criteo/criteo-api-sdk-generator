# criteo\api\retailmedia\experimental\AudienceApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addRemoveContactListByAudienceSegment()**](AudienceApi.md#addRemoveContactListByAudienceSegment) | **POST** /experimental/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove | /experimental/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove |
| [**bulkCreateAudience()**](AudienceApi.md#bulkCreateAudience) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/create | /experimental/retail-media/accounts/{account-id}/audiences/create |
| [**bulkCreateAudienceSegments()**](AudienceApi.md#bulkCreateAudienceSegments) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/create | /experimental/retail-media/accounts/{account-id}/audience-segments/create |
| [**bulkDeleteAudienceSegments()**](AudienceApi.md#bulkDeleteAudienceSegments) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/delete | /experimental/retail-media/accounts/{account-id}/audience-segments/delete |
| [**bulkDeleteAudiences()**](AudienceApi.md#bulkDeleteAudiences) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/delete | /experimental/retail-media/accounts/{account-id}/audiences/delete |
| [**bulkUpdateAudience()**](AudienceApi.md#bulkUpdateAudience) | **PATCH** /experimental/retail-media/accounts/{account-id}/audiences | /experimental/retail-media/accounts/{account-id}/audiences |
| [**bulkUpdateAudienceSegments()**](AudienceApi.md#bulkUpdateAudienceSegments) | **PATCH** /experimental/retail-media/accounts/{account-id}/audience-segments | /experimental/retail-media/accounts/{account-id}/audience-segments |
| [**clearContactListByAudienceSegment()**](AudienceApi.md#clearContactListByAudienceSegment) | **POST** /experimental/retail-media/audience-segments/{audience-segment-id}/contact-list/clear | /experimental/retail-media/audience-segments/{audience-segment-id}/contact-list/clear |
| [**computeAudienceSegmentsSizes()**](AudienceApi.md#computeAudienceSegmentsSizes) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes | /experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes |
| [**computeAudiencesSizes()**](AudienceApi.md#computeAudiencesSizes) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/compute-sizes | /experimental/retail-media/accounts/{account-id}/audiences/compute-sizes |
| [**estimateAudienceSegmentSize()**](AudienceApi.md#estimateAudienceSegmentSize) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size | /experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size |
| [**estimateAudienceSize()**](AudienceApi.md#estimateAudienceSize) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/estimate-size | /experimental/retail-media/accounts/{account-id}/audiences/estimate-size |
| [**getAudienceSegmentContactListStatistics()**](AudienceApi.md#getAudienceSegmentContactListStatistics) | **GET** /experimental/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list | /experimental/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list |
| [**searchAudienceSegments()**](AudienceApi.md#searchAudienceSegments) | **POST** /experimental/retail-media/accounts/{account-id}/audience-segments/search | /experimental/retail-media/accounts/{account-id}/audience-segments/search |
| [**searchAudiences()**](AudienceApi.md#searchAudiences) | **POST** /experimental/retail-media/accounts/{account-id}/audiences/search | /experimental/retail-media/accounts/{account-id}/audiences/search |


## `addRemoveContactListByAudienceSegment()`

```php
addRemoveContactListByAudienceSegment($audience_segment_id, $retail_media_contactlist_amendment_request): \criteo\api\retailmedia\experimental\Model\RetailMediaContactlistOperation
```

/experimental/retail-media/audience-segments/{audience-segment-id}/contact-list/add-remove

Add/remove identifiers to or from a retail-media contact list audience-segment, with external audience segment id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The id of the contact list audience-segment to amend, we only accept external Id here
$retail_media_contactlist_amendment_request = new \criteo\api\retailmedia\experimental\Model\RetailMediaContactlistAmendmentRequest(); // \criteo\api\retailmedia\experimental\Model\RetailMediaContactlistAmendmentRequest

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
| **retail_media_contactlist_amendment_request** | [**\criteo\api\retailmedia\experimental\Model\RetailMediaContactlistAmendmentRequest**](../Model/RetailMediaContactlistAmendmentRequest.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RetailMediaContactlistOperation**](../Model/RetailMediaContactlistOperation.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkCreateAudience()`

```php
bulkCreateAudience($account_id, $rm_audience_bulk_create_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audiences/create

Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_bulk_create_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceBulkCreateInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceBulkCreateInputV1 | Audience creation parameter

try {
    $result = $apiInstance->bulkCreateAudience($account_id, $rm_audience_bulk_create_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->bulkCreateAudience: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_bulk_create_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceBulkCreateInputV1**](../Model/RmAudienceBulkCreateInputV1.md)| Audience creation parameter | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceEntityV1ListResponse**](../Model/RmAudienceEntityV1ListResponse.md)

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
bulkCreateAudienceSegments($account_id, $rm_audience_segment_bulk_create_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audience-segments/create

Creates all segments with a valid configuration, and returns the full segments. For those that cannot be created, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_segment_bulk_create_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkCreateInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkCreateInputV1 | Segment creation parameter

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
| **rm_audience_segment_bulk_create_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkCreateInputV1**](../Model/RmAudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEntityV1ListResponse**](../Model/RmAudienceSegmentEntityV1ListResponse.md)

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
bulkDeleteAudienceSegments($account_id, $rm_audience_segment_bulk_delete_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentIdEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audience-segments/delete

Delete the segments associated to the given IDs.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account id
$rm_audience_segment_bulk_delete_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkDeleteInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkDeleteInputV1 | Segment delete request.

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
| **rm_audience_segment_bulk_delete_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkDeleteInputV1**](../Model/RmAudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentIdEntityV1ListResponse**](../Model/RmAudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkDeleteAudiences()`

```php
bulkDeleteAudiences($account_id, $rm_audience_bulk_delete_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentIdEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audiences/delete

Deletes the audiences associated to the given IDs.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_bulk_delete_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceBulkDeleteInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceBulkDeleteInputV1 | 

try {
    $result = $apiInstance->bulkDeleteAudiences($account_id, $rm_audience_bulk_delete_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->bulkDeleteAudiences: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_bulk_delete_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceBulkDeleteInputV1**](../Model/RmAudienceBulkDeleteInputV1.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentIdEntityV1ListResponse**](../Model/RmAudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `bulkUpdateAudience()`

```php
bulkUpdateAudience($account_id, $rm_audience_bulk_update_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audiences

Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_bulk_update_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceBulkUpdateInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceBulkUpdateInputV1 | 

try {
    $result = $apiInstance->bulkUpdateAudience($account_id, $rm_audience_bulk_update_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->bulkUpdateAudience: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_bulk_update_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceBulkUpdateInputV1**](../Model/RmAudienceBulkUpdateInputV1.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceEntityV1ListResponse**](../Model/RmAudienceEntityV1ListResponse.md)

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
bulkUpdateAudienceSegments($account_id, $rm_audience_segment_bulk_update_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audience-segments

Updates the properties of all segments with a valid configuration, and returns the full segments. For those that cannot be updated, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account id
$rm_audience_segment_bulk_update_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkUpdateInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkUpdateInputV1 | Segment Update request

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
| **rm_audience_segment_bulk_update_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentBulkUpdateInputV1**](../Model/RmAudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEntityV1ListResponse**](../Model/RmAudienceSegmentEntityV1ListResponse.md)

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

/experimental/retail-media/audience-segments/{audience-segment-id}/contact-list/clear

Delete all identifiers from a retail-media contact list audience-segment, with external audience segment id.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
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

## `computeAudienceSegmentsSizes()`

```php
computeAudienceSegmentsSizes($account_id, $rm_audience_segment_compute_sizes_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSizeEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audience-segments/compute-sizes

Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account id
$rm_audience_segment_compute_sizes_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentComputeSizesInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentComputeSizesInputV1 | 

try {
    $result = $apiInstance->computeAudienceSegmentsSizes($account_id, $rm_audience_segment_compute_sizes_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->computeAudienceSegmentsSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account id | |
| **rm_audience_segment_compute_sizes_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentComputeSizesInputV1**](../Model/RmAudienceSegmentComputeSizesInputV1.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSizeEntityV1ListResponse**](../Model/RmAudienceSegmentSizeEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `computeAudiencesSizes()`

```php
computeAudiencesSizes($account_id, $rm_audience_compute_sizes_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSizeEntityV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audiences/compute-sizes

Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_compute_sizes_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceComputeSizesInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceComputeSizesInputV1 | 

try {
    $result = $apiInstance->computeAudiencesSizes($account_id, $rm_audience_compute_sizes_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->computeAudiencesSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_compute_sizes_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceComputeSizesInputV1**](../Model/RmAudienceComputeSizesInputV1.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSizeEntityV1ListResponse**](../Model/RmAudienceSizeEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estimateAudienceSegmentSize()`

```php
estimateAudienceSegmentSize($account_id, $rm_audience_segment_estimate_size_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSizeEstimationV1Response
```

/experimental/retail-media/accounts/{account-id}/audience-segments/estimate-size

Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_segment_estimate_size_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEstimateSizeInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEstimateSizeInputV1 | 

try {
    $result = $apiInstance->estimateAudienceSegmentSize($account_id, $rm_audience_segment_estimate_size_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->estimateAudienceSegmentSize: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_segment_estimate_size_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEstimateSizeInputV1**](../Model/RmAudienceSegmentEstimateSizeInputV1.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSizeEstimationV1Response**](../Model/RmAudienceSegmentSizeEstimationV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estimateAudienceSize()`

```php
estimateAudienceSize($account_id, $rm_audience_estimate_size_input_v1): \criteo\api\retailmedia\experimental\Model\RmAudienceSizeEstimationV1Response
```

/experimental/retail-media/accounts/{account-id}/audiences/estimate-size

Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_estimate_size_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceEstimateSizeInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceEstimateSizeInputV1 | 

try {
    $result = $apiInstance->estimateAudienceSize($account_id, $rm_audience_estimate_size_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->estimateAudienceSize: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **account_id** | **string**| Account Id | |
| **rm_audience_estimate_size_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceEstimateSizeInputV1**](../Model/RmAudienceEstimateSizeInputV1.md)|  | |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSizeEstimationV1Response**](../Model/RmAudienceSizeEstimationV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAudienceSegmentContactListStatistics()`

```php
getAudienceSegmentContactListStatistics($account_id, $audience_segment_id): \criteo\api\retailmedia\experimental\Model\RmContactListStatisticsEntityV1Response
```

/experimental/retail-media/accounts/{account-id}/audience-segments/{audience-segment-id}/contact-list

Returns the statistics of a contact list segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
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

[**\criteo\api\retailmedia\experimental\Model\RmContactListStatisticsEntityV1Response**](../Model/RmContactListStatisticsEntityV1Response.md)

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
searchAudienceSegments($account_id, $rm_audience_segment_search_input_v1, $limit, $offset): \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_segment_search_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSearchInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSearchInputV1 | Segment search filters.
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
| **rm_audience_segment_search_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentSearchInputV1**](../Model/RmAudienceSegmentSearchInputV1.md)| Segment search filters. | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse**](../Model/RmAudienceSegmentEntityV1RmAudienceSegmentSearchMetadataV1ListResponse.md)

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
searchAudiences($account_id, $rm_audience_search_input_v1, $limit, $offset): \criteo\api\retailmedia\experimental\Model\RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse
```

/experimental/retail-media/accounts/{account-id}/audiences/search

Returns a list of audiences that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\experimental\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\experimental\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$account_id = 'account_id_example'; // string | Account Id
$rm_audience_search_input_v1 = new \criteo\api\retailmedia\experimental\Model\RmAudienceSearchInputV1(); // \criteo\api\retailmedia\experimental\Model\RmAudienceSearchInputV1 | Audience search filters.
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
| **rm_audience_search_input_v1** | [**\criteo\api\retailmedia\experimental\Model\RmAudienceSearchInputV1**](../Model/RmAudienceSearchInputV1.md)| Audience search filters. | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 500. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\retailmedia\experimental\Model\RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse**](../Model/RmAudienceEntityV1RmAudienceSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
