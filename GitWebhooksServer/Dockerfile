FROM centos:latest
# YUM RESOURCE
RUN rm -rf /etc/yum.repos.d \
    && mkdir /etc/yum.repos.d \
    && curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-vault-8.5.2111.repo \
    && yum clean all \
    && yum makecache
# CONFIG DEPENDENCY
RUN yum install -y gcc gcc-c++ git make
RUN yum install -y java-1.8.0-openjdk
# INSTALL PYTHON AND SET SOURCE
RUN yum install -y python38 python3-devel \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && python -m pip install --upgrade pip \
    && python -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
RUN yum install -y pcre pcre-devel zlib zlib-devel openssl openssl-devel
# INSTALL NGINX
COPY ./nginx-1.22.0.tar.gz /root/download/nginx-1.22.0.tar.gz
RUN tar -zxvf /root/download/nginx-1.22.0.tar.gz -C /root/download/ \
    && (cd /root/download/nginx-1.22.0; ./configure --with-http_ssl_module) \
    && (cd /root/download/nginx-1.22.0; make && make install)
# INSTALL PROJECT
COPY ./release/ /home/auto-doc/
RUN chmod +x /home/auto-doc/main.py
RUN python -m pip install -r /home/auto-doc/requirements.txt

# EXPOSE 80:http 8080:webhook
EXPOSE 80/tcp
EXPOSE 8080/tcp

# ENTRYPOINT ["/home/auto-doc/main.py", "-g"]

LABEL com.yasenstudio.auto-doc.author=YasenWang \
      com.yasenstudio.auto-doc.email=yasen@yasenstudio.com
