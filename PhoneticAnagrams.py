import re
from collections import Counter

def compare(s, t):
	return Counter(s) == Counter(t)



def generatePAs(base):
	x = open('shorterdict.txt', 'r')
	lines = x.readlines()
	y = open('anagramslist.txt', 'w')
	found = False
	basepros = []
	upbase = base.upper()
	for i in range(len(lines)):
		lines[i] = lines[i].strip().split(' ')
		if(lines[i][0]==upbase):
			basepros.append(Counter(lines[i][1:]))
	anagrams = []
	for pronunciation in basepros:
		anagrams = anagrams + findanagrams(lines, pronunciation)
	y.write(base +': ' + ' '.join(anagrams))

def findanagrams(lines, pro):
	newlist = []
	for line in lines:
		if compare(line[1:],pro):
			newlist.append(line[0])
	return newlist

def findall():
	x = open('shorterdict.txt', 'r')
	lines = x.readlines()
	for line in lines:
		splitline = line.strip().split(' ')
		PAs = generatePAs(splitline[0])

def editdictionary():
	x = open('cmudict-0.7b.txt', 'r')
	y = open('shorterdict.txt', 'w')
	lines = x.readlines()

	newlines = []

	for j in range(len(lines)):
		if re.search('^[A-Z]$', lines[j][0]) and not re.search('(\.)|(8)', lines[j] and lines[j]!=''):
			brokenline = lines[j].strip().split(' ')
			for i in range(len(brokenline)):
				if(brokenline[i]!=''):
					match = re.search('[A-Z\'\-]+', brokenline[i])
					s = match.start()
					e = match.end()
					brokenline[i] = brokenline[i][s:e]
			brokenline.remove('')
			newlines.append(' '.join(brokenline) + '\n')

	for line in newlines:
		y.write(line)

	x.close()
	y.close()
