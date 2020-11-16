import pygame

# Set colors R G B
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 100, 10)
light_blue = (0, 144, 255)
shadow = (192, 192, 192)
purple = (152, 0, 152)

# Display
display_height = 999
display_width = 444
pygame.display.set_caption = ("Arkanoid 1.0")
FPS = 60

# Movement speed
speed = display_width // 60

# Movements
left = (-speed, 0)
right = (speed, 0)
up = (0, speed)
diagonal_left = [-speed, -speed]
diagonal_right = [speed, -speed]

# Game objects dimentions
paddle_dimentions = (display_width // 2, display_height // 100)
brick_width = display_width // 20 * 2
brick_height = display_height // 100
brick_dimentions = [brick_width, brick_height] 
ball_dimentions = (display_height // 100, display_height // 100)

print("Global settings imported")