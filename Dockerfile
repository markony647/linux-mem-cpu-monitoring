# base image
FROM python:latest

WORKDIR /linux-mem-cpu-monitoring

ADD . /linux-mem-cpu-monitoring


RUN pip3 install --upgrade pip \
&& pip3 install psutil
