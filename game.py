import pygame
import config
from event_handler import EventHandler
from snake import Snake
from food import Food
from fonts import Fonts
from timer import Timer


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.events = EventHandler(self)
        self.screen = pygame.display.set_mode([config.WINDOW_SIZE]*2, flags=pygame.SCALED, vsync=1)
        self.timer = Timer()
        self.score = 0
        self.is_game_over = False
        self.game_over_message = ""
        self.snake = Snake()
        self.food = Food(self.snake)
    
    def draw_grid(self):
        for x in range(0, config.WINDOW_SIZE, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (x, 0), (x, config.WINDOW_SIZE))        
        for y in range(0, config.WINDOW_SIZE, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (0, y), (config.WINDOW_SIZE, y))

    def draw(self):
        self.screen.fill(config.BLACK)
        self.draw_grid()
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        Fonts.draw_score(self.screen, self.score)

    def handle_eat_food(self):
        if self.snake.segments[0] == self.food.position:
            self.score+=1
            self.snake.grow()
            self.food.reset(self.snake)
            self.timer.speed_up()

    def game_over(self, message=""):
        self.is_game_over = True
        self.game_over_message = message

    def restart(self):
        self.score = 0
        self.is_game_over = False
        self.game_over_message = ""
        self.snake.reset()
        self.food.reset(self.snake)
        self.timer.reset_speed()

    def update(self):
        if self.timer.is_ready() and not self.is_game_over:
            self.snake.move(self)
            self.handle_eat_food()
        elif self.is_game_over:
            Fonts.draw_game_over(self.screen, self.game_over_message)
        pygame.display.flip()
        self.timer.tick_fps()

    def run(self):
        while True:
            self.events.handle_events()
            self.draw()
            self.update()