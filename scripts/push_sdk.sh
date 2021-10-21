#!/usr/bin/env bash
set -ex

SCRIPT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [[ $GITHUB_RUN_NUMBER != "" ]]; then
    BUILD_NUMBER=$GITHUB_RUN_NUMBER
else
    echo "Usage: $0 BUILD_NUMBER"
    exit 1
fi

git_clone() {
  git clone --depth 1 https://${GH_TOKEN}@github.com/$1.git
}

setup_git() {
  git config user.email $github.actor
  git config user.name "GITHUB CI"
}

git_add_files() {
  GIT_TRACK_FILE="${SCRIPT_ROOT}/git-track/${1}.txt"
  if [[ -f ${GIT_TRACK_FILE} ]]; then
      files_to_add=$(cat ${GIT_TRACK_FILE} | grep -Ev "^\s*#|^\s*$" | tr '\n' ' ')
      git add ${files_to_add}
  else
    echo "'${GIT_TRACK_FILE}' does not exists, no files to add."
    exit 1
  fi
}

git_commit_and_tag() {
  version=$1
  if [[ ${version} == "" ]]; then
    echo "version is not defined"
    exit 1
  fi
  git commit -m "Automatic update of SDK - ${version}" && git tag ${version}
}

git_push() {
  if [[ ${github.actor} == "github" ]]; then
    git push origin --tags --quiet && git push origin --quiet
  else
    echo "Only user travis should be able to push."
  fi
}

process() {
  language=$1
  mkdir ${BUILD_DIR}/criteo
  cd ${BUILD_DIR}/criteo
  REPO="criteo/criteo-api-${language}-sdk"
  git_clone ${REPO}

  NEXT_CLIENT="NEXT_criteo-api-${language}-sdk"
  cp -r "${SCRIPT_ROOT}/../generated-sources/${language}" ${NEXT_CLIENT}
  cp -r "${BUILD_DIR}/${REPO}/.git" ${NEXT_CLIENT}

  cd ${NEXT_CLIENT}

  # add files before doing the diff
  git_add_files ${language}

  # git diff, ignore version's modifications
  modification_count=$(git diff -U0 --staged \
                         | grep '^[+-]' \
                         | grep -Ev '^(--- a/|\+\+\+ b/)' \
                         | grep -Ev 'version|VERSION|Version' \
                         | grep -Ev 'user_agent|UserAgent' \
                         | grep -Ev 'marketing\.java-client.+[0-9]\.[0-9]\.[0-9]' \
                         | wc -l | tr -d '[:space:]')
  next_version=$(cat "/tmp/gh_${BUILD_NUMBER}-build_sdk-${language}.version")

  if [[ ${modification_count} != 0 && ${next_version} != "" ]]; then
      setup_git
      git_commit_and_tag ${next_version}
      git_push
  else
      echo No push to Github. Modifications:
      git diff -U0
  fi
}

BUILD_DIR=${HOME}/build

LANGUAGES=("python" "java" "php")

for language in "${LANGUAGES[@]}"
do
  echo "Starting upload for - ${language}"
  process ${language}
done
