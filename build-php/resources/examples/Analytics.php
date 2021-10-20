<?php

// Install Criteo Marketing Transition SDK, via composer for example: `composer require criteo/criteo-php-marketing-transition-sdk`
// Then import it as follow:
// require_once(__DIR__ . '/vendor/autoload.php');

use Criteo\Marketing\Api\AnalyticsApi;
use Criteo\Marketing\Model\StatisticsReportQueryMessage;
use Criteo\Marketing\TokenAutoRefreshClient;

/*
 * Although the OpenAPI specification, then this generated client, you can't simply use the API key feature.
 * i.e, the next two lines are useless:
 * $config = Criteo\Marketing\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
 * $config = Criteo\Marketing\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');
 *
 * To benefit from automatic token refresh and to avoid setting the correct value for Authorization header for each call,
 * we introduced a wrapper around Guzzle Http client: TokenAutoRefreshClient.
 * If you don't want this feature, use: GuzzleHttp\Client (or simply don't specify any client parameter).
*/

$clientId = 'YOUR_CLIENT_ID';
$clientCredentials = 'YOUR_PASSWORD';

$apiInstance = new AnalyticsApi(new TokenAutoRefreshClient($clientId, $clientCredentials));

$stats_query = new StatisticsReportQueryMessage(array(
    'dimensions'=>["AdsetId"],
    'metrics'=>["Clicks"],
    'start_date'=>"2019-01-01",
    'end_date'=>"2019-01-31",
    'currency'=>"EUR",
    'format'=>"Csv"
));

try {
    $result = $apiInstance->getAdsetReport($stats_query);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->getAdsetReport: ', $e->getMessage(), PHP_EOL;
}

