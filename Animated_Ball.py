import pygame, sys, math, random
from pygame.locals import*

#Initialize all important PyGame modules
pygame.init()

#Assign FPS 
fps = 60
FramePerSec = pygame.time.Clock()

#Setting up color objects
black = (0,0,0)
white = (255,255,255)


#Setup a 999x999 pixel display with caption
displaysurf = pygame.display.set_mode((999,999))
pygame.display.set_caption("Ball animation")
displaysurf.fill(white)

#Defining initial velocity
in_velocity = 10

#Creating a ball
class MyCircle:
    
    def __init__(self, position, size, velocity = pygame.math.Vector2(0,0), color = (0,0,0), width = 0):
        self.position = position
        self.size = size
        self.color = color
        self.width = width
        self.velocity = velocity
        
    #Creating a display function for our circle
    def display(self):
        
        #Making sure that we pass only integers in pygame.draw.circles
        rx, ry = int(self.position.x), int(self.position.y)
        
        pygame.draw.circle(displaysurf, self.color, (rx, ry), self.size, self.width)
    
    #Method to set movement
    def movement(self):
        self.position += self.velocity*dtime
        
    #Method to change velocity
    def ch_velocity(self, velocity):
        self.velocity = velocity
        
#Method generating random velocity
def get_velocity(self, velocity):
    angle = random.uniform(0, math.pi*2)
    new_x = math.sin(angle)
    new_y = math.cos(angle)
    new_vector = pygame.math.Vector2(new_x, new_y)
    new_vector.normalize()
    new_vector*= in_velocity

#Creating our black ball
ball = MyCircle(500,300,30)


#Game Loop
while True:

    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Clear the screen
    #displaysurf.fill(white)
    
    #Display ball
    ball.display()
    
    #Display all
    pygame.display.flip()
    
    #Limit frames per second to fps(60)
    FramePerSec.tick(fps)
