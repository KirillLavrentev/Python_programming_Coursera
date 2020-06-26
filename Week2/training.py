import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
    	parser = argparse.ArgumentParser()
    	parser.add_argument("--key", type = str, help="get key value")
    	parser.add_argument("--val", type = str, action="store_true", help = "get and write value")
	f.write()
	
    
    args = parser.parse_args()
    answer = args.val
    print("the square of {}, {}".format(args.key, args.value))

        
        

