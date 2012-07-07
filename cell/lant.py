#  http://en.wikipedia.org/wiki/Langtons_ant
#

#USAGE:
#usage: (all args optional)
#python lant.py speed #ants dies? '(xpos,ypos)'
#default: speed = .5,num = 1,die = True,pos = (1,1)
#
#python lant help
#   to display usage!

#NOTE:
#early program, don't like all the globals!!!
#probably has (unintentional) bugs
#
#lotsa messy stuff, this one is fun.
#hopefully I'll clean it up more someday!!


import time,os,sys



WHITE = ' '
BLACK = '@'
ANT = 'A'

UP = (0,1)
DOWN = (0,-1)
RIGHT = (1,0)
LEFT = (-1,0)

size = 9

#rotate 90 right at white squares
white = {UP:RIGHT,RIGHT:DOWN,DOWN:LEFT,LEFT:UP}
#rotate 90 left at black squares
black = {UP:LEFT,LEFT:DOWN,DOWN:RIGHT,RIGHT:UP}
rot = [white,black]
terr = [
						[WHITE] *size,
						[WHITE] *size,
						[WHITE] *size,
						[WHITE] *size,
						[WHITE] *size,

						[WHITE] *size,
						[WHITE] *size,
						[WHITE] *size,
						[WHITE] *size ]

class lants:
	ants = []

	def __init__(self,pos = (4,4),territory = terr):
		self.pos = pos
		self.move = RIGHT
		self.color = self.getColor(territory)
		x,y = pos
		territory[x][y] = ANT
		lants.ants.append(self)

	def getColor(self,territory = terr):
		while 1:
			x,y = self.pos
			try:
				if territory[x][y] == WHITE:
					return 0
				else:
					return 1
			except IndexError:
				self.pos = 4,5

	def display(self,pos,territory = terr):
		x,y = self.pos
		territory[x][y] = ANT

	def travel(self):
		x,y = self.pos
		i,j = self.move
		try:
			self.pos = (x+i,y+j)
		except IndexError:
			sef.pos = 4,5	

	def update(self, territory = terr):
		flip(self.pos,self.color,territory)
		self.move = rot[self.color][self.move]
		self.travel()
		self.color = self.getColor(territory)
		self.display(self.pos,territory)

		
	


def ant(speed = .5,num = 1,die = True,pos = (1,1)):
	size = 10
	terre = make()
	ants = []
	if num > 5:
		num = 5

	for i in range(num):
		lants((4,i*2+1))

	print "\n \n"
#	print ant1.color
	while 1:
		print "\n"
		os.system('clear')		
		disp(terr)
		for i in lants.ants:
			i.update()	
		leave()
		print "\n"
		time.sleep(speed)


def leave():
	count = 0
	gonnadie = []
	for i in range(len(lants.ants)):
		for j in range(1,len(lants.ants)):
			if lants.ants[i].pos == lants.ants[j].pos:
				if i not in gonnadie:
					count += 1
					gonnadie.append(i)
				if j not in gonnadie:
					count += 1
					gonnadie.append(j)

	gonnadie.sort()
	gonnadie.reverse()

	for i in gonnadie:
		del lants.ants[i]
	if count != 0:
		print str(count) + " ants crashed and died!\n"




def flip(pos,color,territory = terr):
	x,y = pos
	if color == 0:
		territory[x][y] = BLACK
	else:
		territory[x][y] = WHITE

def make(n = 9,m = 9):
	forest = []
	for i in range(n):
		tmp = [WHITE] * m
		forest.extend([tmp])
	return forest

def disp(forest):
	for i in range(len(forest)):
		print ''.join(map(str,forest[i]))




if __name__ == '__main__':
  argc = len(sys.argv)

  if argc == 1:
    ant()
  elif argc >= 2:
    if sys.argv[1] == 'help':
      print "usage: (all args optional)"
      print "python lant.py speed #ants dies? '(xpos,ypos)'"
      print "default: speed = .5,num = 1,die = True,pos = (1,1)"
    elif argc >= 5:
      ant( float(sys.argv[1]), int(sys.argv[2]),
              eval(sys.argv[3]),eval(sys.argv[4]))
    elif argc == 4:
      ant( float(sys.argv[1]), int(sys.argv[2]),
              eval(sys.argv[3]),)
    elif argc == 3:
      ant( float(sys.argv[1]), int(sys.argv[2]) )
    elif argc == 2:
      ant( float(sys.argv[1]) )
    else:
      ant()
