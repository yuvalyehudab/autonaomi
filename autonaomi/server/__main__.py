#__main__.py
#CLI sits here
import datetime
import click
import urllib.parse
import pathlib
import json
import google.protobuf.json_format
from ..utils.autonaomi_pb2 import User, Snapshot

from .server import run_server

from ..utils.queue import queue_uploader

def build_message(info, snapshot, path):
    color_path = path / 'color.bin'
    depth_path = path / 'depth.bin'

    color_path.write_bytes(snapshot.color_image.data)
    depth_path.write_text(json.dumps(list(snapshot.depth_image.data)))

    snapshot.color_image.ClearField('data')
    snapshot.depth_image.ClearField('data')

    return json.dumps(  {
                        'user_info': google.protobuf.json_format.MessageToJson(info),
                        'snapshot': google.protobuf.json_format.MessageToJson(snapshot),
                        'path': str(path)
                        })

@click.group()
def cli():
    pass

def create_publisher(parsed_url):
    def publish(data):
        info = data['user_info']
        snapshot = data['snapshot']

        timestamp = datetime.datetime.fromtimestamp(snapshot.datetime / 1000)
        autonaomi_data_home = pathlib.Path.home() / f'autonaomi_data'
        autonaomi_data_home.mkdir(parents=True, exist_ok=True)
        snap_path = autonaomi_data_home / f'{info.user_id}' / f'{timestamp:%Y-%m-%d_%H-%M-%S-%f}'


        snap_path.mkdir(exist_ok=True, parents=True)
        message = build_message(info, snapshot, snap_path)

        uploader = queue_uploader(  queue_type=parsed_url.scheme,
                                    host=parsed_url.hostname,
                                    port=parsed_url.port)

        uploader.publish(data=message, exchange='for_process')
    return publish

@cli.command('run-server')
@click.option('-h', '--host', default='localhost', help='where shoukd the server run', type=str)
@click.option('-p', '--port', default=8000, help='port where the server listens', type=int)
@click.argument('url')
def run_command(host, port, url):
    '''-p/--port INT -h/--host ADDRESS PUBLISH'''

    parsed_url = urllib.parse.urlparse(url)
    publisher = create_publisher(parsed_url)
    
    run_server(host=host, port=port, publish=publisher)

if __name__ == '__main__':
    cli()




