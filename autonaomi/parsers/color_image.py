#color_image.py
#autonaomi.parsers
from PIL import Image

def color_image(snapshot, path):
	result = {	'height': snapshot.color_image.height,
				'width': snapshot.color_image.width,
				'data': str(path / 'color.jpg')}

	bin_data = (path / 'color.bin').read_bytes()

	data = []
	for i in range(len(bin_data) // 3):
		data.append(tuple(bin_data[3 * i: (3 * i) + 3]))
	im = Image.new('RGB', (result['width'], result['height']))
	im.putdata(data)
	im.save(str(path / 'color.jpg'))
	return result