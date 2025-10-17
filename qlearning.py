import random
from ai_helper import AIHelper
from control import AIControl
from game import Game
from game_engine import GameEngine
from timer import Timer

NUM_ACTIONS = 3
LEARNING_RATE = 0.1 #alpha
DISCOUNT_FACTOR = 0.95 #gamma
EXPLORATION_RATE = 0.1 #epsilon
EPISODES = 5_000

class QLearning:
    def __init__(self):
        self.q = {} #Q[state] = [straight, left, right]
        self.game = Game()
        self.ai_helper = AIHelper(self.game)
        self.state = self.ai_helper.get_state()
        self.done = False

    def choose_action(self, state):
        if state not in self.q:
            self.q[state] = [0.0]*NUM_ACTIONS

        if random.random() < EXPLORATION_RATE:
            return random.randint(0, NUM_ACTIONS - 1)
        else:
            return self.q[state].index(max(self.q[state]))

    def update_q(self, state, action, reward, next_state):
        if state not in self.q:
            self.q[state] = [0.0] * NUM_ACTIONS
        if next_state not in self.q:
            self.q[next_state] = [0.0] * NUM_ACTIONS

        old_value = self.q[state][action]
        next_max = max(self.q[next_state])

        new_value = old_value + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_max - old_value)
        self.q[state][action] = new_value

    def play_episode(self):
        self.game.restart()
        self.state = self.ai_helper.get_state()
        self.done = False
        total_reward = 0

        while not self.done:
            action = self.choose_action(self.state)

            # Game moves
            self.game.snake.set_direction_by_action(action)
            self.game.snake.move(self.game, False)
            is_food_eaten = self.game.handle_eat_food()

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
        game = Game()
        control = AIControl(game, self.q, self)
        timer = Timer(True, 100)
        GameEngine(game, control, timer).run()

if __name__ == "__main__":
    qlearning = QLearning()
    qlearning.train()
    qlearning.play_trained()