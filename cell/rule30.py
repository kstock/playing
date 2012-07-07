#http://en.wikipedia.org/wiki/Rule_30

#USAGE:
#python rule30.py [size]


OFF = ' '
ON = '*'
import time,sys
def rule30(size = 40):

	rules = {(ON,ON,ON):OFF,(ON,ON,OFF):OFF,(ON,OFF,ON):OFF,(ON,OFF,OFF):ON,
						(OFF,ON,ON):ON,(OFF,ON,OFF):ON,(OFF,OFF,ON):ON,(OFF,OFF,OFF):OFF}

	gen = make(size)

	print ''.join(map(str,gen))
	for i in range(size//2):
		gen = update(gen,rules)
		time.sleep(1)
		print ''.join(map(str,gen))

def update(gen,rules):
	new_gen = []
#corrects for non-existent edges
	new_gen.append(rules[(OFF,gen[0],gen[1])])
	for i in range(len(gen)-2):
		new_gen.append(rules[(gen[i],gen[i+1],gen[i+2])])
#corrects ....	
	new_gen.append(rules[(gen[-2],gen[-1],OFF)])
	return new_gen

def make(size):
	return [OFF] * (size // 2) + [ON] + [OFF] * (size // 2)

if __name__ == '__main__':
  argc = len(sys.argv)

  if argc == 1:
    rule30()
  else:
    rule30(int(sys.argv[1]))
