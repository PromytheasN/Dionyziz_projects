"""In this project we make a simple version of the snake game,
where the games start with a snake that has size of 10 and
can move around. Randomly food appears that the snake can "eat",
were then get larger by 1. If hit the walls or itself, you loose."""

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
screen_width = 920
pygame.display.set_caption("Snake Game")

# Number of cells
cells_on_x = 48
cells_on_y = 28

# Grid
cell_size = (screen_width / cells_on_x, screen_height / cells_on_y)
grid_width = int(screen_width / cell_size[0])
grid_height = int(screen_height / cell_size[1])

# Grid Walls
y_axis = range(0, grid_height)
y_walls = (list((0, y) for y in y_axis) +
           list((grid_width - 1, y) for y in y_axis))
x_axis = range(0, grid_width)
x_walls = (list((x, 0) for x in x_axis) +
           list((x, grid_height - 1) for x in x_axis))
walls = x_walls + y_walls

# Initializing font
pygame.font.init()
txt_font = pygame.font.SysFont('Score: ', 20)


class Snake():
    """A snake that has size 10,
    terminates the game if hits wall."""

    def __init__(self):
        self.length = 10
        self.positions = [(grid_width // 2, grid_height // 2)]
        self.direction = random.choice([up, down, left, right])
        self.color = black
        self.score = 0

    def get_head_position(self):
        # Get position of the head of the snake
        return self.positions[0]

    def check_new_direction(self, direction):
        return self.length > 1 and (-direction[0],
                                    -direction[1]) == self.direction

    def turn(self, direction):
        # Turn the snake to all direcations except the oposite
        # of it's current if longer than 1
        if self.check_new_direction(direction):
            pass
        else:
            self.direction = direction

    def eat_self(self, new):
        return len(self.positions) > 2 and new in self.positions[2:]

    def touches_wall(self):
        return self.positions[0] in walls

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)
        if self.eat_self(new):
            self.reset()
        elif self.touches_wall():
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 10
        self.positions = [(grid_width // 2, grid_height // 2)]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def render(self, surface):
        for x, y in self.positions:
            r = pygame.Rect((x * cell_size[0], y * cell_size[1]),
                            (cell_size[0], cell_size[1]))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

    def eat_food(self):
        self.get_head_position()
        if self.get_head_position() == food.get_position():
            self.length += 1
            self.score += 1
            food.random_position()


class Food():

    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.random_position()

    def get_position(self):
        return self.position

    def random_position(self):
        self.position = (random.randint(1, grid_width - 2),
                         random.randint(1, grid_height - 2))

    def check_food_loc(self):
        if self.position in snake.positions:
            self.random_position()

    def render(self, surface):
        r = pygame.Rect((self.position[0] * cell_size[0],
                         self.position[1] * cell_size[1]),
                        cell_size)
        pygame.draw.rect(surface, self.color, r)

    def reset(self):
        self.position = self.random_position()


def handle_keys():
    # Keys Dictionarie
    keys_d = {pygame.K_UP: up, pygame.K_DOWN: down,
              pygame.K_LEFT: left, pygame.K_RIGHT: right}

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_d:
                snake.turn(keys_d[event.key])
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def render_grid(surface):
    for y in range(int(grid_height)):
        for x in range(int(grid_width)):
            r = pygame.Rect((x * cell_size[0], y * cell_size[1]),
                            (cell_size[0], cell_size[1]))
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, dark_green, r)
            else:
                pygame.draw.rect(surface, light_green, r)


snake = Snake()
food = Food()


def integrate():
    # Calls game logic related invocations
    handle_keys()
    snake.move()
    snake.eat_food()
    food.check_food_loc()

def render_classes(surface):
    snake.render(surface)
    food.render(surface)

def render_text(screen):
    text = txt_font.render("Score: {0}".format(snake.score), 1, (0, 0, 0))
    return screen.blit(text, (5, 10))


# Game main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    render_grid(surface)

    while True:
        clock.tick(10)
        render_grid(surface)
        integrate()
        render_classes(surface)
        screen.blit(surface, (0, 0))
        food.check_food_loc()
        render_text(screen)
        pygame.display.update()


main()
