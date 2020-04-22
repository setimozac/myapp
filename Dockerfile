FROM python:3.7-alpine

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /

RUN apk add --update --no-cache postgresql-client 
RUN apk add --update --no-cache --virtual build-deps \ 
    gcc libc-dev linux-headers postgresql-dev
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH /lib:/usr/lib

RUN apk add --no-cache libmemcached-dev zlib-dev

RUN pip install -r requirements.txt

RUN apk del build-deps

RUN mkdir /app && cd /app
WORKDIR /app

COPY ./app .

RUN adduser -D user1
USER user1





