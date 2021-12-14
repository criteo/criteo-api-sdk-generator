from os import path

from .clients.git_client import GitException
from .utils import get_logger, assert_environment_variable, assert_criteo_service, assert_api_version, get_formatted_date

logger = get_logger()

class PushPhpSdkAction:

  def __init__(self, git_client, fs_client, os_client):
    self.fs = fs_client
    self.git = git_client
    self.os = os_client
    
    self.programming_language = 'php'
    self.generator_version = 0
    self.cloned_repositories = []
    self.__init_environment_variables()

    logger.info(f'Setting up Git with user {self.git_user}...')
    self.git.setup(self.git_user)

  def execute(self):
    if not self.fs.exists(self.generated_sources_base_path):
      raise FileNotFoundError(f'[ERROR] Path {self.generated_sources_base_path} does not exist')
    
    for directory in self.fs.list_dir(self.generated_sources_base_path):
      logger.info(f'Handling generated sources for {directory}')

      if path.isfile(path.join(self.generated_sources_base_path, directory)):
        continue

      self.criteo_service = assert_criteo_service(directory)
      self.api_version = assert_api_version(directory)
      
      logger.info(f'Found Criteo Service "{self.criteo_service}" and API version "{self.api_version}"')
      
      if not self.is_prod_environment:
        private_key = self.os.get_private_key(self.programming_language, self.criteo_service)
        self.git.setup_ssh(private_key)
  
      self.clone_repo()

      self.checkout()

      self.update_sources()

      self.upload()

    self.clean()

  def clone_repo(self):
    self.fs.change_dir(self.sdk_base_folder)

    repository_name = f'criteo-api-{self.criteo_service}-php-sdk'

    self.sdk_repo_dir = path.join(self.sdk_base_folder, repository_name)

    if not self.fs.exists(self.sdk_repo_dir):
      organization_name = 'criteo'
    
      logger.info(f'Cloning repository {organization_name}/{repository_name}...')

      self.git.clone(organization_name, repository_name)

      self.cloned_repositories.append(self.sdk_repo_dir)

  def checkout(self):
    self.fs.change_dir(self.sdk_repo_dir)
  
    branch_name = self.api_version
    if self.criteo_service != 'preview':
      branch_name = branch_name.replace('-', '.')

    logger.info(f'Checkout branch {branch_name}.')

    self.git.checkout(branch_name)

  def update_sources(self):
    logger.info('Copying new sources to repository...')

    # Remove repository content except .git file
    for element_name in self.fs.list_dir(self.sdk_repo_dir):
      if element_name == '.git':
        continue
      
      self.fs.remove(path.join(self.sdk_repo_dir, element_name))
    
    generated_sources_path = path.join(self.generated_sources_base_path, f'{self.criteo_service}_{self.api_version}')
    for element_name in self.fs.list_dir(generated_sources_path):
      source = path.join(generated_sources_path, element_name)
      destination = path.join(self.sdk_repo_dir, element_name)
      self.fs.copy(source, destination)

  def upload(self):
    self.fs.change_dir(self.sdk_repo_dir)

    self.git.add()

    diff_count = self.git.diff_count()

    logger.info(f'{diff_count} new lines modified.')

    if diff_count > 0:
      now_date = get_formatted_date()

      self.git.commit(f'[{now_date}] Automatic update of SDK.')

      logger.info(f'Committing and tagging...')

      tag_name = self.__tag_with_retry()

      logger.info(f'Pushing commit and tag "{tag_name}"...')

      self.git.push(include_tags=True)      

  def clean(self):
    logger.info(f'Removing directory {self.sdk_repo_dir}')

    for repository in self.cloned_repositories:
      self.fs.remove(repository)
  
  def __init_environment_variables(self):
    self.generated_sources_base_path = self.os.get_generated_sources_base_path(self.programming_language)
    self.sdk_base_folder = self.os.get_sdk_repo_base_path()
    self.git_user = self.os.get_git_user()
    self.is_prod_environment = self.os.is_prod_environment()

  def __get_tag_name(self, patch=0):
      now_date = get_formatted_date()

      if self.api_version == 'preview':
        api_version = 0
      else:
        api_version = self.api_version.replace('-', '.')

      tag_name = f'{api_version}.{self.generator_version}.{now_date}'

      if patch > 0:
        tag_name += f'-patch{patch}'
      
      return tag_name
    
  def __tag_with_retry(self, max_retries=100):
    retry_count = 0;
    while retry_count < max_retries:
        try:
            tag_name = self.__get_tag_name(retry_count)
            self.git.tag(tag_name)
            
            return tag_name
        except GitException:
            retry_count += 1
            continue
    
    raise GitException(f'Maximum number of retry reached for the tag operation: {max_retries}')
