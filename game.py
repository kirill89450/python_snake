# game.py

import pygame
import config
from snake import Snake
from apple import Apple
from agent import Agent


class Game:
    def __init__(self, display, menu):
        self.display = display
        self.menu    = menu
        self.clock   = pygame.time.Clock()
        self.snake   = Snake()
        self.apple   = Apple()
        self.agent   = Agent()

    def get_state(self):
        # Получаем текущее состояние игры
        # Здесь можно вернуть информацию о положении змейки, яблока и других важных параметрах

        # В качестве примера, мы можем возвращать расстояние между головой змеи и яблоком
        head_x, head_y = self.snake.snake_list[-1]
        apple_x, apple_y = self.apple.x, self.apple.y
        distance_to_apple = abs(head_x - apple_x) + abs(head_y - apple_y)

        # Также можно вернуть другие важные параметры игры, которые могут помочь агенту принимать решения
        return [distance_to_apple]  # Возвращаем список с одним параметром в качестве примера

    def execute_action(self, action):
        # Выполняем действие в игре на основе выбранного агентом действия
        if action == 0:
            self.snake.change_direction("UP")
        elif action == 1:
            self.snake.change_direction("DOWN")
        elif action == 2:
            self.snake.change_direction("LEFT")
        elif action == 3:
            self.snake.change_direction("RIGHT")

    def calculate_reward(self):
        # Вычисляем награду в зависимости от состояния игры
        reward = 0

        if self.snake.check_collision(self.apple):
            reward += 10  # Если змея съела яблоко, добавляем 10 к награде
        else:
            # В противном случае, можно награждать за приближение к яблоку и наказывать за удаление от него
            head_x, head_y = self.snake.snake_list[-1]
            apple_x, apple_y = self.apple.x, self.apple.y
            prev_distance_to_apple = self.get_state()[0]  # Получаем предыдущее расстояние до яблока
            distance_to_apple = abs(head_x - apple_x) + abs(head_y - apple_y)

            if distance_to_apple < prev_distance_to_apple:
                reward += 1  # Если змея приблизилась к яблоку, добавляем 1 к награде
            elif distance_to_apple > prev_distance_to_apple:
                reward -= 1  # Если змея отдалилась от яблока, вычитаем 1 из награды

        return reward

    def run_game(self):
        game_over = False

        while not game_over:
            state = self.get_state()  # Получаем текущее состояние игры
            action = self.agent.act(state)  # Получаем действие от агента
            self.execute_action(action)  # Выполняем действие
            self.snake.move()

            if self.snake.check_collision(self.apple):
                self.snake.grow()
                self.apple.respawn()

            if self.snake.check_self_collision() or self.snake.check_boundary_collision():
                game_over = True

            self.display.fill(config.BLACK)
            self.snake.draw(self.display)
            self.apple.draw(self.display)
            pygame.display.update()
            self.clock.tick(config.GAME_SPEED)

            next_state = self.get_state()  # Получаем следующее состояние игры
            reward = self.calculate_reward()  # Вычисляем награду
            done = game_over  # Флаг окончания игры
            self.agent.remember(state, action, reward, next_state, done)  # Сохраняем опыт агента
            self.agent.replay()  # Обучаем агента на опыте

        self.menu.save_best_score(self.snake.length_of_snake - 1)
        self.menu.show_menu()
