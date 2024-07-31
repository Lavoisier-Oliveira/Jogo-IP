import pygame
from parameters import *

class TankSelectionScreen:
	def __init__(self):
		self.start_game = False
		self.colors = ('A', 'B', 'C', 'D')
		self.color = self.colors[0]
		self.model = 1

		self.font = pygame.font.Font(None, 50)
		self.tank_image = self.tank_image = pygame.image.load(f"assets/Hulls_Color_{self.color}/Hull_0{self.model}.png")

		# Retângulo que contém a imagem do tanque
		self.tank_img_rect = self.tank_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

		# Retângulos dos botões
		self.left_button_rect = pygame.Rect(self.tank_img_rect.left-50, self.tank_img_rect.bottom, 50, 50) # Botão da esquerda do modelo do tanque
		self.left_color_rect = pygame.Rect(self.left_button_rect.left, self.left_button_rect.bottom, 50, 50) # Botão da esquerda da cor do tanque
		self.right_button_rect = pygame.Rect(self.tank_img_rect.right, self.left_button_rect.top, 50, 50) # Botão da direita do modelo do tanque
		self.right_color_left = pygame.Rect(self.right_button_rect.left, self.left_button_rect.bottom, 50, 50) # Botão da direita da cor do tanque

		self.modelo_text_rect = pygame.Rect(self.tank_img_rect.left, self.tank_img_rect.bottom, self.tank_img_rect.width, 50) # Retângulo do texto do modelo
		self.color_text_rect = pygame.Rect(self.modelo_text_rect.left, self.left_button_rect.bottom, self.tank_img_rect.width, 50) # Retângulo do texto da cor
		self.select_tank_button = pygame.Rect((SCREEN_WIDTH - 200) // 2, 550, 200, 100) # Retângulo do botão de seleção do tanque

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			#  Aqui é feito o tratamento dos cliques nos botões, para que o usuário possa escolher o modelo e a cor do tanque

			# Verifica se o clique foi dentro do retângulo do botão do modelo do tanque
			if self.left_button_rect.collidepoint(event.pos):
				self.model = 8 if self.model == 1 else self.model - 1 # Mantém as escolhas no conjunto de 1 a 8
				self.tank_image = pygame.image.load(f"assets/Hulls_Color_{self.color}/Hull_0{self.model}.png")
			elif self.right_button_rect.collidepoint(event.pos):
				self.model = 1 if self.model == 8 else self.model + 1 # Mantém as escolhas no conjunto de 1 a 8
				self.tank_image = pygame.image.load(f"assets/Hulls_Color_{self.color}/Hull_0{self.model}.png")
			elif self.select_tank_button.collidepoint(event.pos):
				self.start_game = True

			# Verifica se o clique foi dentro do retângulo do botão da cor do tanque
			if self.left_color_rect.collidepoint(event.pos):
				self.color = self.colors[(self.colors.index(self.color) - 1) % len(self.colors)] # Mantém as escolhas no conjunto de A a D
				self.tank_image = pygame.image.load(f"assets/Hulls_Color_{self.color}/Hull_0{self.model}.png")
			elif self.right_color_left.collidepoint(event.pos):
				self.color = self.colors[(self.colors.index(self.color) + 1) % len(self.colors)] # Mantém as escolhas no conjunto de A a D
				self.tank_image = pygame.image.load(f"assets/Hulls_Color_{self.color}/Hull_0{self.model}.png")


	def draw(self, screen):
		screen.fill(BLACK_COLOR)
		self.font_titulo = pygame.font.Font(None, 75)
		text = self.font_titulo.render('Escolha seu tanque', True, WHITE_COLOR)
		text_w, text_h = text.get_size()
		screen.blit(text, ((SCREEN_WIDTH - text_w) // 2, 50, text_w, text_h))

		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.tank_img_rect)
		screen.blit(self.tank_image, self.tank_img_rect)

		# Seta para esquerda do modelo do tanque
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.left_button_rect) # Desenha o botão da esquerda do modelo do tanque
		left_text = self.font.render('<', True, WHITE_COLOR) # Desenha o texto do botão da esquerda do modelo do tanque
		left_text_rect = left_text.get_rect(center=self.left_button_rect.center) # Centraliza o texto no retângulo correspondente
		screen.blit(left_text, left_text_rect) # Insere o texto na tela do jogo

		# Seta para esquerda da cor do tanque
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.left_color_rect)
		color_left = self.font.render('<', True, WHITE_COLOR)
		left_color_rect = color_left.get_rect(center=self.left_color_rect.center)
		screen.blit(color_left, left_color_rect)

		# Seta para direita do modelo do tanque
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.right_button_rect)
		right_text = self.font.render('>', True, WHITE_COLOR)
		right_text_rect = right_text.get_rect(center=self.right_button_rect.center)
		screen.blit(right_text, right_text_rect)

		# Seta para direita da cor do tanque
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.right_color_left)
		color_right = self.font.render('>', True, WHITE_COLOR)
		right_color_left = color_right.get_rect(center=self.right_color_left.center)
		screen.blit(color_right, right_color_left)

		# Texto do Modelo
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.modelo_text_rect)
		modelo_text = self.font.render(f'MODELO {self.model}', True, WHITE_COLOR)
		modelo_text_rect = modelo_text.get_rect(center=self.modelo_text_rect.center)
		screen.blit(modelo_text, modelo_text_rect)

		# Texto da cor
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.color_text_rect)
		color_text = self.font.render(f'COR {self.color}', True, WHITE_COLOR)
		color_text_rect = color_text.get_rect(center=self.color_text_rect.center)
		screen.blit(color_text, color_text_rect)

		# Texto do Jogar
		pygame.draw.rect(screen, GREEN_LIGHT_COLOR, self.select_tank_button)
		select_text = self.font.render('JOGAR', True, WHITE_COLOR)
		select_text_rect = select_text.get_rect(center=self.select_tank_button.center)
		screen.blit(select_text, select_text_rect)