'''
http://en.wikipedia.org/wiki/Longest_common_substring_problem
'''
import numpy as np


def comSub(str1,str2):
    m = len(str1) + 1
    n = len(str2) + 1

    table = np.zeros((m,n),dtype=np.int)
    lenBest = 0 #length of the current longest found substring
    ans = set()

    for i in xrange(1,m):
        for j in xrange(1,n):

            print "str1 == " + str1[i-1]  + " str2 = " + str2[j-1]
            print (str(i),str(j))
            if str1[i-1] == str2[j-1]:

                if i == 0 or j == 0:
                    table[i,j] = 1
                else:
                    table[i,j] = table[i-1,j-1] + 1

                print (i,j,table[i,j])
                if table[i,j] > lenBest:
                    lenBest = table[i,j]
                    #longest substring of new best length
                    ans = set( str1[ i-lenBest - 1:i ] )
                    print ans
                elif table[i,j] == lenBest:
                    #add another of best length
                    ans.add( str1[i-lenBest - 1 +1:i])
                    print "added " + str(ans)

    print table
    return ans
