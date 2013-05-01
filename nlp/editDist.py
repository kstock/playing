import sys
'''
http://en.wikipedia.org/wiki/Levenshtein_distance
'''

def editDist(source,target):
#fill up table!
	table = []
	for i in range(len(source)+1):
		tmp = [0] * (len(target)+1)
		table.extend([tmp])

#distance from string to empty string
	for i in range(len(source)+1):
		table[i][0] = i
	for j in range(len(target)+1):
		table[0][j] = j

#stupid hack, correct for getting confused
#when translating pseudo-code that used 1 indexed arrays
	source = ' ' + source
	target = ' ' + target
	for i in range(1,len(source)):
		for j in range(1,len(target)):
#copy or substitution?
			if source[i] == target[j]:
				table[i][j] = table[i-1][j-1]
			else:
				table[i][j] = min(
													table[i-1][j]+ 1, #deletion
													table[i][j-1] +1, #insertion
													table[i-1][j-1] + 1, #substitution
													)


	print '\n'

	for i in table:
		print i

if __name__ == "__main__":
    editDist(sys.argv[1], sys.argv[2])



