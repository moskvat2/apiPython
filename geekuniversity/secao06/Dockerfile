FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install curl apt-get utils

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]