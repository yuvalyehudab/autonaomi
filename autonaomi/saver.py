#saver.py
import click

class Saver:
    def __init__(self, url):
        self.database_url = url

    def save(self, name, data):
        print(f'{self.database_url=}\t{name=}\t{data=}')




@click.group()
def cli():
    pass

@cli.command('save')
@click.option('-d', '--database', required=True)
@click.argument('name')
@click.argument('data')
def save_command(database, name, data):
    Saver(database).save(name, data)

@cli.command('run-saver')
@click.argument('database_url')
@click.argument('queue_url')
def run_command(database_url, queue_url):
    '''-p/--port INT -h/--host ADDRESS PUBLISH'''
    run_saver(database_url, queue_url)

def run_saver(database_url, queue_url):
    print(f'run_saver.py: database: {database_url}\t queue: {queue_url}')

if __name__ == '__main__':
    cli()

