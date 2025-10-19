class Game:
    def __init__(self, snake, food, width, height, wrap_map):
        self.width = width
        self.height = height
        self.snake = snake
        self.food = food
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
        if not (0 <= x < self.width) or not (0 <= y < self.height):
            if self.wrap_map:
                x %= self.width
                y %= self.height
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