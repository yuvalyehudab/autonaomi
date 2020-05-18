#cli.py

import click
import requests

@click.group()
click.option('-h', '--host')
click.option('-p', '--port')
def cli(host='127.0.0.1', port=8000):
    pass

@click.command('get-users')
def get_users():
    pass

@click.command('get-user')
@click.argument('user_id')
def get_user(user_id):
    pass

@click.command('get-snapshots')
@click.argument('user_id')
def get_snapshots(user_id):
    pass

@click.command('get-snapshot')
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(user_id, snapshot_id):
    pass

@click.command('get-result')
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('parser')
@click.option('-s', '--save')
def get_result(user_id, snapshot_id, parser, save):
    pass

if __name__ == '__main__':
    cli()
