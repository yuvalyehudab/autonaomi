#client.py

import requests
import gzip
from ..utils.autonaomi_pb2 import User, Snapshot
from google.protobuf.json_format import MessageToJson

def upload_sample(host='localhost', port=8000, path='sample.mind.gz'):
    with gzip.open(path) as file:
        user_length = int.from_bytes(file.read(4), 'little')
        
        user_info = User()
        user_info.ParseFromString(file.read(user_length))
        u_info_json = MessageToJson(user_info)
        snapshot_len = file.read(4)
        
        while snapshot_len:

            snapshot_len = int.from_bytes(snapshot_len, 'little')
            snapshot = Snapshot()
            snapshot.ParseFromString(file.read(snapshot_len))
            data = {
                    'user_info': u_info_json,
                    'snapshot': MessageToJson(snapshot)
                    }
            requests.post(f'http://{host}:{port}/', json=data)
            snapshot_len = file.read(4)

    #print(f'client.py: host: {host}\t port: {port}\t path: {path}')

