import pygame
import config
from ai_helper import AIHelper
from text_renderer import TextRenderer

class Renderer:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.ai_helper = AIHelper(self.game)

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

    def draw(self):
        self.screen.fill(config.BLACK)
        self.draw_grid()
        self.draw_food(self.game.food)
        self.draw_snake(self.game.snake)
        TextRenderer.draw_score(self.screen, self.game.score)
        if self.game.is_game_over:
            TextRenderer.draw_game_over(self.screen, self.game.game_over_message)