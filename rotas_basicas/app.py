# Seu código aqui

from flask import Flask
from datetime import datetime
from http import HTTPStatus

app = Flask(__name__)

@app.get('/')
def home():
    return {'data': 'Hello Flask!'}, HTTPStatus.OK

@app.get('/current_datetime')
def current_datetime():
    new_date = datetime.now().strftime("%d/%m/%Y")
    new_hour = datetime.now().strftime("%H") 
    am_pm = datetime.now().strftime('%p')
    data = {
        "current_datetime": datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"),
        "message": ""
    }
    
    if int(new_hour) < 12:
        data.update({"message": "Bom dia!"})
    elif 12 <= int(new_hour) and int(new_hour) < 18:
        data.update({"message": "Boa tarde!"})
    elif int(new_hour) >= 18:
        data.update({"message": "Boa noite!"})

    return data, HTTPStatus.OK

