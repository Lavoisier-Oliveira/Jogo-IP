import random
import pygame
from parameters import *

class Municao:
	def __init__(self):
		self.position = SCREEN_SIZE
		self.image = pygame.image.load('assets/Effects/Medium_Shell.png')
		self.size = (SCREEN_WIDTH//25, SCREEN_HEIGHT//10)
		self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
		self.current_position = [0, 0]

	# Função que retorna o próprio retângulo da bandeira
	def rect_self(self):
		return pygame.Rect(self.current_position[0], self.current_position[1], self.size[0], self.size[1])

	# Função que renderiza a imagem da munição em um local aleatório da tela
	def render(self, display):
		self.current_position[0], self.current_position[1] = random.uniform(SCREEN_WIDTH*0.1, SCREEN_WIDTH*0.9), random.uniform(SCREEN_HEIGHT*0.1, SCREEN_HEIGHT*0.9)
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	# Função que guarda a posição atual da munição, e continua renderizando na tela
	def update(self, display):
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	def collisao_municao(self, display, game_time, municao_aparecer, municao_desaparecer, municao_na_tela, player1, player2, municao_p1, municao_p2):
		font = pygame.font.Font(None, 48)
		display.blit(self.image, (SCREEN_WIDTH*0.07, SCREEN_HEIGHT*0.9))
		display.blit(self.image, (SCREEN_WIDTH*0.82, SCREEN_HEIGHT*0.9))
		municao_tab1 = font.render(f': {municao_p1}', True, (0, 0, 0))
		municao_tab2 = font.render(f': {municao_p2}', True, (0, 0, 0))
		display.blit(municao_tab1, (SCREEN_WIDTH*0.1, SCREEN_HEIGHT*0.93))
		display.blit(municao_tab2, (SCREEN_WIDTH*0.85, SCREEN_HEIGHT*0.93))

		# Gerando a munição do tanque em um local aleatório no intervalo de 7 segundos
		if game_time > 7000*municao_aparecer and game_time < 10000*municao_aparecer:
			self.render(display) # Função da classe Flag para renderizar a flag em um local aleatório
			municao_aparecer += 1
			municao_na_tela= True
		# Após 3 segundos que a munição foi gerada, ela não deve mais aparecer na tela
		if game_time > 10000*municao_desaparecer: 
			municao_na_tela = False
			municao_desaparecer += 1
		if municao_na_tela:
			self.update(display)# Função para sempre renderizar a munição na tela	
		
		if player1.rect.colliderect(self.rect_self()):
			if municao_p1 < 21:
				if municao_na_tela and municao_p1 < 21:
					municao_p1 += 1
				municao_na_tela = False
		elif player2.rect.colliderect(self.rect_self()):
			if municao_p2 < 21:
				if municao_na_tela:
					municao_p2 += 1
				municao_na_tela = False
		return (municao_p1, municao_p2, municao_aparecer, municao_desaparecer, municao_na_tela)