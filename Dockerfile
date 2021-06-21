FROM python:3.7.3

WORKDIR usr/src/dash_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .