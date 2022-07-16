
from flask import Flask, request
import requests
import json
import base64
from config import CONFIG

app = Flask(__name__)

@app.route('/<name>' , methods=['GET', 'POST', 'PUT'])
def sendRequest(name):
    url = CONFIG["API_HOST"] + "/api/v1/namespaces/guest/actions/" + name + "?result=true&blocking=true"

    headers = {
        'Authorization': CONFIG["AUTH"],
        'Content-Type': 'application/json'
    }
    data = json.dumps(request.json)
    response = requests.request("POST", url, headers=headers, data=data)
    return json.loads(response.text)