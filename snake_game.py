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
cell_size = 20
grid_width = int(screen_width / cell_size)
grid_height = int(screen_height / cell_size)

# Grid Walls
y_axis = list(range(0, screen_height, cell_size))
y_walls = (list((0, y) for y in y_axis) +
           list((screen_width - cell_size, y) for y in y_axis))
x_axis = list(range(0, screen_width, cell_size))
x_walls = (list((x, 0) for x in x_axis) +
           list((x, screen_height - cell_size) for x in x_axis))
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
        if self.length > 1 and (-point[0], -point[1]) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*cell_size)) % screen_width),
               (cur[1] + (y*cell_size)) % screen_height)

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
        self.length = 10
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (cell_size, cell_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

    def handle_keys(self):
        # Keys Dictionarie
        keys_d = {pygame.K_UP: up, pygame.K_DOWN: down,
                  pygame.K_LEFT: left, pygame.K_RIGHT: right}

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in keys_d:
                    self.turn(keys_d[event.key])
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def eat_food(self):
        if self.get_head_position() == Food.random_position(food):
            self.length += 1
            self.score += 1
            Food.random_position(food)


class Food():

    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.random_position()

    def random_position(self):
        self.position = (random.randint(cell_size, grid_width - 2) * cell_size,
                         random.randint(cell_size, grid_height - 2) * cell_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]),
                        (cell_size, cell_size))
        pygame.draw.rect(surface, self.color, r)

    def reset(self):
        self.position = random_position()


def draw_grid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            r = pygame.Rect((x*cell_size, y*cell_size), (cell_size, cell_size))
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
        snake.eat_food()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()


main()
