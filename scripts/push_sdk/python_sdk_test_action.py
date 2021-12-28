import os
from os import path

from push_sdk import utils
from push_sdk.clients.fs_client import IFsClient
from push_sdk.clients.os_client import IOsClient

class PythonSdkTestAction:
  def __init__(self, os_client: IOsClient, fs_client: IFsClient):
      self.logger = utils.get_logger()
      self.os_client = os_client
      self.fs_client = fs_client

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
      self.logger.error(f'Test Action failed for SDK {sdk_name}, removing it...')
      sdk_path = path.join(self.os_client.get_generated_sources_base_path('python'), sdk_name)
      self.fs_client.remove(sdk_path)
      self.logger.info('Removal successful')
      return

    self.logger.info('Test successful')

    self.logger.info('Cleaning package...')
    status_code = os.system('pip freeze | xargs pip uninstall -y')

    if status_code > 0:
      self.logger.warning('Clean operation failed, the uploaded artifact may contain some downloaded packages or generated files.')
      return

    self.logger.info('Clean successful')
