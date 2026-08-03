package com.criteo.api.api.experimental;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.lang.*;
import java.util.Arrays;
import java.util.List;

import com.criteo.api.api.experimental.api.AnalyticsApi;
import com.criteo.api.api.experimental.model.BaseType;
import com.criteo.api.api.experimental.model.BaseTypeListRequest;
import com.criteo.api.api.experimental.model.BaseTypeListResponse;
import com.criteo.api.api.experimental.model.BaseTypeRequest;
import com.criteo.api.api.experimental.model.BaseTypeResource;
import com.criteo.api.api.experimental.model.BaseTypeResponse;
import com.criteo.api.api.experimental.model.DerivedTypeOne;
import com.criteo.api.api.experimental.model.DerivedTypeOneRequest;
import com.criteo.api.api.experimental.model.DerivedTypeOneResource;
import com.criteo.api.api.experimental.model.DerivedTypeOneResponse;
import com.criteo.api.api.experimental.model.DerivedTypeTwo;

public class PolymorphismTests {

    // A valid bearer token has a short lifetime; fill it in here (single place) before running the success tests.
    private static final String VALID_TOKEN = "";

    private static final String TYPE_ONE_VALUE = "type-one";
    private static final int TYPE_TWO_VALUE = 42;
    private static final int COMMON_DATA_LENGTH = 12;

    private static AnalyticsApi apiWithToken(String bearerToken) {
        ApiClient client = new ApiClient();
        client.setAccessToken(bearerToken);
        return new AnalyticsApi(client);
    }

    // NOTE on typeDiscriminator: the generated model defaults it to the class name
    // ("DerivedTypeOne"), but the server expects the discriminator mapping value
    // ("derivedTypeOne"), so it is set explicitly on every derived instance below.

    private static DerivedTypeOne sampleDerivedTypeOne() {
        DerivedTypeOne attributes = new DerivedTypeOne();
        attributes.setTypeOneValue(TYPE_ONE_VALUE);
        attributes.setCommonData(new byte[COMMON_DATA_LENGTH]);
        attributes.setTypeDiscriminator("derivedTypeOne");
        return attributes;
    }

    private static DerivedTypeTwo sampleDerivedTypeTwo() {
        DerivedTypeTwo attributes = new DerivedTypeTwo();
        attributes.setTypeTwoValue(TYPE_TWO_VALUE);
        attributes.setCommonData(new byte[COMMON_DATA_LENGTH]);
        attributes.setTypeDiscriminator("derivedTypeTwo");
        return attributes;
    }

    private static DerivedTypeOneRequest sampleInheritanceRequest() {
        return new DerivedTypeOneRequest()
                .data(new DerivedTypeOneResource()
                        .type("DerivedTypeOne")
                        .attributes(sampleDerivedTypeOne()));
    }

    @Test
    public void testPostInheritanceWithEmptyTokenShouldReturnUnauthorized() {
        // Arrange
        AnalyticsApi api = apiWithToken("");

        // Act & Assert
        ApiException exception = assertThrows(ApiException.class, () -> {
            api.postInheritance(sampleInheritanceRequest());
        });

        assertEquals(401, exception.getCode());
    }

    @Test
    public void testPostInheritanceShouldSucceedWithValidToken() throws ApiException {
        // Arrange
        AnalyticsApi api = apiWithToken(VALID_TOKEN);

        // Act
        ApiResponse<DerivedTypeOneResponse> httpResponse = api.postInheritanceWithHttpInfo(sampleInheritanceRequest());

        // Assert
        assertEquals(200, httpResponse.getStatusCode());

        DerivedTypeOne attributes = httpResponse.getData().getData().getAttributes();
        assertNotNull(attributes);
        assertNotNull(attributes.getCommonData());
        assertEquals(COMMON_DATA_LENGTH, attributes.getCommonData().length);
        assertEquals(TYPE_ONE_VALUE, attributes.getTypeOneValue());
    }

    @Test
    public void testPostPolymorphismWithDerivedTypeOneShouldSucceed() throws ApiException {
        // Arrange
        AnalyticsApi api = apiWithToken(VALID_TOKEN);
        BaseTypeRequest request = new BaseTypeRequest()
                .data(new BaseTypeResource()
                        .type("DerivedTypeOne")
                        .attributes(sampleDerivedTypeOne()));

        // Act
        ApiResponse<BaseTypeResponse> httpResponse = api.postPolymorphismWithHttpInfo(request);

        // Assert
        assertEquals(200, httpResponse.getStatusCode());

        BaseType attributes = httpResponse.getData().getData().getAttributes();
        assertTrue(attributes instanceof DerivedTypeOne,
                "attributes should be deserialized as DerivedTypeOne but was " + attributes.getClass().getName());
        DerivedTypeOne derived = (DerivedTypeOne) attributes;
        assertEquals(COMMON_DATA_LENGTH, derived.getCommonData().length);
        assertEquals(TYPE_ONE_VALUE, derived.getTypeOneValue());
    }

    @Test
    public void testPostPolymorphismWithDerivedTypeTwoShouldSucceed() throws ApiException {
        // Arrange
        AnalyticsApi api = apiWithToken(VALID_TOKEN);
        BaseTypeRequest request = new BaseTypeRequest()
                .data(new BaseTypeResource()
                        .type("DerivedTypeTwo")
                        .attributes(sampleDerivedTypeTwo()));

        // Act
        ApiResponse<BaseTypeResponse> httpResponse = api.postPolymorphismWithHttpInfo(request);

        // Assert
        assertEquals(200, httpResponse.getStatusCode());

        BaseType attributes = httpResponse.getData().getData().getAttributes();
        assertTrue(attributes instanceof DerivedTypeTwo,
                "attributes should be deserialized as DerivedTypeTwo but was " + attributes.getClass().getName());
        DerivedTypeTwo derived = (DerivedTypeTwo) attributes;
        assertEquals(COMMON_DATA_LENGTH, derived.getCommonData().length);
        assertEquals(TYPE_TWO_VALUE, derived.getTypeTwoValue().intValue());
    }

    @Test
    public void testPostPolymorphicListWithDerivedTypesShouldSucceed() throws ApiException {
        // Arrange
        AnalyticsApi api = apiWithToken(VALID_TOKEN);
        BaseTypeListRequest request = new BaseTypeListRequest()
                .data(Arrays.asList(
                        new BaseTypeResource()
                                .type("DerivedTypeOne")
                                .attributes(sampleDerivedTypeOne()),
                        new BaseTypeResource()
                                .type("DerivedTypeTwo")
                                .attributes(sampleDerivedTypeTwo())));

        // Act
        ApiResponse<BaseTypeListResponse> httpResponse = api.postPolymorphicListWithHttpInfo(request);

        // Assert
        assertEquals(200, httpResponse.getStatusCode());

        List<BaseTypeResource> data = httpResponse.getData().getData();
        assertNotNull(data);
        assertEquals(2, data.size());

        // First element should round-trip as DerivedTypeOne.
        BaseType first = data.get(0).getAttributes();
        assertTrue(first instanceof DerivedTypeOne,
                "first element should be DerivedTypeOne but was " + first.getClass().getName());
        DerivedTypeOne firstDerived = (DerivedTypeOne) first;
        assertEquals(COMMON_DATA_LENGTH, firstDerived.getCommonData().length);
        assertEquals(TYPE_ONE_VALUE, firstDerived.getTypeOneValue());

        // Second element should round-trip as DerivedTypeTwo.
        BaseType second = data.get(1).getAttributes();
        assertTrue(second instanceof DerivedTypeTwo,
                "second element should be DerivedTypeTwo but was " + second.getClass().getName());
        DerivedTypeTwo secondDerived = (DerivedTypeTwo) second;
        assertEquals(COMMON_DATA_LENGTH, secondDerived.getCommonData().length);
        assertEquals(TYPE_TWO_VALUE, secondDerived.getTypeTwoValue().intValue());
    }
}
