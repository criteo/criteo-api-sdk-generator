from ..result_or_exception import ResultOrException

from ..dummies.dummy_fs_client import DummyFsClient

class FsClientBuilder:
  
  def __init__(self):
    self.client = DummyFsClient()
  
  def that_responds_on_exists(self, file_path, response):
    self.client.responses_on_exists[file_path] = ResultOrException.from_response(response)
    return self
    
  def that_responds_on_list_dir(self, directory_path, response):
    self.client.responses_on_list_dir[directory_path] = ResultOrException.from_response(response)
    return self

  def that_fails_on_copy(self, exception):
    self.client.response_on_copy = ResultOrException.from_exception(exception)
    return self

  def that_fails_on_remove(self, exception):
    self.client.response_on_remove = ResultOrException.from_exception(exception)
    return self