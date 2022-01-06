import os

from shared.utils import get_logger

class PythonSdkTestAction:
  def __init__(self):
      self.logger = get_logger()

  def execute(self, sdk_name):
    self.logger.info(f'Starting testing SDK {sdk_name}...')

    self.logger.info('Installing dependencies...')
    status_code = os.system('pip install pytest')
    status_code += os.system('pip install -r test-requirements.txt')
    status_code += os.system('pip install -r requirements.txt')
    self.logger.info('Install successful')

    self.logger.info('Testing...')
    status_code += os.system('python -m pytest -s')

    if status_code > 0:
      raise Exception(f'Test Action failed for SDK {sdk_name}')

    self.logger.info('Test successful')

    self.logger.info('Cleaning package...')
    status_code = os.system('pip freeze | xargs pip uninstall -y')

    if status_code > 0:
      self.logger.warning('Clean operation failed, the uploaded artifact may contain some downloaded packages or generated files.')
      return

    self.logger.info('Clean successful')
