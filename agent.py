# agent.py

import numpy as np
import config
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from collections import deque
import random

class Agent:
    def __init__(self):
        self.memory        = deque(maxlen=config.MEMORY_SIZE)
        self.gamma         = config.GAMMA  
        self.epsilon       = config.INITIAL_EPSILON 
        self.epsilon_min   = config.MIN_EPSILON
        self.epsilon_decay = config.EPSILON_DECAY
        self.learning_rate = config.LEARNING_RATE
        self.model         = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(config.LAYER_SIZES[0], input_dim=8, activation='relu'))  # Входной слой
        for layer_size in config.LAYER_SIZES[1:]:
            model.add(Dense(layer_size, activation='relu'))  # Скрытые слои
        model.add(Dense(4, activation='linear'))  # Выходной слой с 4 нейронами (по одному на каждое действие)
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(4)  # Случайное действие
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # Выбор наилучшего действия

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self):
        if len(self.memory) < config.BATCH_SIZE:
            return
        batch = random.sample(self.memory, config.BATCH_SIZE)
        for state, action, reward, next_state, done in batch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
