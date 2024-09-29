FROM python:3.12-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install gcc -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt
