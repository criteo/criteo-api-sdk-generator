import subprocess
from subprocess import *
import os

class Git:

    def __init__(self, generator_repo_dir, github_actor, sdk_repo_private_key):
        print("Setting up push to PHP repositories")
        self.generator_repo_dir = generator_repo_dir
        self.github_actor = github_actor
        self.sdk_repo_private_key = sdk_repo_private_key

        print("generator_repo_dir : " + self.generator_repo_dir)
        pipe =  Popen(
            'eval $(ssh-agent -s)', shell=True, stdout=PIPE, stderr=STDOUT
        )
        output, errors = pipe.communicate(input=input)
        print(output)
        print ("Setting up ssh")
        subprocess.run(['ssh-agent', '-s'], shell=True)
        subprocess.run(['eval'], shell=True)
        # subprocess.run(['eval', '$(ssh-agent -s)'], shell=True)
        os.system(f'ssh-add - <<< "{self.sdk_repo_private_key}"')
    

    def clone(organization, repository):
        # subprocess.run(['cd', '/home/runner/work/_temp'])
        # subprocess.run(['ls', '-l'])
        # os.system(f'mkdir /home/runner/work/{repository}')

        print("Cloning repo")
        os.system(f'git clone --depth 1 git@github.com:${organization}/{repository}.git')
    
    def add(*args):
        files = '.' if (len(args) == 0) else ''

        for file in args:
            files += file + ' '
        
        os.system(f'git add {files}')
    
    def commit(message):
        os.system(f'git commit -m {message}')
    
    def tag(tag_name):
        os.system(f'git tag {tag_name}')
    
    def push(tag = True):
        options = '--quiet'

        if (tag):
            options += ' --tags'
        else:
            options += ' --all'

        os.system(f'git push origin {options}')


# print("Cloning git repositories")


# print("remove previous sdk")

# print("copy new sdks")

# print("git add files")

# print("check modifications and push")

# Push specifications:
# iterate over the generate sdks
# 1. Get Criteo Service
# 2. Get Version Name
# 3. Determine Branch Name:
#   -- For Preview Branch, branch name should be 0.generator.yyyyMMdd (ex. 0.0.211124)
#   -- For Stable Branch, branch name should be Api.version.generator.yyyyMMdd (ex. 2021.01.0.211124)
#   -- Create Tag for the branch (with the actual version ex. 20201.10.0.2)
# 4. Check for existence of Tag
# 5. If Tag exists, append -patchX to new branch. If X is 100, fail the script with an error.
# 6. Push branches and tags

