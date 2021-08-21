import json

with open('test.txt', 'r') as f:
	content = f.read()
	jsonData = json.dumps({'content' : content})
	
	with open('output.json', 'w') as g:
		g.write(jsonData)

