import config
from direction import Direction

class Snake:
    def __init__(self):
        self.segments = [[config.CELLS_NUMBER//2]*2]
        self.direction = Direction.UP
        self.grow_next = False

    def move(self):
        head_x, head_y = self.segments[0]
        new_x = (head_x+self.direction.x)
        new_y = (head_y+self.direction.y)

        if config.WRAP_MAP:
            new_x %= config.CELLS_NUMBER
            new_y %= config.CELLS_NUMBER
        else:
            if not (0 <= new_x < config.CELLS_NUMBER) or not (0 <= new_y < config.CELLS_NUMBER):
                raise Exception("Game Over: Snake hit the wall!")

        new_head = (new_x, new_y)

        if new_head in self.segments:
            raise Exception("Game Over: Snake collided with itself!")

        self.segments.insert(0, new_head)
        if not self.grow_next:
            self.segments.pop()
        else:
            self.grow_next = False

    def grow(self):
        self.grow_next = True

    def draw(self, screen, pygame):
        for cell in self.segments:
            segment = pygame.rect.Rect(cell[0]*config.CELL_SIZE, cell[1]*config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
            pygame.draw.rect(screen, config.GREEN, segment)