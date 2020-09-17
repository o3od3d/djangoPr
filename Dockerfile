FROM ubuntu:18.04

MAINTAINER DEV-GO

RUN apt-get update -y && \
    apt-get install -y \
    nginx \
    python3-dev \
    python3-pip \
    python3.6-dev libmysqlclient-dev

RUN pip3 install django uwsgi
RUN pip3 install djangorestframework
RUN pip3 install mysqlclient

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/sites-enabled/default
COPY mysite_nginx.conf /etc/nginx/sites-enabled/mysite_nginx.conf

COPY . /djangoPro/
WORKDIR /djangoPro/
#ADD requirements.txt /djangoPro/
#
#RUN pip3 install -r requirements.txt
RUN chmod +x /djangoPro/docker_start.sh # give permission
CMD /djangoPro/docker_start.sh

expose 80