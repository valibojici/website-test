import sys

def escapeHTML(string):
	chars = {'&' : '&amp;', '<' : '&lt;','>' : '&gt;','"' : '&quot;',"'" : '&#39;'}
	for k, v in chars.items():
		string = string.replace(k, v)

	return string

if __name__ == '__main__':
	try:
		with open(sys.argv[1]) as f:
			lines = f.read()
			chars = {'&' : '&amp;','<' : '&lt;','>' : '&gt;','"' : '&quot;',"'" : '&#39;'}
			
			print(escapeHTML(lines)[1:-1],end='')

	except Exception as e:
		print(e)


