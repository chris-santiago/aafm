from typing import Tuple

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model


class Autoencoder(Model):
    def __init__(self, nodes: int):
        super().__init__()
        self.nodes = nodes
        self.encoder = tf.keras.Sequential([
            layers.Dense(self.nodes, activation='relu'),

        ])
        self.decoder = tf.keras.Sequential([
            layers.Dense(75, activation='sigmoid')
        ])

    def call(self, inputs, training=None, mask=None):
        return self.decoder(self.encoder(inputs))
