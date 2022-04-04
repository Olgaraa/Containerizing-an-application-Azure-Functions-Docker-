# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /

	
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev \
  && apt-get clean

RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot
