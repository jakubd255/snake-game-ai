import config
import random

def generate_position():
    x = random.randint(0, config.CELLS_NUMBER-1)
    y = random.randint(0, config.CELLS_NUMBER-1)
    return [x, y]

class Food:
    def __init__(self):
        self.position = generate_position()

    def draw(self, screen, pygame):
        rect = pygame.rect.Rect(self.position[0]*config.CELL_SIZE, self.position[1]*config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, config.RED, rect)

    def reset(self):
        self.position = generate_position()