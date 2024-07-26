from random import uniform
import pygame

class Flag:
	def __init__(self, position, image, size: tuple, current_position=[]):
		self.position = list(position)
		self.image = image
		self.size = size
		self.current_position = [0, 0]

	# Função que renderiza a imagem de uma bandeira em um local aleatório do display
	def render(self, display):
		self.current_position[0], self.current_position[1] = uniform(80, self.position[0] - 80), uniform(80, self.position[1] - 80)
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	# Função que guarda a posição atual da bandeira, e continua renderizando a bandeira na tela
	def update(self, display):
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	# Função que retorna o próprio retângulo da bandeira
	def rect_self(self, flag_in_map):
		if flag_in_map:
			return pygame.Rect(self.current_position[0], self.current_position[1], self.size[0], self.size[1])
		else:
			return pygame.Rect(9999999, 99999999, self.size[0], self.size[1])