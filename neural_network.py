# neural_network.py

import numpy as np
import tensorflow as tf
import random
from collections import deque
import config

class NeuralNetwork:
    def __init__(self):
        self.memory = deque(maxlen=config.MEMORY_SIZE)
        self.model = self.build_model()
        self.epsilon = config.INITIAL_EPSILON
        self.gamma = config.GAMMA
        self.batch_size = config.BATCH_SIZE

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(config.LAYER_SIZES[0], input_shape=(config.SENSORS,), activation='relu'),
            tf.keras.layers.Dense(config.LAYER_SIZES[1], activation='relu'),
            tf.keras.layers.Dense(config.LAYER_SIZES[2], activation='relu'),
            tf.keras.layers.Dense(4, activation='softmax')  # 4 возможных действия
        ])
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=config.LEARNING_RATE))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def choose_action(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.choice(4)  # случайный выбор действия
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])  # выбор действия с наилучшим q-value

    def replay(self):
        if len(self.memory) < self.batch_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > config.MIN_EPSILON:
            self.epsilon *= config.EPSILON_DECAY
