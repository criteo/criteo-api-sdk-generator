from ...git_client import IGitClient, GitException

class DummyGitClient(IGitClient):
    def __init__(self):
      self.nth_failures_before_success = 0
      self.retries_count = 0
      self.diff_count_response = 0
      self.is_pushed = False

    def clone(self, organization, repository):
      self.cloned_repository = f'{organization}/{repository}'
      pass
    
    def checkout(self, branch_name):
      self.current_branch = branch_name
      pass

    def branch(self, branch_name):
      pass

    def diff_count(self):
      return self.diff_count_response

    def add(self, *args):
      pass
    
    def commit(self, message):
      pass
    
    def tag(self,tag_name):
      while self.retries_count < self.nth_failures_before_success:
        self.retries_count += 1
        raise GitException()

      self.current_tag = tag_name
    
    def push(self, include_tags = True):
      self.is_pushed = True
