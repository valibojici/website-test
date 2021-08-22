import json
import sys
import argparse

parser=argparse.ArgumentParser(
    description='''Prettify JSON file and output to stdout by default.''',)

parser.add_argument('file',help='input JSON file')
parser.add_argument('-o', '--output', help='output file')
args=parser.parse_args()

if __name__ == '__main__':
	try:
		with open(args.file, 'r') as f:
			jsonData = json.loads(f.read());
			if args.output is not None:
				with open(args.output, 'w') as g:
					g.write(json.dumps(jsonData, indent=4))
			else:
				print(json.dumps(jsonData, indent=4))
	except Exception as e:
		print(e)