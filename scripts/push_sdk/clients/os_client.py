from ..models.programming_language import ProgrammingLanguage
from ..models.criteo_service import CriteoService
from ..utils import assert_environment_variable


class IOsClient:
  def get_private_key(programming_language, criteo_service = None):
    if programming_language == ProgrammingLanguage.php:
      return (assert_environment_variable('PHP_SDK_REPO_PRIVATE_KEY_MS')
        if criteo_service == CriteoService.marketingsolutions
        else assert_environment_variable('PHP_SDK_REPO_PRIVATE_KEY_RM'))
    else:
      raise Exception(f'Unsupported programming language ({programming_language})')

assert_environment_variable('GITHUB_WORKSPACE')
generator_repo_dir = assert_environment_variable('GITHUB_WORKSPACE')
    generator_repo_dir += '/generated-sources/php'

    self.sdk_base_folder = assert_environment_variable('RUNNER_TEMP')
    self.git_user = assert_environment_variable('GITHUB_ACTOR')