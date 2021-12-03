import os
import subprocess
import git

print("Setting up push to PHP repositories")

generator_repo_dir = os.environ["GITHUB_WORKSPACE"]
sdk_repo_dir = os.environ["RUNNER_TEMP"]
github_actor = os.environ["GITHUB_ACTOR"]
tag_version = os.environ["GITHUB_RUN_NUMBER"]
sdk_repo_private_key = os.environ["SDK_REPO_PRIVATE_KEY"]

print(sdk_repo_dir)


def setup_ssh():
    print ("Setting up ssh")
    subprocess.run(['eval', "$(ssh-agent -s)"], shell=True)
    subprocess.run(['ssh-add', '-', '<<<', '"${SDK_REPO_PRIVATE_KEY}"'], shell=True)

def clone_repo():
    print("Cloning repo")
    git.Repo.clone_from('git@github.com:criteo/criteo-api-marketingsolutions-php-sdk.git', sdk_repo_dir)

setup_ssh()
clone_repo()

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

