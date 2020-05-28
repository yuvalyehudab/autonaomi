#__main__.py

import click
import json
from .saver import Saver
import urllib.parse
from ..utils.queue import queue_uploader

@click.group()
def cli():
    pass

@cli.command('save')
@click.option('-d', '--database', required=True)
@click.argument('name')
@click.argument('data_path')
def save_command(database, name, data_path):
    with open(data_path) as file:
        data = file.read()
    Saver(database).save(name, data)

@cli.command('run-saver')
@click.argument('database_url')
@click.argument('queue_url')
def run_command(database_url, queue_url):
    '''-p/--port INT -h/--host ADDRESS PUBLISH'''
    def save_callback(data):
        q, = json.loads(data)['result'].keys()
        Saver(database_url).save(q, data)
    parsed_url = urllib.parse.urlparse(queue_url)
    uploader = queue_uploader(  queue_type=parsed_url.scheme,
                                    host=parsed_url.hostname,
                                    port=parsed_url.port)

    uploader.consume(exchange='processed', queue='to-saver', callback=save_callback)

if __name__ == '__main__':
    cli()

