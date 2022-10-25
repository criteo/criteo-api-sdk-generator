package com.criteo.app;

import com.criteo.api.marketingsolutions.v2022_07.ApiClient;
import com.criteo.api.marketingsolutions.v2022_07.ApiException;
import com.criteo.api.marketingsolutions.v2022_07.Configuration;
import com.criteo.api.marketingsolutions.v2022_07.auth.*;
import com.criteo.api.marketingsolutions.v2022_07.model.*;
import com.criteo.api.marketingsolutions.v2022_07.api.AdvertiserApi;

public class App {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        
        // Configure OAuth2, two options:
        // 1. Set your access token manually, refresh token mechanism IS NOT handled by the client
        OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        oauth.setAccessToken("YOUR_TOKEN");

        // 2. Set your credentials within the ApiClient, refresh token mechanism IS handled for you 💚
        // defaultClient.setUsername("YOUR_CIENT_ID");
        // defaultClient.setPassword("YOUR_CLIENT_SECRET");

        AdvertiserApi apiInstance = new AdvertiserApi(defaultClient);
        try {
            GetPortfolioResponse result = apiInstance.apiPortfolioGet();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdvertiserApi#apiPortfolioGet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}