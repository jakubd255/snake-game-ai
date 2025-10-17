from control import HumanControl
from game import Game
from game_engine import GameEngine
from timer import Timer

if __name__ == "__main__":
    game = Game()
    control = HumanControl(game)
    timer = Timer(False, 100)
    GameEngine(game, control, timer).run()