# Параметры игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
GAME_SPEED = 20
FILENAME = "best_score.txt"

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Параметры нейронной сети
MEMORY_SIZE = 100000  # Размер памяти для повторного воспроизведения
INITIAL_EPSILON = 1  # Начальное значение epsilon
GAMMA = 0.95  # Фактор дисконтирования
BATCH_SIZE = 500  # Размер пакета для обучения
MIN_EPSILON = 0.01  # Минимальное значение epsilon
EPSILON_DECAY = 0.995  # Скорость уменьшения epsilon
LEARNING_RATE = 0.00025  # Скорость обучения
LAYER_SIZES = [128, 128, 128]  # Размеры скрытых слоев нейронной сети
SENSORS = 12  # Количество сенсоров (входных параметров для нейронной сети)
