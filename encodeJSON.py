from os import sep
import sys
from typing import List
import encodeHTML as ec
import json
import argparse
import re

parser=argparse.ArgumentParser(
    description='''Convert file to JSON. 
	Code must begin with #BEGIN_CODE and end with #END_CODE
	Solution must begin with #BEGIN_SOLUTION and end with #END_SOLUTION. Code blocks must be enclosed in <inline> or <block> tags.
	Tags section must begin with #BEGIN_TAGS and end with #END_TAGS. Individual tags must be separated by''',)

parser.add_argument('file',help='input text file path')
parser.add_argument('-w', '--write', help='file path for output')
parser.add_argument('-u','--update', help='file path to update')
parser.add_argument('-v', '--verbose', help='prettify json', action='store_true')
args=parser.parse_args()

if __name__ == '__main__':
	try:
		with open(args.file) as f:
			text = f.read()

			problem = re.search(r'#BEGIN_PROBLEM(.*)#END_PROBLEM', text, flags=re.S).group(1).strip()
			solution = re.search(r'#BEGIN_SOLUTION(.*)#END_SOLUTION', text, flags=re.S).group(1).strip()
			tags = [tag.strip() for tag in re.search(r'#BEGIN_TAGS(.*)#END_TAGS', text, flags=re.S).group(1).strip().split(';')]

			solution = re.sub(
				'<inline>(.*)<inline>',
				lambda m: f"<pre class='inline'><code>{ec.escapeHTML(m.group(1).strip())}</code></pre>",
				solution, flags=re.S)

			# print(re.search('<block>(.*)<block>', solution, re.S).group(1))

			solution = re.sub(
				'<block>(.*)<block>',
				lambda m: f"<pre><code>{ec.escapeHTML(m.group(1).strip())}</code></pre>",
				solution, flags=re.S)

			solution = '<span>' + solution + '</span>'

			if args.write or args.update:
				if args.write:
					with open(args.write, 'w') as jsonFile:
						jsonFile.write(json.dumps(
							{
								'content': [ {'id' : 1, 'problem' : problem, 'solution' : solution, 'tags' : tags} ]
							}, 
						indent=4 if args.verbose else None ))
				else:
					with open(args.update, 'r') as jsonFile:
						jsonFileData = json.loads(jsonFile.read())
						
						lastId = None
						if 'content' in jsonFileData:
							if isinstance(jsonFileData['content'], List):
								if 'id' in jsonFileData['content'][-1]:
									lastId = jsonFileData['content'][-1]['id']

						if lastId is None:
							jsonFileData = { 'content': [ {'id' : 1, 'problem' : problem, 'solution' : solution, 'tags' : tags} ] }
						else:
							jsonFileData['content'].append({'id' : lastId+1, 'problem' : problem, 'solution' : solution, 'tags' : tags})

					with open(args.update, 'w') as jsonFile:
						jsonFile.write(json.dumps(jsonFileData, indent=4 if args.verbose else None ))
			else:
				print(json.dumps({'content': [
					{'id' : 1, 'problem' : problem, 'solution' : solution, 'tags' : tags},
				]}, indent= 4 if args.verbose else None ))

	except Exception as e:
		print(e)