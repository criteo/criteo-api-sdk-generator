import pytest
from os import path

from ..models.criteo_service import CriteoService
from ..push_php_sdk_action import PushPhpSdkAction
from ..clients.git_client import GitException
from ..utils import InvalidCriteoServiceException, InvalidApiVersionException, get_formatted_date
from ..builders.git_client_builder import GitClientBuilder
from ..builders.fs_client_builder import FsClientBuilder
from ..builders.os_client_builder import OsClientBuilder


class TestPushSdkAction:
  @pytest.fixture(autouse=True)
  def setup_builders(self):
    self.criteo_service = CriteoService.marketingsolutions
    self.api_version = '2021-10'
    self.repository_name = f'criteo-api-{self.criteo_service}-php-sdk'
    self.generated_sources = '/Users/john.doe/criteo-api-sdk-generator/generated-sources/php'
    self.sdk_repository = '/temp'

    self.git_client_builder = GitClientBuilder().that_responds_on_diff_count(2)

    self.fs_client_builder = (FsClientBuilder().that_responds_on_exists(self.generated_sources, True)
                              .that_responds_on_exists(path.join(self.sdk_repository, self.repository_name), True)
                              .that_responds_on_list_dir(self.generated_sources, [f'{self.criteo_service}_{self.api_version}'])
                              .that_responds_on_list_dir(path.join(self.sdk_repository, self.repository_name), ['lib'])
                              .that_responds_on_list_dir(path.join(self.generated_sources, f'{self.criteo_service}_{self.api_version}'), ['lib']))

    self.os_client_builder = (OsClientBuilder().that_responds_on_get_generated_sources_base_path(self.generated_sources)
                              .that_responds_on_get_sdk_repo_base_path(self.sdk_repository))

  def test_execute_should_fail_when_sdks_folder_not_found(self):
    # Arrange
    fs_client = self.fs_client_builder.that_responds_on_exists(self.generated_sources, False).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)

    # Act & Assert
    with pytest.raises(FileNotFoundError):
      action.execute()
  
  
  def test_execute_should_fail_when_invalid_folder_name_for_generate_source(self):
    # Arrange
    invalid_folder_name = 'invalid_folder_name'
    
    fs_client = (self.fs_client_builder.that_responds_on_list_dir(self.generated_sources, [invalid_folder_name])
      .client)
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)
    
    # Act & Assert
    with pytest.raises(InvalidCriteoServiceException):
      action.execute()
  
  def test_execute_should_fail_when_invalid_criteo_service(self):
    # Arrange
    invalid_criteo_service = 'invalid_criteo_service'
    
    fs_client = self.fs_client_builder.that_responds_on_list_dir(self.generated_sources, [f'{invalid_criteo_service}_preview']).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)
    
    # Act & Assert
    with pytest.raises(InvalidCriteoServiceException):
      action.execute()
      
  def test_execute_should_fail_when_invalid_api_version(self):
    # Arrange
    invalid_api_version = 'invalid-api-version'
    
    fs_client = self.fs_client_builder.that_responds_on_list_dir(self.generated_sources, [f'{CriteoService.marketingsolutions}_{invalid_api_version}']).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)
    
    # Act & Assert
    with pytest.raises(InvalidApiVersionException):
      action.execute()
  
  def test_execute_should_fail_when_remove_previous_sources_fails(self):
    # Arrange
    expected_exception = FileNotFoundError()
    
    fs_client = self.fs_client_builder.that_fails_on_remove(expected_exception).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)
    
    # Act & Assert
    with pytest.raises(FileNotFoundError):
      action.execute()
  
  def test_execute_should_fail_when_copy_new_sources_fails(self):
    # Arrange
    expected_exception = FileNotFoundError()
    
    fs_client = self.fs_client_builder.that_fails_on_copy(expected_exception).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)
    
    # Act & Assert
    with pytest.raises(FileNotFoundError):
      action.execute()
      
  def test_execute_should_fail_when_copy_new_sources_fails(self):
    # Arrange
    expected_exception = FileNotFoundError()
    
    fs_client = self.fs_client_builder.that_fails_on_copy(expected_exception).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)
    
    # Act & Assert
    with pytest.raises(FileNotFoundError):
      action.execute()
  
  test_data = [
    ('preview', 0, f'0.0.{get_formatted_date()}'),
    ('preview', 1, f'0.0.{get_formatted_date()}-patch1'),
    ('preview', 99, f'0.0.{get_formatted_date()}-patch99'),
    ('2021-10', 0, f'2021.10.0.{get_formatted_date()}'),
    ('2021-10', 1, f'2021.10.0.{get_formatted_date()}-patch1'),
    ('2021-10', 99, f'2021.10.0.{get_formatted_date()}-patch99'),
  ]

  @pytest.mark.parametrize("api_version, failure_count, expected_tag", test_data)
  def test_tag_successful(self, api_version, failure_count, expected_tag):
    # Arrange
    git_client = self.git_client_builder.with_nth_failures_before_success(failure_count).client
    fs_client = (self.fs_client_builder.that_responds_on_list_dir(self.generated_sources, [f'{self.criteo_service}_{api_version}'])
                                       .that_responds_on_list_dir(path.join(self.generated_sources, f'{self.criteo_service}_{api_version}'), ['lib'])).client
    action = PushPhpSdkAction(git_client, fs_client, self.os_client_builder.client)

    # Act
    action.execute()

    # Assert
    assert git_client.current_tag == expected_tag
  
  def test_tag_should_fail_when_tag_retries_exceed_max(self):
    # Arrange
    git_client = self.git_client_builder.with_nth_failures_before_success(100).client
    action = PushPhpSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client)

    # Act & Assert
    with pytest.raises(GitException):
      action.execute()
  
  test_data = [
    ('preview', 'preview'),
    ('2021-04', '2021.04'),
    ('2021-07', '2021.07'),
    ('2021-10', '2021.10'),
    ('2022-01', '2022.01'),
  ]

  @pytest.mark.parametrize("api_version, expected_branch", test_data)
  def test_checkout_successful(self, api_version, expected_branch):
    # Arrange
    fs_client = (self.fs_client_builder.that_responds_on_list_dir(self.generated_sources, [f'{self.criteo_service}_{api_version}'])
                                       .that_responds_on_list_dir(path.join(self.generated_sources, f'{self.criteo_service}_{api_version}'), ['lib'])).client
    action = PushPhpSdkAction(self.git_client_builder.client, fs_client, self.os_client_builder.client)

    # Act
    action.execute()

    # Assert
    assert self.git_client_builder.client.current_branch == expected_branch
  
  def test_upload_should_not_be_triggered_if_no_diff(self):
    # Arrange
    git_client = self.git_client_builder.that_responds_on_diff_count(0).client
    action = PushPhpSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client)

    # Act
    action.execute()

    # Assert
    assert not git_client.is_pushed
    
  def test_upload_should_be_triggered_if_diff_exists(self):
    # Arrange
    git_client = self.git_client_builder.that_responds_on_diff_count(42).client
    action = PushPhpSdkAction(git_client, self.fs_client_builder.client, self.os_client_builder.client)

    # Act
    action.execute()

    # Assert
    assert git_client.is_pushed
