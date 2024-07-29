import pygame
import random


class Engrenagem:
    def __init__(self):
        self.image = pygame.image.load("assets\Collectibles\engrenagem.png")
        self.image = pygame.transform.scale(self.image, (50,50))  # Redimensiona a imagem do tanque
        self.rect = self.image.get_rect()

    def render(self,display):
        centro_x= random.randint(0, display.get_width())
        centro_y= random.randint(0, display.get_height())
        display.blit(self.image,(centro_x,centro_y))

    def death(self):
        del self
