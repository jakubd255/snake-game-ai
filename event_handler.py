import sys
import pygame

def quit_game():
    pygame.quit()
    sys.exit()

class EventHandler:
    def __init__(self, game, disable_change_direction=False):
        self.game = game
        self.disable_change_direction = disable_change_direction
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)

    def handle_keydown(self, key):
        if key == pygame.K_ESCAPE:
            quit_game()
        elif key == pygame.K_SPACE and self.game.is_game_over:
            self.game.restart()
        elif not self.disable_change_direction:
            self.game.snake.set_direction_by_key(key)