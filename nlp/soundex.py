import sys
'''
http://en.wikipedia.org/wiki/Soundex
'''

def main(word):
	code = word[0]

#strip vowels
	word = [w for w in word if w not in ['a','e','h','i','o',
	                                         'u','w','y']]

	#replace letters
	for i in range(len(word)):
		if word[i] in ['b','f','p','v']:
			word[i] = 1
		elif word[i] in ['c','g','j','k','q','s','x','z']:
			word[i] = 2
		elif word[i] in ['d','t']:
			word[i] = 3
		elif word[i] == 'l':
			word[i] = 4
		elif word[i] in ['m','n']:
			word[i] = 5
		elif word[i] == 'r':
			word[i] = 6


	for i in range(1,len(word)):
		if str(word[i]) != code[i-1]:
			code += str(word[i])





	print word
	print code

if __name__ == '__main__':
	main(sys.argv[1])
