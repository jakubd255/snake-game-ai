from core import config
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

    def reset(self, snake):
        self.position = generate_position(snake)