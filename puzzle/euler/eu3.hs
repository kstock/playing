{-
What is the largest prime factor of the number 600851475143 ?

http://projecteuler.net/problem=3

Bad running time! should decrease the takeWhile arg to sqrt n
but type system difficulties
-}

ans = filter checkFor (takeWhile (<600851475143) primes)

checkFor a = if 600851475143 `mod` a == 0 then True else False   

primes :: [Integer]
primes = sieve [2..] 
  where sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p > 0]
