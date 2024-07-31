import pygame
from parameters import *
from entities.tank import Tank

class GameScreen:
	def __init__(self):
		self.background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
		self.background_image = pygame.transform.scale(self.background_image, SCREEN_SIZE)  # Resize the background image to fit the screen

	def handle_event(self, event):
		pass

	def update(self):
		pass

	def draw(self, screen):
		screen.blit(self.background_image, (0, 0))  # Desenhar o background

		# Atualizar o estado do tanque
		for player in Tank.tanks:
			player.update()

		for player in Tank.tanks:
			screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen