import os
from os import path

from push_sdk.fs_client import FsClient
from push_sdk.git_client import GitClient
from push_sdk.php_pipeline import PushPhpSdkPipeline
from push_sdk.utils import assert_environment_variable, assert_criteo_service, assert_api_version, get_logger

logger = get_logger()

def main():
  fs_client = FsClient()

  generator_repo_dir = assert_environment_variable('GITHUB_WORKSPACE')
  generator_repo_dir += '/generated-sources/php'

  if not fs_client.exists(generator_repo_dir):
    raise Exception(f'[ERROR] Path {generator_repo_dir} does not exist')
  
  for directory in os.listdir(generator_repo_dir):
    logger.info(f'Handling generated sources for {directory}')

    if path.isfile(path.join(generator_repo_dir, directory)):
      continue

    criteo_service = assert_criteo_service(directory)
    api_version = assert_api_version(directory)

    logger.info(f'Found Criteo Service "{criteo_service}" and API version "{api_version}"')

    git_client = GitClient()
    pipeline = PushPhpSdkPipeline(git_client, fs_client, criteo_service, api_version)

    pipeline.clone_repo()

    pipeline.checkout()

    pipeline.update_sources()

    pipeline.upload()

    pipeline.clean()
    

if __name__ == '__main__':
    main()
