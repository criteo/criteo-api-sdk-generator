from ..dummies.dummy_fs_client import DummyFsClient

class FsClientBuilder:
  def __init__(self):
    self.client = DummyFsClient()
  
  def that_responds_list_dir(self, diff_count):
    self.client.diff_count_response = diff_count
    return self