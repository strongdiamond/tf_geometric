# coding=utf-8
import tensorflow as tf

if tf.__version__[0] == "1":
    tf.enable_eager_execution()

from tf_geometric.data.graph import Graph

import tf_geometric.nn as nn
import tf_geometric.utils as utils
import tf_geometric.data as data
import tf_geometric.datasets as datasets
