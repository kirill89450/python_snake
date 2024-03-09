import pygame
import random
from config import Config

class Apple:
    def __init__(self):
        self.block_size = Config.BLOCK_SIZE
        self.x = round(random.randrange(0, Config.SCREEN_WIDTH - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, Config.SCREEN_HEIGHT - self.block_size) / self.block_size) * self.block_size

    def respawn(self):
        self.x = round(random.randrange(0, Config.SCREEN_WIDTH - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, Config.SCREEN_HEIGHT - self.block_size) / self.block_size) * self.block_size

    def draw(self, display):
        pygame.draw.rect(display, Config.RED, [self.x, self.y, self.block_size, self.block_size])
