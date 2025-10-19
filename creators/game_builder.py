from config import defaults
from core.game import Game
from entities.food import Food
from entities.snake import Snake

class GameBuilder:
    def __init__(self):
        self._width = defaults.WIDTH
        self._height = defaults.HEIGHT
        self._wrap_map = defaults.WRAP_MAP

    def width(self, width):
        self._width = width
        return self

    def height(self, height):
        self._height = height
        return self

    def wrap_map(self, wrap_map):
        self._wrap_map = wrap_map
        return self

    def build(self):
        snake = Snake(self._width, self._height)
        food = Food(snake, self._width, self._height)
        return Game(snake, food, self._width, self._height, self._wrap_map)