#!/usr/bin/python

import json

with open('output.json', 'r') as f:
	jsonData = json.loads(f.read())

elem = jsonData['content'][0]

for i in range(250):
	jsonData['content'].append(elem)

with open('output.json', 'w') as f:
	f.write(json.dumps(jsonData))
	 