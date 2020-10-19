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
screen_width = 333
pygame.display.set_caption = ("Arkanoid 1.0")

# Movements
left = (-1, 0)
right = (1, 0)

# Initializing text font
pygame.font.init()
txt_font = pygame.font.SysFont("Score: ", screen_height//10)

class Bricks():
    pass

    def render(self):
        pass


class Ball():
    pass

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