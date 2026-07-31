# AdvertiserApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAdvertisers**](AdvertiserApi.md#listAdvertisers) | **GET** /experimental/advertisers/me | /experimental/advertisers/me |
| [**listDatasetsByAdvertiser**](AdvertiserApi.md#listDatasetsByAdvertiser) | **GET** /experimental/advertisers/{advertiser-id}/datasets | /experimental/advertisers/{advertiser-id}/datasets |
| [**listIndustries**](AdvertiserApi.md#listIndustries) | **GET** /experimental/industries | /experimental/industries |



## listAdvertisers

> GetPortfolioResponse listAdvertisers()

/experimental/advertisers/me

Fetch the portfolio of Advertisers for this account

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AdvertiserApi;

public class Example {
    public static void main(String[] args) {

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        AdvertiserApi apiInstance = new AdvertiserApi(defaultClient);
        try {
            GetPortfolioResponse result = apiInstance.listAdvertisers();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdvertiserApi#listAdvertisers");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPortfolioResponse**](GetPortfolioResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## listDatasetsByAdvertiser

> AdvertiserDatasetListResponse listDatasetsByAdvertiser(advertiserId)

/experimental/advertisers/{advertiser-id}/datasets

Retrieves corresponding Datasets for a given Advertiser. Only those Datasets are included for which the given Advertiser is marked a primary.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AdvertiserApi;

public class Example {
    public static void main(String[] args) {

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        AdvertiserApi apiInstance = new AdvertiserApi(defaultClient);
        String advertiserId = "advertiserId_example"; // String | The id of the Advertiser for which Datasets are being retrieved.
        try {
            AdvertiserDatasetListResponse result = apiInstance.listDatasetsByAdvertiser(advertiserId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdvertiserApi#listDatasetsByAdvertiser");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **advertiserId** | **String**| The id of the Advertiser for which Datasets are being retrieved. | |

### Return type

[**AdvertiserDatasetListResponse**](AdvertiserDatasetListResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## listIndustries

> ListAvailableIndustriesResponse listIndustries()

/experimental/industries

Returns the list of available industries for new advertisers.

### Example

```java
package com.criteo.api.marketingsolutions.experimental;

import com.criteo.api.marketingsolutions.experimental.ApiClient;
import com.criteo.api.marketingsolutions.experimental.ApiClientBuilder;
import com.criteo.api.marketingsolutions.experimental.ApiException;
import com.criteo.api.marketingsolutions.experimental.Configuration;
import com.criteo.api.marketingsolutions.experimental.auth.*;
import com.criteo.api.marketingsolutions.experimental.model.*;
import com.criteo.api.marketingsolutions.experimental.api.AdvertiserApi;

public class Example {
    public static void main(String[] args) {

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR CLIENT ID";
        String clientSecret = "YOUR CLIENT SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
        
        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR ACCESS TOKEN");

        AdvertiserApi apiInstance = new AdvertiserApi(defaultClient);
        try {
            ListAvailableIndustriesResponse result = apiInstance.listIndustries();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdvertiserApi#listIndustries");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAvailableIndustriesResponse**](ListAvailableIndustriesResponse.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

