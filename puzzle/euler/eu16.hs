digits :: Integer -> [Int]
digits = map (read . return) .show

ans = sum $ digits (2^1000)

