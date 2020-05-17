#client.py

import click

@click.group()
def cli():
    pass

@cli.command('upload-sample')
@click.option('-h', '--host', required=True)
@click.option('-p', '--port', required=True, type=int)
@click.argument('path')
def upload_command(host, port, path):
    '''-p/--port INT -h/--host ADDRESS PATH'''
    upload_sample(host, port, path)

def upload_sample(host, port, path):
    print(f'client.py: host: {host}\t port: {port}\t path: {path}')

if __name__ == '__main__':
    cli()

