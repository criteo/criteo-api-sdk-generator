from github import Github
import os

print("Setting up push to PHP repositories")

generator_repo_dir = os.environ["GITHUB_WORKSPACE"]
sdk_repo_dir = os.environ["RUNNER_TEMP"]
github_actor = os.environ["GITHUB_ACTOR"]
tag_version = os.environ["GITHUB_RUN_NUMBER"]
sdk_repo_private_key = os.environ["SDK_REPO_PRIVATE_KEY"]


print("Initializing github")
g = Github("access_token")
g = Github(base_url="https://github.com/criteo/criteo-api-marketingsolutions-php-sdk", login_or_token=sdk_repo_private_key)

for repo in g.get_user().get_repos():
    print(repo.name)


# print ("Setting up ssh")


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

