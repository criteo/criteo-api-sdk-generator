#!/usr/bin/env bash
# With -e, the shell will execute the ERR trap and then exit, whenever a simple command returns a non-zero exit
set -ex

LANGUAGE=$1

ORGANIZATION_NAME="criteo"
REPOSITORY_NAME="criteo-api-${LANGUAGE}-sdk"

GENERATOR_REPO_DIR=$GITHUB_WORKSPACE
SDK_REPO_DIR=$RUNNER_TEMP

TAG_VERSION="v$GITHUB_RUN_NUMBER"

if [ "$LANGUAGE" = "" ]; then
  echo "[ERROR] LANGUAGE not set"
  exit 1
fi

if [ "$GENERATOR_REPO_DIR" = "" ]; then
  echo "[ERROR] GENERATOR_REPO_DIR not set"
  exit 1
fi

if [ "$SDK_REPO_DIR" = "" ]; then
  echo "[ERROR] SDK_REPO_DIR not set"
  exit 1
fi

if [ "$GITHUB_ACTOR" = "" ]; then
  echo "[ERROR] GITHUB_ACTOR not set"
  exit 1
fi

if [ "$SDK_REPO_PRIVATE_KEY" = "" ]; then
  echo "[ERROR] SDK_REPO_PRIVATE_KEY not set"
  exit 1
fi

if [[ $TAG_VERSION == "" ]]; then
  echo "[ERROR] TAG_VERSION is not defined"
  exit 1
fi

setup_ssh() {
  eval "$(ssh-agent -s)"
  ssh-add - <<< "${SDK_REPO_PRIVATE_KEY}"
}

git_clone() {
  echo "[INFO] Cloning $ORGANIZATION_NAME/$REPOSITORY_NAME repository..."

  cd $SDK_REPO_DIR
  git clone --depth 1 git@github.com:$ORGANIZATION_NAME/$REPOSITORY_NAME.git
  SDK_REPO_DIR="$SDK_REPO_DIR/$REPOSITORY_NAME"

  echo "[INFO] Success. Repository cloned at $SDK_REPO_DIR"
}

remove_previous_sdks() {
  echo "[INFO] Removing previous SDKs..."

  sdks_directory="$SDK_REPO_DIR/sdks/$LANGUAGE"

  if [[ -d $sdks_directory ]]; then
    cd $sdks_directory
    rm -rf *
    echo "[INFO] Success."
  else
    echo "[WARN] Directory $REPO_NAME/sdks doesn't exists, skipping."
  fi
}

copy_new_sdks() {
  echo "[INFO] Copying new SDKs..."

  sdks_directory="$SDK_REPO_DIR/sdks"

  if [[ ! -d $sdks_directory ]]; then
    echo "[WARN] Directory $sdks_directory doesn't exists, creating it..."
    mkdir $sdks_directory
    echo "[INFO] Directory $sdks_directory created."
  fi

  cp -r "$GENERATOR_REPO_DIR/generated-sources/$LANGUAGE/." "$SDK_REPO_DIR/sdks" || echo "[ERROR]"

  echo "[INFO] Copy successful."
}

setup_git() {
  echo "[INFO] Setting up GH credentials..."

  git config user.email "$GITHUB_ACTOR@users.noreply.github.com"
  git config user.name "$GITHUB_ACTOR"

  echo "[INFO] Success. Email: $GITHUB_ACTOR@users.noreply.github.com, Name: $GITHUB_ACTOR"
}

git_add_files() {
  cd $SDK_REPO_DIR
  git add .
}

git_commit_and_tag() {
  git commit -m "Automatic update of SDK - $TAG_VERSION"
  git tag $TAG_VERSION
}

git_push() {
  git push origin --quiet
  # Push tag
  git push origin --tags --quiet
}

process() {
  setup_ssh

  git_clone

  remove_previous_sdks

  copy_new_sdks

  git_add_files

  # git diff, ignore version's modifications
  modification_count=$(git diff -U0 --staged \
                         | grep '^[+-][^+-]' \
                         | grep -Ev 'version|VERSION|Version' \
                         | grep -Ev 'user_agent|UserAgent' \
                         | wc -l | tr -d '[:space:]')

  if [[ ${modification_count} != 0 ]]; then
      setup_git
      git_commit_and_tag
      git_push
  else
      echo No push to Github. Modifications:
      git diff -U0
  fi
}

echo "Starting push for - ${LANGUAGE}"

process
