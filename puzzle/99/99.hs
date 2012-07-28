import Data.List
--1) (*) Find the last element of a list.

--pattern matching and recursion
myLast (a:[]) = a
myLast (a:b) = myLast b

--using in-built functions
myLast' a = head $ reverse a



--2) (*) Find the last but one element of a list.

myButLast x = head $ tail $ reverse x

--3) (*) Find the K'th element of a list. The first element in the list is number 1.

elemAt (a:_) 1 = a
elemAt (_:as) k = elemAt as (k-1)




--4) (*) Find the number of elements of a list.
myLength xs = foldl (\acc x -> acc + 1) 0 xs

--5) (*) Reverse a list.
rev xs = foldl (\acc x -> x:acc) [] xs

--older ugly solution!
reverse' a = reverse'' a [] 
reverse'' [] b = b
reverse'' (a:as) b = reverse'' as (a:b) 

--6) (*) Find out whether a list is a palindrome. A palindrome can be read forward or backward; e.g. (x a m a x).

isPalindrome x = x == reverse x 


--7) UNSOLVED (**) Flatten a nested list structure.

--flatten x = [ex | ex <- x]


--flatten [x] = x
--flatten (x:xs) = (flatten [x]): [xs]

--8) (**) Eliminate consecutive duplicates of list elements.

compress (x:[]) = [x]
compress (x:y:ys) | x == y = compress (y:ys)
             | otherwise =  (x: compress (y:ys))

--9) (**) Pack consecutive duplicates of list elements into sublists.
--If a list contains repeated elements they should be placed in
--separate sublists.

pack [] = []
pack (x:xs) = run: pack rest
              where run = takeWhile (==x) (x:xs)
                    runLen = length run
                    rest = drop runLen (x:xs)

{- 10)
(*) Run-length encoding of a list. Use the result of problem P09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as lists (N E) where N is the number of duplicates of the element E.
-}


encode x = [(length ex, head ex ) | ex <- pack x]

{-
11) (*) Modified run-length encoding.

Modify the result of problem 10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as (N E) lists.
-}
--turns tuples into lists : /
encodeMod x = map mod ex
              where ex = encode x
                    mod (n,e) | n == 1 = [e]
                              |otherwise = [n,e]




--14) (*) Duplicate the elements of a list.


dupli [] = []
dupli (x:xs) = x:x:dupli xs



--15) (**) Replicate the elements of a list a given number of times.



repli x n = concat $ repli' x n
repli' [] n = []
repli' (x:xs) n = (re x [] n):(repli' xs n)
              where re x xs n | n <= 0 = xs
                              | otherwise = re x (x:xs) (n-1)

-- (**) Drop every N'th element from a list.



dropEvery [] n = []
dropEvery x n = take (n-1) x ++ dropEvery (drop n x) n 


--17) (*) Split a list into two parts; the length of the first part is given.
--Do not use any predefined predicates.

split (x:xs) n =  split' (x:xs) [] n

split' [] acc n = (acc,[])
split' (x:xs) acc 1 =  (acc ++ [x],xs)
split' (x:xs) acc n =  split' xs (acc ++ [x]) (n-1) 


{-
18)
(**) Extract a slice from a list.

Given two indices, i and k, the slice is the list containing the elements between the i'th and k'th element of the original list (both limits included). Start counting the elements with 1.
-}

slice xs i k = take (k-i +1) $ drop (i-1) xs



--19) (**) Rotate a list N places to the left.

rotate x n | n > 0 = (drop n x) ++ take n x
           | n < 0 = (drop (lx + n) x) ++ take (lx + n) x 
           |otherwise = x
           where lx = length x

-- 20) (*) Remove the K'th element from a list.

removeAt k x = (x !! (k-1), take (k-1) x ++ drop (k) x)


-- 21) Insert an element at a given position into a list.


insertAt ch x n  = take (n-1) x ++ ch ++ drop (n-1) x


--22) Create a list containing all integers within a given range.

range i j = [i..j]

range' i j | j == i = [j]
           | otherwise = i: range' (i+1) j



-- 28) Sorting a list of lists according to length of sublists

lsort x  = sortBy (byLen) x

byLen a b | la > lb = GT
          | la < lb = LT
          | otherwise = EQ
          where la = length a
                lb = length b

--31) (**) Determine whether a given integer number is prime.

isPrime n = null [x | x<- [2..(n-1)], n `mod` x == 0 ]


--32) (**) Determine the greatest common divisor of two positive integer numbers. Use Euclid's algorithm.

myGCD a 0 = a
myGCD a b = gcd b (a `mod` b)

--33) (*) Determine whether two positive integer numbers are coprime. Two numbers are coprime if their greatest common divisor equals 1.

coprime a b = 1 == myGCD a b 


totient 1 = 1
totient m = length [r| r <- [1..(m-1)], coprime r m]

{-
lfsort x = [(head ex, length ex)| ex <- group ( sort ( map length x ) )]

byFreq (a,b) (c,d) | a > c = GT
                   | b <  = LT
                   | otherwise = EQ
                   -}

--46)

and2 True b = b
and2 False b = False

nand2 a b = not $ and2 a b

nor2 False False = True
nor2 _ _ = False

or2 False False = False
or2 _ _ = True

xor2 a b | a == b = False
        | otherwise = True

impl2 True False = False
impl2 _ _ = True

table f = [ [a,b, f a b] | a<- [True,False], b <- [True,False]]

equ2 a b = and2 c d
           where (c,d) = ( (impl2 a b), (impl2 b a) )
