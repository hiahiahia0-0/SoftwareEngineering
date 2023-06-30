FROM python:3.10

MAINTAINER Juice

RUN mkdir /app

WORKDIR /app/CET/

COPY . /app

RUN pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/

EXPOSE 8000


