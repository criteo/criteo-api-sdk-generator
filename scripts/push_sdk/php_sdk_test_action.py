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
    exit_code += os.system('SYMFONY_DEPRECATIONS_HELPER=disabled composer test')

    if exit_code != 0:
      raise Exception(f'Test Action failed to SDK {sdk_name}')

    self.logger.info('Test successful')

    self.logger.info('Cleaning...')
    self.fs_client.remove('vendor')
    self.fs_client.remove('.php_cs.cache')
    self.fs_client.remove('.phpunit.result.cache')
    self.logger.info('Clean successful')