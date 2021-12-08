import sys, getopt

from push_sdk.clients.fs_client import FsClient
from push_sdk.clients.git_client import GitClient
from push_sdk.clients.os_client import OsClient
from push_sdk.php_sdk_push_action import PhpSdkPushAction
from push_sdk.default_push import DefaultPushSdkAction
from push_sdk.utils import get_logger

logger = get_logger()

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
  
  git_client = GitClient()
  fs_client = FsClient()
  os_client = OsClient()

  if language.lower() in ('python', 'java'):
    pipeline = DefaultPushSdkAction(git_client, fs_client, os_client, language)
  elif language.lower() == 'php':
    pipeline = PhpSdkPushAction(git_client, fs_client, os_client)
  else:
    raise Exception(f'Unsupported programming language ({language}).')
  
  pipeline.execute()

if __name__ == '__main__':
  main()
