from push_sdk import utils

class JavaSdkTestAction:
  def __init__(self):
      self.logger = utils.get_logger()
      self.java_error_template = r'\[ERROR\] ?.*'

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

    self.logger.info('Installing dependencies...')
    utils.run_command('mvn install', error_template=self.java_error_template)
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    utils.run_command('mvn test', error_template=self.java_error_template, env={
      'TEST_CLIENT_ID': utils.assert_environment_variable('TEST_CLIENT_ID'),
      'TEST_CLIENT_SECRET': utils.assert_environment_variable('TEST_CLIENT_SECRET'),
      'TEST_APPLICATION_ID': utils.assert_environment_variable('TEST_APPLICATION_ID'),
    })
    self.logger.info('Test successful')

    self.logger.info('Cleaning package...')
    utils.run_command('mvn clean')
    self.logger.info('Clean successful')
