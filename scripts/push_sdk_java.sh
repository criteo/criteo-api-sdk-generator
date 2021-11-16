#!/usr/bin/env bash
set -ex

BUILD_DIR=$GITHUB_REPOSITORY
TEMP_DIR=$RUNNER_TEMP

LANGUAGE="java"

GITHUB_USER_NAME="Criteo GITHUB CI"

ORGANIZATION="criteo"
REPO="criteo-api-${LANGUAGE}-sdk"

VERSION="1.0"

if [ "$BUILD_DIR" = "" ]; then
    echo "[ERROR] BUILD_DIR not set"
    exit 1
fi

if [ "$TEMP_DIR" = "" ]; then
    echo "[ERROR] TEMP_DIR not set"
    exit 1
fi

if [ "$GITHUB_ACTOR" = "" ]; then
    echo "[ERROR] GITHUB_ACTOR not set"
    exit 1
fi

if [ "$GITHUB_TOKEN" = "" ]; then
    echo "[ERROR] GITHUB_TOKEN not set"
    exit 1
fi

git_clone() {
  echo "[INFO] Cloning $ORGANIZATION/$REPO repository..."

  cd $RUNNER_TEMP
  git clone --depth 1 https://$GITHUB_ACTOR:$GITHUB_TOKEN@github.com/$ORGANIZATION/$REPO.git

  echo "[INFO] Success. Repository cloned at $RUNNER_TEMP/$REPO"
  echo ""
}

remove_previous_sdks() {
  echo "[INFO] Removing previous SDKs..."
  sdks_directory="$TEMP_DIR/$REPO/sdks"
  if [ -d sdks_directory ]; then
      cd $TEMP_DIR/$REPO
      rm -rf *
      echo "[INFO] Success."
  else
    echo "[WARN] Directory $REPO/sdks doesn't exists, skipping."
  fi
  echo ""
}

copy_new_sdks() {
  echo "[INFO] Copying new SDKs..."

  sdks_directory="$TEMP_DIR/$REPO/sdks"

  if [ ! -d sdks_directory ]; then
    echo "[WARN] Directory $sdks_directory doesn't exists, creating it..."
    mkdir $sdks_directory
    echo "[INFO] Directory $sdks_directory created."
  fi

  cp -r "$BUILD_DIR/generated-sources/$LANGUAGE" "$TEMP_DIR/$REPO/sdks"

  echo "[INFO] Copy successful."
  echo ""
}

setup_git() {
  echo "[INFO] Setting up GH credentials..."

  git config user.email $GITHUB_ACTOR
  git config user.name $GITHUB_USER_NAME

  echo "[INFO] Success. Email: $GITHUB_ACTOR, Name: $GITHUB_USER_NAME"
  echo ""
}

git_add_files() {
  cd $TEMP_DIR/$REPO
  git add .
}

git_commit_and_tag() {
  if [[ ${VERSION} == "" ]]; then
    echo "[ERROR] Version is not defined"
    exit 1
  fi
  git commit -m "Automatic update of SDK - ${VERSION}" && git tag ${VERSION}
}

git_push() {
  git push origin --tags --quiet && git push origin --quiet
}

process() {
  git_clone

  remove_previous_sdks

  copy_new_sdks

  git_add_files

  # git diff, ignore version's modifications
  modification_count=$(git diff -U0 --staged \
                         | grep '^[+-]' \
                         | grep -Ev '^(--- a/|\+\+\+ b/)' \
                         | grep -Ev 'version|VERSION|Version' \
                         | grep -Ev 'user_agent|UserAgent' \
                         | grep -Ev 'marketing\.java-client.+[0-9]\.[0-9]\.[0-9]' \
                         | wc -l | tr -d '[:space:]')

  if [[ ${modification_count} != 0 ]]; then
      git_commit_and_tag
      git_push
  else
      echo No push to Github. Modifications:
      git diff -U0
  fi
}

echo "Starting push for - ${LANGUAGE}"

process
