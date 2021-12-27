from ...shared.clients.git_client import GitException
from ..dummies.dummy_git_client import DummyGitClient

class GitClientBuilder:
  def __init__(self):
    self.client = DummyGitClient()

  def that_responds_on_diff_count(self, diff_count):
    self.client.diff_count_response = diff_count
    return self

  def with_nth_failures_before_success(self, nth_failures):
    self.client.nth_failures_before_success = nth_failures
    return self
  
  def that_fails_on_push(self):
    self.client.response_on_push.exception = GitException()
    return self
