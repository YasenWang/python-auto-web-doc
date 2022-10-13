#!/usr/bin/env bash
while getopts n:u:h args; do
  case $args in
  n)
    PROJECT_NAME=$OPTARG
  ;;
  u)
    GIT_URL=$OPTARG
  ;;
  ?)
    help
  ;;
  *);;
  esac
done
FILE_NAME=$(basename "$0")
GIT_REPOSITORY_PATH=/home/sphinx-doc/"$PROJECT_NAME"-soucre

function help() {
  echo "How to use if."
  echo "$FILE_NAME" '[-n PROJECT_NAME] [-u GIT_URL]'
  exit 0
}

# Use std log with [std_log $LOG_LEVEL $LOG_MSG]
function std_log () {
  DATE=$(date +%Y-%m-%d" "%H:%M:%S)
  USER=$(whoami)
  echo "${DATE} ${USER} execute $0 [$1] $2"
}

if [ ! -d "$GIT_REPOSITORY_PATH" ];then
  mkdir -p "$GIT_REPOSITORY_PATH"
fi

std_log INFO "Git repository creating..."
cd "$GIT_REPOSITORY_PATH" || exit 0
git clone "$GIT_URL" "$GIT_REPOSITORY_PATH"
std_log INFO "Git repository created."