"""This is a simple version of arkanoid game"""

import sys
import pygame
import random


# Set colors R G B
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 100, 10)
light_blue = (0, 255, 255)
shadow = (192, 192, 192)
purple = (102, 0, 102)
light_blue = (0, 0, 255)

# Display
display_height = int(999)
display_width = int(444)
pygame.display.set_caption = ("Arkanoid 1.0")
FPS = 60

# Movements
left = (-1, 0)
right = (1, 0)
up = (0, 1)
diagonal_left = (-1, 1)
diagonal_right = (1, 1)

# Classes dimentions
base_dimentions =(display_width // 10, display_height // 100)

# Initializing text font
pygame.font.init()
txt_font = pygame.font.SysFont("Score: ", display_height//10)

class Brick():

    def __init__(self, p_value, str_value):
        self.position = (0, 0)
        self.color = orange
        self.random_position()
        self.size = (display_width // 20, display_height // 100)
        self.p_value = p_value
        self.str_value = str_value

    def render(self, surface):
        r_brick = pygame.Rect((self.position[1],
                                self.position[0]), self.size[0], self.size[1])
        pygame.draw.rect(surface, self.color, r_brick)

    def get_position(self):
        return self.position

    def random_position(self):
        self.position = (0, random.randint(display_width - self.size[1]),
                         random.randit(0, display_height // 2))
        # while self.location self.location_check():
            # self.random_position()

    def reset(self):
        self.position = self.random_position()

    def get_point_value(self):
        return self.value

    def location_check(self):
        return self.location in bricks  # List has to be created

class Ball():
    
    def __init__(self):
        self.position = (0, 0)
        self.radius = display_height // 100
        self.color = light_blue
        self.direction = random.choice([diagonal_left, diagonal_right])


    def render(self, surface):
        c_ball = pygame.Rect(self.position[0] - self.radius, self.position[1] - self.radius,
                             self.radius * 2, self.radius * 2)
        pygame.draw.circle(surface, self.color, c_ball, self.radius)

    def deflect(self):
        pass

class Base_board(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(base_dimentions)
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width // 2, display_height - 2 * base_dimentions[1])
        self.x_direction = 0

    def update(self):
        self.x_direction = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x_direction = -3
        if keystate[pygame.K_RIGHT]:
            self.x_direction = 3
        self.rect.x += self.x_direction

    def shoot(self):
        pass

    def enlogate(self):
        pass

def control():
    keys_dic = {pygame.K_LEFT: left, pygame.K_RIGHT: right}

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        """elif event.type == pygame.KEYDOWN:
            if event.key in keys_dic:
                board.turn(keys_dic[event.key])"""


def render():
    pass

# Initializing sprite list and adding all sprites on it
all_sprites = pygame.sprite.Group()
board = Base_board()
all_sprites.add(board)

# Game main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((display_width, display_height))

    while True:

        # Events
        clock.tick(FPS)
        control()

        # Update
        all_sprites.update()

        # Render
        screen.fill(shadow)
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()


main()
