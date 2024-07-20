import pygame
import math

class Tank():
	def __init__(self, color_tank, choice_tank):
		self.image = pygame.image.load(f"assets/Hulls_Color_{color_tank}/Hull_0{choice_tank}.png")  # Carrega a imagem do tanque
		self.image = pygame.transform.scale(self.image, (80,80))  # Redimensiona a imagem do tanque
		self.pos = pygame.math.Vector2(400, 300)  # Posição inicial do tanque (centro da tela)
		self.player_speed = 3
		self.angle = 0  # Armazena o ângulo atual
		self.original_image = self.image.copy()  # Guarda a imagem original para futuras rotações
		self.rect = self.image.get_rect(center=self.pos)

	def player_input(self):   
		self.velocity_x, self.velocity_y = 0, 0

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.velocity_y = -self.player_speed
		if keys[pygame.K_a]:
			self.velocity_x = -self.player_speed
		if keys[pygame.K_s]:
			self.velocity_y = self.player_speed
		if keys[pygame.K_d]:
			self.velocity_x = self.player_speed

		if self.velocity_x != 0 and self.velocity_y != 0:  # se estiver movendo na diagonal
			self.velocity_x /= math.sqrt(2)
			self.velocity_y /= math.sqrt(2)

	def turn(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]: 
			self.angle = 0
		if keys[pygame.K_a]:
			self.angle = 90
		if keys[pygame.K_s]:
			self.angle = 180
		if keys[pygame.K_d]:
			self.angle = -90
		if keys[pygame.K_w] and keys[pygame.K_d]:
			self.angle = -45
		if keys[pygame.K_s] and keys[pygame.K_d]:
			self.angle = -135
		if keys[pygame.K_s] and keys[pygame.K_a]:
			self.angle = 135
		if keys[pygame.K_w] and keys[pygame.K_a]:
			self.angle = 45

		# Preserve the center position while rotating
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center=self.rect.center)  # Atualiza o retângulo da imagem com o centro preservado

	def move(self):
		self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)
		self.rect.center = self.pos  # Atualiza a posição do retângulo com a nova posição

	def update(self):
		self.player_input()
		self.move()
		self.turn()
