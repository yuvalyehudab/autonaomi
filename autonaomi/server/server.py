#server.py
import flask
from flask import request

import datetime

import json
import google.protobuf.json_format
from ..utils.autonaomi_pb2 import User, Snapshot


app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def get_snapshot():
    raw_data = request.json
    data = parse_data(raw_data)
    app.config['publish'](data)

    return ''

def run_server(host, port, publish):
    #print(f'run_server.py: host: {host}\t port: {port}\t path: {publish}')
    app.config['publish'] = publish
    app.run(host=host, port=port, threaded=True)

def parse_data(data):
    info = google.protobuf.json_format.Parse(data['user_info'], User())
    
    snapshot = google.protobuf.json_format.Parse(data['snapshot'], Snapshot())
    
    return {'user_info': info,'snapshot': snapshot}
