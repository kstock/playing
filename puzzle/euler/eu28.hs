{-
http://projecteuler.net/problem=28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

my solution: spiral function computes the outer corners of a length n square.
sum all the square for each inner square

-}


spiral 1 = 1
spiral n = n2 + (n2 - step) +  (n2 - 2*step) +  (n2 - 3* step)  
          where n2 = n * n
                step = n - 1


ans = sum $ map spiral [1,3..1001]
