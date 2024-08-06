import pygame
import random
from parameters import *

class Collectible:
	def __init__(self, name, image_path, size_w_ratio, size_h_ratio):
		self.size_w = SCREEN_WIDTH // size_w_ratio
		self.size_h = SCREEN_HEIGHT // size_h_ratio
		self.size = (self.size_w, self.size_h)
		self.name = name

		self.image = pygame.image.load(image_path)
		self.image = pygame.transform.scale(self.image, self.size)

		self.pos_x = self.pos_y = 0

		self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size_w, self.size_h)
		self.spawn_time = pygame.time.get_ticks()

	def add_collectible_to_dict(self, dict_collectibles):
		dict_collectibles[self.name].append(self)

	def create_collectible(self):
		self.pos_x = random.randint(int(SCREEN_WIDTH*0.001), int(SCREEN_WIDTH * 0.95))
		self.pos_y = random.randint(int(SCREEN_HEIGHT * 0.05), int(SCREEN_HEIGHT * 0.85))
		self.rect = self.rect_self()

	def show_in_screen(self, image, screen):
		screen.blit(image, (self.pos_x, self.pos_y))

	def check_collectible_timeout(self, game_time, dict_collectibles):
		if self.spawn_time + COLLECTIBLE_REMOVE_TIME < game_time:
			self.remove_from_screen(dict_collectibles)

	def remove_from_screen(self, dict_collectibles):
		dict_collectibles[self.name].remove(self)

	def rect_self(self):
		return pygame.Rect(self.pos_x, self.pos_y, self.size_w, self.size_h)
	
	def check_collision(self, player1, player2):
		if self.rect.colliderect(player1.rect):
			return 1
		elif self.rect.colliderect(player2.rect):
			return 2
		return False