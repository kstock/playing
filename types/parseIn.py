from __future__ import division
import re
#Plmokn

if __name__ == 'main':
	calc()


def calc():
	print "f"
	table = {}
	while 1:
		get = raw_input()
		
		if '=' in get:
			table = assign(get,table)
			print table
		else:
			get = list(get)#string -> list
			print get
			
#replace variables with values:
			for ch in range(len(get)):
				if get[ch] in table:
					get[ch] = str(table[get[ch]])

			get = ''.join(get)
			print "get at .join(get) : " + get
			print evaluate(get)


#shunting-yard algorithm
# http://en.wikipedia.org/wiki/Shunting-yard_algorithm
#infix notation -> RPN (postfix)
# 3 + 4 -> 3 4 +

def sY(tokens):

	tokens = tokens.split()
#numbers go in output
	output = []

#function tokens go on stack
	stack = []
	print tokens

	for token in tokens:

		if re.match('[0-9]+',token):
			output.append(token)
		elif re.match('[-+*/^]',token):
			stack.append(token)
			#while re.match('[-+*/^]',stack[-1]):
			#	output.append(stack.pop())
		elif token == ')':
			stack.append(token)
		elif token == '(':
			top = stack.pop()
			while top != ')':
				output.append(top)
				top = stack.pop()
			stack.pop()
		else:
			print "????? unknown token!!!"

		print "output = " + str(output)
		print "stack = " + str(stack)
		print "tokens = " + str(tokens)

	while stack:
		output.append(stack.pop())

	print output

	








def assign(get,table):
	a = '?'
	if re.match('[^a-zA-z]', get):
		print 'invalid!'
		return table

	key = get.split()[0]
	table[key] = evaluate(get[get.index('=') + 1:])
	return table



def paren(word):
	tmp = re.search('\(.+\)', word)
	if tmp == None:
		return None
	else: 
		tmp = tmp.group()
		tmp = tmp[1:-1]
		print "tmp = "
		print tmp
		return tmp

	








def evaluate(string):
	test = paren(string)

	if test:
		tmp = str(evaluate(test))
		string = re.sub('\(.+\)',tmp,string)

	ans = 0
	st = string.split()
	print "st = "
	print st


	if st[0] == '+':
		ans =  reduce(lambda x,y: x+y,map(float,st[1:]))
	elif st[0] == '-':
		ans =  reduce(lambda x,y: x-y,map(float,st[1:]))
	elif st[0] == '*':
		ans =  reduce(lambda x,y: x*y,map(float,st[1:]))
	elif st[0] == '/':
		ans =  reduce(lambda x,y: x/y,map(float,st[1:]))
	elif st[0] == '^':
		ans =  reduce(lambda x,y: x**y,map(float,st[1:]))	
	elif st[0] == '&':
		ans =  reduce(lambda x,y: x and y,map(toBool,st[1:]))
	elif st[0] == '|':
		ans =  reduce(lambda x,y: x or y,map(toBool,st[1:]))
#	elif len(st[0]) > 1 and st[0][0] == '\\':		
	else:
		ans = map(float,st)[0]

	return ans


def toBool(string):
	if re.match('[tT]|[1-9]',string):
		return 1
	else:
		return 0


