sieve :: [Int] -> [Int]
sieve (x:xs) = x : (sieve $ filter (\n -> n `mod` x /= 0) xs)
sieve []     = []

main :: IO ()
main = print $ takeWhile (< 500) (sieve [2..])
