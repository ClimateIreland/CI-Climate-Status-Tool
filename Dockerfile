FROM python:3.7.3

WORKDIR /usr/src
COPY . ./app
RUN apt update && \
    apt install libgdal-dev && \
    cd /usr/src/app && pip install --no-cache-dir -r requirements.txt
WORKDIR /usr/src/app/dash_app
