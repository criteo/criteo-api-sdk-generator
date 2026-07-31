package com.criteo.api.marketingsolutions.preview;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.lang.*;

import com.criteo.api.marketingsolutions.preview.ApiClient;
import com.criteo.api.marketingsolutions.preview.ApiClientBuilder;
import com.criteo.api.marketingsolutions.preview.ApiException;
import com.criteo.api.marketingsolutions.preview.ApiResponse;
import com.criteo.api.marketingsolutions.preview.Configuration;
import com.criteo.api.marketingsolutions.preview.ExampleApplication;
import com.criteo.api.marketingsolutions.preview.api.GatewayApi;
import com.criteo.api.marketingsolutions.preview.model.ApplicationSummaryModelResponse;

public class GatewayApiTest {
    private ApiClient client;

    private static String clientId = System.getenv("MARKETINGSOLUTIONS_TEST_CLIENT_ID");
    private static String clientSecret = System.getenv("MARKETINGSOLUTIONS_TEST_CLIENT_SECRET");
    private static Integer applicationId = Integer.parseInt(System.getenv("MARKETINGSOLUTIONS_TEST_APPLICATION_ID"));

    @BeforeEach
    public void setUp() {
        assertNotNull(clientId);
        assertNotNull(clientSecret);
        assertNotNull(applicationId);

        client = ApiClientBuilder.ForClientCredentials(clientId, clientSecret);
    }

    @Test
    public void testExampleWorks() throws ApiException {
        // Act
        ExampleApplication.CallTheApplicationEndpoint(clientId, clientSecret);
    }
 
    @Test
    public void testGetCurrentApplicationShouldSucceedWithValidToken() throws ApiException {
        // Arrange
        GatewayApi api = new GatewayApi(client);

        // Act
        ApiResponse<ApplicationSummaryModelResponse> httpResponse = api.getCurrentApplicationWithHttpInfo();

        // Assert
        assertEquals(200, httpResponse.getStatusCode());

        ApplicationSummaryModelResponse response = httpResponse.getData();
        assertEquals(applicationId, response.getData().getAttributes().getApplicationId());
    }

    @Test
    public void testGetCurrentApplicationShouldSucceedWithRenewedInvalidToken() throws ApiException {
        // Arrange
        String invalidToken = "invalid.access.token";
        client.setAccessToken(invalidToken);
        GatewayApi api = new GatewayApi(client);

        // Act
        ApiResponse<ApplicationSummaryModelResponse> httpResponse = api.getCurrentApplicationWithHttpInfo();

        // Assert
        assertEquals(200, httpResponse.getStatusCode());

        ApplicationSummaryModelResponse response = httpResponse.getData();
        assertEquals(applicationId, response.getData().getAttributes().getApplicationId());
    }

    @Test
    public void testGetCurrentApplicationShouldFailWithoutToken() throws ApiException {
        // Arrange
        GatewayApi api = new GatewayApi(new ApiClient());

        // Act & Assert
        ApiException exception = assertThrows(ApiException.class, () -> {
            api.getCurrentApplication();
        });
        assertTrue(exception.getMessage().contains("must be authenticated"));
    }
}
