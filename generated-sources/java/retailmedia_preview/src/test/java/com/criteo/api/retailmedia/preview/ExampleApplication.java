package com.criteo.api.retailmedia.preview;

import com.criteo.api.retailmedia.preview.ApiClient;
import com.criteo.api.retailmedia.preview.ApiClientBuilder;
import com.criteo.api.retailmedia.preview.ApiException;
import com.criteo.api.retailmedia.preview.ApiResponse;
import com.criteo.api.retailmedia.preview.Configuration;
import com.criteo.api.retailmedia.preview.api.GatewayApi;
import com.criteo.api.retailmedia.preview.model.*;


public class ExampleApplication {

    public static void main(String[] args) throws ApiException{
        
        String clientId = "client-id";
        String clientSecret = "client-secret";

        CallTheApplicationEndpoint(clientId, clientSecret);
    }

    public static void CallTheApplicationEndpoint(String clientId, String clientSecret) throws ApiException{

        //Create a client using your choosen OAuth flow. The client will handle the token generation/renewal for you
        ApiClient client = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);        

        //The Gateway API regroups common technical endpoints that exists for all versions
        //You can find the other endpoints in the other *Api
        //You can reuse the same client with several Apis, but be careful, as they will then use the same token and credentials
        GatewayApi api = new GatewayApi(client);

        try {
            //Perform the call to the application introspection endpoint
            ApplicationSummaryModelResponse myApplicationResponse = api.getCurrentApplication();

            /*
            * Most of Criteo's API response follow the same structure: 
            * The response consists of a Data, Errors and Warnings fields
            * The Data fields contains an Id (if applicable), a Type, and an Attributes field that contains the business object
            */
            ApplicationSummaryModel myApplication = myApplicationResponse.getData().getAttributes();
            System.out.println("Hello, I'm using Criteo API and I'm connected as " + myApplication.getName());

            //Additionally, all endpoints can be called with the 'WithHttpInfo' prefix, to access more details on the HTTP call
            ApiResponse<ApplicationSummaryModelResponse> myHttpResponse = api.getCurrentApplicationWithHttpInfo();
            System.out.println("The call status is " + myHttpResponse.getStatusCode());

        } catch (ApiException e) {
            System.err.println(e.getCode());
            System.err.println(e.getResponseBody());
            throw e;
        }
    }
}
