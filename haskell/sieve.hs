main = print $ take 500 (sieve [2..])

sieve :: [Int] -> [Int]
sieve (x:xs) = x : (sieve $ filter (\n -> n `mod` x /= 0) xs)
