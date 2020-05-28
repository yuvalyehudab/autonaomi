#__main__.py
#autonaomi.cli
import click
import requests

context={}
context['url'] = f'http://'

@click.group()
@click.option('-h', '--host', default='loaclhost')
@click.option('-p', '--port', default=8000)
def cli(host, port):
  context['url'] = context['url'] + f'{host}:{port}'

@cli.command('get-users')
def get_users():
  click.echo(requests.get(context['url'] + f'/users').json())

@cli.command('get-user')
@click.argument('user_id')
def get_user(user_id):
  click.echo(requests.get(context['url'] + f'/users/{user_id}').json())

@cli.command('get-snapshots')
@click.argument('user_id')
def get_snapshots(user_id):
  click.echo(requests.get(context['url'] + f'/users/{user_id}/snapshots').json())

@cli.command('get-snapshot')
@click.argument('user_id')
@click.argument('snapshot_id')
def get_snapshot(user_id, snapshot_id):
  click.echo(requests.get(context['url'] + f'/users/{user_id}/snapshots/{snapshot_id}').json())

@cli.command('get-result')
@click.argument('user_id')
@click.argument('snapshot_id')
@click.argument('result_name')
@click.option('-s', '--save', default='')
def get_result(user_id, snapshot_id, result_name, save):
  r = requests.get(context['url'] + f'/users/{user_id}/snapshots/{snapshot_id}/{result_name}')
  if save:
    with open(save, 'w') as file:
      file.write(r)
  else:
    click.echo(r.json())

if __name__ == '__main__':
  cli()
