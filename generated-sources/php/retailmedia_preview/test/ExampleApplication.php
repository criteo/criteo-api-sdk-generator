<?php

// Install Criteo Marketing sdk, via composer for example: `composer require criteo/criteo-api-retailmedia-sdk`
// Then import it as follow:
// require_once(__DIR__ . '/vendor/autoload.php');

use criteo\api\retailmedia\preview\Api\GatewayApi;
use criteo\api\retailmedia\preview\ClientCredentialsClient;

class ExampleApplication
{
    function CallTheApplicationEndpoint($clientId, $clientSecret ) {
        //Create a client using your choosen OAuth flow. The client will handle the token generation/renewal for you
        $client = new ClientCredentialsClient($clientId, $clientSecret);

        //The Gateway API regroups common technical endpoints that exists for all versions
        //You can find the other endpoints in the other *Api
        //You can reuse the same client with several Apis, but be careful, as they will then use the same token and credentials
        $api = new GatewayApi($client);

        try {
            //Perform the call to the application introspection endpoint
            $response = $api->getCurrentApplication();

            /*
            * Most of Criteo's API response follow the same structure:
            * The response consists of a Data, Errors and Warnings fields
            * The Data fields contains an Id (if applicable), a Type, and an Attributes field that contains the business object
            */
            $myApplication = $response->getData()->getAttributes();
            print_r("Hello, I'm using Criteo API and I'm connected as {$myApplication->getName()}");
        } catch (ApiException $e) {
            print_r($e->getResponseBody());
            throw $e;
        }
    }
}
