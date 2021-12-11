from ..dummies.dummy_git_client import DummyGitClient

class GitClientBuilder:
  def __init__(self):
    self.client = DummyGitClient()
  
  def with_diff_count(self, diff_count):
    self.client.diff_count_response = diff_count
    return self

  def with_failures_before_success(self, nth_failures):
    self.client.nth_failures_before_success = nth_failures
    return self