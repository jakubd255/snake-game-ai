import pygame
import config
from fonts import Fonts

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_grid(self):
        for x in range(0, config.WINDOW_SIZE, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50] * 3, (x, 0), (x, config.WINDOW_SIZE))
        for y in range(0, config.WINDOW_SIZE, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50] * 3, (0, y), (config.WINDOW_SIZE, y))

    def draw_snake(self, snake):
        for i, cell in enumerate(snake.segments):
            color = config.GREEN_LIGHT if i == 0 else config.GREEN_DARK
            segment = pygame.rect.Rect(cell[0]*config.CELL_SIZE, cell[1]*config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
            pygame.draw.rect(self.screen, color, segment)

    def draw_food(self, food):
        rect = pygame.rect.Rect(food.position[0]*config.CELL_SIZE, food.position[1]*config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(self.screen, config.RED, rect)

    def draw(self, game):
        self.screen.fill(config.BLACK)
        self.draw_grid()
        self.draw_food(game.food)
        self.draw_snake(game.snake)
        Fonts.draw_score(self.screen, game.score)
        if game.is_game_over:
            Fonts.draw_game_over(self.screen, game.game_over_message)