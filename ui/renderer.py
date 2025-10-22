import pygame
from ai.ai_helper import AIHelper
from config import defaults, colors
from ui.text_renderer import TextRenderer

class Renderer:
    def __init__(self, game, caption=defaults.WINDOW_TITLE):
        pygame.init()
        pygame.display.set_caption(caption)
        self.game = game
        self.width = self.game.width*defaults.CELL_SIZE
        self.height = self.game.height*defaults.CELL_SIZE
        self.screen = pygame.display.set_mode([self.width, self.height], flags=pygame.SCALED, vsync=1)
        self.ai_helper = AIHelper(self.game)

    def draw_grid(self):
        for x in range(0, self.width, defaults.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (x, 0), (x, self.height))
        for y in range(0, self.height, defaults.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (0, y), (self.width, y))

    def draw_snake(self, snake):
        for i, cell in enumerate(reversed(snake.segments)):
            color = colors.SNAKE_HEAD if i == len(snake.segments)-1 else colors.SNAKE_BODY
            segment = pygame.rect.Rect(cell[0]*defaults.CELL_SIZE, cell[1]*defaults.CELL_SIZE, defaults.CELL_SIZE, defaults.CELL_SIZE)
            pygame.draw.rect(self.screen, color, segment)

    def draw_food(self, food):
        rect = pygame.rect.Rect(food.position[0]*defaults.CELL_SIZE, food.position[1]*defaults.CELL_SIZE, defaults.CELL_SIZE, defaults.CELL_SIZE)
        pygame.draw.rect(self.screen, colors.FOOD, rect)

    def draw(self):
        pygame.display.flip()
        self.screen.fill(colors.BACKGROUND)
        self.draw_grid()
        self.draw_food(self.game.food)
        self.draw_snake(self.game.snake)
        TextRenderer.draw_score(self.screen, self.game.score)
        if self.game.is_game_over:
            TextRenderer.draw_game_over(self.screen, self.game.game_over_message)