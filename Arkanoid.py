"""This is a simple version of arkanoid game"""

import sys
import pygame
import random


# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 100, 10)

# Display
screen_height = 999
screen_width = 444
pygame.display.set_caption = ("Arkanoid 1.0")

# Movements
left = (-1, 0)
right = (1, 0)

# Initializing text font
pygame.font.init()
txt_font = pygame.font.SysFont("Score: ", screen_height//10)

class Bricks():

    def __init__(self, p_value, str_value):
        self.position = (0, 0)
        self.color = orange
        self.random_position()
        self.size = (screen_width // 20, screen_height // 100)
        self.p_value = p_value
        self.str_value = str_value

    def render(self, surface):
        r_brick = pygame.Rect((self.position[1],
                                self.position[0]), self.size[0], self.size[1])
        pygame.draw.rect(surface, self.color, r)

    def get_position(self):
        return self.position

    def random_position(self):
        self.position = (0, random.randint(screen_width - self.size[1]),
                         random.randit(0, screen_height // 2))
        while self.location self.location_check():
            self.random_position()

    def reset(self):
        self.position = self.random_position()

    def get_point_value(self):
        return self.value

    def location_check(self):
        return self.location in bricks  # List has to be created

class Ball():
    
    def __init__(self):
        self.position = ()

    def render(self):
        pass

class Base_board():

    def __init__(self):
        self.position = (screen_width//2, screen_height) # Have to add something here
        self.color = orange

    def render(self):
        pass

    def move(self):
        pass

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
        elif event.type == pygame.KEYDOWN:
            if event.key in keys_dic:
                base_board.turn(keys_dic[event.key]) # init base_board before


# Game main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    while True:
        clock.tick(10)
        screen.fill(white)
        control()
        pygame.display.update()


main()
