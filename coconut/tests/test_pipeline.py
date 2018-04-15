#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x23dfb492

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

import pytest

from pipeline import Estimator
from pipeline import Transformer
from pipeline import fit
from pipeline import transform
from pipeline import fit_transform
from pipeline import mappend
from pipeline import mconcat
from pipeline import parallel_mconcat
from pipeline import MatchError

def test_fit():
    estimator = Estimator(lambda x: Transformer(lambda y: x + y))
    transformer = fit(estimator, 1)
    assert transformer.transform_fn(2) == 3, 'Fit function on Estimator is incorrect.'

    transformer = Transformer(lambda x: x + 1)
    fitted_transformer = fit(transformer, 2)
    assert fitted_transformer.transform_fn(3) == 4, 'Fit function on Transformer incorrect.'

def test_transform():
    with pytest.raises(MatchError):
        transform(Estimator(None), 1)

    transformer = Transformer(lambda x: x * x)
    assert transform(transformer, 5) == 5 * 5, 'Transform function on Transformer incorrect.'

def test_mappend():
    xformer0 = Transformer(lambda x: x + 1)
    xformer1 = Transformer(lambda x: x * x)
    assert mappend(xformer0, xformer1).transform_fn(5) == 36, ('Mappend function on (Transformer, Transformer) incorrect.')
    assert mappend(xformer1, xformer0).transform_fn(5) == 26, ('Mappend function on (Transformer, Transformer) ignores order.')

    estimator0 = Estimator(lambda _: Transformer(lambda x: x + 1))
    assert fit_transform(mappend(estimator0, xformer0), 1) == 3, ('Mappend function on (Estimator, Transformer) incorrect.')
    assert fit_transform(mappend(xformer1, estimator0), 2) == 5, ('Mappend function on (Transformer, Estimator) incorrect.')

    estimator1 = Estimator(lambda _: Transformer(lambda x: x * x * x))
    assert fit_transform(mappend(estimator0, estimator1), 1) == 8, ('Mappend function on (Estimator, Estimator) incorrect.')

def test_mconcat():
    stages = [Transformer(lambda x: x + 1), Estimator(lambda x: Transformer(lambda y: x + y)), Transformer(lambda x: x * x), Estimator(lambda x: Transformer(lambda y: x * y))]
    assert transform(fit(mconcat(stages), 2), 3) == 72, ('Mconcat does not order the stages correctly.')

# These are required because parallel_mconcat cannot handle unpicklable objects
def square(x):
    return x * x
@_coconut_tco
def add_transform(x):
    return _coconut_tail_call(Transformer, _coconut.functools.partial(_coconut.operator.add, x))
@_coconut_tco
def multiply_transform(x):
    return _coconut_tail_call(Transformer, _coconut.functools.partial(_coconut.operator.mul, x))
def test_parallel_mconcat():
    stages = [Transformer(_coconut.functools.partial(_coconut.operator.add, 1)), Estimator(add_transform), Transformer(square), Estimator(multiply_transform)]
    x = transform(fit(parallel_mconcat(stages), 2), 3)
    assert transform(fit(parallel_mconcat(stages), 2), 3) == 72, ('Mconcat does not order the stages correctly.')
