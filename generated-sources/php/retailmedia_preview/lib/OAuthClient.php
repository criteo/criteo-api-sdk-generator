<?php
namespace criteo\api\retailmedia\preview;

use criteo\api\retailmedia\preview\ApiException;
use criteo\api\retailmedia\preview\Configuration;
use criteo\api\retailmedia\preview\ObjectSerializer;
use criteo\api\retailmedia\preview\ClientCredentialsClient\Token;
use GuzzleHttp\Client;
use GuzzleHttp\ClientInterface;
use GuzzleHttp\Psr7\Request;

class OAuthClient{
    /**
     * @var ClientInterface
     */
    protected $client;

    /**
     * @var Configuration
     */
    protected $config;

    /**
     * OAuthClient constructor.
     * @param ClientInterface|null $client
     * @param Configuration|null $config
     */
    public function __construct(
        $client = null, 
        $config = null)
    {
        $this->client = $client ?: new Client();
        $this->config = $config ?: new Configuration();
    }

    public function getToken($grant_type, $client_id, $client_secret)
    {
        $request = $this->getTokenRequest($grant_type, $client_id, $client_secret);
        $response = $this->client->send($request, []);                   
        $statusCode = $response->getStatusCode();
        if ($statusCode < 200 || $statusCode > 299) {
            throw new ApiException(
                sprintf(
                    '[%d] Error connecting to the API (%s)',
                    $statusCode,
                    (string) $request->getUri()
                ),
                $statusCode,
                $response->getHeaders(),
                (string) $response->getBody()
            );
        }

        $content = json_decode((string) $response->getBody());
        
        list($response) = [
            $content,
            $response->getStatusCode(),
            $response->getHeaders()
        ];

        return $response;
    }

    /**
     * Create request to get token
     *
     * @param  string $grant_type (required)
     * @param  string $client_id (required)
     * @param  string $client_secret (required)
     *
     * @return \GuzzleHttp\Psr7\Request
     */
    private function getTokenRequest($grant_type, $client_id, $client_secret){
        $resourcePath = '/oauth2/token';
        $formParams = [];
        $httpBody = '';

        // form params
        $formParams['grant_type'] = ObjectSerializer::toFormValue($grant_type);
        $formParams['client_id'] = ObjectSerializer::toFormValue($client_id);
        $formParams['client_secret'] = ObjectSerializer::toFormValue($client_secret);

        $headers = [
            'Accept' => 'application/json',
            'Content-Type' => 'application/x-www-form-urlencoded',
            'User-Agent' => $this->config->getUserAgent()
        ];

        $httpBody = ObjectSerializer::buildQuery($formParams);

        $operationHost = $this->config->getHost();
        return new Request(
            'POST',
            $operationHost . $resourcePath,
            $headers,
            $httpBody
        );

    }
}
