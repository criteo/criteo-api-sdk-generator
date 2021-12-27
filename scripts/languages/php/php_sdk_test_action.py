import os

from push_sdk.clients.fs_client import IFsClient
from push_sdk import utils

class PhpSdkTestAction:
  def __init__(self, fs_client: IFsClient):
    self.logger = utils.get_logger()
    self.fs_client = fs_client

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

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
