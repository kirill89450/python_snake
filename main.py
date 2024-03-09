import pygame
from config import Config
from snake import Snake
from apple import Apple

pygame.init()

# Создание окна
display = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

def gameLoop():
    game_over = False
    game_close = False

    snake = Snake()
    apple = Apple()

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            display.fill(Config.BLACK)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Ты проиграл! Нажми C чтобы начать заново.", True, Config.RED)
            display.blit(message, [Config.SCREEN_WIDTH / 6, Config.SCREEN_HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")

        snake.move()

        # Првверка на столкновение с яблоком
        if snake.snake_list[-1][0] == apple.x and snake.snake_list[-1][1] == apple.y:
            apple.respawn()
            snake.grow()

        # Проверка столкновения с собой
        for segment in snake.snake_list[:-1]:
            if segment == snake.snake_list[-1]:
                game_close = True

        # Проверка столкновения с стеной
        if (snake.snake_list[-1][0] >= Config.SCREEN_WIDTH or snake.snake_list[-1][0] < 0 or
            snake.snake_list[-1][1] >= Config.SCREEN_HEIGHT or snake.snake_list[-1][1] < 0):
            game_close = True

        display.fill(Config.BLACK)
        snake.draw(display)
        apple.draw(display)
        pygame.display.update()
        clock.tick(Config.GAME_SPEED)

    pygame.quit()

gameLoop()
