FROM python:3.10-alpine
FROM gorialis/discord.py

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .