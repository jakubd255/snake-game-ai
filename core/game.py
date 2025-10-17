from core import config
from entities.snake import Snake
from entities.food import Food

class Game:
    def __init__(self, wrap_map=config.WRAP_MAP):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.score = 0
        self.is_game_over = False
        self.game_over_message = ""
        self.wrap_map = wrap_map

    def game_over(self, message=""):
        self.is_game_over = True
        self.game_over_message = message

    def handle_eat_food(self):
        if self.snake.segments[0] == self.food.position:
            self.score+=1
            self.snake.grow()
            self.food.reset(self.snake)
            return True
        else:
            return False

    def restart(self):
        self.score = 0
        self.is_game_over = False
        self.game_over_message = ""
        self.snake.reset()
        self.food.reset(self.snake)

    def handle_collision(self):
        x, y = self.snake.get_head()
        if not (0 <= x < config.CELLS_NUMBER) or not (0 <= y < config.CELLS_NUMBER):
            if self.wrap_map:
                x %= config.CELLS_NUMBER
                y %= config.CELLS_NUMBER
                self.snake.set_head([x, y])
            else:
                self.game_over("Snake hit the wall!")
                return
        if [x, y] in self.snake.segments[1:]:
            self.game_over("Snake collided with itself!")

    def update(self):
        if self.is_game_over:
            return False
        self.snake.move()
        self.handle_collision()
        return self.handle_eat_food()