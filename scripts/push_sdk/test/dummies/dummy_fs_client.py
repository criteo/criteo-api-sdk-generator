from ...fs_client import IFsClient

class DummyFsClient(IFsClient):
  def change_dir(self, path):
      self.current_dir = path
      pass

  def remove(self, path):
      """Remove directory (recursively) or file"""
      pass

  def copy(self, source, destination):
      """Copy directory (recursively) or folder"""
      pass