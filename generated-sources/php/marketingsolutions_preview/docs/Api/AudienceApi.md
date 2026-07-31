# criteo\api\marketingsolutions\preview\AudienceApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**computeAudienceSegmentsSizes()**](AudienceApi.md#computeAudienceSegmentsSizes) | **POST** /preview/marketing-solutions/audience-segments/compute-sizes | /preview/marketing-solutions/audience-segments/compute-sizes |
| [**computeAudiencesSizes()**](AudienceApi.md#computeAudiencesSizes) | **POST** /preview/marketing-solutions/audiences/compute-sizes | /preview/marketing-solutions/audiences/compute-sizes |
| [**createAudienceSegments()**](AudienceApi.md#createAudienceSegments) | **POST** /preview/marketing-solutions/audience-segments/create | /preview/marketing-solutions/audience-segments/create |
| [**createAudiences()**](AudienceApi.md#createAudiences) | **POST** /preview/marketing-solutions/audiences/create | /preview/marketing-solutions/audiences/create |
| [**deleteAudienceSegments()**](AudienceApi.md#deleteAudienceSegments) | **POST** /preview/marketing-solutions/audience-segments/delete | /preview/marketing-solutions/audience-segments/delete |
| [**deleteAudiences()**](AudienceApi.md#deleteAudiences) | **POST** /preview/marketing-solutions/audiences/delete | /preview/marketing-solutions/audiences/delete |
| [**deleteContactListByAudienceSegment()**](AudienceApi.md#deleteContactListByAudienceSegment) | **DELETE** /preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list | /preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list |
| [**estimateAudienceSegmentsSizes()**](AudienceApi.md#estimateAudienceSegmentsSizes) | **POST** /preview/marketing-solutions/audience-segments/estimate-size | /preview/marketing-solutions/audience-segments/estimate-size |
| [**estimateAudiencesSizes()**](AudienceApi.md#estimateAudiencesSizes) | **POST** /preview/marketing-solutions/audiences/estimate-size | /preview/marketing-solutions/audiences/estimate-size |
| [**getAudienceSegmentContactListStatistics()**](AudienceApi.md#getAudienceSegmentContactListStatistics) | **GET** /preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics | /preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics |
| [**getAudienceSegmentsInMarketBrands()**](AudienceApi.md#getAudienceSegmentsInMarketBrands) | **GET** /preview/marketing-solutions/audience-segments/in-market-brands | /preview/marketing-solutions/audience-segments/in-market-brands |
| [**getAudienceSegmentsInMarketInterests()**](AudienceApi.md#getAudienceSegmentsInMarketInterests) | **GET** /preview/marketing-solutions/audience-segments/in-market-interests | /preview/marketing-solutions/audience-segments/in-market-interests |
| [**modifyAudienceUsersWithAttributes()**](AudienceApi.md#modifyAudienceUsersWithAttributes) | **PATCH** /preview/marketing-solutions/audiences/{audience-id}/contactlist-attributes | /preview/marketing-solutions/audiences/{audience-id}/contactlist-attributes |
| [**searchAudienceSegments()**](AudienceApi.md#searchAudienceSegments) | **POST** /preview/marketing-solutions/audience-segments/search | /preview/marketing-solutions/audience-segments/search |
| [**searchAudiences()**](AudienceApi.md#searchAudiences) | **POST** /preview/marketing-solutions/audiences/search | /preview/marketing-solutions/audiences/search |
| [**updateAudienceSegments()**](AudienceApi.md#updateAudienceSegments) | **PATCH** /preview/marketing-solutions/audience-segments | /preview/marketing-solutions/audience-segments |
| [**updateAudiences()**](AudienceApi.md#updateAudiences) | **PATCH** /preview/marketing-solutions/audiences | /preview/marketing-solutions/audiences |
| [**updateContactListByAudienceSegment()**](AudienceApi.md#updateContactListByAudienceSegment) | **PATCH** /preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list | /preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list |


## `computeAudienceSegmentsSizes()`

```php
computeAudienceSegmentsSizes($audience_segment_compute_sizes_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSegmentSizeEntityV1ListResponse
```

/preview/marketing-solutions/audience-segments/compute-sizes

Gets the size of all segments. An error is returned for those whose size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_compute_sizes_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSegmentComputeSizesInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSegmentComputeSizesInputV1 | 

try {
    $result = $apiInstance->computeAudienceSegmentsSizes($audience_segment_compute_sizes_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->computeAudienceSegmentsSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_compute_sizes_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentComputeSizesInputV1**](../Model/AudienceSegmentComputeSizesInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentSizeEntityV1ListResponse**](../Model/AudienceSegmentSizeEntityV1ListResponse.md)

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
computeAudiencesSizes($audience_compute_sizes_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSizeEntityV1ListResponse
```

/preview/marketing-solutions/audiences/compute-sizes

Gets the size of all audiences. An error is returned for those whose size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_compute_sizes_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceComputeSizesInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceComputeSizesInputV1 | 

try {
    $result = $apiInstance->computeAudiencesSizes($audience_compute_sizes_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->computeAudiencesSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_compute_sizes_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceComputeSizesInputV1**](../Model/AudienceComputeSizesInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSizeEntityV1ListResponse**](../Model/AudienceSizeEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAudienceSegments()`

```php
createAudienceSegments($audience_segment_bulk_create_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSegmentEntityV1ListResponse
```

/preview/marketing-solutions/audience-segments/create

Creates all segments with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_bulk_create_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkCreateInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkCreateInputV1 | Segment creation parameter

try {
    $result = $apiInstance->createAudienceSegments($audience_segment_bulk_create_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->createAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_bulk_create_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkCreateInputV1**](../Model/AudienceSegmentBulkCreateInputV1.md)| Segment creation parameter | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentEntityV1ListResponse**](../Model/AudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `createAudiences()`

```php
createAudiences($audience_bulk_create_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceEntityV1ListResponse
```

/preview/marketing-solutions/audiences/create

Creates all audiences with a valid configuration, and returns their IDs. For those that cannot be created, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_bulk_create_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceBulkCreateInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceBulkCreateInputV1 | 

try {
    $result = $apiInstance->createAudiences($audience_bulk_create_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->createAudiences: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_bulk_create_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceBulkCreateInputV1**](../Model/AudienceBulkCreateInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceEntityV1ListResponse**](../Model/AudienceEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAudienceSegments()`

```php
deleteAudienceSegments($audience_segment_bulk_delete_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSegmentIdEntityV1ListResponse
```

/preview/marketing-solutions/audience-segments/delete

Delete the segments associated to the given audience IDs.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_bulk_delete_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkDeleteInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkDeleteInputV1 | Segment delete request.

try {
    $result = $apiInstance->deleteAudienceSegments($audience_segment_bulk_delete_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->deleteAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_bulk_delete_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkDeleteInputV1**](../Model/AudienceSegmentBulkDeleteInputV1.md)| Segment delete request. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentIdEntityV1ListResponse**](../Model/AudienceSegmentIdEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteAudiences()`

```php
deleteAudiences($audience_bulk_delete_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceIdEntityV1ListResponse
```

/preview/marketing-solutions/audiences/delete

Deletes the audiences associated to the given audience IDs.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_bulk_delete_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceBulkDeleteInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceBulkDeleteInputV1 | 

try {
    $result = $apiInstance->deleteAudiences($audience_bulk_delete_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->deleteAudiences: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_bulk_delete_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceBulkDeleteInputV1**](../Model/AudienceBulkDeleteInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceIdEntityV1ListResponse**](../Model/AudienceIdEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteContactListByAudienceSegment()`

```php
deleteContactListByAudienceSegment($audience_segment_id): \criteo\api\marketingsolutions\preview\Model\DeleteAudienceContactListResponse
```

/preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list

Delete all identifiers from a contact list audience-segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The id of the contact list audience-segment to amend

try {
    $result = $apiInstance->deleteContactListByAudienceSegment($audience_segment_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->deleteContactListByAudienceSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The id of the contact list audience-segment to amend | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\DeleteAudienceContactListResponse**](../Model/DeleteAudienceContactListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estimateAudienceSegmentsSizes()`

```php
estimateAudienceSegmentsSizes($audience_segment_estimate_size_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSegmentSizeEstimationV1Response
```

/preview/marketing-solutions/audience-segments/estimate-size

Gets the size estimation of a non existent segment. An error is returned when size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_estimate_size_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSegmentEstimateSizeInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSegmentEstimateSizeInputV1 | 

try {
    $result = $apiInstance->estimateAudienceSegmentsSizes($audience_segment_estimate_size_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->estimateAudienceSegmentsSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_estimate_size_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentEstimateSizeInputV1**](../Model/AudienceSegmentEstimateSizeInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentSizeEstimationV1Response**](../Model/AudienceSegmentSizeEstimationV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estimateAudiencesSizes()`

```php
estimateAudiencesSizes($audience_estimate_size_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSizeEstimationV1Response
```

/preview/marketing-solutions/audiences/estimate-size

Gets the size estimation of a non existent audience. An error is returned when size calculation is not supported.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_estimate_size_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceEstimateSizeInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceEstimateSizeInputV1 | 

try {
    $result = $apiInstance->estimateAudiencesSizes($audience_estimate_size_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->estimateAudiencesSizes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_estimate_size_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceEstimateSizeInputV1**](../Model/AudienceEstimateSizeInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSizeEstimationV1Response**](../Model/AudienceSizeEstimationV1Response.md)

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
getAudienceSegmentContactListStatistics($audience_segment_id): \criteo\api\marketingsolutions\preview\Model\ContactListStatisticsEntityV1Response
```

/preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list/statistics

Returns the statistics of a contact list segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
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
    echo 'Exception when calling AudienceApi->getAudienceSegmentContactListStatistics: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The segment ID. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ContactListStatisticsEntityV1Response**](../Model/ContactListStatisticsEntityV1Response.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAudienceSegmentsInMarketBrands()`

```php
getAudienceSegmentsInMarketBrands($advertiser_id, $country): \criteo\api\marketingsolutions\preview\Model\InMarketAudienceSegmentBrandEntityV1ListResponse
```

/preview/marketing-solutions/audience-segments/in-market-brands

Returns a list with all available in-market brands that can be used to define an in-market segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser ID.
$country = 'country_example'; // string | The ISO 3166-1 alpha-2 country code.

try {
    $result = $apiInstance->getAudienceSegmentsInMarketBrands($advertiser_id, $country);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->getAudienceSegmentsInMarketBrands: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser ID. | |
| **country** | **string**| The ISO 3166-1 alpha-2 country code. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\InMarketAudienceSegmentBrandEntityV1ListResponse**](../Model/InMarketAudienceSegmentBrandEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getAudienceSegmentsInMarketInterests()`

```php
getAudienceSegmentsInMarketInterests($advertiser_id, $country): \criteo\api\marketingsolutions\preview\Model\InMarketAudienceSegmentInterestEntityV1ListResponse
```

/preview/marketing-solutions/audience-segments/in-market-interests

Returns a list with all available in-market interests that can be used to define an in-market segment. These in-market interests correspond to the Google product taxonomy.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$advertiser_id = 'advertiser_id_example'; // string | The advertiser ID.
$country = 'country_example'; // string | The ISO 3166-1 alpha-2 country code.

try {
    $result = $apiInstance->getAudienceSegmentsInMarketInterests($advertiser_id, $country);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->getAudienceSegmentsInMarketInterests: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **advertiser_id** | **string**| The advertiser ID. | |
| **country** | **string**| The ISO 3166-1 alpha-2 country code. | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\InMarketAudienceSegmentInterestEntityV1ListResponse**](../Model/InMarketAudienceSegmentInterestEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `modifyAudienceUsersWithAttributes()`

```php
modifyAudienceUsersWithAttributes($audience_id, $contactlist_with_attributes_amendment_request): \criteo\api\marketingsolutions\preview\Model\ModifyAudienceResponse
```

/preview/marketing-solutions/audiences/{audience-id}/contactlist-attributes

Add/remove identifiers to or from a contact list.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_id = 'audience_id_example'; // string | The id of the contact list audience-segment to amend
$contactlist_with_attributes_amendment_request = new \criteo\api\marketingsolutions\preview\Model\ContactlistWithAttributesAmendmentRequest(); // \criteo\api\marketingsolutions\preview\Model\ContactlistWithAttributesAmendmentRequest

try {
    $result = $apiInstance->modifyAudienceUsersWithAttributes($audience_id, $contactlist_with_attributes_amendment_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->modifyAudienceUsersWithAttributes: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_id** | **string**| The id of the contact list audience-segment to amend | |
| **contactlist_with_attributes_amendment_request** | [**\criteo\api\marketingsolutions\preview\Model\ContactlistWithAttributesAmendmentRequest**](../Model/ContactlistWithAttributesAmendmentRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ModifyAudienceResponse**](../Model/ModifyAudienceResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAudienceSegments()`

```php
searchAudienceSegments($audience_segment_search_input_v1, $limit, $offset): \criteo\api\marketingsolutions\preview\Model\AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse
```

/preview/marketing-solutions/audience-segments/search

Returns a list of segments that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_search_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSegmentSearchInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSegmentSearchInputV1 | Segment search filters.
$limit = 50; // int | The number of elements to be returned. The default is 50 and the maximum is 100.
$offset = 0; // int | The (zero-based) offset into the collection. The default is 0.

try {
    $result = $apiInstance->searchAudienceSegments($audience_segment_search_input_v1, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->searchAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_search_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentSearchInputV1**](../Model/AudienceSegmentSearchInputV1.md)| Segment search filters. | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse**](../Model/AudienceSegmentEntityV1AudienceSegmentSearchMetadataV1ListResponse.md)

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
searchAudiences($audience_search_input_v1, $limit, $offset): \criteo\api\marketingsolutions\preview\Model\AudienceEntityV1AudienceSearchMetadataV1ListResponse
```

/preview/marketing-solutions/audiences/search

Returns a list of audiences that match the provided filters. If present, the filters are AND'ed together when applied.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_search_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSearchInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSearchInputV1 | Audience search filters.
$limit = 50; // int | The number of elements to be returned. The default is 50 and the maximum is 100.
$offset = 0; // int | The (zero-based) offset into the collection. The default is 0.

try {
    $result = $apiInstance->searchAudiences($audience_search_input_v1, $limit, $offset);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->searchAudiences: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_search_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSearchInputV1**](../Model/AudienceSearchInputV1.md)| Audience search filters. | |
| **limit** | **int**| The number of elements to be returned. The default is 50 and the maximum is 100. | [optional] [default to 50] |
| **offset** | **int**| The (zero-based) offset into the collection. The default is 0. | [optional] [default to 0] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceEntityV1AudienceSearchMetadataV1ListResponse**](../Model/AudienceEntityV1AudienceSearchMetadataV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateAudienceSegments()`

```php
updateAudienceSegments($audience_segment_bulk_update_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceSegmentEntityV1ListResponse
```

/preview/marketing-solutions/audience-segments

Updates the properties of all segments with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_bulk_update_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkUpdateInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkUpdateInputV1 | Segment Update request

try {
    $result = $apiInstance->updateAudienceSegments($audience_segment_bulk_update_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->updateAudienceSegments: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_bulk_update_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentBulkUpdateInputV1**](../Model/AudienceSegmentBulkUpdateInputV1.md)| Segment Update request | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceSegmentEntityV1ListResponse**](../Model/AudienceSegmentEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateAudiences()`

```php
updateAudiences($audience_bulk_update_input_v1): \criteo\api\marketingsolutions\preview\Model\AudienceEntityV1ListResponse
```

/preview/marketing-solutions/audiences

Updates the properties of all audiences with a valid configuration, and returns their IDs. For those that cannot be updated, one or multiple errors are returned.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_bulk_update_input_v1 = new \criteo\api\marketingsolutions\preview\Model\AudienceBulkUpdateInputV1(); // \criteo\api\marketingsolutions\preview\Model\AudienceBulkUpdateInputV1 | 

try {
    $result = $apiInstance->updateAudiences($audience_bulk_update_input_v1);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->updateAudiences: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_bulk_update_input_v1** | [**\criteo\api\marketingsolutions\preview\Model\AudienceBulkUpdateInputV1**](../Model/AudienceBulkUpdateInputV1.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\AudienceEntityV1ListResponse**](../Model/AudienceEntityV1ListResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateContactListByAudienceSegment()`

```php
updateContactListByAudienceSegment($audience_segment_id, $contactlist_amendment_request): \criteo\api\marketingsolutions\preview\Model\ModifyAudienceResponse
```

/preview/marketing-solutions/audience-segments/{audience-segment-id}/contact-list

Add/remove identifiers to or from a contact list audience-segment.

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\AudienceApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$audience_segment_id = 'audience_segment_id_example'; // string | The id of the contact list audience-segment to amend
$contactlist_amendment_request = new \criteo\api\marketingsolutions\preview\Model\ContactlistAmendmentRequest(); // \criteo\api\marketingsolutions\preview\Model\ContactlistAmendmentRequest

try {
    $result = $apiInstance->updateContactListByAudienceSegment($audience_segment_id, $contactlist_amendment_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AudienceApi->updateContactListByAudienceSegment: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **audience_segment_id** | **string**| The id of the contact list audience-segment to amend | |
| **contactlist_amendment_request** | [**\criteo\api\marketingsolutions\preview\Model\ContactlistAmendmentRequest**](../Model/ContactlistAmendmentRequest.md)|  | |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\ModifyAudienceResponse**](../Model/ModifyAudienceResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
