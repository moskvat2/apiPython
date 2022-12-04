FROM python:3.10-slim

WORKDIR /usr/src/app

RUN apt-get update
# RUN apt-get install -y curl apt-utils gnupg unixodbc unixodbc-dev
# RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl -sSL https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
# RUN apt-get update
# RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18 && apt-get clean


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
