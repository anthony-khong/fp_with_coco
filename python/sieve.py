def sieve(numbers):
    head = next(numbers)
    yield head
    yield from sieve(filter(lambda x: x % head, numbers))

if __name__ == '__main__':
    from itertools import count, takewhile
    print(list(takewhile(lambda x: x < 500, sieve(count(2)))))
