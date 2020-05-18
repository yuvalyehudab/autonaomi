#server.py


import click

@click.group()
def cli():
    pass

@cli.command('run-server')
@click.option('-h', '--host', required=True)
@click.option('-p', '--port', required=True, type=int)
@click.argument('publish')
def run_command(host, port, publish):
    '''-p/--port INT -h/--host ADDRESS PUBLISH'''
    run_server(host, port, publish)

def run_server(host, port, publish):
    print(f'run_server.py: host: {host}\t port: {port}\t path: {publish}')

if __name__ == '__main__':
    cli()

