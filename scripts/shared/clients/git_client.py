from shared.utils import run_command, CommandException

class IGitClient:
    def setup(self, actor):
        pass

    def setup_ssh(self, private_key):
        pass

    def clone(self, organization, repository):
        pass
    
    def checkout(self, branch_name):
        pass

    def branch(self, branch_name):
        pass

    def diff_count(self, pathspec=None):
        pass

    def restore(self, pathspec):
        pass

    def add(self, *args):
        pass
    
    def commit(self, message):
        pass
    
    def tag(self, tag_name):
        pass
    
    def push(self, include_tags = True):
        pass

class GitClient(IGitClient):
    def setup(self, actor):
        run_command(f'git config --global user.email "{actor}@users.noreply.github.com"')
        run_command(f'git config --global user.name "{actor}"')
    
    def setup_ssh(self, private_key):
        run_command('eval $(ssh-agent)')
        run_command('ssh-add -D')
        run_command(f'ssh-add - <<< "{private_key}"')

    def clone(self, organization, repository):
        run_command(f'git clone git@github.com:{organization}/{repository}.git')
    
    def checkout(self, branch_name):
        is_branch_exist = int(run_command(f'git branch --all | grep -l {branch_name} | wc -l | tr -d \'[:space:]\'')[0]) > 0

        if not is_branch_exist:
            self.branch(branch_name)
        
        run_command(f'git checkout {branch_name}')

    def branch(self, branch_name):
        run_command(f'git branch {branch_name}')

    def diff_count(self, pathspec=None):
        path_arg = f' -- {pathspec}' if pathspec else ''
        diff_count = run_command(
            f"git -c diff.renameLimit=0 diff -U0 --staged{path_arg}"
            " | grep '^[+-][^+-]'"
            r" | grep -Ev '[0-9]+\.[0-9]+(\.[0-9]+)*\.[0-9]{6}'"
            " | wc -l | tr -d '[:space:]'"
        )
        return int(diff_count)

    def restore(self, pathspec):
        run_command(f'git restore --staged --worktree -- {pathspec}')

    def add(self, *args):
        files = '.' if (len(args) == 0) else ''

        for file in args:
            files += file + ' '
        
        run_command(f'git add {files}')
    
    def commit(self, message):
        run_command(f'git commit -m "{message}"')
    
    def tag(self, tag_name):
        try:
            run_command(f'git tag {tag_name}')
        except CommandException as e:

            raise GitException(f'Git tag operation failed: {str(e)}')
    
    def push(self, include_tags = True):
        # In case of issue, be sure to check the known remotes.
        run_command(f'git ls-remote')
        
        run_command(f'git push origin --all')

        if include_tags:
            run_command(f'git push origin --tags')

class GitException(Exception):
    pass
