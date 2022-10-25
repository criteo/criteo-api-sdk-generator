<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure OAuth2 access token for authorization: oauth
// $config = criteo\api\marketingsolutions\v2022_07\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_TOKEN');
$clientId = "YOUR_CLIENT_ID";
$clientSecret = "YOUR_CLIENT_SECRET";

$client = new criteo\api\marketingsolutions\v2022_07\ClientCredentialsClient($clientId, $clientSecret);

$apiInstance = new criteo\api\marketingsolutions\v2022_07\Api\AdvertiserApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    client: $client
    // new GuzzleHttp\Client(),
    // $config
);

try {
    $result = $apiInstance->apiPortfolioGet();
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AdvertiserApi->apiPortfolioGet: ', $e->getMessage(), PHP_EOL;
}