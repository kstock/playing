{-
http://projecteuler.net/problem=1
Find the sum of all the multiples of 3 or 5 below 1000.

sum {n | n is nat # < 1000 && (n % 3 == 0 || n % 5 == 0)}
-}

--using nice trick, 
-- mult [3,6,9..] is like 3 * [1,2,3..]
-- so sum of mult would be 3 * sum([1,2,3..]
--yay! Constant time!

--div instead of / bc of type system difficulties
sum_i  n = (n * (n + 1)) `div` 2 
sum_mult n = (sum_i (999 `div` n)) * n

ans = sum_mult 5  + (sum_mult 3) - (sum_mult 15)

--solve by filtering the list!s
ans1 = sum (filter divCheck [1..999])
divCheck n | n `mod` 3 == 0 = True
           | n `mod` 5 == 0 = True
           | otherwise = False

--solve with foldl!
addif total n | n `mod` 3 == 0 = total + n
              | n `mod` 5 == 0 = total + n
              | otherwise = total
ans2 = foldl (addif) 0 [1..999]


--solve with simple list comprehension! O(n) 
ans3 = (sum [x | x <- [1..999],x `mod` 3 == 0 || x `mod` 5 == 0]) 




