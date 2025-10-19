import pygame
from core import config
from ai.ai_helper import AIHelper
from ui.text_renderer import TextRenderer

class Renderer:
    def __init__(self, game):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.game = game
        self.width = self.game.width*config.CELL_SIZE
        self.height = self.game.height*config.CELL_SIZE
        self.screen = pygame.display.set_mode([self.width, self.height], flags=pygame.SCALED, vsync=1)
        self.ai_helper = AIHelper(self.game)

    def draw_grid(self):
        for x in range(0, self.width, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (x, 0), (x, self.height))
        for y in range(0, self.height, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (0, y), (self.width, y))

    def draw_snake(self, snake):
        for i, cell in enumerate(snake.segments):
            color = config.GREEN_LIGHT if i == 0 else config.GREEN_DARK
            segment = pygame.rect.Rect(cell[0] * config.CELL_SIZE, cell[1] * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
            pygame.draw.rect(self.screen, color, segment)

    def draw_food(self, food):
        rect = pygame.rect.Rect(food.position[0] * config.CELL_SIZE, food.position[1] * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(self.screen, config.RED, rect)

    def draw(self):
        self.screen.fill(config.BLACK)
        self.draw_grid()
        self.draw_food(self.game.food)
        self.draw_snake(self.game.snake)
        TextRenderer.draw_score(self.screen, self.game.score)
        if self.game.is_game_over:
            TextRenderer.draw_game_over(self.screen, self.game.game_over_message)