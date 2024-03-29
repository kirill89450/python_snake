import turtle
import random
import time
import math
import gym
from gym import spaces
from gym.utils import seeding
import config

class Snake(gym.Env):

    def __init__(self, human=False, env_info={'state_space': None}):
        super(Snake, self).__init__()

        self.done = False
        self.seed()
        self.reward = 0
        self.action_space = 4
        self.state_space = 12

        self.total, self.maximum = 0, 0
        self.human = human
        self.env_info = env_info

        # Создание окна игры с черным фоном
        self.win = turtle.Screen()
        self.win.title(config.GAME_TITLE)
        self.win.bgcolor(config.BG_COLOR)
        self.win.tracer(0)
        
        # Установка размеров окна игры с дополнительным пространством для текста
        self.win.setup(width=config.PIXEL_W + 32, height=config.PIXEL_H + 64)
        # Добавляем глазки змейке
        self.eye1 = turtle.Turtle()
        self.eye1.shape("circle")
        self.eye1.color("black")
        self.eye1.speed(0)
        self.eye1.penup()
        self.eye1.goto(-10, 10)  # Положение первого глаза
        # Создание змейки
        self.snake = turtle.Turtle()
        self.snake.shape(config.SNAKE_SHAPE)
        self.snake.speed(0)
        self.snake.penup()
        self.snake.color(config.SNAKE_COLOR)
        self.snake.goto(config.SNAKE_START_LOC_H, config.SNAKE_START_LOC_V)
        self.snake.direction = 'stop'
        
        
        # Создание тела змейки
        self.snake_body = []
        self.add_to_body()

        # Создание яблока
        self.apple = turtle.Turtle()
        self.apple.speed(0)
        self.apple.shape(config.APPLE_SHAPE)
        self.apple.color(config.APPLE_COLOR)
        self.apple.penup()
        self.move_apple(first=True)

        # Расстояние между яблоком и змейкой
        self.dist = math.sqrt((self.snake.xcor() - self.apple.xcor())**2 + (self.snake.ycor() - self.apple.ycor())**2)

        # Блок счета
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.color('white')
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 200)  # Устанавливаем блок счета и рекорда над игровым полем

        # Управление
        self.win.listen()
        self.win.onkey(self.go_up, 'Up')
        self.win.onkey(self.go_right, 'Right')
        self.win.onkey(self.go_down, 'Down')
        self.win.onkey(self.go_left, 'Left')


    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def random_coordinates(self):
        apple_x = random.randint(-int(config.WIDTH/2), int(config.WIDTH/2))
        apple_y = random.randint(-int(config.HEIGHT/2), int(config.HEIGHT/2))
        return apple_x, apple_y
    
    def move_snake(self):
        if self.snake.direction == 'stop':
            self.reward = 0
        if self.snake.direction == 'up':
            y = self.snake.ycor()
            self.snake.sety(y + 20)
        if self.snake.direction == 'right':
            x = self.snake.xcor()
            self.snake.setx(x + 20)
        if self.snake.direction == 'down':
            y = self.snake.ycor()
            self.snake.sety(y - 20)
        if self.snake.direction == 'left':
            x = self.snake.xcor()
            self.snake.setx(x - 20)
        
    
    def go_up(self):
        if self.snake.direction != "down":
            self.snake.direction = "up"
    
    
    def go_down(self):
        if self.snake.direction != "up":
            self.snake.direction = "down"
    
    
    def go_right(self):
        if self.snake.direction != "left":
            self.snake.direction = "right"
    
    
    def go_left(self):
        if self.snake.direction != "right":
            self.snake.direction = "left"


    def move_apple(self, first=False):
        if first or self.snake.distance(self.apple) < 20:    
            while True:
                self.apple.x, self.apple.y = self.random_coordinates()
                self.apple.goto(round(self.apple.x*20), round(self.apple.y*20))
                if not self.body_check_apple():
                    break
            if not first:
                self.update_score()
                self.add_to_body()
            first = False
            return True


    def update_score(self):
        self.total += 1
        if self.total >= self.maximum:
            self.maximum = self.total
        self.score.clear()
        self.score.write(f"Текущий: {self.total}   Рекорд: {self.maximum}", align='center', font=('Courier', 18, 'normal'))


    def reset_score(self):
        self.score.clear()
        self.total = 0
        self.score.write(f"Текущий: {self.total}   Рекорд: {self.maximum}", align='center', font=('Courier', 18, 'normal'))
                    

    def add_to_body(self):
        body = turtle.Turtle()
        body.speed(0)
        body.shape('square')
        body.color(config.SNAKE_COLOR)
        body.penup()
        self.snake_body.append(body)
        

    def move_snakebody(self):
        if len(self.snake_body) > 0:
            for index in range(len(self.snake_body)-1, 0, -1):
                x = self.snake_body[index-1].xcor()
                y = self.snake_body[index-1].ycor()
                self.snake_body[index].goto(x, y)

            self.snake_body[0].goto(self.snake.xcor(), self.snake.ycor())
        
    
    def measure_distance(self):
        self.prev_dist = self.dist
        self.dist = math.sqrt((self.snake.xcor()-self.apple.xcor())**2 + (self.snake.ycor()-self.apple.ycor())**2)


    def body_check_snake(self):
        if len(self.snake_body) > 1:
            for body in self.snake_body[1:]:
                if body.distance(self.snake) < 20:
                    self.reset_score()
                    return True     

    def body_check_apple(self):
        if len(self.snake_body) > 0:
            for body in self.snake_body[:]:
                if body.distance(self.apple) < 20:
                    return True

    def wall_check(self):
        if self.snake.xcor() > 200 or self.snake.xcor() < -200 or self.snake.ycor() > 200 or self.snake.ycor() < -200:
            self.reset_score()
            return True
    
    def reset(self):
        if self.human:
            time.sleep(1)
        for body in self.snake_body:
            body.goto(1000, 1000)

        self.snake_body = []
        self.snake.goto(config.SNAKE_START_LOC_H, config.SNAKE_START_LOC_V)
        self.snake.direction = 'stop'
        self.reward = 0
        self.total = 0
        self.done = False

        state = self.get_state()

        return state


    def run_game(self):
        reward_given = False
        self.win.update()
        self.move_snake()
        if self.move_apple():
            self.reward = 10
            reward_given = True
        self.move_snakebody()
        self.measure_distance()
        if self.body_check_snake():
            self.reward = -100
            reward_given = True
            self.done = True
            if self.human:
                self.reset()
        if self.wall_check():
            self.reward = -100
            reward_given = True
            self.done = True
            if self.human:
                self.reset()
        if not reward_given:
            if self.dist < self.prev_dist:
                self.reward = 1
            else:
                self.reward = -1
        # time.sleep(0.1)
        if self.human:
            time.sleep(config.SLEEP)
            state = self.get_state()

    
    # AI agent
    def step(self, action):
        if action == 0:
            self.go_up()
        if action == 1:
            self.go_right()
        if action == 2:
            self.go_down()
        if action == 3:
            self.go_left()
        self.run_game()
        state = self.get_state()
        return state, self.reward, self.done, {}


    def get_state(self):
        # snake coordinates abs
        self.snake.x, self.snake.y = self.snake.xcor()/config.WIDTH, self.snake.ycor()/config.HEIGHT   
        # snake coordinates scaled 0-1
        self.snake.xsc, self.snake.ysc = self.snake.x/config.WIDTH+0.5, self.snake.y/config.HEIGHT+0.5
        # apple coordintes scaled 0-1 
        self.apple.xsc, self.apple.ysc = self.apple.x/config.WIDTH+0.5, self.apple.y/config.HEIGHT+0.5

        # wall check
        if self.snake.y >= config.HEIGHT/2:
            wall_up, wall_down = 1, 0
        elif self.snake.y <= -config.HEIGHT/2:
            wall_up, wall_down = 0, 1
        else:
            wall_up, wall_down = 0, 0
        if self.snake.x >= config.WIDTH/2:
            wall_right, wall_left = 1, 0
        elif self.snake.x <= -config.WIDTH/2:
            wall_right, wall_left = 0, 1
        else:
            wall_right, wall_left = 0, 0

        # body close
        body_up = []
        body_right = []
        body_down = []
        body_left = []
        if len(self.snake_body) > 3:
            for body in self.snake_body[3:]:
                if body.distance(self.snake) == 20:
                    if body.ycor() < self.snake.ycor():
                        body_down.append(1)
                    elif body.ycor() > self.snake.ycor():
                        body_up.append(1)
                    if body.xcor() < self.snake.xcor():
                        body_left.append(1)
                    elif body.xcor() > self.snake.xcor():
                        body_right.append(1)
        
        if len(body_up) > 0: body_up = 1
        else: body_up = 0
        if len(body_right) > 0: body_right = 1
        else: body_right = 0
        if len(body_down) > 0: body_down = 1
        else: body_down = 0
        if len(body_left) > 0: body_left = 1
        else: body_left = 0

        # state: apple_up, apple_right, apple_down, apple_left, obstacle_up, obstacle_right, obstacle_down, obstacle_left, direction_up, direction_right, direction_down, direction_left
        if self.env_info['state_space'] == 'coordinates':
            state = [self.apple.xsc, self.apple.ysc, self.snake.xsc, self.snake.ysc, \
                    int(wall_up or body_up), int(wall_right or body_right), int(wall_down or body_down), int(wall_left or body_left), \
                    int(self.snake.direction == 'up'), int(self.snake.direction == 'right'), int(self.snake.direction == 'down'), int(self.snake.direction == 'left')]
        elif self.env_info['state_space'] == 'no direction':
            state = [int(self.snake.y < self.apple.y), int(self.snake.x < self.apple.x), int(self.snake.y > self.apple.y), int(self.snake.x > self.apple.x), \
                    int(wall_up or body_up), int(wall_right or body_right), int(wall_down or body_down), int(wall_left or body_left), \
                    0, 0, 0, 0]
        elif self.env_info['state_space'] == 'no body knowledge':
            state = [int(self.snake.y < self.apple.y), int(self.snake.x < self.apple.x), int(self.snake.y > self.apple.y), int(self.snake.x > self.apple.x), \
                    wall_up, wall_right, wall_down, wall_left, \
                    int(self.snake.direction == 'up'), int(self.snake.direction == 'right'), int(self.snake.direction == 'down'), int(self.snake.direction == 'left')]
        else:
            state = [int(self.snake.y < self.apple.y), int(self.snake.x < self.apple.x), int(self.snake.y > self.apple.y), int(self.snake.x > self.apple.x), \
                    int(wall_up or body_up), int(wall_right or body_right), int(wall_down or body_down), int(wall_left or body_left), \
                    int(self.snake.direction == 'up'), int(self.snake.direction == 'right'), int(self.snake.direction == 'down'), int(self.snake.direction == 'left')]
            
        # print(state)
        return state

    def bye(self):
        self.win.bye()



if __name__ == '__main__':            
    human = True
    env = Snake(human=human)

    if human:
        while True:
            env.run_game()

    

    



    
