import random

def is_available(position, snake):
    for segment in snake.segments:
        if segment == position:
            return False
    return True

class Food:
    def __init__(self, snake, width, height):
        self.width = width
        self.height = height
        self.position = self.generate_position(snake)

    def reset(self, snake):
        self.position = self.generate_position(snake)

    def generate_position(self, snake):
        while True:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            position = [x, y]
            if is_available(position, snake):
                return position