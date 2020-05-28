#run_parser.py
#autonaomi.parsers

import datetime
import json
import pathlib
import google.protobuf.json_format
from ..utils.autonaomi_pb2 import Snapshot, User

from .feelings import feelings
from .pose import pose
from .color_image import color_image
from .depth_image import depth_image

parsers_dict = {
	'feelings': feelings,
	'pose': pose,
	'depth_image': depth_image,
	'color_image': color_image
}

def run_parser(name, data):
    if name not in parsers_dict:
    	raise
    d = json.loads(data)

    t = google.protobuf.json_format.Parse(d['snapshot'], Snapshot())
    tmp=d['path']

    path = pathlib.Path(d['path'])
    d['result'] = {name: parsers_dict[name](t, path)}
    return json.dumps(d)