from itertools import count, takewhile

def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve(filter(lambda x: x % head, numbers))
    return sieve(count(2))

if __name__ == '__main__':
    print(list(takewhile(lambda x: x < 250, primes())))
