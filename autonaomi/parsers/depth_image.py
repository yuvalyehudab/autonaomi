#depth_image.py
#autonaomi.parsers
from matplotlib import pyplot
import json
import numpy as np

def depth_image(snapshot, path):
	result = {	'height': snapshot.depth_image.height,
				'width': snapshot.depth_image.width,
				'data': str(path / 'depth.jpg')}

	bin_data = json.loads((path / 'depth.bin').read_text())

	p = np.asarray(bin_data)
	data = p.reshape((result['height'],result['width']))
	pyplot.imsave(result['data'], data, cmap='hot')
	return result
