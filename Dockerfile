FROM python:3.8-slim-buster

WORKDIR /appserver

COPY . .

CMD [ "python3", "server.py"]