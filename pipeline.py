#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x51eb7650

# Compiled with Coconut version 1.3.1 [Dead Parrot]

'''
Pipeline Type Tetris
--------------------

Estimator = DataFrame -> Transformer
Transformer = DataFrame -> DataFrame
PipelineStage = Estimator | Transformer

fit :: PipelineStage -> DataFrame -> Transformer
transform :: Transformer -> DataFrame -> DataFrame
fit_transform :: PipelineStage -> DataFrame -> DataFrame
pipeline :: [PipelineStage] -> PipelineStage
'''

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



class Estimator(_coconut.collections.namedtuple("Estimator", "fit_fn")):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
class Transformer(_coconut.collections.namedtuple("Transformer", "transform_fn")):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

@_coconut_tco
def fit(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "df" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], Estimator)) and (_coconut.len(_coconut_match_to_args[0]) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("df")
        fit_fn = _coconut_match_to_args[0][0]
        if not _coconut_match_to_kwargs:
            df = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def fit(Estimator(fit_fn), df) = fit_fn(copy(df))'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def fit(Estimator(fit_fn), df) = fit_fn(copy(df))'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(fit_fn, copy(df))

@addpattern(fit)
@_coconut_tco
def fit(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut.isinstance(_coconut_match_to_args[0], Transformer)) and (_coconut.len(_coconut_match_to_args[0]) == 1):
        transform_fn = _coconut_match_to_args[0][0]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def fit(Transformer(transform_fn), _) = Transformer(transform_fn)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def fit(Transformer(transform_fn), _) = Transformer(transform_fn)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(Transformer, transform_fn)

@_coconut_tco
def transform(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "df" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], Transformer)) and (_coconut.len(_coconut_match_to_args[0]) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("df")
        transform_fn = _coconut_match_to_args[0][0]
        if not _coconut_match_to_kwargs:
            df = _coconut_match_temp_0
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def transform(Transformer(transform_fn), df) = transform_fn(copy(df))'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def transform(Transformer(transform_fn), df) = transform_fn(copy(df))'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(transform_fn, copy(df))

@_coconut_tco
def fit_transform(stage, df):
    return _coconut_tail_call(transform, fit(stage, df), df)

@_coconut_tco
def mappend(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    _coconut_match_check = False
    if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut.isinstance(_coconut_match_to_args[0], Transformer)) and (_coconut.len(_coconut_match_to_args[0]) == 1) and (_coconut.isinstance(_coconut_match_to_args[1], Transformer)) and (_coconut.len(_coconut_match_to_args[1]) == 1):
        fn0 = _coconut_match_to_args[0][0]
        fn1 = _coconut_match_to_args[1][0]
        if not _coconut_match_to_kwargs:
            _coconut_match_check = True
    if not _coconut_match_check:
        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def mappend(Transformer(fn0), Transformer(fn1)) = Transformer(fn1..fn0)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
        _coconut_match_err.pattern = 'def mappend(Transformer(fn0), Transformer(fn1)) = Transformer(fn1..fn0)'
        _coconut_match_err.value = _coconut_match_to_args
        raise _coconut_match_err

    return _coconut_tail_call(Transformer, _coconut_forward_compose(fn0, fn1))

@addpattern(mappend)
@_coconut_tco
def mappend(stage0, stage1):
    return _coconut_tail_call(Estimator, lambda df: mappend(fit(stage0, df), fit(stage1, df)))

@_coconut_tco
def mconcat(stages):
    return _coconut_tail_call(reduce, mappend, stages)
pipeline = mconcat

def copy(x):
    return x.copy() if hasattr(x, 'copy') else x
