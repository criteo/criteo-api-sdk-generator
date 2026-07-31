# RecoApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBoostedAdAssociation**](RecoApi.md#createBoostedAdAssociation) | **POST** /2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id} | /2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id} |
| [**createProductSet**](RecoApi.md#createProductSet) | **POST** /2026-07/marketing-solutions/product-sets | /2026-07/marketing-solutions/product-sets |
| [**deleteBoostedAdAssociation**](RecoApi.md#deleteBoostedAdAssociation) | **DELETE** /2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id} | /2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id} |
| [**disableProductFiltering**](RecoApi.md#disableProductFiltering) | **DELETE** /2026-07/marketing-solutions/ads/{ad-id}/product-filter | /2026-07/marketing-solutions/ads/{ad-id}/product-filter |
| [**enableProductFiltering**](RecoApi.md#enableProductFiltering) | **POST** /2026-07/marketing-solutions/ads/{ad-id}/product-filter | /2026-07/marketing-solutions/ads/{ad-id}/product-filter |
| [**fetchBoostedAdAssociation**](RecoApi.md#fetchBoostedAdAssociation) | **GET** /2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id} | /2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id} |
| [**fetchBoostedAdAssociationByPartnerId**](RecoApi.md#fetchBoostedAdAssociationByPartnerId) | **GET** /2026-07/marketing-solutions/dataset/{dataset-id}/product-boost | /2026-07/marketing-solutions/dataset/{dataset-id}/product-boost |
| [**fetchBoostedAdAssociations**](RecoApi.md#fetchBoostedAdAssociations) | **GET** /2026-07/marketing-solutions/ads/{ad-id}/product-boost | /2026-07/marketing-solutions/ads/{ad-id}/product-boost |
| [**fetchProductFilteringConfig**](RecoApi.md#fetchProductFilteringConfig) | **GET** /2026-07/marketing-solutions/ads/{ad-id}/product-filter | /2026-07/marketing-solutions/ads/{ad-id}/product-filter |
| [**fetchProductFilteringUsages**](RecoApi.md#fetchProductFilteringUsages) | **GET** /2026-07/marketing-solutions/product-sets/{product-set-id}/product-filters | /2026-07/marketing-solutions/product-sets/{product-set-id}/product-filters |
| [**fetchProductSet**](RecoApi.md#fetchProductSet) | **GET** /2026-07/marketing-solutions/product-sets/{product-set-id} | /2026-07/marketing-solutions/product-sets/{product-set-id} |
| [**fetchProductSets**](RecoApi.md#fetchProductSets) | **GET** /2026-07/marketing-solutions/product-sets/dataset/{dataset-id} | /2026-07/marketing-solutions/product-sets/dataset/{dataset-id} |
| [**patchProductSet**](RecoApi.md#patchProductSet) | **PATCH** /2026-07/marketing-solutions/product-sets/{product-set-id} | /2026-07/marketing-solutions/product-sets/{product-set-id} |
| [**removeProductSet**](RecoApi.md#removeProductSet) | **DELETE** /2026-07/marketing-solutions/product-sets/{product-set-id} | /2026-07/marketing-solutions/product-sets/{product-set-id} |



## createBoostedAdAssociation

> ValueResourceOutcomeOfBoostedAdProductSet createBoostedAdAssociation(adId, productSetId, valueResourceInputOfBoostingConfigurationRequest)

/2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id}

Create or update product boosting configuration

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        String productSetId = "productSetId_example"; // String | ID of the product set
        ValueResourceInputOfBoostingConfigurationRequest valueResourceInputOfBoostingConfigurationRequest = new ValueResourceInputOfBoostingConfigurationRequest(); // ValueResourceInputOfBoostingConfigurationRequest | 
        try {
            ValueResourceOutcomeOfBoostedAdProductSet result = apiInstance.createBoostedAdAssociation(adId, productSetId, valueResourceInputOfBoostingConfigurationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#createBoostedAdAssociation");
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
| **adId** | **String**| ID of the ad | |
| **productSetId** | **String**| ID of the product set | |
| **valueResourceInputOfBoostingConfigurationRequest** | [**ValueResourceInputOfBoostingConfigurationRequest**](ValueResourceInputOfBoostingConfigurationRequest.md)|  | [optional] |

### Return type

[**ValueResourceOutcomeOfBoostedAdProductSet**](ValueResourceOutcomeOfBoostedAdProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **201** | successful operation |  -  |


## createProductSet

> ResourceOutcomeOfProductSet createProductSet(valueResourceInputOfCreateProductSetRequest)

/2026-07/marketing-solutions/product-sets

Create a new product set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        ValueResourceInputOfCreateProductSetRequest valueResourceInputOfCreateProductSetRequest = new ValueResourceInputOfCreateProductSetRequest(); // ValueResourceInputOfCreateProductSetRequest | 
        try {
            ResourceOutcomeOfProductSet result = apiInstance.createProductSet(valueResourceInputOfCreateProductSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#createProductSet");
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
| **valueResourceInputOfCreateProductSetRequest** | [**ValueResourceInputOfCreateProductSetRequest**](ValueResourceInputOfCreateProductSetRequest.md)|  | |

### Return type

[**ResourceOutcomeOfProductSet**](ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product set created successfully |  -  |


## deleteBoostedAdAssociation

> ValueResourceOutcomeOfBoostedAdProductSet deleteBoostedAdAssociation(adId, productSetId)

/2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id}

Delete association and configuration.

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        String productSetId = "productSetId_example"; // String | ID of the product set
        try {
            ValueResourceOutcomeOfBoostedAdProductSet result = apiInstance.deleteBoostedAdAssociation(adId, productSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#deleteBoostedAdAssociation");
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
| **adId** | **String**| ID of the ad | |
| **productSetId** | **String**| ID of the product set | |

### Return type

[**ValueResourceOutcomeOfBoostedAdProductSet**](ValueResourceOutcomeOfBoostedAdProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


## disableProductFiltering

> ValueResourceOutcomeOfProductFilterConfig disableProductFiltering(adId)

/2026-07/marketing-solutions/ads/{ad-id}/product-filter

Disable product filtering for a given ad

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        try {
            ValueResourceOutcomeOfProductFilterConfig result = apiInstance.disableProductFiltering(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#disableProductFiltering");
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
| **adId** | **String**| ID of the ad | |

### Return type

[**ValueResourceOutcomeOfProductFilterConfig**](ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |


## enableProductFiltering

> ValueResourceOutcomeOfProductFilterConfig enableProductFiltering(adId, valueResourceInputOfCreateProductFilterRequest)

/2026-07/marketing-solutions/ads/{ad-id}/product-filter

Enable product filtering for a given ad

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        ValueResourceInputOfCreateProductFilterRequest valueResourceInputOfCreateProductFilterRequest = new ValueResourceInputOfCreateProductFilterRequest(); // ValueResourceInputOfCreateProductFilterRequest | 
        try {
            ValueResourceOutcomeOfProductFilterConfig result = apiInstance.enableProductFiltering(adId, valueResourceInputOfCreateProductFilterRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#enableProductFiltering");
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
| **adId** | **String**| ID of the ad | |
| **valueResourceInputOfCreateProductFilterRequest** | [**ValueResourceInputOfCreateProductFilterRequest**](ValueResourceInputOfCreateProductFilterRequest.md)|  | [optional] |

### Return type

[**ValueResourceOutcomeOfProductFilterConfig**](ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


## fetchBoostedAdAssociation

> ValueResourceOutcomeOfBoostedAdProductSet fetchBoostedAdAssociation(adId, productSetId)

/2026-07/marketing-solutions/ads/{ad-id}/product-boost/{product-set-id}

Fetch boosting association and configuration

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        String productSetId = "productSetId_example"; // String | ID of the product set
        try {
            ValueResourceOutcomeOfBoostedAdProductSet result = apiInstance.fetchBoostedAdAssociation(adId, productSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchBoostedAdAssociation");
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
| **adId** | **String**| ID of the ad | |
| **productSetId** | **String**| ID of the product set | |

### Return type

[**ValueResourceOutcomeOfBoostedAdProductSet**](ValueResourceOutcomeOfBoostedAdProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


## fetchBoostedAdAssociationByPartnerId

> ValueResourceCollectionOutcomeOfBoostedAdProductSet fetchBoostedAdAssociationByPartnerId(datasetId, clientType)

/2026-07/marketing-solutions/dataset/{dataset-id}/product-boost

Fetch boosting association and configuration for a given partner

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String datasetId = "datasetId_example"; // String | ID of the dataset
        String clientType = "Unknown"; // String | Client type filter
        try {
            ValueResourceCollectionOutcomeOfBoostedAdProductSet result = apiInstance.fetchBoostedAdAssociationByPartnerId(datasetId, clientType);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchBoostedAdAssociationByPartnerId");
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
| **datasetId** | **String**| ID of the dataset | |
| **clientType** | **String**| Client type filter | [optional] [enum: Unknown, CGrowth, CMax] |

### Return type

[**ValueResourceCollectionOutcomeOfBoostedAdProductSet**](ValueResourceCollectionOutcomeOfBoostedAdProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


## fetchBoostedAdAssociations

> ValueResourceCollectionOutcomeOfBoostedAdProductSet fetchBoostedAdAssociations(adId)

/2026-07/marketing-solutions/ads/{ad-id}/product-boost

Fetch all boosting associations and configurations

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        try {
            ValueResourceCollectionOutcomeOfBoostedAdProductSet result = apiInstance.fetchBoostedAdAssociations(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchBoostedAdAssociations");
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
| **adId** | **String**| ID of the ad | |

### Return type

[**ValueResourceCollectionOutcomeOfBoostedAdProductSet**](ValueResourceCollectionOutcomeOfBoostedAdProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


## fetchProductFilteringConfig

> ValueResourceOutcomeOfProductFilterConfig fetchProductFilteringConfig(adId)

/2026-07/marketing-solutions/ads/{ad-id}/product-filter

Fetch product filtering configuration for a given ad

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String adId = "adId_example"; // String | ID of the ad
        try {
            ValueResourceOutcomeOfProductFilterConfig result = apiInstance.fetchProductFilteringConfig(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchProductFilteringConfig");
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
| **adId** | **String**| ID of the ad | |

### Return type

[**ValueResourceOutcomeOfProductFilterConfig**](ValueResourceOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. Returns the product filtering configuration if it exists, or empty data if it doesn&#39;t. |  -  |


## fetchProductFilteringUsages

> ValueResourceCollectionOutcomeOfProductFilterConfig fetchProductFilteringUsages(productSetId)

/2026-07/marketing-solutions/product-sets/{product-set-id}/product-filters

Fetch product filtering usages for a given product set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String productSetId = "productSetId_example"; // String | ID of the product set
        try {
            ValueResourceCollectionOutcomeOfProductFilterConfig result = apiInstance.fetchProductFilteringUsages(productSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchProductFilteringUsages");
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
| **productSetId** | **String**| ID of the product set | |

### Return type

[**ValueResourceCollectionOutcomeOfProductFilterConfig**](ValueResourceCollectionOutcomeOfProductFilterConfig.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


## fetchProductSet

> ResourceOutcomeOfProductSet fetchProductSet(productSetId)

/2026-07/marketing-solutions/product-sets/{product-set-id}

Fetch an existing product set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String productSetId = "productSetId_example"; // String | ID of the product set
        try {
            ResourceOutcomeOfProductSet result = apiInstance.fetchProductSet(productSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchProductSet");
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
| **productSetId** | **String**| ID of the product set | |

### Return type

[**ResourceOutcomeOfProductSet**](ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product set fetched successfully |  -  |


## fetchProductSets

> ResourceCollectionOutcomeOfProductSet fetchProductSets(datasetId)

/2026-07/marketing-solutions/product-sets/dataset/{dataset-id}

Fetch product sets of a given dataset

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String datasetId = "datasetId_example"; // String | The ID of the dataset that should be used for product set retrieval
        try {
            ResourceCollectionOutcomeOfProductSet result = apiInstance.fetchProductSets(datasetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#fetchProductSets");
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
| **datasetId** | **String**| The ID of the dataset that should be used for product set retrieval | |

### Return type

[**ResourceCollectionOutcomeOfProductSet**](ResourceCollectionOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products sets fetched successfully |  -  |


## patchProductSet

> ResourceOutcomeOfProductSet patchProductSet(productSetId, valueResourceInputOfPatchProductSetRequest)

/2026-07/marketing-solutions/product-sets/{product-set-id}

Patch an existing product set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String productSetId = "productSetId_example"; // String | ID of the product set
        ValueResourceInputOfPatchProductSetRequest valueResourceInputOfPatchProductSetRequest = new ValueResourceInputOfPatchProductSetRequest(); // ValueResourceInputOfPatchProductSetRequest | 
        try {
            ResourceOutcomeOfProductSet result = apiInstance.patchProductSet(productSetId, valueResourceInputOfPatchProductSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#patchProductSet");
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
| **productSetId** | **String**| ID of the product set | |
| **valueResourceInputOfPatchProductSetRequest** | [**ValueResourceInputOfPatchProductSetRequest**](ValueResourceInputOfPatchProductSetRequest.md)|  | |

### Return type

[**ResourceOutcomeOfProductSet**](ResourceOutcomeOfProductSet.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product set modified successfully |  -  |


## removeProductSet

> Outcome removeProductSet(productSetId)

/2026-07/marketing-solutions/product-sets/{product-set-id}

Remove a product set

### Example

```java
package com.criteo.api.marketingsolutions.v2026_07;

import com.criteo.api.marketingsolutions.v2026_07.ApiClient;
import com.criteo.api.marketingsolutions.v2026_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2026_07.ApiException;
import com.criteo.api.marketingsolutions.v2026_07.Configuration;
import com.criteo.api.marketingsolutions.v2026_07.auth.*;
import com.criteo.api.marketingsolutions.v2026_07.model.*;
import com.criteo.api.marketingsolutions.v2026_07.api.RecoApi;

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

        RecoApi apiInstance = new RecoApi(defaultClient);
        String productSetId = "productSetId_example"; // String | ID of the product set to remove
        try {
            Outcome result = apiInstance.removeProductSet(productSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling RecoApi#removeProductSet");
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
| **productSetId** | **String**| ID of the product set to remove | |

### Return type

[**Outcome**](Outcome.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | ProductSet removed successfully |  -  |

