HEIGHT                = 20      # number of steps vertically from wall to wall of screen
WIDTH                 = 20       # number of steps horizontally from wall to wall of screen
PIXEL_H               = 20*HEIGHT  # pixel height + border on both sides
PIXEL_W               = 20*WIDTH   # pixel width + border on both sides
SLEEP                 = 0.1     # time to wait between steps

GAME_TITLE            = 'Snake'
BG_COLOR              = 'black'


SNAKE_SHAPE           = 'square'
SNAKE_COLOR           = 'green'
SNAKE_START_LOC_H     = 0
SNAKE_START_LOC_V     = 0

APPLE_SHAPE           = 'circle'
APPLE_COLOR           = 'red'

params = {
    'epsilon': 1,
    'gamma': 0.95,
    'batch_size': 500,
    'epsilon_min': 0.01,
    'epsilon_decay': 0.995,
    'learning_rate': 0.00025,
    'layer_sizes': [128, 128, 128]
}
action_space = 4  # сколько возможных действий
state_space = 12  # размер пространства состояний
