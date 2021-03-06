#__main__.py
#autonaomi.gui

import click
from .gui import run_server

@click.group()
def cli():
    pass

@cli.command('run-server')
@click.option('-h', '--host', default='localhost')
@click.option('-p', '--port', type=int, default=5000)
@click.option('-d', '--database', default='mongodb://localhost:27017')
def run_server_command(host, port, database):
    run_server(host=host, port=port, database_url=database)

if __name__ == '__main__':
    cli()
