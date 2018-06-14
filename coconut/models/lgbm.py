#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x283b43de

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

import lightgbm as lgb

from pipeline import Estimator
from pipeline import Transformer

@_coconut_tco
def lgbm(**params):
    return _coconut_tail_call((Estimator), _coconut.functools.partial(fit, params))

@_coconut_tco
def fit(params, df):
    features = df[[c for c in df if 'feat:' in c]].values
    targets = df[[c for c in df if 'target:' in c]].values.flatten()
    lgb_dataset = lgb.Dataset(features, targets)
    gbm = lgb.train(params, lgb_dataset, params.get('num_boost_round', 100))
    return _coconut_tail_call((Transformer), _coconut.functools.partial(transform, gbm))

@_coconut_tco
def transform(gbm, df):
    features = df[[c for c in df if 'feat:' in c]].values
    return _coconut_tail_call(df.assign, prediction=gbm.predict(features))
