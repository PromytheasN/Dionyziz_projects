import pygame
import settings

class Brick(pygame.sprite.Sprite):

    def __init__(self, point_value, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(settings.brick_dimentions)
        self.image.fill(settings.purple)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.point_value = point_value

    def collide(self):
        self.point_value -= 1
        if self.point_value == 0:
            self.kill()