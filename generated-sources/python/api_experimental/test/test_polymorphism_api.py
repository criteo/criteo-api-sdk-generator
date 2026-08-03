import base64

import pytest

from criteo_api_api_experimental.api.analytics_api import AnalyticsApi
from criteo_api_api_experimental.api_client import ApiClient
from criteo_api_api_experimental.configuration import Configuration
from criteo_api_api_experimental.rest import ApiException
from criteo_api_api_experimental.model.base_type_list_request import BaseTypeListRequest
from criteo_api_api_experimental.model.base_type_request import BaseTypeRequest
from criteo_api_api_experimental.model.base_type_resource import BaseTypeResource
from criteo_api_api_experimental.model.derived_type_one import DerivedTypeOne
from criteo_api_api_experimental.model.derived_type_one_request import DerivedTypeOneRequest
from criteo_api_api_experimental.model.derived_type_one_resource import DerivedTypeOneResource
from criteo_api_api_experimental.model.derived_type_two import DerivedTypeTwo


# A valid bearer token has a short lifetime; fill it in here (single place) before running the success tests.
VALID_TOKEN = ""

TYPE_ONE_VALUE = "type-one"
TYPE_TWO_VALUE = 42
COMMON_DATA_LENGTH = 12
# commonData is a byte field, serialized as a base64 string.
COMMON_DATA = base64.b64encode(bytes(COMMON_DATA_LENGTH)).decode("ascii")


class TestPolymorphismApi:

    @staticmethod
    def _api_with_token(token):
        configuration = Configuration()
        configuration.access_token = token
        return AnalyticsApi(ApiClient(configuration))

    # NOTE on type_discriminator: the generated model does not populate the discriminator
    # with the mapping value, and the server expects the mapping value ("derivedTypeOne"),
    # so it is set explicitly on every derived instance below.

    @staticmethod
    def _sample_derived_type_one():
        return DerivedTypeOne(
            type_one_value=TYPE_ONE_VALUE,
            common_data=COMMON_DATA,
            type_discriminator="derivedTypeOne",
        )

    @staticmethod
    def _sample_derived_type_two():
        return DerivedTypeTwo(
            type_two_value=TYPE_TWO_VALUE,
            common_data=COMMON_DATA,
            type_discriminator="derivedTypeTwo",
        )

    def _sample_inheritance_request(self):
        return DerivedTypeOneRequest(
            data=DerivedTypeOneResource(
                type="DerivedTypeOne",
                attributes=self._sample_derived_type_one(),
            )
        )

    def test_post_inheritance_with_empty_token_should_return_unauthorized(self):
        # Arrange
        api = self._api_with_token("")

        # Act & Assert
        with pytest.raises(ApiException) as exc_info:
            api.post_inheritance(derived_type_one_request=self._sample_inheritance_request())

        assert exc_info.value.status == 401

    def test_post_inheritance_should_succeed_with_valid_token(self):
        # Arrange
        api = self._api_with_token(VALID_TOKEN)

        # Act
        response = api.post_inheritance(derived_type_one_request=self._sample_inheritance_request())

        # Assert
        attributes = response.data.attributes
        assert attributes is not None
        assert len(base64.b64decode(attributes.common_data)) == COMMON_DATA_LENGTH
        assert attributes.type_one_value == TYPE_ONE_VALUE

    def test_post_polymorphism_with_derived_type_one_should_succeed(self):
        # Arrange
        api = self._api_with_token(VALID_TOKEN)
        request = BaseTypeRequest(
            data=BaseTypeResource(
                type="DerivedTypeOne",
                attributes=self._sample_derived_type_one(),
            )
        )

        # Act
        response = api.post_polymorphism(base_type_request=request)

        # Assert
        attributes = response.data.attributes
        assert isinstance(attributes, DerivedTypeOne), \
            "attributes should be deserialized as DerivedTypeOne but was %s" % type(attributes).__name__
        assert len(base64.b64decode(attributes.common_data)) == COMMON_DATA_LENGTH
        assert attributes.type_one_value == TYPE_ONE_VALUE

    def test_post_polymorphism_with_derived_type_two_should_succeed(self):
        # Arrange
        api = self._api_with_token(VALID_TOKEN)
        request = BaseTypeRequest(
            data=BaseTypeResource(
                type="DerivedTypeTwo",
                attributes=self._sample_derived_type_two(),
            )
        )

        # Act
        response = api.post_polymorphism(base_type_request=request)

        # Assert
        attributes = response.data.attributes
        assert isinstance(attributes, DerivedTypeTwo), \
            "attributes should be deserialized as DerivedTypeTwo but was %s" % type(attributes).__name__
        assert len(base64.b64decode(attributes.common_data)) == COMMON_DATA_LENGTH
        assert attributes.type_two_value == TYPE_TWO_VALUE

    def test_post_polymorphic_list_with_derived_types_should_succeed(self):
        # Arrange
        api = self._api_with_token(VALID_TOKEN)
        request = BaseTypeListRequest(
            data=[
                BaseTypeResource(type="DerivedTypeOne", attributes=self._sample_derived_type_one()),
                BaseTypeResource(type="DerivedTypeTwo", attributes=self._sample_derived_type_two()),
            ]
        )

        # Act
        response = api.post_polymorphic_list(base_type_list_request=request)

        # Assert
        data = response.data
        assert len(data) == 2

        # First element should round-trip as DerivedTypeOne.
        first = data[0].attributes
        assert isinstance(first, DerivedTypeOne), \
            "first element should be DerivedTypeOne but was %s" % type(first).__name__
        assert len(base64.b64decode(first.common_data)) == COMMON_DATA_LENGTH
        assert first.type_one_value == TYPE_ONE_VALUE

        # Second element should round-trip as DerivedTypeTwo.
        second = data[1].attributes
        assert isinstance(second, DerivedTypeTwo), \
            "second element should be DerivedTypeTwo but was %s" % type(second).__name__
        assert len(base64.b64decode(second.common_data)) == COMMON_DATA_LENGTH
        assert second.type_two_value == TYPE_TWO_VALUE
