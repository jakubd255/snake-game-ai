import config
from direction import Direction

class Snake:
    def __init__(self):
        self.segments = [[config.CELLS_NUMBER//2]*2]
        self.direction = Direction.UP
        self.grow_next = False

    def move(self, game, wrap_map=config.WRAP_MAP):
        head_x, head_y = self.segments[0]
        new_x = (head_x+self.direction.x)
        new_y = (head_y+self.direction.y)

        if wrap_map:
            new_x %= config.CELLS_NUMBER
            new_y %= config.CELLS_NUMBER
        else:
            if not (0 <= new_x < config.CELLS_NUMBER) or not (0 <= new_y < config.CELLS_NUMBER):
                game.game_over("Snake hit the wall!")

        new_head = [new_x, new_y]
        if new_head in self.segments:
            game.game_over("Snake collided with itself!")

        self.segments.insert(0, new_head)
        if not self.grow_next:
            self.segments.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True

    def reset(self):
        self.segments = [[config.CELLS_NUMBER//2]*2]
        self.direction = Direction.UP
        self.grow_next = False

    def set_direction(self, direction):
        self.direction = direction

    def set_direction_by_key(self, key):
        self.direction = Direction.get_direction_by_key(self.direction, key)