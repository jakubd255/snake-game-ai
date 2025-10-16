import pygame
import config
from event_handler import EventHandler
from renderer import Renderer
from timer import Timer

class GameEngine:
    def __init__(self, game):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.game = game
        self.events = EventHandler(self.game)
        self.timer = Timer()
        self.screen = pygame.display.set_mode([config.WINDOW_SIZE]*2, flags=pygame.SCALED, vsync=1)
        self.renderer = Renderer(self.screen)

    def run(self):
        while True:
            self.events.handle_events()
            self.renderer.draw(self.game)
            if self.timer.is_ready():
                is_food_eaten = self.game.update()
                if is_food_eaten:
                    self.timer.speed_up()
            pygame.display.flip()
            self.timer.tick_fps()