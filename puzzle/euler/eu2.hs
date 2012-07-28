{-
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.

http://projecteuler.net/problem=2
-}

fibs = scanl (+) 0 (1:fibs)

ans = foldl (addIfEven) 0 (takeWhile (<4000000) fibs)

addIfEven total n | n `mod` 2 == 0 = total+ n 
                  | otherwise = total
