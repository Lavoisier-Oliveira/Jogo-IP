import pygame
import math
from parameters import *

pygame.init()
monitor = pygame.display.Info()

class Tank:
	tanks = []

	angle = 0  # Armazena o ângulo atual # talvez seja possível armar uma equação que, baseado na posição inicial do tanque, forneça o angulo inicial tal que este aponte para o centro da tela - seria preciso passar as dimensoes da tela para o construtor e importar uma função trigonometrica para tranformar os catetos em angulo # dessa forma o angulo seria atribuido no construtor
	vx, vy = 0, 0

	def __init__(self, color: str, model: int, initial_pos: list, size: int, speed: int, keys: tuple):
		self.keys = keys  # pass pygame.K_x in the order: left, up, down, right
		self.size = size
		self.image = pygame.image.load(f"./Assets/Tanks/Hulls_Color_{color}/Hull_0{model}.png")  # Carrega a imagem do tanque
		self.image = pygame.transform.scale(self.image, (self.size, self.size)).convert_alpha()  # Redimensiona a imagem do tanque e tranforma num formato mais versatil para o pygame operar
		self.original_image = self.image.copy()  # Guarda a imagem original para futuras rotações
		self.cannon_image = pygame.image.load(f"./Assets/Weapons/Weapon_Color_{color}/Gun_0{model}.png")
		self.cannon_image = pygame.transform.scale(self.cannon_image, (self.size, self.size)).convert_alpha()
		self.original_cannon_image = self.cannon_image.copy()
		
		self.rect = self.image.get_rect(center=initial_pos)
		self.speed = speed  # pixels percorridos por tick
		self.mask = pygame.mask.from_surface(self.image) # Criando uma nova superfície a partir da imagem do tanque, que realiza a dimensão pixel a pixel
		self.gears = INITIAL_QTD_GEARS
		self.ammo = INITIAL_QTD_AMMO
		self.flags = 0
		self.is_alive = True

		Tank.tanks.append(self)

	def read_input(self):

		k = 100  # coeficiente de inercia - diretamente proporcional à aceleração  # valores recomendados : 10 até 200
		aceleracao = k/((self.speed*(self.size**2))**0.5)  # formula empirica (saí testando e ficou top)
		desaceleracao = aceleracao

		keys = pygame.key.get_pressed()
		left_key, up_key, down_key, right_key = keys[self.keys[0]], keys[self.keys[1]], keys[self.keys[2]], keys[self.keys[3]]

		# X axis
		if left_key ^ right_key:  # acelera
			"""
			IMPLEMENTAR:
			caso o tank acelere para o sentido oposto ao deslocamento, sua velocidade deve diminuir 2x mais rapido do que o faria caso estivesse apenas dissipando
			"""
			if right_key:
				self.vx = self.vx + aceleracao if self.vx + aceleracao <= self.speed else self.speed
			elif left_key:
				self.vx = self.vx - aceleracao if self.vx - aceleracao >= -self.speed else -self.speed
		else:  # desacelera
			if self.vx < 0:
				self.vx = self.vx + desaceleracao if self.vx < -desaceleracao else 0
			elif self.vx > 0:
				self.vx = self.vx - desaceleracao if self.vx > desaceleracao else 0
		# Y axis
		if up_key ^ down_key:  # acelera
			if up_key:
				self.vy = self.vy - aceleracao if self.vy - aceleracao >= -self.speed else -self.speed
			elif down_key:
				self.vy = self.vy + aceleracao if self.vy + aceleracao <= self.speed else self.speed
		else:  # desacelera
			if self.vy < 0:
				self.vy = self.vy + desaceleracao if self.vy < -desaceleracao else 0
			elif self.vy > 0:
				self.vy = self.vy - desaceleracao if self.vy > desaceleracao else 0

		# calibrar vetores x e y quando o resultante ultrapassa o limite(self.speed)
		if (self.vx**2 + self.vy**2)**0.5 > self.speed:
			if self.vx >= self.speed/(2**0.5):
				self.vx -= 1*desaceleracao
			elif self.vx <= -self.speed/(2**0.5):
				self.vx += 1*desaceleracao
			if self.vy >= self.speed/(2**0.5):
				self.vy -= 1*desaceleracao
			elif self.vy <= -self.speed / (2 ** 0.5):
				self.vy += 1*desaceleracao

	def angle_image(self):
		self.angle = math.degrees(math.atan2(-self.vy, self.vx))-90
		# Preserve the center position while rotating
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.cannon_image = pygame.transform.rotate(self.original_cannon_image, self.angle)
		self.rect = self.image.get_rect(center=self.rect.center)  # Atualiza o retângulo da imagem com o centro preservado

	def move(self):

		test_rect = self.rect.copy()  # um rect de teste simulará o movimento do input, e então testaremos se houve colisão

		# check X collision
		test_rect.centerx += self.vx
		x_collision = False
		if 0 <= test_rect.left and test_rect.right <= monitor.current_w:
			for player in Tank.tanks:
				if player is not self:
					if test_rect.colliderect(player):
						x_collision = True
		else:
			x_collision = True

		# check Y collision
		test_rect.centerx -= self.vx
		test_rect.centery += self.vy
		y_collision = False
		if 0 <= test_rect.top and test_rect.bottom <= monitor.current_h:
			for player in Tank.tanks:
				if player is not self:
					if test_rect.colliderect(player):
						y_collision = True
		else:
			y_collision = True

		if not x_collision:
			self.rect.centerx += self.vx
		if not y_collision:
			self.rect.centery += self.vy

	def update(self):
		if self.is_alive:
			self.read_input()
			if self.vx != 0 or self.vy != 0:
				self.move()
				self.angle_image()
