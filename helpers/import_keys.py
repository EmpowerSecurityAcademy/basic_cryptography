
import json
import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '../keys/keys.json')

def load_keys():
	with open(file_path) as json_data:
		config = json.load(json_data)
		return config