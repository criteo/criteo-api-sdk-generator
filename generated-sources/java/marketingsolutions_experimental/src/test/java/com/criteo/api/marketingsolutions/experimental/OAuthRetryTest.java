package com.criteo.api.marketingsolutions.experimental;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Protocol;
import okhttp3.Response;
import okhttp3.ResponseBody;

import org.apache.oltu.oauth2.client.request.OAuthClientRequest;
import org.apache.oltu.oauth2.common.message.types.GrantType;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.concurrent.atomic.AtomicInteger;

import com.criteo.api.marketingsolutions.experimental.auth.RetryingOAuth;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class OAuthRetryTest {
    @Test
    public void updateAccessTokenShouldRetryTransientTokenRequestIoFailures() throws Exception {
        AtomicInteger attempts = new AtomicInteger();
        OkHttpClient tokenClient = new OkHttpClient.Builder()
                .addInterceptor(chain -> {
                    int attempt = attempts.incrementAndGet();
                    if (attempt < 3) {
                        throw new IOException("connect timed out");
                    }

                    return new Response.Builder()
                            .request(chain.request())
                            .protocol(Protocol.HTTP_1_1)
                            .code(200)
                            .message("OK")
                            .addHeader("Content-Type", "application/json")
                            .body(ResponseBody.create(
                                    "{\"access_token\":\"retry-token\",\"token_type\":\"Bearer\",\"expires_in\":3600}",
                                    MediaType.parse("application/json")))
                            .build();
                })
                .build();

        RetryingOAuth retryingOAuth = new RetryingOAuth(
                tokenClient,
                OAuthClientRequest.tokenLocation("https://api.criteo.com/oauth2/token")
                        .setClientId("client-id")
                        .setClientSecret("client-secret")
                        .setGrantType(GrantType.CLIENT_CREDENTIALS));
        retryingOAuth.setTokenRequestMaxAttempts(3);
        retryingOAuth.setTokenRequestRetryBackoffMillis(1L);

        assertTrue(retryingOAuth.updateAccessToken(null));

        assertEquals("retry-token", retryingOAuth.getAccessToken());
        assertEquals(3, attempts.get());
    }
}
