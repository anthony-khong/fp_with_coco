#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xdd4b7c9

# Compiled with Coconut version 1.3.1 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

# Original
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve(filter(lambda x: x % head, numbers))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    print(list(takewhile(lambda x: x < 250, primes())))

# Nicer lambdas
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve((n for n in numbers if n % head))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    print(list(takewhile(lambda x: x < 250, primes())))

# Forward Piping
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve((n for n in numbers if n % head))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    (lambda ps: (print)((list)(takewhile(lambda x: x < 250, ps))))(primes())

# Currying
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    def sieve(numbers):
        head = next(numbers)
        yield head
        yield from sieve((n for n in numbers if n % head))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    (print)((list)(takewhile(lambda x: x < 250, primes())))

# Iterator Chaining
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    @_coconut_tco
    def sieve(numbers):
        head = next(numbers)
        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (f() for f in (lambda: [head], lambda: sieve((n for n in numbers if n % head)))))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    (print)((list)(takewhile(lambda x: x < 250, primes())))

# Pattern-matching
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    @_coconut_tco
    def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
            tail = _coconut.iter(_coconut_match_to_args[0])
            _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(tail, _coconut.slice(None, 1)))
            if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):
                head = _coconut_match_temp_0[0]
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def sieve([head] :: tail):'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def sieve([head] :: tail):'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (f() for f in (lambda: [head], lambda: sieve((n for n in tail if n % head)))))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    (print)((list)(takewhile(lambda x: x < 250, primes())))

# Function Assignments
from itertools import count
from itertools import takewhile
@_coconut_tco
def primes():
    @_coconut_tco
    def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
            xs = _coconut.iter(_coconut_match_to_args[0])
            _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
            if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):
                x = _coconut_match_temp_0[0]
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def sieve([x] :: xs) = [x] :: sieve(n for n in xs if n % x)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def sieve([x] :: xs) = [x] :: sieve(n for n in xs if n % x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (f() for f in (lambda: [x], lambda: sieve((n for n in xs if n % x)))))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    (print)((list)(takewhile(lambda x: x < 250, primes())))

# No more imports
@_coconut_tco
def primes():
    @_coconut_tco
    def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
            xs = _coconut.iter(_coconut_match_to_args[0])
            _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
            if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):
                x = _coconut_match_temp_0[0]
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def sieve([x] :: xs) = [x] :: sieve(n for n in xs if n % x)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def sieve([x] :: xs) = [x] :: sieve(n for n in xs if n % x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (f() for f in (lambda: [x], lambda: sieve((n for n in xs if n % x)))))
    return _coconut_tail_call(sieve, count(2))
if __name__ == '__main__':
    (print)((list)(takewhile(lambda x: x < 250, primes())))


# Bonuses
@_coconut_tco
def sieve(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Iterable)):
        xs = _coconut.iter(_coconut_match_to_args[0])
        _coconut_match_temp_0 = _coconut.tuple(_coconut_igetitem(xs, _coconut.slice(None, 1)))
        if (_coconut.len(_coconut_match_temp_0) == 1) and (not _coconut_match_to_kwargs):
            x = _coconut_match_temp_0[0]
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def sieve([x] :: xs) = [x] :: sieve(n for n in xs if n % x)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def sieve([x] :: xs) = [x] :: sieve(n for n in xs if n % x)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (f() for f in (lambda: [x], lambda: sieve((n for n in xs if n % x)))))

if __name__ == '__main__':
    (print)((list)(takewhile(lambda x: x < 500, (sieve)(count(2)))))
