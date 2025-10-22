from entities.direction import Direction

class AIHelper:
    def __init__(self, game):
        self.game = game

    def is_collision_ahead(self, direction):
        x, y = self.game.snake.segments[0]
        x += direction.x
        y += direction.y

        if not (0 <= x < self.game.width) or not (0 <= y < self.game.height):
            return True
        if [x, y] in self.game.snake.segments:
            return True
        return False

    def get_state(self):
        head_x, head_y = self.game.snake.segments[0]
        food_x, food_y = self.game.food.position

        direction_left = self.game.snake.direction == Direction.LEFT
        direction_right = self.game.snake.direction == Direction.RIGHT
        direction_up = self.game.snake.direction == Direction.UP
        direction_down = self.game.snake.direction == Direction.DOWN

        food_left = food_x < head_x
        food_right = food_x > head_x
        food_up = food_y < head_y
        food_down = food_y > head_y

        danger_left = self.is_collision_ahead(Direction.LEFT)
        danger_right = self.is_collision_ahead(Direction.RIGHT)
        danger_up = self.is_collision_ahead(Direction.UP)
        danger_down = self.is_collision_ahead(Direction.DOWN)

        return (
            direction_left, direction_right, direction_up, direction_down,
            food_left, food_right, food_up, food_down,
            danger_left, danger_right, danger_up, danger_down
        )