import random
from ai.ai_helper import AIHelper
from core.control import AIControl
from core.game_engine import GameEngine
from core.timer import Timer
from creators.game_builder import GameBuilder
from ui.renderer import Renderer

NUM_ACTIONS = 4
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.95
EXPLORATION_DECAY = 0.9995
MIN_EXPLORATION_RATE = 0.01
EPISODES = 5_000

class QLearning:
    def __init__(self):
        self.q = {} #Q[state] = [left, right, up, down]
        self.game = GameBuilder().wrap_map(False).build()
        self.ai_helper = AIHelper(self.game)
        self.state = self.ai_helper.get_state()
        self.done = False
        self.exploration_rate = 0.1

    def choose_action(self, state):
        if state not in self.q:
            self.q[state] = [0.0]*NUM_ACTIONS

        if random.random() < self.exploration_rate:
            return random.randint(0, NUM_ACTIONS-1)
        else:
            return self.q[state].index(max(self.q[state]))

    def update_q(self, state, action, reward, next_state):
        if state not in self.q:
            self.q[state] = [0.0]*NUM_ACTIONS
        if next_state not in self.q:
            self.q[next_state] = [0.0]*NUM_ACTIONS

        old_value = self.q[state][action]
        next_max = max(self.q[next_state])

        new_value = old_value + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_max - old_value)
        self.q[state][action] = new_value

    def play_episode(self):
        self.game.restart()
        self.state = self.ai_helper.get_state()
        self.exploration_rate = max(self.exploration_rate*EXPLORATION_DECAY, MIN_EXPLORATION_RATE)
        self.done = False
        total_reward = 0

        while not self.done:
            action = self.choose_action(self.state)
            self.game.snake.set_direction_by_action(action)
            is_food_eaten = self.game.update()

            reward = 0
            if is_food_eaten:
                reward = 1
            elif self.game.is_game_over:
                reward = -10
                self.done = True

            next_state = self.ai_helper.get_state()
            self.update_q(self.state, action, reward, next_state)
            self.state = next_state
            total_reward += reward

        return total_reward

    def train(self):
        for episode in range(EPISODES):
            reward = self.play_episode()
            if episode % 100 == 0:
                print(f"Episode {episode}: reward = {reward}")

    def play_trained(self):
        game = GameBuilder().wrap_map(False).build()
        control = AIControl(game, self.q, self)
        timer = Timer(True, 50)
        renderer = Renderer(game, "Snake AI")
        GameEngine(game, control, timer, renderer).run()

if __name__ == "__main__":
    qlearning = QLearning()
    qlearning.train()
    qlearning.play_trained()