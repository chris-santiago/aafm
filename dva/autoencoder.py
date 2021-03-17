import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model


class Autoencoder(Model):
    def __init__(self, compressed_dim):
        super().__init__()
        self.n_dim = compressed_dim
        self.encoder = tf.keras.Sequential([
            layers.InputLayer(input_shape=(64,)),
            layers.Dense(32, activation='relu'),
            layers.Dense(self.n_dim, activation='relu')
        ])
        self.decoder = tf.keras.Sequential([
            layers.Dense(32, activation='relu'),
            layers.Dense(64, activation='sigmoid')
        ])

    def call(self, inputs, training=None, mask=None):
        return self.decoder(self.encoder(inputs))
