"""This is a simple version of arkanoid game"""

import sys
import pygame
import random
from arkanoid import brick_pack
from arkanoid import settings

# Initializing text font
pygame.font.init()
txt_font = pygame.font.SysFont("Score: ", settings.display_height//44)

# Initializing sprite lists
ball_paddle_sprites = pygame.sprite.Group()
brick_sprites = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    """Initiates a moving ball and its' attributes"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(settings.ball_dimentions)
        self.image.fill(settings.light_blue)
        self.rect = self.image.get_rect()
        self.rect.center = self.init_position()
        self.direction = random.choice([settings.diagonal_left, settings.diagonal_right])
        self.score = 0

    def update(self):
        self.move()

    def init_position(self):
        # Initialize position of the ball
        init_position = (paddle.rect.center[0],
                         (paddle.rect.center[1] - (settings.paddle_dimentions[1] / 2)
                          - (settings.ball_dimentions[1] / 2)))
        return init_position

    def collide(self):
        # If hit bricks
        self.direction[1] *= -1
        self.score += 1

    def move(self):
        self.containment()
        self.rect[1] += self.direction[1]
        self.rect[0] += self.direction[0]
        self.deflect()
        self.ball_loss()

    def containment(self):
        if self.rect.right >= settings.display_width or self.rect.left <= 0:
            self.direction[0] *= -1
        if self.rect.top <= 0:
            self.direction[1] *= -1

    def ball_loss(self):
        ###
        if self.rect.bottom >= settings.display_height:
            self.reset()
            reset_bricks()

    def reset(self):
        self.rect.center = self.init_position()
        self.direction[1] *= -1
        self.reset_angle()
        self.score = 0

    def deflect(self):
        # If hit Paddle, deflect
        if (self.rect.bottom == paddle.rect.top and
            (paddle.rect.left <= self.rect.left <= paddle.rect.right or
             paddle.rect.left <= self.rect.right <= paddle.rect.right)):
            self.direction[1] *= -1
            self.interact_ball_paddle()

    def reset_angle(self):
        self.direction = random.choice([settings.diagonal_left, settings.diagonal_right])

    def interact_ball_paddle(self):
        # When Paddle is moving, effects balls direction/speed
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and paddle.rect.left > 0:
            self.direction[0] -= settings.speed // 2
        elif keystate[pygame.K_RIGHT] and paddle.rect.right < settings.display_width:
            self.direction[0] += settings.speed // 2


class Paddle(pygame.sprite.Sprite):
    """Initiates paddle class and it's attributes"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(settings.paddle_dimentions)
        self.image.fill(settings.orange)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.display_width // 2,
                            settings.display_height - 2 * settings.paddle_dimentions[1])
        self.x_direction = 0

    def update(self):
        # Up-dates classes' position according to user's imput
        self.x_direction = 0
        self.move()
        self.rect.x += self.x_direction

    def move(self):
        # Creates movement and constrains object within screen dimentions
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.x_direction = -settings.speed
        elif keystate[pygame.K_RIGHT]:
            if self.rect.right < settings.display_width:
                self.x_direction = settings.speed

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
paddle = Paddle()
ball = Ball()

ball_paddle_sprites.add(paddle)
ball_paddle_sprites.add(ball)


def create_brick_list():
    # Creates and adds bricks into a list
    i = 9
    point_value = 3
    coordinates = [settings.display_width // 20 + settings.brick_width / 6, settings.display_height // 20]
    while i > 0:
        brick = brick_pack.Brick(point_value, (coordinates))
        coordinates[0] += settings.brick_width * 1.1
        brick_sprites.add(brick)
        i -= 1
    return brick_sprites


def reset_bricks():
    # Reset brick list
    brick_sprites.empty()
    create_brick_list()
    return brick_sprites


def render_text(screen):
    text = txt_font.render("Score: {0}".format(ball.score), 1, (0, 0, 0))
    return screen.blit(text, (5, 10))


def render_main(screen):
    ball_paddle_sprites.draw(screen)
    brick_sprites.draw(screen)
    render_text(screen)

def update_collisions():
    list_of_collisions = pygame.sprite.spritecollide(ball, brick_sprites, False)
    if list_of_collisions:
        ball.collide()
        for instance in list_of_collisions:
            instance.collide()

# Game main
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings.display_width, settings.display_height))
    create_brick_list()

    while True:
        # Events
        clock.tick(settings.FPS)
        control()
        update_collisions()

        # Update
        ball_paddle_sprites.update()

        # Render
        render_main(screen)
        pygame.display.flip()
        pygame.display.update()
        screen.fill(settings.shadow)


main()
