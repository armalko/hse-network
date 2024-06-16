FROM ubuntu:20.04

RUN apt update && apt install -y iputils-ping && apt install -y python3
RUN apt-get install -y python3-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install validators
