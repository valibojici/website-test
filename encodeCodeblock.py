import sys

if __name__ == '__main__':
	try:
		with open(sys.argv[1]) as f:
			lines = f.read()
			chars = {'<' : '&lt;','>' : '&gt;','&' : '&amp;','"' : '&quot;',"'" : '&#39;'}
			
			print(escapeHTML(lines)[1:-1],end='')

	except Exception as e:
		print(e)


def escapeHTML(string):
	chars = {'<' : '&lt;','>' : '&gt;','&' : '&amp;','"' : '&quot;',"'" : '&#39;'}
	for k, v in chars.items():
		string = string.replace(k, v);
	return string