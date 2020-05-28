#gui.py
#autonaomi.gui

from ..utils import database

import flask
from flask import render_template, request, send_file
import pathlib
import urllib.parse


app = flask.Flask(__name__)

def number_to_gender_w(number):
	if number == 0:
		return 'Male'
	if number == 1:
		return 'Female'
	return 'Other'

@app.route('/')
@app.route('/dashbosrd/')
def get_users():
	api_res = app.config['db'].get_users()
	for u in api_res:
		t = u['user_id']
		u['url'] = f'{request.url_root}{t}/'
	return render_template('users.html', users=api_res)

@app.route('/<user_id>/')
def get_user(user_id):
	try:
		int(user_id)
	except:
		return ""
	api_res = app.config['db'].get_user(user_id)
	api_res['url'] = f'{request.url_root}{user_id}/snapshots/'
	api_res['gender_w'] = number_to_gender_w(api_res['gender'])
	return render_template('user.html', user=api_res)

@app.route('/<user_id>/snapshots/')
def get_snapshots(user_id):
	api_res = app.config['db'].get_snapshots(user_id)
	return render_template('snapshots.html', snapshots=api_res, user_id=user_id)

@app.route('/<user_id>/<snapshot_id>/')
def get_snapshot(user_id, snapshot_id):
	api_res = app.config['db'].get_snapshot(user_id, snapshot_id)
	res = {'depth_image' : None,  'color_image' : None, 'feelings' : None,  'pose' : None}
	
	for result in api_res['available results']:
		res[result] = app.config['db'].get_result(user_id, snapshot_id, result)

		if 'data' in res[result]:
			res[result]['image_url'] = f'file://' + res[result]['data']

		
	return render_template('snapshot.html', snapshot=api_res, depth=res['depth_image'], color=res['color_image'], feelings=res['feelings'], pose=res['pose'])



@app.route('/<user_id>/<snapshot_id>/<result_name>')
def get_result_data(user_id, snapshot_id, result_name):
	r = app.config['db'].get_result(user_id, snapshot_id, result_name)
	
	if 'data' in r:
		result_file = pathlib.Path(r['data'])
		if result_file.exists():
			r['data'] = f'/users/{user_id}/snapshots/{snapshot_id}/{result_name}/data'
	return send_file(str(result_file), mimetype='image/jpeg')

@app.route('/clear_db')
def clear_db():
	app.config['db'].clear_all()
	return ""

def run_server(host, port, database_url):
  parsed = urllib.parse.urlparse(database_url)
  app.config['db'] = database.database(parsed.scheme, parsed.hostname, parsed.port)
  app.run(host=host, port=port, threaded=True)


