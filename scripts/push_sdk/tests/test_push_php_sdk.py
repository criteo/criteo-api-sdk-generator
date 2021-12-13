import pytest

from ..php_pipeline import PushPhpSdkPipeline
from ..utils import get_formatted_date
from .dummies.dummy_git_client import DummyGitClient
from .dummies.dummy_fs_client import DummyFsClient
from .builders.git_client_builder import GitClientBuilder

# test_execute_should_fail_when_sdks_folder_not_found
# test_execute_should_fail_when_invalid_criteo_service
# test_execute_should_fail_when_invalid_api_version
# test_execute_should_fail_when_generated_sources_not_found
# test_execute_should_fail_when_copy_new_sources_fails
# test_execute_should_fail_when_remove_old_sources_fails
# test_execute_should_fail_when_tag_fails_more_than_max_retries
# test_execute_should_fail_when_commit_fails
# test_execute_should_fail_when_push_fails
# test_execute_should_succeed_when_no_diff
# test_execute_should_succeed_when_diff
# test_execute_should_succeed_when_tag_succeed_after_less_than_max_retries
# test_execute_should_fail_when_cloned_repositories_removal_fails

test_data = [
  ('marketingsolutions', 'preview'),
  ('marketingsolutions', '2021-10'),
  ('retailmedia', 'preview'),
  ('retailmedia', '2021-10')
]

def test_execute_should_fail_when_sdks_folder_not_found():
  criteo_service = 'marketingsolutions'
  api_version = 'preview'

  git_client = GitClientBuilder().with_diff_count(2).with_failures_before_success(100).client
  fs_client = DummyFsClient()
  pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

  # Act & Assert
  with pytest.raises(Exception):
    pipeline.upload()

@pytest.mark.parametrize("criteo_service, api_version", test_data)
def test_clone_successful(criteo_service, api_version):
  # Arrange
  expected_repository = f'criteo/criteo-api-{criteo_service}-php-sdk'

  git_client = DummyGitClient()
  fs_client = DummyFsClient()
  pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

  # Act
  pipeline.clone_repo()

  # Assert
  assert git_client.cloned_repository == expected_repository

test_data = [
  ('preview', 'preview'),
  ('2021-04', '2021.04'),
  ('2021-07', '2021.07'),
  ('2021-10', '2021.10'),
  ('2022-01', '2022.01'),
]

@pytest.mark.parametrize("api_version, expected_branch", test_data)
def test_checkout_successful(api_version, expected_branch):
  criteo_service = 'marketingsolutions'
  git_client = DummyGitClient()
  fs_client = DummyFsClient()
  pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

  # Act
  pipeline.checkout()

  # Assert
  assert git_client.current_branch == expected_branch

test_data = [
  ('preview', 0, f'0.0.{get_formatted_date()}'),
  ('preview', 1, f'0.0.{get_formatted_date()}-patch1'),
  ('preview', 99, f'0.0.{get_formatted_date()}-patch99'),
  ('2021-10', 0, f'2021.10.0.{get_formatted_date()}'),
  ('2021-10', 1, f'2021.10.0.{get_formatted_date()}-patch1'),
  ('2021-10', 99, f'2021.10.0.{get_formatted_date()}-patch99'),
]

@pytest.mark.parametrize("api_version, failure_count, expected_tag", test_data)
def test_tag_successful(api_version, failure_count, expected_tag):
  criteo_service = 'marketingsolutions'

  git_client = GitClientBuilder().with_diff_count(2).with_failures_before_success(failure_count).client
  fs_client = DummyFsClient()
  pipeline = PushPhpSdkPipeline(git_client, fs_client)

  # Act
  pipeline.upload()

  # Assert
  assert git_client.current_tag == expected_tag

def test_tag_should_fail_when_tag_retries_exceed_max():
  criteo_service = 'marketingsolutions'
  api_version = 'preview'

  git_client = GitClientBuilder().with_diff_count(2).with_failures_before_success(100).client
  fs_client = DummyFsClient()
  pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

  # Act & Assert
  with pytest.raises(Exception):
    pipeline.upload()

def test_upload_should_not_be_triggered_if_no_diff():
  criteo_service = 'marketingsolutions'
  api_version = 'preview'

  git_client = GitClientBuilder().with_diff_count(0).client
  fs_client = DummyFsClient()
  pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

  # Act
  pipeline.upload()

  # Assert
  assert not git_client.is_pushed
