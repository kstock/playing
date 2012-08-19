{-
Find the largest palindrome made from the product of two 3-digit numbers.
http://projecteuler.net/problem=4

NOTES:
This is really slow, I should redo it someday!

I found the [900..999] through binary searching through the input space
-}

{-
make array of all combos of 3 digit mults

reverse array

find first palindrome 

only works if you go from high num to high num,
  prob some problem with lazy eval?
-}

maxPalin = head $ filter (isPalin) (reverse (multArray [900..999] [900..999]))


--mistake, algo prob : (
multArray a b = if b == [] then []
                  else if a == [] then []
                  else (map (*(head a)) b) ++ (multArray (tail a) b)

isPalin a = if show a == reverse (show a) then True else False



