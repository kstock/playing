#http://en.wikipedia.org/wiki/Ulam_spiral
#old learning era code! but fun so I share!

#TODO: 
# fix command line args! 
#
# improve display!
#   fix spacing issues

def ulam(size = 7,dot = False):
	row = size
	col = size

	board = [ ['0']*row for i in range(col)]
	prim = prime_numbers_less_than(row * col)

	num = row * col
	cur_col = col 
	cur_row = row - 1

	i = -1
	while i != 1:
#left
		for i in range(num,num - col,-1):
#		print 'num = ' + str(num)
			cur_col -= 1
			board[cur_row][cur_col] = i
			if i == 1:
				print 'break'
				break

		if i == 1:
			break

		
#set num to next number to be placed
		num = i - 1
		print 'h'
		row -= 1	
#up
		for i in range(num,num - row,-1):
#		print 'cur_col = ' + str(cur_col)
#		print 'num = ' + str(num)
			cur_row -= 1
			board[cur_row][cur_col] = i
			if i == 1:
				print 'break'
				break


		if i == 1:
			break
		
		num = i - 1
		col -= 1

#right
		for i in range(num,num - col,-1):
			cur_col += 1
			board[cur_row][cur_col] = i
			if i == 1:
				print 'break'
				break

		num = i -1
		row -= 1

		if i == 1:
			break

#down
		for i in range(num,num - row,-1):
			cur_row += 1
			board[cur_row][cur_col] = i
			if i == 1:
				print 'break'
				break

		if i == 1:
			break

		num = i-1
		col -=1

	if dot == True:
#display primes as stars
		for ro in range(len(board)):
			for co in range(len(board[0])):
				board[ro][co] = dotDisp(board[ro][co],prim)
	else:
#display numbers
		for ro in range(len(board)):
			for co in range(len(board[0])):
				board[ro][co] = testPrim(board[ro][co],prim,size*size)

	print len(board)
	for i in board:
		print ''.join(i)

def dotDisp(item,listPrimes):
	if item in listPrimes:
		return '.'
	else:
		return ' '

def testPrim(item,listPrimes,size):
	if item in listPrimes:
		return str2(str(item),size)
	else:
		return str2('',size) 

def str2(num,size):
	if len(num) < len(str(size)):
		#fillerSize = (size - len(num))//2
		return ' '*(len(str(size)) - len(num)) + num
	else:
		return str(num)



def prime_numbers_less_than(N):
    if N <= 3:
        return range(2,N)

    primes = [2] +  range(3,N,2)

    index = 1
    max = N ** 0.5
    while 1:
        i = primes[index]
        if i>max:
            break
        index += 1
        primes = [x for x in primes if (x % i) or (x == i)]
    return primes

if __name__ == '__main__':
	 
  import sys
  if len(sys.argv) < 2:
	  ulam()
  elif len(sys.argv) < 3:
		ulam(int(sys.argv[1]))
  else:
		ulam(bool(sys.argv[2]))
