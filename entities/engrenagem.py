from entities.collectible import Collectible
from parameters import *

class Engrenagem(Collectible):
	def __init__(self):
		super().__init__('engrenagem', "./assets/collectibles/engrenagem.png", 35, 20)
		self.create_collectible()


	def main(self, screen, player1, player2, game_time, dict_collectibles):
		self.show_in_screen(self.image, screen)
		self.check_collectible_timeout(game_time, dict_collectibles)

		collision = self.check_collision(player1, player2)
		if collision is not False:
			if collision == 1:
				player1.gears += 1
			else:
				player2.gears += 1
			GEAR_COLLISION_SOUND.play()
			self.remove_from_screen(dict_collectibles)