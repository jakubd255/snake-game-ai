import pygame
from ai.ai_helper import AIHelper

class ControlStrategy:
    def control(self, events, is_ready):
        raise NotImplementedError

class HumanControl(ControlStrategy):
    def __init__(self, game):
        self.game = game

    def control(self, events, is_ready=None):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.game.snake.set_direction_by_key(event.key)

class AIControl(ControlStrategy):
    def __init__(self, game, q, q_learning):
        self.game = game
        self.q = q
        self.q_learning = q_learning
        self.ai_helper = AIHelper(self.game)

    def control(self, events, is_ready):
        if is_ready:
            state = self.ai_helper.get_state()
            action = self.q_learning.choose_action(state)
            self.game.snake.set_direction_by_action(action)