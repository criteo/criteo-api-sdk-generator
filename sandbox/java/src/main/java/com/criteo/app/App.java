package com.criteo.app;

import com.criteo.api.marketingsolutions.v2022_07.ApiClient;
import com.criteo.api.marketingsolutions.v2022_07.ApiClientBuilder;
import com.criteo.api.marketingsolutions.v2022_07.ApiException;
import com.criteo.api.marketingsolutions.v2022_07.Configuration;
import com.criteo.api.marketingsolutions.v2022_07.auth.*;
import com.criteo.api.marketingsolutions.v2022_07.model.*;
import com.criteo.api.marketingsolutions.v2022_07.api.AdvertiserApi;

public class App {
    public static void main(String[] args) {
        
        // Configure OAuth2, two options:
        // 1. Use ApiClientBuilder to create the ApiClient with the credentials you want, refresh token mechanism IS handled for you 💚
        String clientId = "YOUR_CLIENT_ID";
        String clientSecret = "YOUR_CLIENT_SECRET";
        ApiClient defaultClient = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);

        // 2. Set your access token manually, refresh token mechanism IS NOT handled by the client
        // ApiClient defaultClient = Configuration.getDefaultApiClient();
        // OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
        // oauth.setAccessToken("YOUR_TOKEN");

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