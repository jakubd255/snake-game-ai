from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.score = 0
        self.is_game_over = False
        self.game_over_message = ""

    def handle_eat_food(self):
        if self.snake.segments[0] == self.food.position:
            self.score+=1
            self.snake.grow()
            self.food.reset(self.snake)
            return True
        else:
            return False

    def game_over(self, message=""):
        self.is_game_over = True
        self.game_over_message = message

    def restart(self):
        self.score = 0
        self.is_game_over = False
        self.game_over_message = ""
        self.snake.reset()
        self.food.reset(self.snake)

    def update(self):
        if self.is_game_over:
            return False
        self.snake.move(self)
        return self.handle_eat_food()