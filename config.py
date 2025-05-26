import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 650, 650
FPS = 60

square_size = 30
width_square_size = 10
height_square_size = 20

pos_x = 6
pos_y = 6

COLORS = {
    'I': (0, 240, 240),    # Голубой (циан)
    'O': (240, 240, 0),    # Желтый
    'T': (160, 0, 240),    # Фиолетовый
    'L': (240, 160, 0),    # Оранжевый
    'J': (0, 0, 240),      # Синий
    'S': (0, 240, 0),      # Зеленый
    'Z': (240, 0, 0)       # Красный
}

blocks = {
    'I': [pygame.Rect(square_size * i, square_size * 2, square_size, square_size) for i in range(3, 7)]
}