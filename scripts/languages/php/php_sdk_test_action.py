import os

from shared.clients.fs_client import IFsClient
from shared.utils import run_command, assert_environment_variable, get_logger

class PhpSdkTestAction:
  def __init__(self, fs_client: IFsClient):
    self.logger = get_logger()
    self.fs_client = fs_client

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')
    self.logger.info("tempGT: varenv: " + str(len(os.environ.get("TEST_CLIENT_ID"))))
    self.logger.info("tempGT: varenv: " + str(len(os.environ.get("TEST_CLIENT_SECRET"))))
    self.logger.info("tempGT: varenv from util method: " + str(len(assert_environment_variable("TEST_CLIENT_ID"))))
    self.logger.info("tempGT: varenv from util method: " + str(len(assert_environment_variable("TEST_CLIENT_SECRET"))))

    self.logger.info('Installing dependencies...')
    exit_code = os.system('composer install')
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    exit_code += os.system('composer test')

    if exit_code > 0:
      raise Exception(f'Test Action failed for SDK {sdk_name}')

    self.logger.info('Test successful')

    self.logger.info('Cleaning...')
    elements_to_remove = ['vendor', '.php_cs', '.php_cs.cache', '.phpunit.result', '.phpunit.result.cache']
    for element_to_remove in elements_to_remove:
      if self.fs_client.exists(element_to_remove):
        self.fs_client.remove(element_to_remove)
    self.logger.info('Clean successful')
