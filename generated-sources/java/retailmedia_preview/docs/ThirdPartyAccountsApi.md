# ThirdPartyAccountsApi

All URIs are relative to *https://api.criteo.com*. Please check the detailed instructions about this API at [https://developers.criteo.com/](https://developers.criteo.com/).

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addThirdPartyAccountBrands**](ThirdPartyAccountsApi.md#addThirdPartyAccountBrands) | **POST** /preview/retail-media/third-party-accounts/{accountId}/brands/add | /preview/retail-media/third-party-accounts/{accountId}/brands/add |
| [**createThirdPartyBrandAccount**](ThirdPartyAccountsApi.md#createThirdPartyBrandAccount) | **POST** /preview/retail-media/third-party-accounts/{accountId}/create-brand-account | /preview/retail-media/third-party-accounts/{accountId}/create-brand-account |
| [**createThirdPartySellerAccount**](ThirdPartyAccountsApi.md#createThirdPartySellerAccount) | **POST** /preview/retail-media/third-party-accounts/{accountId}/create-seller-account | /preview/retail-media/third-party-accounts/{accountId}/create-seller-account |
| [**grantThirdPartyConsent**](ThirdPartyAccountsApi.md#grantThirdPartyConsent) | **POST** /preview/retail-media/accounts/{accountId}/grant-third-party-consent | /preview/retail-media/accounts/{accountId}/grant-third-party-consent |
| [**removeThirdPartyAccountBrand**](ThirdPartyAccountsApi.md#removeThirdPartyAccountBrand) | **POST** /preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove | /preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove |
| [**updateThirdPartyAccountSellers**](ThirdPartyAccountsApi.md#updateThirdPartyAccountSellers) | **PUT** /preview/retail-media/third-party-accounts/{accountId}/sellers | /preview/retail-media/third-party-accounts/{accountId}/sellers |



## addThirdPartyAccountBrands

> ValueResourceOutcomeOfRetailMediaBrands addThirdPartyAccountBrands(accountId, valueResourceInputOfRetailMediaBrands)

/preview/retail-media/third-party-accounts/{accountId}/brands/add

add the provided brands to an account. This will not remove any existing brands.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.ThirdPartyAccountsApi;

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

        ThirdPartyAccountsApi apiInstance = new ThirdPartyAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | account to add brands to
        ValueResourceInputOfRetailMediaBrands valueResourceInputOfRetailMediaBrands = new ValueResourceInputOfRetailMediaBrands(); // ValueResourceInputOfRetailMediaBrands | list of bands to add to an account
        try {
            ValueResourceOutcomeOfRetailMediaBrands result = apiInstance.addThirdPartyAccountBrands(accountId, valueResourceInputOfRetailMediaBrands);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ThirdPartyAccountsApi#addThirdPartyAccountBrands");
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
| **accountId** | **String**| account to add brands to | |
| **valueResourceInputOfRetailMediaBrands** | [**ValueResourceInputOfRetailMediaBrands**](ValueResourceInputOfRetailMediaBrands.md)| list of bands to add to an account | [optional] |

### Return type

[**ValueResourceOutcomeOfRetailMediaBrands**](ValueResourceOutcomeOfRetailMediaBrands.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## createThirdPartyBrandAccount

> EntityResourceOutcomeOfRetailMediaAccountV2 createThirdPartyBrandAccount(accountId, valueResourceInputOfRetailMediaBrandAccountCreationV2)

/preview/retail-media/third-party-accounts/{accountId}/create-brand-account

Create a private market demand brand account under a given parent account.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.ThirdPartyAccountsApi;

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

        ThirdPartyAccountsApi apiInstance = new ThirdPartyAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | parent supply account to create account under
        ValueResourceInputOfRetailMediaBrandAccountCreationV2 valueResourceInputOfRetailMediaBrandAccountCreationV2 = new ValueResourceInputOfRetailMediaBrandAccountCreationV2(); // ValueResourceInputOfRetailMediaBrandAccountCreationV2 | 
        try {
            EntityResourceOutcomeOfRetailMediaAccountV2 result = apiInstance.createThirdPartyBrandAccount(accountId, valueResourceInputOfRetailMediaBrandAccountCreationV2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ThirdPartyAccountsApi#createThirdPartyBrandAccount");
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
| **accountId** | **String**| parent supply account to create account under | |
| **valueResourceInputOfRetailMediaBrandAccountCreationV2** | [**ValueResourceInputOfRetailMediaBrandAccountCreationV2**](ValueResourceInputOfRetailMediaBrandAccountCreationV2.md)|  | [optional] |

### Return type

[**EntityResourceOutcomeOfRetailMediaAccountV2**](EntityResourceOutcomeOfRetailMediaAccountV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## createThirdPartySellerAccount

> EntityResourceOutcomeOfRetailMediaAccountV2 createThirdPartySellerAccount(accountId, valueResourceInputOfRetailMediaSellerAccountCreationV2)

/preview/retail-media/third-party-accounts/{accountId}/create-seller-account

Create a private market demand seller account under a given parent account.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.ThirdPartyAccountsApi;

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

        ThirdPartyAccountsApi apiInstance = new ThirdPartyAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | parent supply account to create account under
        ValueResourceInputOfRetailMediaSellerAccountCreationV2 valueResourceInputOfRetailMediaSellerAccountCreationV2 = new ValueResourceInputOfRetailMediaSellerAccountCreationV2(); // ValueResourceInputOfRetailMediaSellerAccountCreationV2 | 
        try {
            EntityResourceOutcomeOfRetailMediaAccountV2 result = apiInstance.createThirdPartySellerAccount(accountId, valueResourceInputOfRetailMediaSellerAccountCreationV2);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ThirdPartyAccountsApi#createThirdPartySellerAccount");
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
| **accountId** | **String**| parent supply account to create account under | |
| **valueResourceInputOfRetailMediaSellerAccountCreationV2** | [**ValueResourceInputOfRetailMediaSellerAccountCreationV2**](ValueResourceInputOfRetailMediaSellerAccountCreationV2.md)|  | [optional] |

### Return type

[**EntityResourceOutcomeOfRetailMediaAccountV2**](EntityResourceOutcomeOfRetailMediaAccountV2.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |


## grantThirdPartyConsent

> grantThirdPartyConsent(accountId, grantConsentInput)

/preview/retail-media/accounts/{accountId}/grant-third-party-consent

Grant third-party consent to a business application on behalf of a Private Market demand account

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.ThirdPartyAccountsApi;

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

        ThirdPartyAccountsApi apiInstance = new ThirdPartyAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | The demand account ID on which to grant consent
        GrantConsentInput grantConsentInput = new GrantConsentInput(); // GrantConsentInput | The request input containing clientId, callbackURL, and callbackState
        try {
            apiInstance.grantThirdPartyConsent(accountId, grantConsentInput);
        } catch (ApiException e) {
            System.err.println("Exception when calling ThirdPartyAccountsApi#grantThirdPartyConsent");
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
| **accountId** | **String**| The demand account ID on which to grant consent | |
| **grantConsentInput** | [**GrantConsentInput**](GrantConsentInput.md)| The request input containing clientId, callbackURL, and callbackState | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |


## removeThirdPartyAccountBrand

> ValueResourceOutcomeOfRetailMediaBrands removeThirdPartyAccountBrand(accountId, brandId)

/preview/retail-media/third-party-accounts/{accountId}/brands/{brandId}/remove

Attempt to remove the provided brand from the account.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.ThirdPartyAccountsApi;

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

        ThirdPartyAccountsApi apiInstance = new ThirdPartyAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | account id to remove brand from
        String brandId = "brandId_example"; // String | brand to remove
        try {
            ValueResourceOutcomeOfRetailMediaBrands result = apiInstance.removeThirdPartyAccountBrand(accountId, brandId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ThirdPartyAccountsApi#removeThirdPartyAccountBrand");
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
| **accountId** | **String**| account id to remove brand from | |
| **brandId** | **String**| brand to remove | |

### Return type

[**ValueResourceOutcomeOfRetailMediaBrands**](ValueResourceOutcomeOfRetailMediaBrands.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


## updateThirdPartyAccountSellers

> ValueResourceCollectionOutcomeOfRetailMediaSeller updateThirdPartyAccountSellers(accountId, valueResourceCollectionInputOfRetailMediaSeller)

/preview/retail-media/third-party-accounts/{accountId}/sellers

Update the list of sellers mapped to the account. This will override any existing mappings.

### Example

```java
package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.auth.*;
import com.criteo.api.retailmedia.preview.model.*;
import com.criteo.api.retailmedia.preview.api.ThirdPartyAccountsApi;

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

        ThirdPartyAccountsApi apiInstance = new ThirdPartyAccountsApi(defaultClient);
        String accountId = "accountId_example"; // String | accountId to update sellers for
        ValueResourceCollectionInputOfRetailMediaSeller valueResourceCollectionInputOfRetailMediaSeller = new ValueResourceCollectionInputOfRetailMediaSeller(); // ValueResourceCollectionInputOfRetailMediaSeller | 
        try {
            ValueResourceCollectionOutcomeOfRetailMediaSeller result = apiInstance.updateThirdPartyAccountSellers(accountId, valueResourceCollectionInputOfRetailMediaSeller);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling ThirdPartyAccountsApi#updateThirdPartyAccountSellers");
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
| **accountId** | **String**| accountId to update sellers for | |
| **valueResourceCollectionInputOfRetailMediaSeller** | [**ValueResourceCollectionInputOfRetailMediaSeller**](ValueResourceCollectionInputOfRetailMediaSeller.md)|  | |

### Return type

[**ValueResourceCollectionOutcomeOfRetailMediaSeller**](ValueResourceCollectionOutcomeOfRetailMediaSeller.md)

### Authorization

[oauth](../README.md#oauth), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

