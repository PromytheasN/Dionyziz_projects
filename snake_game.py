"""In this project we make a simple version of the snake game,
where the games start with a snake that has size of 10 and 
can move around and if hit the walls only, you loose"""

import sys
import pygame
import random

pygame.init()


# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
dark_green = (0, 111, 0)

# Create an object to help track time so we can define max FPS
clock = pygame.time.Clock()

# Possible snake movments
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Display
screen_height = 540
screen_width = 960
pygame.display.set_caption("Snakessss Game")
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(dark_green)

grid_size = 20
grid_width = screen_height / grid_size
grid_height = screen_width / grid_size

surface = pygame.Surface(screen.get_size())
surface = surface.convert()


class Snake():
    """A snake that has size 10, 
    terminates the game if hits wall."""

    def __init__(self):
        
        self.length = 10
        self.positions = [((screen_width // 2), (screen_height // 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = black

    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0] + (x*grid_size))%screen_width), (cur[1]+(y*grid_size))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
                
    def reset(self):
        self.lenth = 10
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_size,grid_size))
            pygame.draw.rect(surface, self.color, r)
            #makes a little draw around the black cube
            pygame.draw.rect(surface, dark_green, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


def draw_grid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*grid_size, y*grid_size),(grid_size,grid_size))
                pygame.draw.rect(surface, dark_green, r)
            else:
                rr = pygame.Rect((x*grid_size, y*grid_size), (grid_size,grid_size))
                pygame.draw.rect(surface, dark_green, rr)


draw_grid(surface)
snake = Snake()

# Game Loop
def game_loop():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

        
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        screen.fill(dark_green)
        snake.draw(surface)
        pygame.display.update()
        clock.tick(20)

        
game_loop()
