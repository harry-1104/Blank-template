FROM python:slim
WORKDIR /code/python
RUN apt update -y && apt-get update -y
RUN apt upgrade -y && apt-get upgrade -y
RUN apt-get install -y vim
RUN touch main.py
RUN vim main.py