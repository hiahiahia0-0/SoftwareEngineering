FROM python:3.10

MAINTAINER Juice

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt -i  https://mirrors.aliyun.com/pypi/simple/

EXPOSE 8000

CMD python manage.py runserver 0:8000
