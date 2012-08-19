{-
http://projecteuler.net/problem=10
http://projecteuler.net/problem=10
-}
{-
steal efficient prime # generator

get array of all primes <2 million

sum array
-}

ans = sum $ takeWhile (<2000000) primes

primes = 2: 3: sieve (tail primes) 3 []
   where
    notDivsBy d n     = n `mod` d /= 0
    sieve (p:ps) x ds = foldr (filter . notDivsBy) 
                                [x+2,x+4..p*p-2] ds
                        ++ sieve ps (p*p) (p:ds)



