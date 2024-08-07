import pygame
from Entities.collectible import Collectible
from parameters import *

class Flag(Collectible):
	def __init__(self):
		super().__init__('bandeira', "./assets/collectibles/bandeira_vermelha.png", 37, 12)
		self.blue_flag_image = pygame.image.load("./assets/collectibles/bandeira_azul.png")
		self.blue_flag_image = pygame.transform.scale(self.blue_flag_image, self.size)
		self.create_collectible()

	def main(self, screen, player1, player2, game_time, dict_collectibles):
		self.show_in_screen(self.image, screen)
		self.check_collectible_timeout(game_time, dict_collectibles)

		collision = self.check_collision(player1, player2)
		if collision is not False:
			if collision == 1:
				player1.flags += 1
			else:
				player2.flags += 1
			FLAG_COLLISION_SOUND.play()
			self.remove_from_screen(dict_collectibles)