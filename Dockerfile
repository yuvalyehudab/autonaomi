
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y --no-install-recommends ca-certificates make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

RUN apt-get install -y python3.8 python3-pip
RUN python3.8 -m pip install --upgrade pip setuptools wheel

RUN ln -s /usr/bin/python3.8 /usr/local/bin/python 
RUN python3.8 -m pip install --upgrade pip setuptools wheel

COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY autonaomi/ /autonaomi
RUN mkdir -p /home/user/autonaomi_data




