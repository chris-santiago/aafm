from typing import Tuple

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model


class Autoencoder(Model):
    def __init__(self, nodes: Tuple[int]):
        super().__init__()
        self.nodes = nodes
        self.encoder = tf.keras.Sequential([
            layers.Dense(self.nodes[0], activation='relu'),
            # layers.Dropout(0.2),
            layers.Dense(self.nodes[1], activation='relu')
        ])
        self.decoder = tf.keras.Sequential([
            layers.Dense(self.nodes[0], activation='relu'),
            # layers.Dropout(0.2),
            layers.Dense(64, activation='sigmoid')
        ])

    def call(self, inputs, training=None, mask=None):
        return self.decoder(self.encoder(inputs))
