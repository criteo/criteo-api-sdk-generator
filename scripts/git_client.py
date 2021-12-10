import utils
import os
from os import path
from git import Repo

os.environ['GIT-PYTHON-TRACE'] = '1'
class IGitClient:
    def setup_ssh(self, private_key):
        pass

    def clone(self, organization, repository):
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

class GitClient2:
    def setup_ssh(self, private_key):
        self.private_key = private_key


    def clone(self, organization, repository):
        path2 = utils.assert_environment_variable('RUNNER_TEMP')

        pk_path = path.join(path2, 'pk')
        
        with open(pk_path, 'w') as f:
            f.write(self.private_key)
        
        utils.run_command(f'cat {pk_path}')
        utils.run_command(f'chmod 600 {pk_path}')
        utils.run_command(f'cat {pk_path}')
        
        Repo.clone_from(f'git@github.com:{organization}/{repository}.git', repository, env= { 'GIT_SSH_COMMAND': f'ssh -i {pk_path}'})
    
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

class GitClient(IGitClient):

    def setup_ssh(self, sdk_repo_private_key):
        utils.run_command('eval `ssh-agent -s`')
        utils.run_command('ssh-add -D')
        utils.run_command(f'ssh-add - <<< "{sdk_repo_private_key}"')

    def clone(self, organization, repository):
        output = utils.run_command(f'git clone git@github.com:{organization}/{repository}.git')
        print("output", output)
    
    def checkout(self, branch_name):
        is_branch_exist = int(utils.run_command(f'git branch --all | grep -l {branch_name} | wc -l | tr -d \'[:space:]\'')[0]) > 0

        if not is_branch_exist:
            self.branch(branch_name)
        
        utils.run_command(f'git checkout {branch_name}')

    def branch(self, branch_name):
        utils.run_command(f'git branch {branch_name}')

    def diff_count(self):
        diff_count = utils.run_command('git diff -U0 --staged | grep \'^[+-][^+-]\' | grep -Ev \'version|VERSION|Version\' | grep -Ev \'user_agent|UserAgent\' | wc -l | tr -d \'[:space:]\'')

        return int(diff_count[0])

    def add(self, *args):
        files = '.' if (len(args) == 0) else ''

        for file in args:
            files += file + ' '
        
        utils.run_command(f'git add {files}')
    
    def commit(self, message):
        utils.run_command(f'git commit -m "{message}"')
    
    def tag(self,tag_name):
        try:
            utils.run_command(f'git tag {tag_name}')
        except utils.CommandException as e:

            raise GitException(f'Git tag operation failed: {str(e)}')
    
    def push(self, include_tags = True):
        utils.run_command(f'git push origin --quiet --all')

        if include_tags:
            utils.run_command(f'git push origin --tags')

class GitException(Exception):
    pass
