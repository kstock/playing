#makes a Sierpinski triangle of size nXn 
#built by a cellular automata!!
#http://en.wikipedia.org/wiki/Rule_90
#http://en.wikipedia.org/wiki/Sierpinski_triangle
#
#NOTE:
#really old one

from Tkinter import *
import sys


OFF = ' '
ON = '*'

def main(size = 40):

	rules = {(ON,ON,ON):OFF,(ON,ON,OFF):OFF,(ON,OFF,ON):OFF,(ON,OFF,OFF):ON,
						(OFF,ON,ON):ON,(OFF,ON,OFF):ON,(OFF,OFF,ON):ON,(OFF,OFF,OFF):OFF}

	gen = make(size)
	
	root = Tk()

	c = Canvas(root,width=400,height=600)
	c.pack()

	x1 = 0
	y1 = 0

	for i in range(len(gen)):
		if gen[i] == ON:
			c.create_rectangle( (x1,y1,x1 + 10,y1 + 10),fill='red')
		else:
			c.create_rectangle( (x1,y1,x1 + 10,y1 + 10),fill='black')
		x1+=10

	y1 +=10
	x1 = 0


	for i in range(size//2):
		gen = update(gen,rules)
		c.after(300)

#display
		for i in range(len(gen)):
			if gen[i] == ON:
				c.create_rectangle( (x1,y1,x1 + 10,y1 + 10),fill='red')
			else:
				c.create_rectangle( (x1,y1,x1 + 10,y1 + 10),fill='black')
			x1+=10

		y1 += 10
		x1 = 0

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
