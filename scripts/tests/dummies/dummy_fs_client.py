from ..result_or_exception import ResultOrException
from shared.clients.fs_client import IFsClient

class DummyFsClient(IFsClient):
  def __init__(self):
    self.responses_on_exists = dict()
    self.responses_on_list_dir = dict()
    self.response_on_copy = ResultOrException()
    self.response_on_remove = ResultOrException()

  def list_dir(self, dir_path):
    if dir_path in self.responses_on_list_dir:
      response_on_list_dir = self.responses_on_list_dir.get(dir_path)
    
      if response_on_list_dir.is_exception():
        raise response_on_list_dir.exception
  
      return response_on_list_dir.result

    raise FileNotFoundError(dir_path)

  def change_dir(self, path):
    self.current_dir = path
    pass

  def remove(self, path):
    if self.response_on_remove.is_exception():
      raise self.response_on_remove.exception
  
    return self.response_on_remove.result

  def copy(self, source, destination):
    if self.response_on_copy.is_exception():
      raise self.response_on_copy.exception
  
    return self.response_on_copy.result

  def exists(self, file_path):
    if file_path in self.responses_on_exists:
      response_on_exists = self.responses_on_exists.get(file_path)
      
      if response_on_exists.is_exception():
        raise response_on_exists.exception
  
      return response_on_exists.result

    raise FileNotFoundError(file_path)
