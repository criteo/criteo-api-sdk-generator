import os

from push_sdk import utils

class PhpSdkTestAction:
  def __init__(self):
    self.logger = utils.get_logger()

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

    self.logger.info('Installing dependencies...')
    os.system('composer install')
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    os.system('composer test')
    self.logger.info('Test successful')
