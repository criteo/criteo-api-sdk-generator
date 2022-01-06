from os import path

from shared.models.programming_language import ProgrammingLanguage
from shared.models.criteo_service import CriteoService
from shared.utils import assert_environment_variable


class IOsClient:
  def get_private_key(self, programming_language, criteo_service = None):
    """
    Returns SSH private key for accessing SDK's repository:
    PHP - MarketingSolutions: PHP_SDK_REPO_PRIVATE_KEY_MS
    PHP - RetailMedia: PHP_SDK_REPO_PRIVATE_KEY_RM
    """
    pass
  
  def get_generated_sources_base_path(self, programming_language):
    """Returns path of directory containing generated SDKs"""
    pass

  def get_sdk_repo_base_path(self):
    """Returns rath of directory where SDK repository will be cloned"""
    pass
  
  def get_git_user(self):
    """Returns GIT user"""
    pass
  
  def is_prod_environment(self):
    """Returns True if environment is Github Actions, False if not"""
    pass

class OsClient(IOsClient):
  def get_private_key(self, programming_language, criteo_service = None):
    if programming_language == ProgrammingLanguage.php:
      return (assert_environment_variable('PHP_SDK_REPO_PRIVATE_KEY_MS')
        if criteo_service == CriteoService.marketingsolutions
        else assert_environment_variable('PHP_SDK_REPO_PRIVATE_KEY_RM'))
    else:
      raise Exception(f'Unsupported programming language ({programming_language})')
  
  def get_generated_sources_base_path(self, programming_language):
    generator_repo_dir = path.join(assert_environment_variable('GITHUB_WORKSPACE'), f'generated-sources/{programming_language}')
    return generator_repo_dir

  def get_sdk_repo_base_path(self):
    sdk_repo_base_path = assert_environment_variable('RUNNER_TEMP')
    return sdk_repo_base_path
  
  def get_git_user(self):
    git_user = assert_environment_variable('GITHUB_ACTOR')
    return git_user

  def is_prod_environment(self):
    try:
      assert_environment_variable('CI')
      return True
    except Exception:
      return False
