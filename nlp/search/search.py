import glob



#def main():

invertedIndex = {}

#get name of txt files in folder
textFiles = glob.glob('*.txt')

for filename in textFiles:
	f = open(filename,'r')
	s = f.read()
	s = s.split()
	for word in s:
		if word not in invertedIndex:
			invertedIndex[word] = [filename]
		elif filename not in invertedIndex[word]:
			invertedIndex[word] += [filename]
	f.close()


#for each word in file,
#add to dictionary {word:[name.txt]}


print invertedIndex

print "What word would you like to search for?"
lookFor = raw_input()
if lookFor in invertedIndex:
	print invertedIndex[lookFor]
else: print "not found!"

print inter(invertedIndex['hey'],invertedIndex['this'])

def inter(a,b):
	return list(set(a) & set(b))


