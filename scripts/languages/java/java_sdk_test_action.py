from shared.utils import run_command, assert_environment_variable, get_logger

class JavaSdkTestAction:
  def __init__(self):
      self.logger = get_logger()
      self.java_error_template = r'\[ERROR\] ?.*'

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')
    run_command('chmod u+x ./gradlew')
    run_command('./gradlew check', error_template=self.java_error_template, env={
      'TEST_CLIENT_ID': assert_environment_variable('TEST_CLIENT_ID'),
      'TEST_CLIENT_SECRET': assert_environment_variable('TEST_CLIENT_SECRET'),
      'TEST_APPLICATION_ID': assert_environment_variable('TEST_APPLICATION_ID'),
    })
    self.logger.info('Gradle Check successful')

    self.logger.info('Cleaning package...')
    run_command('./gradlew clean')
    self.logger.info('Clean successful')
