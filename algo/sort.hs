import Data.List

--quicksort
quickSort [] = []
quickSort (x:xs) = smaller ++ [x] ++ bigger
          where smaller = filter (<x) xs
                bigger = filter (>x) xs

--merge sort
mergeSort (a:[]) = [a]
mergeSort a = merge (mergeSort b) (mergeSort c)
  where
    n = length a `div` 2
    b = take n a
    c = drop n a

merge [] r = r 
merge l [] = l  
merge (l:ls) (r:rs) | l < r = [l] ++ merge ls (r:rs) 
                    | otherwise = [r] ++ merge (l:ls) rs

--selection sort
selSort [] = []
selSort a = minEl:(selSort (delete minEl a))
            where minEl = foldl1 min a











--binary search
binS t [] = -1
binS t l  | (l !! n) > t = binS t (drop (n) l)
          | (l !! n) < t = binS t (take (n-1) l)
          | (l !! n ) == t =n
          |otherwise = -1
          where
            n = length l `div` 2

-- split in halves
--half list [1,2,3]
left a = [b,c]
  where
    n = length a `div` 2
    b = take n a
    c = drop n a
--modified to count inversions
--inversions = mergeSort'
{- 
mergeSort' (a:[]) = [a]
mergeSort' a = merge (mergeSort b) (mergeSort c)
  where
    n = length a `div` 2
    b = take n a
    c = drop n a

--mergeSort (a:as) = merge
--mergeSort a = merge
merge' [] r acc = (r,acc) 
merge' l [] acc = (l,acc)  
merge' (l:ls) (r:rs) acc | l < r = ([l] ++ rest,acc2)
                         | otherwise = ([r] ++ rest',acc2')
                            where 
                              ans = merge ls (r:rs) acc 
                              rest = fst ans
                              acc2 = snd ans + acc
                              ans' = merge (l:ls) rs acc 
                              rest' = fst ans'
                              acc2' = snd ans' + acc
-}
