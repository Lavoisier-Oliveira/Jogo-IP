from random import uniform
import pygame
from parameters import *

class Flag:
	def __init__(self):
		self.position = SCREEN_SIZE
		self.image = [pygame.image.load('assets/Collectibles/bandeira.png'), pygame.image.load('assets/Collectibles/bandeira_azul.png')]
		self.size = (SCREEN_WIDTH//37, SCREEN_HEIGHT//12)
		self.image[0], self.image[1] = pygame.transform.scale(self.image[0], (self.size[0], self.size[1])), pygame.transform.scale(self.image[1], (self.size[0], self.size[1])) 
		self.current_position = [0, 0]

	# Função que renderiza a imagem de uma bandeira em um local aleatório do display
	def render(self, display):
		self.current_position[0], self.current_position[1] = uniform(80, self.position[0] - 80), uniform(80, self.position[1] - 80)
		display.blit(self.image[0], (self.current_position[0], self.current_position[1]))

	# Função que guarda a posição atual da bandeira, e continua renderizando a bandeira na tela
	def update(self, display):
		display.blit(self.image[0], (self.current_position[0], self.current_position[1]))

	def collision_flag(self, display, game_time, flag_gen, flag_del, flag_in_map, flag_taken, player1, player2, score1, score2):
		font = pygame.font.Font(None, 48)
		score_tab1 = font.render(f': {score1}', True, (0, 0, 0))
		display.blit(self.image[0], (SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.9))
		display.blit(score_tab1, (SCREEN_WIDTH*0.036, SCREEN_HEIGHT*0.93))
		score_tab2 = font.render(f': {score2}', True, (0, 0, 0))
		display.blit(self.image[1], (SCREEN_WIDTH*0.904, SCREEN_HEIGHT*0.9))
		display.blit(score_tab2, (SCREEN_WIDTH*0.93, SCREEN_HEIGHT*0.93))

		# Gerando uma bandeira em um local aleatório no intervalo de 7 segundos
		if game_time > 7000*flag_gen and game_time < 10000*flag_gen:
			self.render(display) # Função da classe Flag para renderizar a flag em um local aleatório
			flag_gen += 1
			flag_in_map, flag_taken = True, False
		# Após 3 segundos que a bandeira foi gerada, ela não deve mais aparecer na tela
		if game_time > 10000*flag_del: 
			flag_in_map = False
			flag_del += 1
		if flag_in_map:
			self.update(display)	# Função para sempre renderizar a bandeira na tela
		
		if player1.rect.colliderect(self.rect_self(flag_in_map)):
			if not flag_taken:
				score1 += 1
			flag_in_map, flag_taken = False, True
		elif player2.rect.colliderect(self.rect_self(flag_in_map)):
			if not flag_taken:
				score2 += 1
			flag_in_map, flag_taken = False, True
		return (score1, score2, flag_gen, flag_del, flag_in_map, flag_taken)
	# Função que retorna o próprio retângulo da bandeira
	def rect_self(self, flag_in_map):
		if flag_in_map:
			return pygame.Rect(self.current_position[0], self.current_position[1], self.size[0], self.size[1])
		else:
			return pygame.Rect(9999999, 99999999, self.size[0], self.size[1])