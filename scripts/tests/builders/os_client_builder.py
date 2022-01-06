from tests.dummies.dummy_os_client import DummyOsClient

class OsClientBuilder:
  
  def __init__(self):
    self.client = DummyOsClient()
  
  def that_responds_on_get_generated_sources_base_path(self, response):
    self.client.response_on_get_generated_sources_base_path.result = response
    return self
  
  def that_responds_on_get_sdk_repo_base_path(self, response):
    self.client.response_on_get_sdk_repo_base_path.result = response
    return self
