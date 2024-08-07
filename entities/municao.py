from entities.collectible import Collectible
from parameters import *

class Municao(Collectible):
	def __init__(self):
		super().__init__('municao', "./assets/collectibles/Medium_Shell.png", 25, 10)
		self.create_collectible()

	def main(self, screen, player1, player2, game_time, dict_collectibles):
		self.show_in_screen(self.image, screen)
		self.check_collectible_timeout(game_time, dict_collectibles)

		collision = self.check_collision(player1, player2)
		if collision is not False:
			if collision == 1:
				player1.ammo += 3
			else:
				player2.ammo += 3
			AMMO_COLLISION_SOUND.play()
			self.remove_from_screen(dict_collectibles)