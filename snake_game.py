"""In this project we make a simple version of the snake game,
where the games start with a snake that has size of 10 and
can move around. Randomly food appears that the snake can "eat",
were then get larger by 1. If hit the walls or itself, you loose"""

import sys
import pygame
import random


# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
dark_green = (0, 111, 0)
light_green = (0, 255, 0)
red = (200, 0, 0)

# Possible snake movements
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Display
screen_height = 560
screen_width = 960
pygame.display.set_caption("Snake Game")

# Grid
grid_size = 20
grid_width = int(screen_width / grid_size)
grid_height = int(screen_height / grid_size)

# Grid Walls
y_axel = list(range(0, screen_height, grid_size))
y_walls = (list((0, o) for o in y_axel) +
           list((screen_width - grid_size, o) for o in y_axel))
x_axel = list(range(0, screen_width, grid_size))
x_walls = (list((o, 0) for o in x_axel) +
           list((o, screen_height - grid_size) for o in x_axel))
walls = x_walls + y_walls


class Snake():
    """A snake that has size 10,
    terminates the game if hits wall."""

    def __init__(self):

        self.length = 10
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = black
        self.score = 0

    def get_head_position(self):
        # Get position of the head of the snake
        return self.positions[0]

    def turn(self, point):
        # Turn the snake to all direcations except the oposite
        # of it's current if longer than 1
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*grid_size)) % screen_width),
               (cur[1] + (y*grid_size)) % screen_height)

        # If the new position of head overlaps any
        # of the other positions of the snake, game is ended
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        # If snake touches walls, game is ended
        elif self.positions[0] in walls:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.lenth = 10
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_size, grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


class Food():
    
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.random_position()

    def random_position(self):
        self.position = (random.randint(grid_size, grid_width -2)*grid_size,
                         random.randint(grid_size, grid_height -2)*grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)

    def reset(self):
        self.position = random_position()


def draw_grid(surface):

    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            r = pygame.Rect((x*grid_size, y*grid_size),(grid_size, grid_size))
            if (x+y) % 2 == 0:
                pygame.draw.rect(surface, dark_green, r)
            else:
                pygame.draw.rect(surface, light_green, r)


snake = Snake()
food = Food()


# Game main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)


    while True:

        clock.tick(10)
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.random_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()


main()
