# criteo\api\marketingsolutions\preview\OnSiteRecommendationApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**searchRecommendedProducts()**](OnSiteRecommendationApi.md#searchRecommendedProducts) | **POST** /preview/recommendation/search | /preview/recommendation/search |
| [**searchRecommendedProductsConversational()**](OnSiteRecommendationApi.md#searchRecommendedProductsConversational) | **POST** /preview/recommendation/search-conversational | /preview/recommendation/search-conversational |


## `searchRecommendedProducts()`

```php
searchRecommendedProducts($on_site_reco_request): \criteo\api\marketingsolutions\preview\Model\OnSiteRecoResponse
```

/preview/recommendation/search

Retrieves a list of products recommended for the given user. This end point can either rely on a Criteo UserId, or a list of user events to perform the recommendation

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\OnSiteRecommendationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$on_site_reco_request = new \criteo\api\marketingsolutions\preview\Model\OnSiteRecoRequest(); // \criteo\api\marketingsolutions\preview\Model\OnSiteRecoRequest

try {
    $result = $apiInstance->searchRecommendedProducts($on_site_reco_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OnSiteRecommendationApi->searchRecommendedProducts: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **on_site_reco_request** | [**\criteo\api\marketingsolutions\preview\Model\OnSiteRecoRequest**](../Model/OnSiteRecoRequest.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\OnSiteRecoResponse**](../Model/OnSiteRecoResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchRecommendedProductsConversational()`

```php
searchRecommendedProductsConversational($on_site_reco_request_conversational): \criteo\api\marketingsolutions\preview\Model\OnSiteRecoResponse
```

/preview/recommendation/search-conversational

Retrieves a list of products recommended for the given user based on a conversation between a user and a partner's agent

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\marketingsolutions\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\marketingsolutions\preview\Api\OnSiteRecommendationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$on_site_reco_request_conversational = new \criteo\api\marketingsolutions\preview\Model\OnSiteRecoRequestConversational(); // \criteo\api\marketingsolutions\preview\Model\OnSiteRecoRequestConversational

try {
    $result = $apiInstance->searchRecommendedProductsConversational($on_site_reco_request_conversational);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OnSiteRecommendationApi->searchRecommendedProductsConversational: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **on_site_reco_request_conversational** | [**\criteo\api\marketingsolutions\preview\Model\OnSiteRecoRequestConversational**](../Model/OnSiteRecoRequestConversational.md)|  | [optional] |

### Return type

[**\criteo\api\marketingsolutions\preview\Model\OnSiteRecoResponse**](../Model/OnSiteRecoResponse.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
