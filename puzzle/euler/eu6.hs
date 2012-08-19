{-
http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
-}

--just used closed forms!

sum_to_n n = (n * (n + 1) ) `div` 2

square_of_sum n = en * en
                    where en = sum_to_n n

sum_of_squares n = (n * (n+1) * (2*n + 1)) `div` 6


ans = square_of_sum 100 - sum_of_squares 100
