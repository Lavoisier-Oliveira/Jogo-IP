import pygame
import random

Class Enemy():
	def __init__(self, choice_inimigos):
		self.image = pygame.image.load(f"assets/inimigos/Hull_0{choice_inimigos}.png") 
		self.image = pygame.transform.scale(self.image, (50,50))  # Redimensiona a imagem do tanque
		self.speed = 1
		self.rect = self.image.get_rect(center=self.current_pos)
    self.rect.center = (random.randint(30, 370), 0)