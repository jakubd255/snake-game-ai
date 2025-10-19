from core.control import HumanControl
from core.game_engine import GameEngine
from core.timer import Timer
from creators.game_builder import GameBuilder
from ui.renderer import Renderer

if __name__ == "__main__":
    game = GameBuilder().build()
    control = HumanControl(game)
    timer = Timer(False, 100)
    renderer = Renderer(game)
    GameEngine(game, control, timer, renderer).run()