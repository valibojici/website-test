#!/usr/bin/python

import json

with open('test.txt', 'r') as f:
	content = f.read()
	chars = {'<' : '&lt;', '>' : '&gt;', '"' : '$quot;', "'" : '&#039;', '&' : '&amp;'}
	
	for k,v in chars.items():
		content = content.replace(k, v)

	jsonData = json.dumps({'content' : content})
	
	with open('output.json', 'w') as g:
		g.write(jsonData)

