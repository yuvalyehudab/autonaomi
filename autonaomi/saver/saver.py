#saver.py
import json
from ..utils import database
import urllib.parse
import google.protobuf.json_format
from ..utils.autonaomi_pb2 import User, Snapshot

class Saver:
    def __init__(self, url):
        parsed_url = urllib.parse.urlparse(url)
        self.database_url = url
        self.database = database.database(parsed_url.scheme, host=parsed_url.hostname, port=parsed_url.port)

    def save(self, name, data):
        d = json.loads(data)
        
        self.database.save(google.protobuf.json_format.Parse(d['user_info'], User()), google.protobuf.json_format.Parse(d['snapshot'], Snapshot()).datetime, d['result'])


