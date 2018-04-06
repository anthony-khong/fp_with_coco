#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x3a4d370d

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
import pandas as pd

from pipeline import fit_transform
from features import fmatrix
from features import one_hot_encoder
from features import one_hot_encoder_with_max_bins

def test_one_hot_encoder():
    df = pd.DataFrame({'some_id': [1, 2, 2, 1]})
    estimator = one_hot_encoder('some_id')
    feats = fmatrix(fit_transform(estimator, df))
    expected_feats = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])
    assert np.allclose(feats, expected_feats), 'One-hot encoding incorrect'

def test_one_hot_encoder_with_max_bins():
    df = pd.DataFrame({'some_id': [1, 2, 3, 1, 2, 3], 'some_weights': [1, 2, 3, 4, 5, 6]})

    estimator = one_hot_encoder_with_max_bins('some_id', 'some_weights', max_bins=3)
    feats = fmatrix(fit_transform(estimator, df))
    expected_feats = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert np.allclose(feats, expected_feats), 'One-hot encoding with max bins incorrect'

    estimator = one_hot_encoder_with_max_bins('some_id', 'some_weights', max_bins=2)
    feats = fmatrix(fit_transform(estimator, df))
    expected_feats = np.array([[0, 0], [1, 0], [0, 1], [0, 0], [1, 0], [0, 1]])
    assert np.allclose(feats, expected_feats), 'One-hot encoding with max bins incorrect'

    estimator = one_hot_encoder_with_max_bins('some_id', 'some_weights', max_bins=1)
    feats = fmatrix(fit_transform(estimator, df))
    expected_feats = np.array([[0], [0], [1], [0], [0], [1]])
    assert np.allclose(feats, expected_feats), 'One-hot encoding with max bins incorrect'
