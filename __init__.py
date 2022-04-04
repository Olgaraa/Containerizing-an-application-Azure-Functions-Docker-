import logging
import azure.functions as func
import json
import requests
from flatten_json import flatten
import pyodbc
import re
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    api= requests.get('https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/11')
    api_json =api.json()
    flat=flatten (api_json)
    data = json.dumps(flat)


    data = json.dumps(flat)
    var1=re.findall('\d.', data)[0]
    print(var1)
    var2=re.findall('\d*-\d*-\d* \d*:\d*:\d*', data)[0]
    print(var2)
    list=['Bardzo dobry','Dobry','Umiarkowany', 'Dostateczny','Zły', 'Bardzo zły']
    for var3 in list:
        if var3 in data:
            var3
            break

    server = 'olga.database.windows.net'
    database = 'my_db'
    username = os.environ['db_username']
    password = os.environ['database_pass']
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO dbo.my_db_tab(id,calcDate,indexLevel) VALUES (?,?,?)", (var1, var2, var3)) 
    cnxn.commit()
    return func.HttpResponse (data, status_code=200)  
