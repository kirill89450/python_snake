import pygame
from config import Config

class Snake:
    def __init__(self):
        self.snake_list = [[Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2]]
        self.length_of_snake = 1
        self.block_size = Config.BLOCK_SIZE
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
            pygame.draw.rect(display, Config.GREEN, [x, y, self.block_size, self.block_size])

            # Добавляем глаза и язык к голове змеи
            if i == len(self.snake_list) - 1:
                if self.direction == "UP":
                    pygame.draw.circle(display, Config.BLACK, (x + self.block_size // 4, y + self.block_size // 4), self.block_size // 8)
                    pygame.draw.circle(display, Config.BLACK, (x + 3 * self.block_size // 4, y + self.block_size // 4), self.block_size // 8)
                    pygame.draw.line(display, Config.RED, (x + self.block_size // 2, y - self.block_size // 2), (x + self.block_size // 2, y), 2)
                elif self.direction == "DOWN":
                    pygame.draw.circle(display, Config.BLACK, (x + self.block_size // 4, y + 3 * self.block_size // 4), self.block_size // 8)
                    pygame.draw.circle(display, Config.BLACK, (x + 3 * self.block_size // 4, y + 3 * self.block_size // 4), self.block_size // 8)
                    pygame.draw.line(display, Config.RED, (x + self.block_size // 2, y + self.block_size), (x + self.block_size // 2, y + 3 * self.block_size // 2), 2)
                elif self.direction == "LEFT":
                    pygame.draw.circle(display, Config.BLACK, (x + self.block_size // 4, y + self.block_size // 4), self.block_size // 8)
                    pygame.draw.circle(display, Config.BLACK, (x + self.block_size // 4, y + 3 * self.block_size // 4), self.block_size // 8)
                    pygame.draw.line(display, Config.RED, (x - self.block_size // 2, y + self.block_size // 2), (x, y + self.block_size // 2), 2)
                elif self.direction == "RIGHT":
                    pygame.draw.circle(display, Config.BLACK, (x + 3 * self.block_size // 4, y + self.block_size // 4), self.block_size // 8)
                    pygame.draw.circle(display, Config.BLACK, (x + 3 * self.block_size // 4, y + 3 * self.block_size // 4), self.block_size // 8)
                    pygame.draw.line(display, Config.RED, (x + self.block_size, y + self.block_size // 2), (x + 3 * self.block_size // 2, y + self.block_size // 2), 2)
