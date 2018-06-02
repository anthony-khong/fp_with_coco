#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xeaf6a071

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

import numpy as np
import pandas as pd

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
    assert transformer.xform_fn(2) == 3, 'Fit function on Estimator is incorrect.'

    transformer = Transformer(lambda x: x + 1)
    fitted_transformer = fit(transformer, 2)
    assert fitted_transformer.xform_fn(3) == 4, 'Fit function on Transformer incorrect.'

def test_transform():
    with pytest.raises(MatchError):
        transform(Estimator(None), 1)

    transformer = Transformer(lambda x: x * x)
    assert transform(transformer, 5) == 5 * 5, 'Transform function on Transformer incorrect.'

def test_mappend():
    xformer0 = Transformer(lambda x: x + 1)
    xformer1 = Transformer(lambda x: x * x)
    assert mappend(xformer0, xformer1).xform_fn(5) == 36, ('Mappend function on (Transformer, Transformer) incorrect.')
    assert mappend(xformer1, xformer0).xform_fn(5) == 26, ('Mappend function on (Transformer, Transformer) ignores order.')

    estimator0 = Estimator(lambda _: Transformer(lambda x: x + 1))
    assert fit_transform(mappend(estimator0, xformer0), 1) == 3, ('Mappend function on (Estimator, Transformer) incorrect.')
    assert fit_transform(mappend(xformer1, estimator0), 2) == 5, ('Mappend function on (Transformer, Estimator) incorrect.')

    estimator1 = Estimator(lambda _: Transformer(lambda x: x * x * x))
    assert fit_transform(mappend(estimator0, estimator1), 1) == 8, ('Mappend function on (Estimator, Estimator) incorrect.')

def test_mconcat():
    stages = [Transformer(lambda x: x + 1), Estimator(lambda x: Transformer(lambda y: x + y)), Transformer(lambda x: x * x), Estimator(lambda x: Transformer(lambda y: x * y))]
    assert transform(fit(mconcat(stages), 2), 3) == 1764, ('Mconcat does not order the stages correctly.')

def test_back_to_back_stages():
    df = pd.DataFrame({'a': [1, 2, 3]})
    transformer = mconcat([Transformer(lambda df: df.assign(b=df.a + 1)), Transformer(lambda df: df.assign(c=df.b + 1))])
    fitted_df = fit_transform(transformer, df)
    assert np.allclose(fitted_df.c, [3, 4, 5]), 'Back to back xform does not work.'

    @_coconut_tco
    def dependent_fit(train_df):
        sum_b = train_df.b.sum()
        return _coconut_tail_call(Transformer, lambda test_df: test_df.assign(c=test_df.a + sum_b))
    estimator = mconcat([Transformer(lambda df: df.assign(b=df.a + 1)), Estimator(dependent_fit)])
    fitted_df = transform(fit(estimator, df), df.assign(a=[-1, -2, -3]))
    assert np.allclose(fitted_df.c, [8, 7, 6]), 'Back to back fit does not work.'
