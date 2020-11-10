"""This project's target is to create an 8 pool ball enviroment,
where only the black ball apears on the center of the table
and while keeping steady speed, hits and deflects from walls of the table"""

import sys
import pygame

pygame.init()


# Set collors
white = (255, 255, 255)
green = (0, 155, 0)
black = (0, 0, 0)

# Create an object to help track time so we can define max FPS in our game loop
clock = pygame.time.Clock()

# Display
screen_hight = 555
screen_width = 999
pygame.display.set_caption("8 Pool Ball")
screen = pygame.display.set_mode((screen_width, screen_hight))
screen.fill(green)

size = 30


class PoolBall:
    """A ball that have certain movement
    speed and is displayed on the screen"""

    def __init__(self, x, y, xspeed=3, yspeed=3,
                 color=(0, 0, 0), size=30, width=0):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.color = color
        self.size = size
        self.width = width

    def display(self):
        # Displaying ball
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def integrate(self):
        # Create movements for the ball
        self.x += self.xspeed
        self.y -= self.yspeed

        if self.y < 0 + self.size//2 or self.y > screen_hight - self.size//2:
            self.yspeed *= -1
        if self.x < 0 + self.size//2 or self.x > screen_width - self.size//2:
            self.xspeed *= -1


class Hole:
    """Diplays '8 pool ball hole'"""
    def __init__(self, x, y, color=(0, 0, 0), size=30, width=0):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.width = width

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


coords = [(5, 5), (5, screen_hight - 5),
          (screen_width - 5, 5), (screen_width - 5, 5),
          (screen_width - 5, screen_hight - 5),
          (screen_width // 2, 5),
          (screen_width // 2, screen_hight - 5)]

holes = []
for x, y in coords:
    holes.append(Hole(x, y))

ball = PoolBall(screen_width//2, screen_hight//2)

# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

    screen.fill(green)
    ball.display()
    ball.integrate()

    for hole in holes:
        hole.display()

    pygame.display.update()

    clock.tick(60)
