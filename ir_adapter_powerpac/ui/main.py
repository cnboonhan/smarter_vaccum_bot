import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup
import os

connection_string = os.environ.get("POWERPAC_ADAPTER_CONNECTION_STRING")
app = FastAPI()

@app.put("/remote/left")
def remote_left():
    response_html = requests.put(f"{connection_string}/remote/left")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/right")
def remote_right():
    response_html = requests.put(f"{connection_string}/remote/right")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/up")
def remote_up():
    response_html = requests.put(f"{connection_string}/remote/up")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/down")
def remote_down():
    response_html = requests.put(f"{connection_string}/remote/down")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/center")
def remote_center():
    response_html = requests.put(f"{connection_string}/remote/center")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/return")
def remote_return():
    response_html = requests.put(f"{connection_string}/remote/return")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/edge")
def remote_edge():
    response_html = requests.put(f"{connection_string}/remote/edge")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}

@app.put("/remote/auto")
def remote_auto():
    response_html = requests.put(f"{connection_string}/remote/auto")
    response = BeautifulSoup(response_html.text, 'html.parser').get_text().replace('\n', '').replace('\r', '')
    return {"message": response}
