import os
import re
import subprocess
import logging
from datetime import datetime

logger = None
formatted_date = None

def assert_environment_variable(variable_name):
  try:
    return os.environ[variable_name]
  except:
    raise Exception(f'[ERROR] Environment variable {variable_name} not set.')

def assert_criteo_service(directory_name):
  splitted_directory_name = directory_name.split('_')

  if len(splitted_directory_name) != 2:
    raise InvalidCriteoServiceException(f'Directory name for generated source don\'t have a valid format ({directory_name})')
  
  criteo_service = splitted_directory_name[0].lower()

  if criteo_service != 'marketingsolutions' and criteo_service != 'retailmedia':
    raise InvalidCriteoServiceException(f'Criteo Service found in directory name of generated source is invalid ({criteo_service})')

  return criteo_service

def assert_api_version(directory_name):
  splitted_directory_name = directory_name.split('_')

  if len(splitted_directory_name) != 2:
    raise InvalidApiVersionException(f'Directory name for generated source doesn\'t have a valid format ({directory_name})')

  api_version = splitted_directory_name[1]

  if api_version != 'preview' and not re.match(r'[0-9]{2,}(-[0-9]{2})', api_version):
    raise InvalidApiVersionException(f'API Version found in directory name of generated source is invalid ({api_version})')
  
  return api_version

def get_logger():
  global logger
  if logger is None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger('')

  return logger

def get_formatted_date():
  global formatted_date
  if formatted_date is None:
    formatted_date = datetime.today().strftime('%Y%m%d')[2:]

  return formatted_date

def run_command(command, env=None):
  try:
    output = subprocess.Popen(command,
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       env=env)

    lines = ''
    for line in iter(output.stdout.readline, b''):
      line = line.decode("utf-8").strip().rstrip("\r\n")
      get_logger().info(line)
      lines += line

    output.stdout.close()
    output.wait()

    return lines
  except subprocess.CalledProcessError as e:
    raise CommandException(e.output)

class CommandException(Exception):
  pass

class InvalidCriteoServiceException(Exception):
  pass

class InvalidApiVersionException(Exception):
  pass
