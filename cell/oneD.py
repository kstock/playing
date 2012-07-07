#Lets you define a one dimensional cellular automata!!!

#USAGE: (args optional)
# python oneD.py [size]
#

#TODO:
# This is another old first python days one
#
# actually let you choose symbol representations!!! lying program!!
# 
# clean ui
#
# non-retarded 1st gen creation!
#
# default rules to select from!
#
# save rules!



OFF = ' '
ON = '*'
TWO = '@'
symbols = {0:OFF,1:ON,2:TWO}

import time,re,random,sys

def oneD(size = 40):

	#rules = {(ON,ON,ON):OFF,(ON,ON,OFF):OFF,(ON,OFF,ON):OFF,(ON,OFF,OFF):ON,
	#					(OFF,ON,ON):ON,(OFF,ON,OFF):ON,(OFF,OFF,ON):ON,(OFF,OFF,OFF):OFF}
	while 1:
		rules,n,symbols = getRules()

		gen = defineMake(n,size)

		print ''.join(map(str,gen))
		for i in range(size//2):
			gen = update(gen,rules)
			time.sleep(.2)
			print ''.join(map(str,gen))


#
#generating rules,symbols
#


def useRules(rules, states):
	if states in rules:
		return rules[states]
	else:
		return OFF

def getRules(mode=1,n = 2):
	rule = []
	rules = {}
	vals = []

	while 1:
		print 'how many states do you want? \n \
		enter a number > 1'
		n = raw_input()
		try:
			if int(n) > 1:
				break
		except:
			print "error"
	n = [x for x in range(int(n))]
	n = ''.join(map(str,n))
	print 'the valid states are: ' + str(n)

	print 'what symbols do you want to be mapped to these states?'
	symbols ={}
	for i in str(n):
		while 1:
			print 'What symbol do you want to go with ' + i + '?'
			sym = raw_input()
			if len(sym) > 1:
				print 'that is not valid!'
				continue
			symbols[int(i)] = sym
			break

	print 'These are the symbols:'
	print symbols

	print 'Now, specify the rules for input -> output!'

	while 1:
		print "\nwhat do you want the input to be?\nEX 001 type q to finish"
		inR = raw_input()

		if re.match('[qQ]',inR):
			break

		if not re.match('['+n+']['+n+']['+n+']',inR) or len(inR) > 3:
			print 'invalid input, try again \n\n'
			continue
			
		print "what will be the associated output?"
		inV = raw_input()

		if re.match('[qQ]',inV):
			break

		if not re.match('['+n+']',inV) or len(inV) > 1:
			print 'invalid output, try again'
			continue
		
		rules[tuple(map(convSym,map(int,inR)))] = convSym(int(inV))
		print rules

	return rules,n,symbols

def convSym(num):
	if num in symbols:
		return symbols[num]
	else:
		pick = random.choice(range(len(symbols)))
		return symbols[pick]


#Making,update and displaying the grid		

def update(gen,rules):
	new_gen = []
#corrects for non-existent edges
	new_gen.append(useRules(rules,(OFF,gen[0],gen[1])))
	for i in range(len(gen)-2):
		new_gen.append(useRules(rules,(gen[i],gen[i+1],gen[i+2])))
#corrects ....	
	new_gen.append(useRules(rules,(gen[-2],gen[-1],OFF)))
	return new_gen

def make(size):
	return [OFF] * (size // 2) + [ON] + [OFF] * (size // 2)

def defineMake(n,size = 40):
	print 'enter some string of 1\'s and 0\'s\nEX:010110111'
	print 'this will make the board!'
	check = True
	while check:
		pattern = raw_input()
		if re.search('[^'+str(n)+']',pattern):
				print 'try again! bad input! Only char in ' + str(n) + ' are valid!'
				break
		else:
			check = False
	if len(pattern) < size:
		pattern = pattern * (size//len(pattern) + 1)
		pattern = pattern[:size]
	elif len(pattern) > size:
		pattern = pattern[:size]

	pattern = map(convSym,map(int,pattern))
	return pattern



if __name__ == '__main__':
  argc = len(sys.argv)

  if argc == 1:
    oneD()
  else:
    oneD(int(sys.argv[1]))

