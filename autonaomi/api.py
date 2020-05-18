#api.py

import click

def run_api_server(host, port, database_url):
    pass

@click.group()
def cli():
    pass

@click.command('run-server')
@click.option('-h', '--host', required=True)
@click.option('-p', '--port', type=int, required=True)
@click.option('-d', '--database', required=True)
def run_server_command(host, port, database):
    run_api_server(host, port, database)

if __name__ == '__main__':
    cli()

