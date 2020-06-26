
import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
    	parser = argparse.ArgumentParser()
	parser.add_argument("square", help="display a square of a given number", type=int)
	args = parser.parse_args()
	print(args.square**2)
