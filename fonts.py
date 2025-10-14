import pygame
import config

pygame.font.init()

class Fonts:
    SCORE_FONT = pygame.font.SysFont(None, 30)
    GAME_OVER_FONT = pygame.font.SysFont(None, 85)
    GAME_OVER_MESSAGE_FONT = pygame.font.SysFont(None, 40)

    @staticmethod
    def draw_text_center(screen, text, font, y_offset=0, color=config.WHITE):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (screen.get_width()//2, screen.get_height()//2+y_offset)
        screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_score(screen, score):
        score_text = Fonts.SCORE_FONT.render(f"Score: {score}", True, config.WHITE)
        screen.blit(score_text, (10, 10))

    @staticmethod
    def draw_game_over(screen, message):
        Fonts.draw_text_center(screen, "Game Over", Fonts.GAME_OVER_FONT)
        Fonts.draw_text_center(screen, message, Fonts.GAME_OVER_MESSAGE_FONT, y_offset=50)