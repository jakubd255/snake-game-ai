import pygame
import config

class Timer:
    def __init__(self, disable_speed_up=False, stop_delay=config.STOP_DELAY):
        self.disable_speed_up = disable_speed_up
        self.init_stop_delay = stop_delay
        self.stop_delay = stop_delay
        self.time = 0
        self.clock = pygame.time.Clock()

    def is_ready(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.stop_delay:
            self.time = time_now
            return True
        return False

    def tick_fps(self, fps=60):
        self.clock.tick(fps)

    def speed_up(self):
        if not self.disable_speed_up and self.stop_delay > 20:
            self.stop_delay -= 5

    def reset_speed(self):
        self.stop_delay = self.init_stop_delay