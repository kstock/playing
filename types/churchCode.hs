{-
AUTHOR: Kyle Stock kstock@ucsd.edu
http://en.wikipedia.org/wiki/Church_encoding
based on the exposition in Types And Programming Languages  
-}


tru = \x -> \y -> x --fst
fls = \x -> \y -> y --snd


test b c a = b c a


{-
if b is fls it will return the second arg (fls)
if b is tru it will return c,
c or fls will be evaluated on True False which will
pick match the function to the boolean value
so it will print properly 
-}

cAnd b c = (b c fls)

cOr b c = (b tru c) 

cNeg b = b fls tru

churchToBool lam = lam True False

{-
encodings of pairing, and access

cPair '1' '2' creates a partially applied function
b f s ==> b '1' '2'

calling: cFst (cPair '1' '2') will give you
==> cFst (b '1' '2')
cFst will take a var p and pass tru into it
passing tru into b '1' '2' creates tru '1' '2'
==> '1'
-}

cPair f s b = b f s

cFst p = p tru
cSnd p = p fls

-- Church Numerals
{-

0 := \f -> \x -> x
1 := \f -> \x -> f x
2 := \f -> \x -> f x
.
.
.
n = \f -> \x -> f^n x 

$ churchToInt $ intToChurch 3
==> 3
$ churchToInt c0
==> 0
-}

-- successor function
scc = \n -> \s -> \z -> s (n s z)
{-pluss = \n -> \x -> n scc n-}

c0 = \s -> \z -> z

intToChurch n = foldr (.) id (replicate n scc) c0

-- converts church number to an int!
churchToInt n =  n (+1) 0


isZero = \x -> (x cNeg tru)
isEven = \x -> x (\x ->fls) tru
isOdd = \x -> cNeg $ x fls tru

{-
 - Y combinator
 -}

{-yC = \f -> (\x -> f (x x)) (\x -> f (x x ))-}

