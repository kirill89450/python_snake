# menu.py

import pygame
import config
from game import Game

class Menu:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.SysFont(None, 50)
        self.best_score = self.load_best_score()
        self.menu_loop = True

    def load_best_score(self):
        try:
            with open(config.FILENAME, 'r') as file:
                best_score = int(file.read())
        except FileNotFoundError:
            best_score = 0
        return best_score

    def save_best_score(self, score):
        if score > self.best_score:
            self.best_score = score
            with open(config.FILENAME, 'w') as file:
                file.write(str(score))

    def show_menu(self):
        while self.menu_loop:
            self.display.fill(config.BLACK)
            self.display_menu()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start_game()

    def display_menu(self):
        title_text = self.font.render("Snake Game", True, config.WHITE)
        best_score_text = self.font.render(f"Best Score: {self.best_score}", True, config.WHITE)
        start_text = self.font.render("Press SPACE to Start", True, config.WHITE)

        title_rect = title_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 3))
        best_score_rect = best_score_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        start_rect = start_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 1.5))

        self.display.blit(title_text, title_rect)
        self.display.blit(best_score_text, best_score_rect)
        self.display.blit(start_text, start_rect)

    def start_game(self):
        game = Game(self.display, self)
        game.run_game()
