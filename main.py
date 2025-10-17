from core.control import HumanControl
from core.game import Game
from core.game_engine import GameEngine
from core.timer import Timer

if __name__ == "__main__":
    game = Game()
    control = HumanControl(game)
    timer = Timer(False, 100)
    GameEngine(game, control, timer).run()