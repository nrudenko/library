FROM python:2.7

COPY config.py /etc/library/config
COPY src /usr/library

WORKDIR /usr/library

RUN pip install -r requirements.txt
