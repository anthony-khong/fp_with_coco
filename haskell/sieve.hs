primes :: [Int]
primes = sieve [2..]
  where
    sieve (x:xs) = x : sieve (filter (\n -> n `rem` x /= 0) xs)
    sieve []     = []

main :: IO ()
main = print $ takeWhile (< 250) primes
