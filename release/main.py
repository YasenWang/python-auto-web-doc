#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2022/9/29 16:30
# file: main.py
# author: Yusheng Wang
# email: yasenwang@bupt.edu.cn
import argparse
import os

NGINX_PATH = '/usr/local/nginx/sbin/nginx'
INSTALL_PATH = '/home/auto-doc'


def _cmd_main(args):
    git_url = args.git_url
    # Start Nginx.
    os.system(NGINX_PATH)
    # Chmod +x
    os.system('chmod +x {install_path}/script/nginx-git-init.sh'.format(
        install_path=INSTALL_PATH))
    os.system('chmod +x {install_path}/hooks/post-update'.format(
        install_path=INSTALL_PATH))
    # Initial Git and Nginx
    os.system('{install_path}/script/nginx-git-init.sh -n {name} -u {url}'.format(
        name='web-doc', url=git_url, install_path=INSTALL_PATH))
    # Build docs.system
    os.system('{install_path}/hooks/post-update'.format(
        install_path=INSTALL_PATH))
    # Start Web Server
    os.system('java -jar {install_path}/GitWebhooksServer-0.0.1-SNAPSHOT.jar &2>&1 &'.format(
        install_path=INSTALL_PATH))
    a = input()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--git_url", dest='git_url', type=str, required=True, metavar='URL',
                        help="Git url with token https://{user}:{token}@git.com/your repo.")
    _args = parser.parse_args()
    _cmd_main(_args)
