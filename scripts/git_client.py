import utils

class IGitClient:
    def setup(self, actor):
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

class GitClient(IGitClient):
    def setup(self, actor):
        utils.run_command('git config --global user.email "{actor}@users.noreply.github.com"')
        utils.run_command(f'git config --global user.name "{actor}"')

    def clone(self, organization, repository):
        utils.run_command(f'git clone git@github.com:{organization}/{repository}.git')
    
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
