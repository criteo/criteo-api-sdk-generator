import sys, getopt
from os import path

from push_sdk.clients.fs_client import FsClient
from push_sdk.clients.os_client import OsClient
from push_sdk.utils import get_logger

from push_sdk.java_sdk_test_action import JavaSdkTestAction
from push_sdk.python_sdk_test_action import PythonSdkTestAction

logger = get_logger()

def run_tests(language):
  fs_client = FsClient()
  os_client = OsClient()

  if language == 'java':
    action = JavaSdkTestAction()
  elif language == 'python':
    action = PythonSdkTestAction(os_client, fs_client)
  else:
    raise Exception(f'Unsupported programming language ({language}).')

  generated_sdks_path = os_client.get_generated_sources_base_path(language)
  for sdk_name in fs_client.list_dir(generated_sdks_path):
    fs_client.change_dir(path.join(generated_sdks_path, sdk_name))

    action.execute(sdk_name)

def main():
  try:
    opts, _ = getopt.getopt(sys.argv[1:], "hl:", ["help","language="])
  except getopt.GetoptError:
    logger.error('Invalid call: [help] push_sdk.py -l <language>')
    sys.exit(2)

  for option, value in opts:
    if option in ('-h', '--help'):
      logger.info('push_sdk.py -l <language>')
      sys.exit()
    elif option in ('-l', '--language'):
      language = value
    else:
      raise Exception(f'Unsupported command line option ({option}={value}).')

  run_tests(language)

if __name__ == '__main__':
  main()
