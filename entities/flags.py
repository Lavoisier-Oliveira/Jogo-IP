import random
import pygame

class Flag:
	def __init__(self, position, image, current_position=[]):
		self.position = list(position)
		self.image = image
		self.current_position = [0, 0]

	def render(self, display):
		self.current_position[0], self.current_position[1] = random.uniform(100, self.position[0]), random.uniform(100, self.position[1])
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	def update(self, display):
		display.blit(self.image, (self.current_position[0], self.current_position[1]))