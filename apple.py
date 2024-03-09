# apple.py

import pygame
import random
import config

class Apple:
    def __init__(self):
        self.block_size = config.BLOCK_SIZE
        self.x = round(random.randrange(0, config.SCREEN_WIDTH - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, config.SCREEN_HEIGHT - self.block_size) / self.block_size) * self.block_size

    def respawn(self):
        self.x = round(random.randrange(0, config.SCREEN_WIDTH - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, config.SCREEN_HEIGHT - self.block_size) / self.block_size) * self.block_size

    def draw(self, display):
        pygame.draw.rect(display, config.RED, [self.x, self.y, self.block_size, self.block_size])
