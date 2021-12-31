from shared.clients.os_client import IOsClient
from ..result_or_exception import ResultOrException

class DummyOsClient(IOsClient):
  
  def __init__(self):
    self.response_on_get_private_key = ResultOrException()
    self.response_on_get_generated_sources_base_path = ResultOrException()
    self.response_on_get_sdk_repo_base_path = ResultOrException()
    self.response_on_get_git_user = ResultOrException()

  def get_private_key(self, programming_language, criteo_service = None):
    if self.response_on_get_private_key.is_exception():
      raise self.response_on_get_private_key.exception

    return self.response_on_get_private_key.result
  
  def get_generated_sources_base_path(self, programming_language):
    if self.response_on_get_generated_sources_base_path.is_exception():
      raise self.response_on_get_generated_sources_base_path.exception

    return self.response_on_get_generated_sources_base_path.result

  def get_sdk_repo_base_path(self):
    if self.response_on_get_sdk_repo_base_path.is_exception():
      raise self.response_on_get_sdk_repo_base_path.exception

    return self.response_on_get_sdk_repo_base_path.result
  
  def get_git_user(self):
    if self.response_on_get_git_user.is_exception():
      raise self.response_on_get_git_user.exception

    return self.response_on_get_git_user.result