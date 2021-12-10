import os
from os import path
from datetime import datetime

from git_client import GitClient, GitException
from fs_client import FsClient
import utils

logger = utils.get_logger()

class PushPhpSdkPipeline:
  def __init__(self, git_client, fs_client, criteo_service, api_version):
    self.criteo_service = criteo_service
    self.api_version = api_version
    self.generator_version = 0
    self.__init_environment_variables()

    self.fs = fs_client
    self.fs.change_dir(self.generator_repo_dir)

    self.git = git_client

    logger.info(f'Setup Git with user {self.github_actor}.')
    self.git.setup(self.github_actor)
  
  def clone_repo(self):
    self.fs.change_dir(self.sdk_repo_dir)

    organization_name = 'criteo'
    repository_name = f'criteo-api-{self.criteo_service}-php-sdk'
  
    logger.info(f'Cloning repository {organization_name}/{repository_name}...')

    self.git.clone(organization_name, repository_name)

    self.sdk_repo_dir = path.join(self.sdk_repo_dir, repository_name)

  def checkout(self):
    self.fs.change_dir(self.sdk_repo_dir)
  
    branch_name = self.api_version
    if self.criteo_service != 'preview':
      branch_name = branch_name.replace('-', '.')

    logger.info(f'Checkout branch {branch_name}.')

    self.git.checkout(branch_name)

  def update_sources(self):
    logger.info('Copying new sources to repository...')

    el_to_update = ['docs', 'examples', 'lib', 'test', '.gitignore', '.php_cs', 'README.md', 'composer.json', 'composer.lock', 'phpunit.xml.dist']

    for element_name in el_to_update:
      source = path.join(self.generator_repo_dir, f'generated-sources/php/{self.criteo_service}_{self.api_version}', element_name)
      destination = path.join(self.sdk_repo_dir, element_name)

      if path.exists(destination):
        self.fs.remove(destination)

      if path.exists(source):
        self.fs.copy(source, destination)

  def upload(self):
    self.fs.change_dir(self.sdk_repo_dir)

    self.git.add()

    diff_count = self.git.diff_count()

    logger.info(f'{diff_count} new lines modified.')

    if diff_count > 0:
      now_date = datetime.today().strftime('%Y-%m-%d')
      tag_name = self.__get_tag_name()

      logger.info(f'Committing and tagging with tag name "{tag_name}".')

      self.git.commit(f'[{now_date}] Automatic update of SDK - {tag_name}')

      tag_name = self.__tag_with_retry()

      logger.info(f'Pushing commit and tag "{tag_name}"...')

      self.git.push(include_tags=True)      

  def clean(self):
    logger.info(f'Removing directory {self.sdk_repo_dir}')

    self.fs.remove(self.sdk_repo_dir)
  
  def __init_environment_variables(self):
    self.generator_repo_dir = utils.assert_environment_variable('GITHUB_WORKSPACE')
    self.sdk_repo_dir = utils.assert_environment_variable('RUNNER_TEMP')
    self.github_actor = utils.assert_environment_variable('GITHUB_ACTOR')
    self.tag_version = utils.assert_environment_variable('GITHUB_RUN_NUMBER')

  def __get_tag_name(self, patch=0):
      now_date = datetime.today().strftime('%Y%m%d')[2:]

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

def main():
  generator_repo_dir = utils.assert_environment_variable('GITHUB_WORKSPACE')
  generator_repo_dir += '/generated-sources/php'

  if not path.exists(generator_repo_dir):
    raise Exception(f'[ERROR] Path {generator_repo_dir} does not exist')
  
  for directory in os.listdir(generator_repo_dir):
    logger.info(f'Handling generated sources for {directory}')

    if path.isfile(path.join(generator_repo_dir, directory)):
      continue

    criteo_service = utils.assert_criteo_service(directory)
    api_version = utils.assert_api_version(directory)

    logger.info(f'Found Criteo Service "{criteo_service}" and API version "{api_version}"')

    fs_client = FsClient()
    git_client = GitClient()
    pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

    pipeline.clone_repo()

    pipeline.checkout()

    pipeline.update_sources()

    pipeline.upload()

    pipeline.clean()

main()
