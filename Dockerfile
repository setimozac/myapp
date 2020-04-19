FROM python:3.8-alpine

ENV PYTHONUNBUFFERD 1

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH /lib:/usr/lib

COPY ./requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app && cd /app
WORKDIR /app

COPY ./app .

RUN adduser -D user1
USER user1





