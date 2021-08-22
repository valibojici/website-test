import sys
import encodeCodeblock as ec
import json

if __name__ == '__main__':
	try:
		with open(sys.argv[1]) as f:
			lines = f.read().split('###')
			problem = lines[0].strip()
			solution = lines[1].strip();

			print(repr(problem)[1:-1])
			solution = solution.split('<inline>')

			for i in range(1, len(solution), 2):
				solution[i] = f"<pre class='inline'><code>{ec.escapeHTML(solution[i].strip())}</code></pre>"

			solution = ''.join(solution)

			solution = solution.split('<block>')
			for i in range(1, len(solution), 2):
				solution[i] = f"<pre><code>{ec.escapeHTML(solution[i].strip())}</code></pre>"

			solution = '<span>' + ''.join(solution) + '</span>'
			
			with open(sys.argv[2], 'r') as jsonFile:
				jsonFileData = json.loads(jsonFile.read())
				
				lastId = jsonFileData['content'][-1]['id']

				jsonFileData['content'].append({'id' : lastId + 1, 'problem' : problem, 'solution' : solution})
				

			with open(sys.argv[2], 'w') as jsonFile:
				jsonFile.write(json.dumps(jsonFileData))

	except Exception as e:
		print(e)