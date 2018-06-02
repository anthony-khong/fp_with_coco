#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2211cf36

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

import pipeline as pipe

@_coconut_tco
def transform(transformer, name, df):
    xformed_df = pipe.transform(transformer, df)
    columns_to_assemble = [col for col in xformed_df if col not in df]
    values = xformed_df[columns_to_assemble].values.tolist()
    return _coconut_tail_call(xformed_df.drop(columns=columns_to_assemble).assign, **{name: values})

@_coconut_tco
def fit(pipeline_stage, name, df):
    transformer = pipe.fit(pipeline_stage, df)
    return _coconut_tail_call((pipe.Transformer), _coconut.functools.partial(transform, transformer, name))

@_coconut_tco
def assembler(pipeline_stage, name):
    return _coconut_tail_call((pipe.Estimator), _coconut.functools.partial(fit, pipeline_stage, name))
