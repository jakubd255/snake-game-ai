import pygame
import config
import random

def is_available(position, snake):
    for segment in snake.segments:
        if segment == position:
            return False
    return True

def generate_position(snake):
    while True:
        x = random.randint(0, config.CELLS_NUMBER - 1)
        y = random.randint(0, config.CELLS_NUMBER - 1)
        position = [x, y]
        if is_available(position, snake):
            return position

class Food:
    def __init__(self, snake):
        self.position = generate_position(snake)

    def draw(self, screen):
        rect = pygame.rect.Rect(self.position[0]*config.CELL_SIZE, self.position[1]*config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, config.RED, rect)

    def reset(self, snake):
        self.position = generate_position(snake)