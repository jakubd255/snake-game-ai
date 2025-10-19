import pygame
from config import colors

pygame.font.init()

class TextRenderer:
    SCORE_FONT = pygame.font.SysFont(None, 30)
    GAME_OVER_FONT = pygame.font.SysFont(None, 85)
    GAME_OVER_MESSAGE_FONT = pygame.font.SysFont(None, 40)

    @staticmethod
    def draw_text_center(screen, text, font, y_offset=0, color=colors.WHITE):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (screen.get_width()//2, screen.get_height()//2+y_offset)
        screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_score(screen, score):
        score_text = TextRenderer.SCORE_FONT.render(f"Score: {score}", True, colors.WHITE)
        screen.blit(score_text, (10, 10))

    @staticmethod
    def draw_game_over(screen, message):
        TextRenderer.draw_text_center(screen, "Game Over", TextRenderer.GAME_OVER_FONT)
        TextRenderer.draw_text_center(screen, message, TextRenderer.GAME_OVER_MESSAGE_FONT, y_offset=50)