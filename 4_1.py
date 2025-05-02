# 4-1
def last_line(name):
	last_line = ''
	with open(name, 'r') as f:
		for line in f:
			last_line = line
	if last_line == None:
		return None
	else:
		return last_line.rstrip('\n')

def number_of_characters(name):
	with open(name, 'r') as f:
		content = f.read()
	cnt = 0
	for val in content:
		cnt += 1
	return cnt

def file_upper(infile, outfile):
	with open(infile, 'r') as f:
		content = f.read()
		content = content.upper()
		with open(outfile, 'w') as g:
			print(content, file=g)
