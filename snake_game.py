"""In this project we make a simple version of the snake game,
where the games start with a snake that has size of 10 and 
can move around and if hit the walls only, you loose"""

import sys
import pygame

pygame.init()


# Set colors
white = 255, 255, 255
black = 0, 0, 0
dark_green = 0, 122, 0

# Create an obkect to help track time so we can define max FPS
clock = pygame.time.Clock()

# Display

screen_hight = 1080
screen_width = 1920
pygame.display.set_caption("Snakessss Game")
screen = pygame.display.set_mode((screen_width, screen_hight))
screen.fill(dark_green)

class Snake:
    """A snake that has size 10, 
    terminates the game if hits wall."""
    
    def __init__(self, x, y,):
        
        self.x = x
        self.y = y

# Game Loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
            
        screen.fill(dark_green)
        
        pygame.display.update()
        
        clock.tick(60)
