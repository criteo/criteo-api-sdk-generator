#!/usr/bin/env bash
set -ex

LANGUAGE=$1

ORGANIZATION="criteo"
REPO_NAME="criteo-api-${LANGUAGE}-sdk"

GENERATOR_REPO_DIR=$GITHUB_WORKSPACE
SDK_REPO_DIR=$RUNNER_TEMP

VERSION="v$GITHUB_RUN_NUMBER"

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

if [ "$GH_ACCESS_TOKEN" = "" ]; then
  echo "[ERROR] GH_ACCESS_TOKEN not set"
  exit 1
fi

if [[ $VERSION == "" ]]; then
  echo "[ERROR] VERSION is not defined"
  exit 1
fi

git_clone() {
  echo "[INFO] Cloning $ORGANIZATION/$REPO_NAME repository..."

  cd $SDK_REPO_DIR
  git clone --depth 1 https://x-access-token:$GH_ACCESS_TOKEN@github.com/$ORGANIZATION/$REPO_NAME.git
  SDK_REPO_DIR="$SDK_REPO_DIR/$REPO_NAME"

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

  cp -r "$GENERATOR_REPO_DIR/generated-sources/$LANGUAGE/" "$SDK_REPO_DIR/sdks"

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
  ls
  git add .
}

git_commit_and_tag() {
  git commit -m "Automatic update of SDK - $VERSION"
  git tag $VERSION
}

git_push() {
  git push origin --quiet
  # Push tag
  git push origin --tags --quiet
}

process() {
  git_clone

  remove_previous_sdks

  copy_new_sdks

  git_add_files

  # For test To be removed
  git status
  git config --global core.pager cat
  git diff

  # git diff, ignore version's modifications
  modification_count=$(git diff -U0 --staged \
                         | grep '^[+-]' \
                         | grep -Ev '^(--- a/|\+\+\+ b/)' \
                         | grep -Ev 'version|VERSION|Version' \
                         | grep -Ev 'user_agent|UserAgent' \
                         | grep -Ev 'marketing\.java-client.+[0-9]\.[0-9]\.[0-9]' \
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
