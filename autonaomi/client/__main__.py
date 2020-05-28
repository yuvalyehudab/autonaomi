#autonaomi.client
#__main__.py


import click

from .client import upload_sample

@click.group()
def cli():
    pass

@cli.command('upload-sample')
@click.option('-h', '--host', default='localhost')
@click.option('-p', '--port', default=8000, type=int)
@click.argument('path')
def upload_command(host, port, path):
    '''-p/--port INT -h/--host ADDRESS PATH'''
    upload_sample(host, port, path)


if __name__ == '__main__':
    cli()

