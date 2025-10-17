from core import config
from entities.direction import Direction

class AIHelper:
    def __init__(self, game):
        self.game = game

    def is_collision_ahead(self, direction):
        x, y = self.game.snake.segments[0]
        x += direction.x
        y += direction.y

        if not (0 <= x < config.CELLS_NUMBER) or not (0 <= y < config.CELLS_NUMBER):
            return 1
        if [x, y] in self.game.snake.segments:
            return 1
        return 0

    def get_state(self):
        head_x, head_y = self.game.snake.segments[0]
        food_x, food_y = self.game.food.position

        #Dangers: straight, left, right
        danger_straight = self.is_collision_ahead(self.game.snake.direction)
        danger_left = self.is_collision_ahead(Direction.get_direction_by_action(self.game.snake.direction, 1))
        danger_right = self.is_collision_ahead(Direction.get_direction_by_action(self.game.snake.direction, 2))

        #Snake direction
        direction_left = self.game.snake.direction == Direction.LEFT
        direction_right = self.game.snake.direction == Direction.RIGHT
        direction_up = self.game.snake.direction == Direction.UP
        direction_down = self.game.snake.direction == Direction.DOWN

        #Food direction
        food_left = 1 if food_x < head_x else 0
        food_right = 1 if food_x > head_x else 0
        food_up = 1 if food_y < head_y else 0
        food_down = 1 if food_y > head_y else 0

        return (
            danger_straight, danger_left, danger_right,
            direction_left, direction_right, direction_up, direction_down,
            food_left, food_right, food_up, food_down
        )