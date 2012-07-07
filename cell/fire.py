#"Fire" cellular automata
#idea based on http://nifty.stanford.edu/2007/shiflet-fire/
#
#USAGE:
# python fire.py [probabilty_catch_fire [#rows [#cols]]]
# default: python fire.py .5 9 18
#
# python fire.py help //print above usage message
#
#
#NOTE:
#Doesn't halt for some bad size inputs (e.g, rows = 100, col = 1)
#

import random
from copy import deepcopy
import time,os,sys

TREE = 'T'
BURN = '~'
EMPTY = ' '

def fire(probCatch = .5, n = 9, m = 18):
	forest = make(n,m)
	disp(forest)
	count = 1
	while still(forest):
		forest = update(forest,probCatch)
		print "\n day " + str(count) + "\n"
		time.sleep(1)
		os.system('clear')		
		disp(forest)
		count += 1

def still(forest):
	for i in forest:
		if BURN in i:
			return True
	print "\n The fire died!\n"
	count = 0
	for row in forest:
		for col in row:
			if col == TREE:
				count += 1
	print "There are " + str(count) +" trees left!"
	return False

def update(forest,probCatch):
	gen = deepcopy(forest)
	f = forest
	for i in range(1,len(forest) -1):
		for j in range(1,len(forest[0]) - 1):
			if f[i][j] == BURN:
				gen[i][j] = EMPTY
			elif f[i][j] == EMPTY:
				gen[i][j] = EMPTY
			elif f[i][j] == TREE and True in map(burn,
					 [ f[i-1][j],f[i+1][j],f[i][j-1],f[i][j+1]]
					 ) and probCatch > random.random()     :
					 gen[i][j] = BURN
			else:
				gen[i][j] = TREE
	return gen

def burn(n):
	return n == BURN

def make(n = 9,m = 18):
	forest = []
	for i in range(n):
		tmp = [TREE] * m
		forest.extend([tmp])

#top empty
	for i in range(len(forest[0])):
		forest[0][i] = EMPTY
#bottom empty
	for i in range(len(forest[0])):
		forest[-1][i] = EMPTY
#left empty
	for i in range(len(forest)):
		forest[i][0] = EMPTY
#right empty
	for i in range(len(forest)):
		forest[i][-1] = EMPTY
#middle on fire
	forest[len(forest)//2][
					len(forest[0])//2] = BURN
	return forest

def disp(forest):

	print ' ' + '_' * len(forest[0])
	 
	for i in range(len(forest)):
		print '|' + ''.join(map(str,forest[i])) + '|'

	print ' ' + '_' * len(forest[0])

if __name__ == '__main__':
  argc = len(sys.argv)

  if argc == 1:
    fire()
  elif argc >= 2:
    if sys.argv[1] == 'help':
      print "usage:"
      print "python fire.py [probabilty_catch_fire [#rows [#cols]]]"
      print "default: python fire.py .5 9 18"
    elif argc >= 4:
      fire( float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    elif argc == 3:
      fire( float(sys.argv[1]), int(sys.argv[2]) )
    else:
      fire(float(sys.argv[1]))
