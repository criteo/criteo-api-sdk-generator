import os
import re
from os import path

# $Env:GITHUB_WORKSPACE = "/Users/p.mathon/criteo-api-sdk-generator"
# $Env:RUNNER_TEMP = "/Users/p.mathon/"
# $Env:GITHUB_ACTOR = "paul.mathon"
# $Env:GITHUB_RUN_NUMBER = "8"
# $Env:SDK_REPO_PRIVATE_KEY = "fve"

# export GITHUB_WORKSPACE="/Users/p.mathon/criteo-api-sdk-generator"
# export RUNNER_TEMP="/Users/p.mathon/"
# export GITHUB_ACTOR="paul.mathon"
# export GITHUB_RUN_NUMBER="8"
# export SDK_REPO_PRIVATE_KEY="fve"

from git_client import Git

class PushPhpSdkPipeline:

  def __init__(self, criteo_service, api_version) -> None:
    self.criteo_service = criteo_service
    self.api_version = api_version
    self.__init_environment_variables()
    self.git = Git(self.generator_repo_dir, self.github_actor, self.sdk_repo_private_key)

  def __init_environment_variables(self):
    self.generator_repo_dir = assert_environment_variable('GITHUB_WORKSPACE')
    self.sdk_repo_dir = assert_environment_variable('RUNNER_TEMP')
    self.github_actor = assert_environment_variable('GITHUB_ACTOR')
    self.tag_version = assert_environment_variable('GITHUB_RUN_NUMBER')
    self.sdk_repo_private_key = assert_environment_variable('SDK_REPO_PRIVATE_KEY')


def assert_environment_variable(variable_name):
  try:
    return os.environ[variable_name]
  except:
    raise Exception(f'[ERROR] Environment variable {variable_name} not set.')

def assert_criteo_service(directory_name):
  splitted_directory_name = directory_name.split('_')

  if len(splitted_directory_name) != 2:
    raise Exception(f'Directory name for generated source don\'t have a valid format ({directory_name})')
  
  criteo_service = splitted_directory_name[0].lower()

  if criteo_service != 'marketingsolutions' and criteo_service != 'retailmedia':
    raise Exception(f'Criteo Service found in directory name of generated source is invalid ({criteo_service})')

  return criteo_service

def assert_api_version(directory_name):
  splitted_directory_name = directory_name.split('_')

  if len(splitted_directory_name) != 2:
    raise Exception(f'Directory name for generated source don\'t have a valid format ({directory_name})')
  
  api_version = splitted_directory_name[1]

  if api_version != 'preview' and not re.match(r'[0-9]{2,}(-[0-9]{2})', api_version):
    raise Exception(f'API Version found in directory name of generated source is invalid ({api_version})')
  
  return api_version


def main():
  generator_repo_dir = assert_environment_variable('GITHUB_WORKSPACE')
  print(generator_repo_dir)
  generator_repo_dir += '/generated-sources/php'
  sdk_repo_dir = assert_environment_variable('RUNNER_TEMP')
  print(generator_repo_dir)
  if not path.exists(generator_repo_dir):
    raise Exception(f'[ERROR] Path {generator_repo_dir} does not exist')
  
  for directory in os.listdir(generator_repo_dir):
    print(generator_repo_dir, directory)
    if path.isfile(path.join(generator_repo_dir, directory)):
      continue

    criteo_service = assert_criteo_service(directory)
    api_version = assert_api_version(directory)

    pipeline = PushPhpSdkPipeline(criteo_service, api_version)



    


main()

  

  







# Check environment variables
 
# Loop over ./generated-sources/php/ folder

# Read folder name -> Get criteo-service / API version -> check validity

# Clone "criteo-api-{criteo_service}-php-sdk" repository

# From api_version -> check if branch exists -> yes: checkout, no: checkout -b

# Copy/paste sources

# Add -> Commit

# Tag (if api_version == 'preview' -> tag version = 0.x.yyyyMMdd)

# If tag fail (because it already exists) retry until retry_count == 100 with tag name = 0.0.yyyyMMdd-patch{retry_count}

# push --all and push --tags

