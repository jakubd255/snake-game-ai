import pygame
from core.event_handler import EventHandler
from ui.renderer import Renderer

class GameEngine:
    def __init__(self, game, control, timer):
        self.game = game
        self.control = control
        self.timer = timer
        self.events = EventHandler(self)
        self.renderer = Renderer(self.game)

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