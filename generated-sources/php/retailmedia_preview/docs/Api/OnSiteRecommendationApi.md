# criteo\api\retailmedia\preview\OnSiteRecommendationApi

All URIs are relative to https://api.criteo.com, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**chatbotProductRecommendations()**](OnSiteRecommendationApi.md#chatbotProductRecommendations) | **POST** /preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations | /preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations |


## `chatbotProductRecommendations()`

```php
chatbotProductRecommendations($catalogid, $inbot_discussion_body_model): \criteo\api\retailmedia\preview\Model\MessageBodyModel
```

/preview/retail-media/chatbot-catalogs/{catalogid}/product-recommendations

Ask a chatbot for a product recommendation

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');

// Configure OAuth2 access token for authorization: oauth
$config = criteo\api\retailmedia\preview\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new criteo\api\retailmedia\preview\Api\OnSiteRecommendationApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$catalogid = 'catalogid_example'; // string | the identifier of the catalog to query
$inbot_discussion_body_model = new \criteo\api\retailmedia\preview\Model\InbotDiscussionBodyModel(); // \criteo\api\retailmedia\preview\Model\InbotDiscussionBodyModel

try {
    $result = $apiInstance->chatbotProductRecommendations($catalogid, $inbot_discussion_body_model);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling OnSiteRecommendationApi->chatbotProductRecommendations: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **catalogid** | **string**| the identifier of the catalog to query | |
| **inbot_discussion_body_model** | [**\criteo\api\retailmedia\preview\Model\InbotDiscussionBodyModel**](../Model/InbotDiscussionBodyModel.md)|  | |

### Return type

[**\criteo\api\retailmedia\preview\Model\MessageBodyModel**](../Model/MessageBodyModel.md)

### Authorization

[oauth](../../README.md#oauth), [oauth](../../README.md#oauth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
