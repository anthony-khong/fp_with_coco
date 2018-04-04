#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe685b395

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

@_coconut_tco
def sieve(numbers):
    x = next(numbers)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (f() for f in (lambda: [x], lambda: sieve(filter(lambda n: n % x != 0, numbers)))))

if __name__ == '__main__':
    from itertools import count
    (print)((list)(_coconut_igetitem((sieve)(count(2)), _coconut.slice(None, 3000))))
