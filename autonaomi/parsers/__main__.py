#__main__.py
#autonaomi.parsers
import click
import urllib.parse

from ..utils.queue import queue_uploader
from .run_parser import run_parser

@click.group()
def cli():
	pass

@cli.command('parse')
@click.argument('parser_name')
@click.argument('data_path')
def parse(parser_name, data_path):
	with open(data_path, 'r') as file:
		data = file.read()
	print(run_parser(parser_name, data))

@cli.command('run-parser')
@click.argument('parser_name')
@click.argument('queue', default='rabbitmq://localhost:5672')
def cli_command(parser_name, queue):
	parsed_url = urllib.parse.urlparse(queue)
	def callback(data):
		res = run_parser(parser_name, data)
		uploader = queue_uploader(  queue_type=parsed_url.scheme,
                                    host=parsed_url.hostname,
                                    port=parsed_url.port)
		uploader.publish(data=res, exchange='processed')

	consumer = queue_uploader(queue_type=parsed_url.scheme, host=parsed_url.hostname, port=parsed_url.port)
	consumer.consume(exchange='for_process', queue=parser_name, callback=callback)

if __name__ == '__main__':
	cli()