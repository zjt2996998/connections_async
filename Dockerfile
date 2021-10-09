# syntax=docker/dockerfile:1
FROM pypy:3.7-7.3.5-slim-buster
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev build-essential \
    && apt-get install -y netcat \
    && pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
