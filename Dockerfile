FROM python:3.6

MAINTAINER saufis

RUN mkdir /app

COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pipenv && \
    cd /app/ && \
    pipenv install --deploy --system

RUN apt-get -y update && apt-get -y install gettext

COPY src /app/

WORKDIR /app
