{-
 - fragments of some stuff written while reading 
 - types and programming languages
 -
 - need to clean up sometime
 -
-}
data MyBool = Tru | Fal deriving (Show,Eq)


class UnClass a where
  neg :: a -> a
  myAnd :: a -> a -> a
  myOr :: a -> a -> a
  
  ternary :: a -> a -> a -> a

  myAll :: [a] -> a
  myAny :: [a] -> a


instance UnClass MyBool where
    neg Fal = Tru
    neg Tru = Fal
    
    myAnd Tru b = b
    myAnd _ _ = Fal

    myOr Fal Fal = Fal
    myOr _ _ = Tru

    ternary Tru a b = a
    ternary Fal a b = b
    myAll a = foldl1 (myAnd) a
    myAny a = foldl1 (myOr) a



type Stack = [Int]  
  
pop :: Stack -> (Int,Stack)  
pop (x:xs) = (x,xs)  
  
push :: Int -> Stack -> ((),Stack)  
push a xs = ((),a:xs) 


stackManip :: Stack -> (Int, Stack)  
stackManip stack = let  
    ((),newStack1) = push 3 stack  
    (a ,newStack2) = pop newStack1  
    in pop newStack2  

