from os import path

from shared.clients.git_client import IGitClient
from shared.clients.fs_client import IFsClient
from shared.clients.os_client import IOsClient
from shared.models.programming_language import ProgrammingLanguage
from shared.utils import get_logger, get_formatted_date

class DefaultPushSdkAction:
  def __init__(self, git_client: IGitClient, fs_client: IFsClient, os_client: IOsClient, programming_language: ProgrammingLanguage):
    self.git = git_client
    self.fs = fs_client
    self.os = os_client
    self.logger = get_logger(__name__)

    self.programming_language = programming_language.lower()
    self.generator_version = '0'

    self.__init_environment_variables()

    self.git.setup(self.git_user)
    if not self.is_prod_environment:
      self.git.setup_ssh(self.private_key)

  def execute(self):
    self.__clone_sdk_repository()

    self.__update_sources()

    self.__upload_sources()


  def __clone_sdk_repository(self):
    self.fs.change_dir(self.sdk_repository)

    repository_name = f'criteo-api-{self.programming_language}-sdk'

    self.sdk_repository = path.join(self.sdk_repository, repository_name)

    if not self.fs.exists(self.sdk_repository):
      organization_name = 'criteo'
    
      self.logger.info(f'Cloning repository {organization_name}/{repository_name}...')

      self.git.clone(organization_name, repository_name)


  def __update_sources(self):
    sdks_folder = path.join(self.sdk_repository, 'sdks')

    if self.fs.exists(sdks_folder):
      self.logger.info(f'Remove folder {sdks_folder}...')
      self.fs.remove(sdks_folder)
    
    if self.fs.exists(self.generated_sources):
      self.logger.info(f'Copy sources from {self.generated_sources} to {sdks_folder}...')
      self.fs.copy(self.generated_sources, sdks_folder)


  def __upload_sources(self):
    self.fs.change_dir(self.sdk_repository)

    self.git.add()

    diff_count = self.git.diff_count()

    self.logger.info(f'{diff_count} lines modified.')

    if diff_count > 0:
      now_date = get_formatted_date()

      self.logger.info(f'Committing...')
      self.git.commit(f'[{now_date}] Automatic update of SDK.')

      self.logger.info(f'Pushing commit...')
      self.git.push(include_tags=False)


  def __init_environment_variables(self):
    self.is_prod_environment = self.os.is_prod_environment()
    self.generated_sources = self.os.get_generated_sources_base_path(self.programming_language)
    self.sdk_repository = self.os.get_sdk_repo_base_path()
    self.git_user = self.os.get_git_user()

    if not self.is_prod_environment:
      self.private_key = self.os.get_private_key(self.programming_language)
