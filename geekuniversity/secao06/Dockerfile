FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y install curl apt-utils

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]