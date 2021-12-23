from push_sdk import utils

class JavaSdkTestAction:
  def __init__(self):
      self.logger = utils.get_logger()

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

    self.logger.info('Installing dependencies...')
    utils.run_command('mvn install')
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    utils.run_command('mvn test', env={
      'TEST_CLIENT_ID': utils.assert_environment_variable('TEST_CLIENT_ID'),
      'TEST_CLIENT_SECRET': utils.assert_environment_variable('TEST_CLIENT_SECRET')
    })
    self.logger.info('Test successful')

    self.logger.info('Cleaning package...')
    utils.run_command('mvn clean')
    self.logger.info('Clean successful')
