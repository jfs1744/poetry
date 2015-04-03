import re
def generatePAs(base):
	x = open('cmudict-0.7b.txt', 'r')
	lines = x.readlines();
	x.close()

def editdictionary():
	x = open('cmudict-0.7b.txt', 'r')
	y = open('shorterdict.txt', 'w')
	lines = x.readlines();
	newlines = []

	for j in range(len(lines)):
		if re.search('^[A-Z]$', lines[j][0]) and not re.search('\.', lines[j]):
			brokenline = lines[j].strip().split(' ')
			for i in range(len(brokenline)):
				if(brokenline[i]!=''):
					match = re.search('[A-Z\'\-]+', brokenline[i])
					s = match.start()
					e = match.end()
					brokenline[i] = brokenline[i][s:e]
			newlines.append(' '.join(brokenline) + '\n')

	for line in newlines:
		y.write(line)

	x.close()
	y.close()
