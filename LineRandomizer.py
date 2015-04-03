from random import shuffle
from collections import deque

def getlines(filename):
	x = open(filename,'r')
	types = x.readline().strip()
	typesdict = {}
	for char in types:
		typesdict[char] = []
	x.readline()
	x.readline()
	lines = x.readlines()
	for line in lines:
		if (types.find(line.strip()[:1]) != -1):
			typesdict[line.strip()[:1]].append(line[1:].strip())
	for char in types:
		shuffle(typesdict[char])
	x.close()
	return typesdict

def createpoem(linesdict, poformat):
	poem = ''
	countdict = {}
	for key in linesdict.keys():
		countdict[key] = 0
	for char in poformat:
		newline = linesdict[char][countdict[char]]
		countdict[char] = countdict[char]+1
		poem = poem + newline + '\n'
	return poem + '\n'

def main(inputfile, outputfile):
	linesdict = getlines(inputfile)
	x = open(inputfile, 'r')
	keys = x.readline().strip()
	poformat = x.readline().strip()
	numreps = x.readline().strip()
	x.close()
	x = open(outputfile, 'w')
	for i in range(int(numreps)):
		x.write( "#" + str(i+1) + '\n')
		x.write(createpoem(linesdict, poformat))
		for key in keys:
			shuffle(linesdict[key])
	x.close()





