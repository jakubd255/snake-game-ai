import pygame
from core import config
from core.event_handler import EventHandler
from ui.renderer import Renderer

class GameEngine:
    def __init__(self, game, control, timer):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.game = game
        self.control = control
        self.events = EventHandler(self)
        self.timer = timer
        self.screen = pygame.display.set_mode([config.WINDOW_SIZE] * 2, flags=pygame.SCALED, vsync=1)
        self.renderer = Renderer(self.screen, self.game)

    def restart(self):
        self.timer.reset_speed()
        self.game.restart()

    def run(self):
        while True:
            events = self.events.handle_events()
            is_ready = self.timer.is_ready()
            self.control.control(events, is_ready)
            self.renderer.draw()
            if is_ready:
                is_food_eaten = self.game.update()
                if is_food_eaten:
                    self.timer.speed_up()
            pygame.display.flip()
            self.timer.tick_fps()