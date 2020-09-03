"""This project's target is to create an 8 pool ball enviroment, where only the black ball apears on the center of the table
and while keeping steady speed, hits and deflects from walls of the table"""

import sys, pygame, math, random
from pygame.locals import*

#Initialize all important PyGame modules
pygame.init()


#Setting collors
white = (255,255,255)
green = (0,155,0)
black = (0,0,0)

#Creating an object to help track time so we can define max FPS in our game loop
clock = pygame.time.Clock()

#Display
pygame.display.set_caption("8 Pool Ball")
screen = pygame.display.set_mode((999,555))
screen.fill(green)


size = 30
#Creating a circle class
class ThaCircle:
    """Class for creating balls that has certain movement speed and are displayed on the screen"""
    
    def __init__(self, x, y, xspeed = 3, yspeed = 3, color = (0,0,0), size = 30, width = 0):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.color = color
        self.size = size
        self.width = width
        
    def display(self):
        #Displaying ball
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        
    def reposition(self):
        #Creating movement for the ball
        self.x += self.xspeed
        self.y -= self.yspeed
        
        if self.y < 0 + self.size//2 or self.y > 555 - self.size//2:
            self.yspeed *= -1
        if self.x < 0 + self.size//2 or self.x > 999 - self.size//2:
            self.xspeed *= -1
            
        
class Holes:
    """Class creating and siplaying "holes""""
    def __init__(self, x, y, color = (0,0,0), size = 30, width = 0):
        
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.width = width
    
    def display(self):
        
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
        

#Creating a circle
ball = ThaCircle(999//2, 555//2)

#Creating holes
hole_1 = Holes(5,5)
hole_2 = Holes(5,550)
hole_3 = Holes(994,5)
hole_4 = Holes(994,550)
hole_5 = Holes(999//2,5)
hole_6 = Holes(999//2,550)




#Game Loop
while True:
    
    for event in pygame.event.get():
        #Checking events
        #print(event)
        if event.type == pygame.QUIT: 
            
            pygame.quit()
            sys.exit()
    
    
    
    screen.fill(green)
    ball.display()
    ball.reposition()
    
    #Displaying holes
    hole_1.display()
    hole_2.display()
    hole_3.display()
    hole_4.display()
    hole_5.display()
    hole_6.display()
    pygame.display.update()
    
    #Defining max FPS
    clock.tick(60)
