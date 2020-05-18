#gui.py
import click

def run_server(host, port, api_host, api_port):
    pass

@click.group()
def cli():
    pass

@cli.command('run-server')
@click.option('-h', '--host')
@click.option('-p', '--port')
@click.option('-H', '--api-host', 'api_host')
@click.option('-P', '--api-port', 'api_port')
def run_server_command(host, port, api_host, api_port):
    pass

if __name__ == '__main__':
    cli()

