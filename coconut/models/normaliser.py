#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb5e4efe9

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
def fit(df):
    features = df[[c for c in df if 'feat:' in c]].values.astype('float32')
    means, stds = np.mean(features, axis=0), np.std(features, axis=0)
    return _coconut_tail_call(Transformer, _coconut.functools.partial(transform, means, stds))

@_coconut_tco
def transform(means, stds, df):
    feature_columns = [c for c in df if 'feat:' in c]
    features = df[feature_columns].values.astype('float32')
    normalised = (features - means) / stds
    return _coconut_tail_call(df.assign, **{f: x for f, x in zip(feature_columns, normalised.T)})

normalise_features = Estimator(fit)
