#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x807906

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
import tensorflow as tf

from pipeline import Estimator
from pipeline import Transformer

@_coconut_tco
def mlp(**network_params):
    return _coconut_tail_call(Estimator, _coconut.functools.partial(fit, network_params))

@_coconut_tco
def fit(network_params, df):
    features = df[[c for c in df if 'feat:' in c]].values.astype('float32')
    targets = df[[c for c in df if 'target:' in c]].values.astype('float32')
    n_features, n_targets = features.shape[1], targets.shape[1]
    feat_tensor = tf.placeholder(tf.float32, shape=[None, n_features])
    target_tensor = tf.placeholder(tf.float32, shape=[None, n_targets])
    pred_tensor = ((tf.sigmoid)(fold(feat_tensor, lambda init, n: tf.layers.dense(init, n), network_params['hidden_units'] + [n_targets])))
    loss = tf.losses.log_loss(target_tensor, pred_tensor)
    train = tf.train.AdamOptimizer().minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    m_size, n_epochs = network_params['minibatch_size'], network_params['n_epochs']
    def minibatch_update(update_ix):
        shuffled_ixs = np.random.choice(np.arange(len(df)), m_size, replace=False)
        feed_dict = {feat_tensor: features[shuffled_ixs], target_tensor: targets[shuffled_ixs]}
        _, loss_value = sess.run((train, loss), feed_dict)
        return loss_value
    for epoch in range(n_epochs):
        n_updates = (int)(len(df) / m_size)
        minibatch_losses = [minibatch_update(update_ix) for update_ix in range(n_updates)]
        mu, sigma = np.mean(minibatch_losses), np.std(minibatch_losses)
        (print)(f'Loss in after {epoch + 1} epochs:\n{mu} +/- {sigma}')
    return _coconut_tail_call(Transformer, _coconut.functools.partial(transform, sess, feat_tensor, pred_tensor))

@_coconut_tco
def transform(sess, feat_tensor, pred_tensor, df):
    features = df[[c for c in df if 'feat:' in c]].values.astype('float32')
    predictions = sess.run(pred_tensor, feed_dict={feat_tensor: features})
    return _coconut_tail_call(df.assign, prediction=predictions)

@_coconut_tco
def fold(init, fn, iterable):
    return _coconut_tail_call(reduce, fn, iterable, init)
