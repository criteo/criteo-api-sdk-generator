import os

from push_sdk import utils

class PhpSdkTestAction:
  def __init__(self):
    self.logger = utils.get_logger()

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

    self.logger.info('Installing dependencies...')
    exit_code = os.system('composer install')
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    exit_code += os.system('composer test')

    if exit_code != 0:
      raise Exception(f'Test Action failed to SDK {sdk_name}')

    self.logger.info('Test successful')
