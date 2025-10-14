from enum import Enum
import pygame

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def x(self):
        return self.value[0]

    @property
    def y(self):
        return self.value[1]
    
    def is_opposite(self, other):
        return self.x == -other.x and self.y == -other.y
    
    @staticmethod
    def from_key(key):
        mapping = {
            pygame.K_w: Direction.UP,
            pygame.K_UP: Direction.UP,
            pygame.K_s: Direction.DOWN,
            pygame.K_DOWN: Direction.DOWN,
            pygame.K_a: Direction.LEFT,
            pygame.K_LEFT: Direction.LEFT,
            pygame.K_d: Direction.RIGHT,
            pygame.K_RIGHT: Direction.RIGHT,
        }
        return mapping.get(key)
    
    @staticmethod
    def next_direction(current, key):
        new_dir = Direction.from_key(key)
        if new_dir and not current.is_opposite(new_dir):
            return new_dir
        return current