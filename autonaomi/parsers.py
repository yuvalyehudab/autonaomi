#parsers.py


import click

@click.group()
def cli():
    pass

@cli.command('parse')
@click.argument('name')
@click.argument('data')
def run_parser_command(name, data):
    '''NAME DATA'''
    run_parser(name, data)

def run_parser(name, data):
    print(f'parsers.py: name: {name}\t data: {data}')

if __name__ == '__main__':
    cli()
