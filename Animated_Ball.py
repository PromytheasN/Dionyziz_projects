import pygame, sys, math, random, os, pygame.mixer
from pygame.locals import*

#Initialize all important PyGame modules
pygame.init()

#Assign FPS 
fps = 60
FramePerSec = pygame.time.Clock()

#Setting up color objects
black = (0,0,0)
white = (255,255,255)

#Defining screen size
screen_size = screen_w, screen_h = 999, 999


#Setup screen size and display with caption
displaysurf = pygame.display.set_mode((screen_size))
pygame.display.set_caption("Ball animation")
displaysurf.fill(white)

#Defining initial velocity
in_velocity = 10.0

#Method generating random velocity
def get_velocity():
    angle = random.uniform(0, math.pi*2)
    new_x = math.sin(angle)
    new_y = math.cos(angle)
    new_vector = pygame.math.Vector2(new_x, new_y)
    new_vector.normalize()
    new_vector *= in_velocity
    return new_vector

#Creating class for balls
class MyCircle:
    
    def __init__(self, size, position, velocity = pygame.math.Vector2(0,0), color = (0,0,0), width = 0):
        self.position = position
        self.size = size
        self.color = color
        self.width = width
        self.velocity = velocity
        

    #Creating a display function for our circle
    def display(self):
         
        pygame.draw.circle(displaysurf, self.color, (x,y), self.size, self.width)
    
    #Method to set movement
    def movement(self):
        self.position += self.velocity*dtime
        
    #Method to change velocity
    def ch_velocity(self, velocity):
        self.velocity = velocity

x = random.randint(0, screen_h)
y = random.randint(0, screen_w)


#Creating our black ball
#ball = MyCircle(position ,20 ,(20,2))

balls = []


for n in range(1):
    size = random.randint(10.0 ,20.0)
    x = random.randint(size, screen_h-size)
    y = random.randint(size, screen_w-size)
    color = (0,0,0)
    velocity = get_velocity()
    balls.append(MyCircle(pygame.math.Vector2(x,y),size,color,velocity))

direction_tick = 0.0
ball = balls[0]




run = True

#Game Loop
while run:

    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Limit frames per second to fps(60)
    FramePerSec.tick(fps)
    dtime = FramePerSec.tick(fps)/1000.0
    
    direction_tick += dtime
    if direction_tick > 1.0:
        direction_tick = 0.0
        ball = random.choice(balls)
        new_velocity = get_velocity()
        ball.ch_velocity(new_velocity)
        
        
    
    
    #Clear screen
    displaysurf.fill(white)
    
    
    #Displaying and Moving the ball
    ball.movement()
    ball.display()
    
    #Display all
    pygame.display.flip()
    
    
pygame.quit()
sys.exit()
