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
        run_command('git config --global user.email "{actor}@users.noreply.github.com"')
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

    def diff_count(self):
        # Count staged changed lines that represent a *real* SDK change.
        #
        # A change is NOT counted (so publishing is skipped) when it is only an
        # SDK version-string bump located in:
        #   - README.md          (Package version / maven <version> lines)
        #   - build.gradle        (version = '...') / composer.json ("version")
        #   - the User-Agent literal (OpenAPI-Generator/<version>/...), e.g.
        #     ApiClient.java (Java) or Configuration.php (PHP)
        #
        # The SDK version is recognised by its trailing 6-digit datestamp
        # (e.g. 2026.01.0.260901, 0.0.260901). This is intentionally precise so
        # that unrelated changes -- including third-party dependency version
        # bumps or code that merely mentions "version" -- are still counted.
        awk_filter = (
            "awk '"
            r'/^diff / { next } '
            r'/^@@/ { next } '
            r'/^\+\+\+ / { f=$2; sub(/^b\//,"",f); next } '
            r'/^--- / { next } '
            r'/^[+-]/ {'
            r'  base=f; sub(/.*\//,"",base);'
            r'  ver = ($0 ~ /[0-9]+\.[0-9]+(\.[0-9]+)*\.[0-9][0-9][0-9][0-9][0-9][0-9]/);'
            r'  ua  = ($0 ~ /OpenAPI-Generator\//);'
            r'  ignorable = 0;'
            r'  if (ver && (base=="README.md" || base=="build.gradle" || base=="composer.json")) ignorable=1;'
            r'  else if (ver && ua) ignorable=1;'
            r'  if (!ignorable) count++;'
            r'} '
            r'END { print count+0 }'
            "'"
        )

        diff_count = run_command(
            f"git -c diff.renameLimit=0 diff -U0 --staged | {awk_filter} | tr -d '[:space:]'"
        )

        return int(diff_count)

    def add(self, *args):
        files = '.' if (len(args) == 0) else ''

        for file in args:
            files += file + ' '
        
        run_command(f'git add {files}')
    
    def commit(self, message):
        run_command(f'git commit -m "{message}"')
    
    def tag(self,tag_name):
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
