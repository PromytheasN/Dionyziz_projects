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
base_dimentions = (display_width // 1, display_height // 100)
brick_width = display_width // 20 * 2
brick_height = display_height // 100
brick_dimentions = [brick_width, brick_height] 
ball_dimentions = (display_height // 100, display_height // 100)

# Initializing text font
pygame.font.init()
txt_font = pygame.font.SysFont("Score: ", display_height//44)

# Initializing sprite lists
ball_board_sprites = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()


class Brick(pygame.sprite.Sprite):

    def __init__(self, point_value, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(brick_dimentions)
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.point_value = point_value

    def collision(self):
        self.point_value -= 1
        if self.point_value == 0:
            self.kill() 

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

    def update(self):
        self.movement()

    def init_position(self):
        # Initialize position of the ball
        init_position = (board.rect.center[0],
                         (board.rect.center[1] - (base_dimentions[1] / 2)
                          - (ball_dimentions[1] / 2)))
        return init_position

    def collision(self):
        # If hit bricks
        self.direction[1] *= -1
        self.score += 1

    def movement(self):
        self.containment()
        self.rect[1] += self.direction[1]
        self.rect[0] += self.direction[0]
        self.deflect()
        self.ball_loss()

    def containment(self):
        if self.rect.right >= display_width or self.rect.left <= 0:
            self.direction[0] *= -1
        if self.rect.top <= 0:
            self.direction[1] *= -1

    def ball_loss(self):
        if self.rect.bottom >= display_height:
            self.reset()
            bricks_reset()

    def reset(self):
        self.rect.center = self.init_position()
        self.direction[1] *= -1
        self.score = 0

    def deflect(self):
        # If hit base_board, deflect
        if (self.rect.bottom == board.rect.top and
            (board.rect.left <= self.rect.left <= board.rect.right or
             board.rect.left <= self.rect.right <= board.rect.right)):
            self.direction[1] *= -1
            self.board_ball_interaction()

    def board_ball_interaction(self):
        # When board is moving, effects balls direction/speed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and board.rect.left > 0:
            self.direction[0] -= speed // 2
        elif keystate[pygame.K_RIGHT] and board.rect.right < display_width:
            self.direction[0] += speed // 2


class Base_board(pygame.sprite.Sprite):
    """Initiates base_board class and it's attributes"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(base_dimentions)
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width // 2,
                            display_height - 2 * base_dimentions[1])
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# and adding all sprites on lists
board = Base_board()
ball = Ball()

ball_board_sprites.add(board)
ball_board_sprites.add(ball)


def bricks_list_creator():
    # Creates and adds bricks into a list
    i = 9
    point_value = 3
    coordinates = [display_width // 20 + brick_width / 6, display_height // 20]
    while i > 0:
        brick = Brick(point_value, (coordinates))
        coordinates[0] += brick_width * 1.1
        brick_sprites.add(brick)
        i -= 1
    return brick_sprites


def bricks_reset():
    # Reset brick list
    brick_sprites.empty()
    bricks_list_creator()
    return brick_sprites


def render_text(screen):
    text = txt_font.render("Score: {0}".format(ball.score), 1, (0, 0, 0))
    return screen.blit(text, (5, 10))


def render_main(screen):
    ball_board_sprites.draw(screen)
    brick_sprites.draw(screen)
    render_text(screen)

def update_collisions():
    list_of_collisions = pygame.sprite.spritecollide(ball, brick_sprites, False)
    if list_of_collisions:
        ball.collision()
        for instance in list_of_collisions:
            instance.collision()

# Game main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((display_width, display_height))
    bricks_list_creator()

    while True:
        # Events
        clock.tick(FPS)
        control()
        update_collisions()

        # Update
        ball_board_sprites.update()

        # Render
        screen.fill(shadow)
        render_main(screen)
        pygame.display.flip()
        pygame.display.update()


main()
