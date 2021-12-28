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
    os.system('composer test', env={
        'TEST_CLIENT_ID': utils.assert_environment_variable('TEST_CLIENT_ID'),
        'TEST_CLIENT_SECRET': utils.assert_environment_variable('TEST_CLIENT_SECRET'),
        'TEST_APPLICATION_ID': utils.assert_environment_variable('TEST_APPLICATION_ID'),
    })
    self.logger.info('Test successful')
