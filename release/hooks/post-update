#!/usr/bin/env bash
while getopts n:: args; do
  case $args in
  n)
    PROJECT_NAME=$OPTARG
  ;;
  *);;
  esac
done
PROJECT_NAME="web-doc"
NGINX_PATH=/usr/local/nginx/sbin/nginx
DEPLOY_PATH=/usr/local/nginx/html
GIT_REPOSITORY_PATH=/home/sphinx-doc/"$PROJECT_NAME"-soucre
SPHINX_REPOSITORY_PATH=/home/sphinx-doc/"$PROJECT_NAME"-build
SPHINX_CONFIG=sphinx-config
AUTO_DEPLOYMENT_ROOT=/home/auto-doc

# Use std log with [std_log $LOG_LEVEL $LOG_MSG]
function std_log () {
  DATE=$(date +%Y-%m-%d" "%H:%M:%S)
  USER=$(whoami)
  echo "${DATE} ${USER} execute $0 [$1] $2"
}
if [ ! -d "$DEPLOY_PATH" ];then
  mkdir -p "$DEPLOY_PATH"
fi
if [ ! -d "$SPHINX_REPOSITORY_PATH" ];then
  mkdir -p "$SPHINX_REPOSITORY_PATH"
fi

std_log INFO "========Auto deployment START========"
# Git pull.
std_log INFO "Git pulling..."
cd "$GIT_REPOSITORY_PATH" || exit 1
git pull origin master || exit 1

# Move source code.
rm -rf "${SPHINX_REPOSITORY_PATH:?}"/*
if [ ! -d "$GIT_REPOSITORY_PATH"/"$SPHINX_CONFIG" ];then
  std_log ERROR "Not found $GIT_REPOSITORY_PATH/$SPHINX_CONFIG"
  exit 1
fi
while read -r line || [[ -n ${line} ]]; do
  cp -rf "$GIT_REPOSITORY_PATH"/"$line" "$SPHINX_REPOSITORY_PATH"
done < ./"$SPHINX_CONFIG"/import.txt

# Move sphinx pattern folder.
cp -rf "$AUTO_DEPLOYMENT_ROOT"/sphinx-pattern/* "$SPHINX_REPOSITORY_PATH"

# Move sphinx config.
mkdir -p "$SPHINX_REPOSITORY_PATH"/source
cp -rf "$GIT_REPOSITORY_PATH"/sphinx-config/* "$SPHINX_REPOSITORY_PATH"/source
std_log INFO "Sphinx workspace preparing finished."

std_log INFO "Sphinx start building."
cd "$SPHINX_REPOSITORY_PATH" || exit 1
sphinx-build source/ build/

std_log INFO "Move html files to Nginx."
cp -rf "$SPHINX_REPOSITORY_PATH"/build/* "$DEPLOY_PATH"
"$NGINX_PATH" -s reload
std_log INFO "========Auto deployment END========"