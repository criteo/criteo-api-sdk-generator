import pytest
from push_php_sdk import PushPhpSdkPipeline

criteo_services = ['marketingsolutions', 'retailmedia']

@pytest.mark.parametrize("criteo_service", criteo_services)
def test_should_clone_right_repo(criteo_service):
  # Arrange
  expected_repository = 'criteo-api-{criteo_service}-php-sdk'
  pipeline = PushPhpSdkPipeline()

  # Action


  # Assert
