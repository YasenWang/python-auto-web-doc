# Python Auto Web Docs

## Introduction
This project can help you to deploy a web python docs automatically.
You can get an out-of-the-box service on Docker.
This project has two part, webhooks server based on spring boot and docs builder based on python sphinx.

## Get started

### 1. Add code doc config to your project path.
```text
python-project-root
    package1
    package2
    sphinx-config
        _static
        _templates
        conf.py
        import.txt
        index.rst
```
Edit which package you want to import in *import.txt*.
Author and version info in *config.py*.
Templates RST in *index.rst*.

### 1. Config git repository
Config a git webhook in your git website to catch *post* action.
The hook address need to be set like this.
```
{your server ip or domain}:8080/post-update?p=web-doc
```
e.g.
```
http://docshook.my.com:8080/post-update?p=anythingbutmust
```

### 2. Catch webhooks from git
You can make it both *auto by docker* and *manual by source code*.

#### Auto deployment by docker **suggested**
```shell
docker pull yasenwang/auto-doc:latest
```
This docker image need one param, git url.
In case that, docker image is officially not supposed to set public ssh key inside.
You can generate a token url like example:
```shell
https://{username}:{token}@github.com/{home}/{repository}.git
```
```shell
docker run -p 80:80 -p 8080:8080 -dit yasenwang/auto-doc:latest {git url with token}
```

#### Manual deployment on server

NGINX HTML PATH=/usr/local/nginx/html

PROJECT PATH=/home/auto-doc

1. Move files under *release* folder to **PROJECT PATH**.
2. Pip install -r requirements.txt
3. Vi open main.py change java program in background mode.
> nohup java -jar {install_path}/GitWebhooksServer-0.0.1-SNAPSHOT.jar &2>&1
3. Chmod +x main.py and run it.

***ENVIRONMENT***
- Python
- Java
- Nginx
