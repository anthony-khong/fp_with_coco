def sieve(numbers):
    head = next(numbers)
    yield head
    yield from sieve(filter(lambda n: n % head != 0, numbers))

if __name__ == '__main__':
    from itertools import count, islice
    print(list(islice(sieve(count(2)), 500)))
