"""This is a simple version of arkanoid game"""

import sys
import pygame
import random


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
base_dimentions =(display_width // 10*5, display_height // 100)
brick_dimentions = (display_width // 20*5*2, display_height // 100)
ball_dimentions = (display_height // 100, display_height // 100)

# Initializing text font
pygame.font.init()
txt_font = pygame.font.SysFont("Score: ", display_height//44)

class Brick(pygame.sprite.Sprite):

    def __init__(self, point_value):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(brick_dimentions)
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.center = self.random_position()
        self.point_value = point_value
        # self.str_value = str_value

    def update(self):
        self.collision()

    def get_position(self):
        return self.position

    def random_position(self):
        self.position = (random.randint(0, display_width - brick_dimentions[1]),
                         random.randint(0, display_height // 2))
        return self.position
        # while self.location self.location_check():
            # self.random_position()

    def collision(self):
        # If brick is hit losing point
        collision = pygame.sprite.spritecollideany(ball, brick_sprites)
        if collision:
            print("I have colide")
            self.point_value -= 1
            # score += 1
            if self.point_value == 0:
                self.reset()

    def reset(self):
        self.position = self.random_position()
        self.point_value = 1

    def get_point_value(self):
        return self.value

    def location_check(self):
        return self.location in bricks  # List has to be created


class Ball(pygame.sprite.Sprite):
    """Initiates a moving ball and its' attributes"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(ball_dimentions)
        self.image.fill(light_blue)
        self.rect = self.image.get_rect()
        self.rect.center = self.init_position()
        self.direction = random.choice([diagonal_left, diagonal_right])
        self.score = 0

    def init_position(self):
        # Initialize position of the ball
        init_position = (board.rect.center[0],
                         (board.rect.center[1] - (base_dimentions[1] / 2)
                          - (ball_dimentions[1] / 2)))
        return init_position

    
    def collision(self):
        # If hit bricks
        collision = pygame.sprite.spritecollideany(ball, brick_sprites)
        if collision:
            self.direction[1] *= -1
            self.score += 1
            

    def movement(self):
        self.containment()
        self.rect[1] += self.direction[1]
        self.rect[0] += self.direction[0]
        self.deflect()
        self.collision()
        self.ball_loss()

    def containment(self):
        if self.rect.right >= display_width or self.rect.left <= 0:
            self.direction[0] *= -1
        if self.rect.top <= 0:
            self.direction[1] *= -1

    def ball_loss(self):
        if self.rect.bottom >= display_height:
            self.reset()
            print("I have reseted")

    def reset(self):
        self.init_position()
        self.score = 0

    def update(self):
        self.movement()

    def deflect(self):
        # If hit base_board
        if (self.rect.bottom == board.rect.top and
            (board.rect.left <= self.rect.left <= board.rect.right or
             board.rect.left <= self.rect.right <= board.rect.right )):
            self.direction[1] *= -1


class Base_board(pygame.sprite.Sprite):
    """Initiates base_board class and it's attributes"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(base_dimentions)
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width // 2, display_height - 2 * base_dimentions[1])
        self.x_direction = 0

    def update(self):
        # Up-dates classes' position according to user's imput
        self.x_direction = 0
        self.movement()
        self.rect.x += self.x_direction

    def movement(self):
        # Creates movement and constrains object within screen dimentions
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if not self.rect.left <= 0:
                self.x_direction = -speed
        elif keystate[pygame.K_RIGHT]:
            if not self.rect.right >= display_width:
                self.x_direction = speed

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

# Initializing sprite lists and adding all sprites on lists
all_sprites = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()

board = Base_board()
brick = Brick(1)
ball = Ball()

all_sprites.add(board)
brick_sprites.add(brick)
all_sprites.add(ball)

def render_text(screen):
    text = txt_font.render("Score: {0}".format(ball.score), 1, (0, 0, 0))
    return screen.blit(text, (5, 10))


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
        brick_sprites.update()
        all_sprites.update()

        # Render
        screen.fill(shadow)
        all_sprites.draw(screen)
        brick_sprites.draw(screen)
        render_text(screen)
        pygame.display.flip()
        pygame.display.update()


main()
