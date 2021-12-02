# from github import Github
import os

print("Setting up push to PHP repositories")

generator_directory = os.environ["GITHUB_WORKSPACE"]
tag_version = os.environ["GITHUB_RUN_NUMBER"]
sdk_directory = os.environ["RUNNER_TEMP"]
github_actor = os.environ["GITHUB_ACTOR"]
sdk_repo_private_key = os.environ["SDK_REPO_PRIVATE_KEY"]

print("Github workspace is: ", generator_directory)
print("Github tag is: ", tag_version)
print("Github sdk workspace is: ", sdk_directory)
print("Github actor is: ", github_actor)
print("Sdk repo private key is: ", sdk_repo_private_key)


print ("Setting up ssh")

print("remove previous sdk")

print("copy new sdks")

print("git add files")

print("check modifications and push")

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

