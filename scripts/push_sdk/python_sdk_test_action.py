from push_sdk import utils
import os 
class PythonSdkTestAction:
  def __init__(self):
      self.logger = utils.get_logger()

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

    self.logger.info('Installing dependencies...')
    os.system('pip install pytest')
    os.system('pip install -r test-requirements.txt')
    os.system('pip install -r requirements.txt')
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    os.system('python -m pytest -s')
    self.logger.info('Test successful')

    self.logger.info('Cleaning package...')
    os.system('pip freeze | xargs pip uninstall -y')
    self.logger.info('Clean successful')
