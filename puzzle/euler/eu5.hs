ans = head [ x | x <- [lowerBound,lowerBound+2..], all (==0) (map (x `mod`) [1..20])]
                        where lowerBound = 2*3*5*7*11*13*17*19
                        
