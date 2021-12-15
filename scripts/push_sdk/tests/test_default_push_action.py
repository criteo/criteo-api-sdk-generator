import pytest
from os import path

from ..clients.git_client import GitException
from .builders.git_client_builder import GitClientBuilder
from .builders.fs_client_builder import FsClientBuilder
from .builders.os_client_builder import OsClientBuilder
from ..default_push_action import DefaultPushSdkAction

class TestDefaultPushAction:

  @pytest.fixture(autouse=True)
  def setup_builders(self):
    self.test_programming_language = 'java'
    self.repository_name = f'criteo-api-{self.test_programming_language}-sdk'
    self.generated_sources = f'/Users/john.doe/criteo-api-sdk-generator/generated-sources/{self.test_programming_language}'
    self.sdk_repository = '/temp'

    self.git_client_builder = GitClientBuilder().that_responds_on_diff_count(2)

    self.fs_client_builder = (FsClientBuilder().that_responds_on_exists(self.generated_sources, True)
                              .that_responds_on_exists(path.join(self.sdk_repository, self.repository_name), True)
                              .that_responds_on_exists(path.join(self.sdk_repository, self.repository_name, 'sdks'), True))

    self.os_client_builder = (OsClientBuilder().that_responds_on_get_generated_sources_base_path(self.generated_sources)
                              .that_responds_on_get_sdk_repo_base_path(self.sdk_repository))


  def test_should_not_push_when_diff_count_is_null(self):
    # Arrange
    git_client = self.git_client_builder.that_responds_on_diff_count(0).client
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act
    action.execute()

    # Assert
    assert git_client.is_pushed == False
  
  def test_should_push_when_diff_count_is_not_null(self):
    # Arrange
    git_client = self.git_client_builder.that_responds_on_diff_count(2).client
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act
    action.execute()

    # Assert
    assert git_client.is_pushed == True
  
  def test_should_fail_when_push_fails(self):
    # Arrange
    git_client = self.git_client_builder.that_fails_on_push().client
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act & Assert
    with pytest.raises(GitException):
      action.execute()
