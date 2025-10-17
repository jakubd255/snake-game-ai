import sys
import pygame

def quit_game():
    pygame.quit()
    sys.exit()

class EventHandler:
    def __init__(self, engine, disable_change_direction=False):
        self.engine = engine
        self.disable_change_direction = disable_change_direction
    
    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()
                elif event.key == pygame.K_SPACE and self.engine.game.is_game_over:
                    self.engine.restart()
        return events