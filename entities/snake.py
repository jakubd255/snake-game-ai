from entities.direction import Direction

class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.segments = [[self.width//2, self.height//2]]
        self.direction = Direction.UP
        self.grow_next = False

    def move(self):
        head_x, head_y = self.segments[0]
        new_x = (head_x+self.direction.x)
        new_y = (head_y+self.direction.y)

        self.segments.insert(0, [new_x, new_y])
        if not self.grow_next:
            self.segments.pop()
        else:
            self.grow_next = False

    def get_head(self):
        return self.segments[0]

    def set_head(self, head):
        self.segments[0] = head

    def grow(self):
        self.grow_next = True

    def reset(self):
        self.segments = [[self.width//2, self.height//2]]
        self.direction = Direction.UP
        self.grow_next = False

    def set_direction(self, direction):
        self.direction = direction

    def set_direction_by_key(self, key):
        self.direction = Direction.get_direction_by_key(self.direction, key)

    def set_direction_by_action(self, action):
        new_direction = Direction.get_direction_by_action(action)
        if not self.direction.is_opposite(new_direction):
            self.direction = new_direction