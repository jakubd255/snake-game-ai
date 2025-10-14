import sys
import pygame
import config
from direction import Direction
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode([config.WINDOW_SIZE]*2, flags=pygame.SCALED, vsync=1)
        self.font = pygame.font.SysFont(None, 36)
        self.clock = pygame.time.Clock()
        self.stop_delay = 100
        self.time = 0
        self.score = 0
        self.snake = Snake()
        self.food = Food()

    def delta_time(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.stop_delay:
            self.time = time_now
            return True
        return False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.snake.direction = Direction.next_direction(self.snake.direction, event.key)
    
    def draw_grid(self):
        for x in range(0, config.WINDOW_SIZE, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (x, 0), (x, config.WINDOW_SIZE))        
        for y in range(0, config.WINDOW_SIZE, config.CELL_SIZE):
            pygame.draw.line(self.screen, [50]*3, (0, y), (config.WINDOW_SIZE, y))

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, config.WHITE)
        self.screen.blit(score_text, (10, 10))

    def draw(self):
        self.screen.fill(config.BLACK)
        self.draw_grid()
        self.food.draw(self.screen, pygame)
        self.snake.draw(self.screen, pygame)
        self.draw_score()

    def hanle_eat_food(self):
        if self.snake.segments[0] == self.food.position:
            self.score+=1
            self.snake.grow()
            self.food.respawn()

    def update(self):
        if self.delta_time():
            self.snake.move()
            self.hanle_eat_food()
        pygame.display.flip()
        self.clock.tick(60)

    def run(self):
        while(True):
            self.handle_events()
            self.draw()
            self.update()