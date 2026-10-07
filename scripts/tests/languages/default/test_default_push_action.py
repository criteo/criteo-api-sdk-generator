import pytest
from os import path

from shared.clients.git_client import GitException
from languages.default.default_push_action import DefaultPushSdkAction
from tests.builders.git_client_builder import GitClientBuilder
from tests.builders.fs_client_builder import FsClientBuilder
from tests.builders.os_client_builder import OsClientBuilder

class TestDefaultPushAction:

  @pytest.fixture(autouse=True)
  def setup_builders(self):
    self.test_programming_language = 'java'
    self.repository_name = f'criteo-api-{self.test_programming_language}-sdk'
    self.generated_sources = f'/Users/john.doe/criteo-api-sdk-generator/generated-sources/{self.test_programming_language}'
    self.sdk_repository = '/temp'

    self.sdks_folder = path.join(self.sdk_repository, self.repository_name, 'sdks')
    self.sdk_dirs = ['commercegrid_2026-01', 'commercegrid_2026-07']
    self.sdk_paths = [path.join('sdks', sdk_dir) for sdk_dir in self.sdk_dirs]

    self.git_client_builder = GitClientBuilder().that_responds_on_diff_count(2)

    self.fs_client_builder = (FsClientBuilder().that_responds_on_exists(self.generated_sources, True)
                              .that_responds_on_exists(path.join(self.sdk_repository, self.repository_name), True)
                              .that_responds_on_exists(self.sdks_folder, True)
                              .that_responds_on_list_dir(self.sdks_folder, self.sdk_dirs))

    self.os_client_builder = (OsClientBuilder().that_responds_on_get_generated_sources_base_path(self.generated_sources)
                              .that_responds_on_get_sdk_repo_base_path(self.sdk_repository))


  def test_should_not_push_when_diff_count_returns_zero_for_all_sdks(self):
    # Arrange
    git_client = self.git_client_builder.that_responds_on_diff_count(0).client
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act
    action.execute()

    # Assert
    assert git_client.is_pushed == False
    assert git_client.restored == self.sdk_paths

  def test_should_push_when_at_least_one_sdk_has_meaningful_changes(self):
    # Arrange
    git_client = self.git_client_builder.that_responds_on_diff_count(2).client
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act
    action.execute()

    # Assert
    assert git_client.is_pushed == True
    assert git_client.restored == []

  def test_should_restore_only_sdks_where_diff_count_is_not_zero(self):
    # Arrange
    changed_sdk_path = self.sdk_paths[0]
    unchanged_sdk_path = self.sdk_paths[1]
    git_client = (self.git_client_builder
                  .that_responds_on_diff_count(0)
                  .that_responds_on_diff_count(5, pathspec=changed_sdk_path).client)
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act
    action.execute()

    # Assert
    assert git_client.is_pushed == True
    assert git_client.restored == [unchanged_sdk_path]
  
  def test_should_fail_when_push_fails(self):
    # Arrange
    git_client = self.git_client_builder.that_fails_on_push().client
    action = DefaultPushSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client, self.test_programming_language)

    # Act & Assert
    with pytest.raises(GitException):
      action.execute()
