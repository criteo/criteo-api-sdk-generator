from git_client import IGitClient

class DummyGitClient(IGitClient):
    def clone(self, organization, repository):
      self.cloned_repository = f'{organization}/{repository}'
      pass
    
    def checkout(self, branch_name):
      pass

    def branch(self, branch_name):
      pass

    def diff_count(self):
      pass

    def add(self, *args):
      pass
    
    def commit(self, message):
      pass
    
    def tag(self,tag_name):
      pass
    
    def push(self, include_tags = True):
      pass
