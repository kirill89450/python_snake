# snake.py

import pygame
import config

class Snake:
    def __init__(self):
        self.snake_list = [[config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2]]
        self.length_of_snake = 1
        self.block_size = config.BLOCK_SIZE
        self.direction = "RIGHT"

    def move(self):
        head = list(self.snake_list[-1])
        if self.direction == "UP":
            head[1] -= self.block_size
        elif self.direction == "DOWN":
            head[1] += self.block_size
        elif self.direction == "LEFT":
            head[0] -= self.block_size
        elif self.direction == "RIGHT":
            head[0] += self.block_size
        self.snake_list.append(head)
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

    def grow(self):
        self.length_of_snake += 1

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def draw(self, display):
        for i, segment in enumerate(self.snake_list):
            x, y = segment[0], segment[1]
            pygame.draw.rect(display, config.GREEN, [x, y, self.block_size, self.block_size])

    def check_collision(self, apple):
        return self.snake_list[-1] == [apple.x, apple.y]

    def check_self_collision(self):
        return self.snake_list[-1] in self.snake_list[:-1]

    def check_boundary_collision(self):
        head_x, head_y = self.snake_list[-1]
        return head_x >= config.SCREEN_WIDTH or head_x < 0 or head_y >= config.SCREEN_HEIGHT or head_y < 0
