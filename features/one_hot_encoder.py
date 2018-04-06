#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x9a70d57

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

import numpy as np

from pipeline import Estimator
from pipeline import Transformer

@_coconut_tco
def one_hot_encoder_with_max_bins(column, weight_column, max_bins):
    return _coconut_tail_call(Estimator, lambda x: Transformer(fit_with_max_bins(x, column, weight_column, max_bins)))

@_coconut_tco
def fit_with_max_bins(df, column, weight_column, max_bins):
    ix_map = map_of_indices(df[column])
    if max_bins >= len(ix_map):
        return _coconut_tail_call(fit, df, column)
    else:
        weights = df[weight_column].values
        f_weights = {f: np.sum(weights[ix]) for f, ix in ix_map.items()}
        w_cutoff = ((list)((sorted)(f_weights.values())))[-(max_bins + 1)]
        selected_factors = [f for f, w in f_weights.items() if w > w_cutoff]
        return lambda x: transform(x, column, selected_factors)

def map_of_indices(values):
    ix_map = {}
    for index, value in enumerate(values):
        if value in ix_map:
            ix_map[value].append(value)
        else:
            ix_map[value] = [index]
    return ix_map

@_coconut_tco
def one_hot_encoder(column):
    return _coconut_tail_call(Estimator, lambda x: Transformer(fit(x, column)))

def fit(df, column):
    factors = np.unique(df[column])
    return lambda x: transform(x, column, factors)

def transform(df, column, factors):
    name = lambda factor: f'feat:{column}_is_{factor}'
    for factor in factors:
        df[name(factor)] = (df[column] == factor).values.astype(float)
    return df
