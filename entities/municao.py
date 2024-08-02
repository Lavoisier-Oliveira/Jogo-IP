from random import uniform
import pygame
from parameters import *

class Municao:
	def __init__(self):
		self.position = SCREEN_SIZE
		self.image = pygame.image.load('assets/Effects/Medium_Shell.png')
		self.size = (SCREEN_WIDTH//25, SCREEN_HEIGHT//12)
		self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
		self.current_position = [0, 0]

	# Função que renderiza a imagem da munição em um local aleatório da tela
	def render(self, display):
		self.current_position[0], self.current_position[1] = uniform(80, self.position[0] - 80), uniform(80, self.position[1] - 80)
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	# Função que guarda a posição atual da munição, e continua renderizando a bandeira na tela
	def update(self, display):
		display.blit(self.image, (self.current_position[0], self.current_position[1]))

	def collisao_municao(self, display, game_time, municao_aparecer, municao_desaparecer, municao_na_tela, player1, player2, score1, score2):
		font = pygame.font.Font(None, 48)
		score_tab1 = font.render(f': {score1}', True, (0, 0, 0))
		display.blit(self.image, (SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.9))
		display.blit(score_tab1, (SCREEN_WIDTH*0.036, SCREEN_HEIGHT*0.93))
		score_tab2 = font.render(f': {score2}', True, (0, 0, 0))
		display.blit(self.image, (SCREEN_WIDTH*0.904, SCREEN_HEIGHT*0.9))
		display.blit(score_tab2, (SCREEN_WIDTH*0.93, SCREEN_HEIGHT*0.93))

		# Gerando uma bandeira em um local aleatório no intervalo de 7 segundos
		if game_time > 7000*municao_aparecer and game_time < 10000*municao_aparecer:
			self.render(display) # Função da classe Flag para renderizar a flag em um local aleatório
			municao_aparecer += 1
			municao_na_tela= True
		# Após 3 segundos que a bandeira foi gerada, ela não deve mais aparecer na tela
		if game_time > 10000*municao_desaparecer: 
			municao_na_tela = False
			municao_desaparecer += 1
		if municao_na_tela:
			self.update(display )# Função para sempre renderizar a bandeira na tela	
		
		if player1.rect.colliderect(self.rect_self()):
			if score1 < 21:
				if municao_na_tela and score1 < 21:
					score1 += 1
				municao_na_tela = False
		elif player2.rect.colliderect(self.rect_self()):
			if score2 < 21:
				if municao_na_tela:
					score2 += 1
				municao_na_tela = False
		return (score1, score2, municao_aparecer, municao_desaparecer, municao_na_tela)
	# Função que retorna o próprio retângulo da bandeira
	def rect_self(self):
            return pygame.Rect(self.current_position[0], self.current_position[1], self.size[0], self.size[1])
