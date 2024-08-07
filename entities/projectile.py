import math
import pygame
from Entities.animations import Explosion
from parameters import *

# Função para definir o player que está realizando o disparo do projétil
def main(player1, player2, screen, key):
	if key == PLAYER_1_SHOT_BUTTON and player1.ammo > 0 and player1.is_alive:
		PROJECTILE_SOUND.play()
		projectile = Projectile(player1.rect.centerx, player1.rect.centery, -90-player1.angle, player2, screen)
		PROJECTILE_SPRITES.add(projectile)
		player1.ammo -= 1
	elif key == PLAYER_2_SHOT_BUTTON and player2.ammo > 0 and player2.is_alive:
		PROJECTILE_SOUND.play()
		projectile = Projectile(player2.rect.centerx, player2.rect.centery, -90-player2.angle, player1, screen)
		PROJECTILE_SPRITES.add(projectile)
		player2.ammo -= 1

# Instanciando os grupos de sprites para renderizar as explosões e projéteis
def instance_sprites(screen):
	PROJECTILE_SPRITES.update(EXPLOSION_SPRITES)
	PROJECTILE_SPRITES.draw(screen)
	EXPLOSION_SPRITES.update()
	EXPLOSION_SPRITES.draw(screen)

class Projectile(pygame.sprite.Sprite):
	def __init__(self, x, y, angle, player, display):
		super(Projectile, self).__init__()
		self.size = [SCREEN_WIDTH//23, SCREEN_HEIGHT//10]
		self.image = pygame.image.load(R"assets/collectibles/Medium_Shell.png")
		self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
		self.image = pygame.transform.rotate(self.image, -90-angle)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.angle = math.radians(angle)
		self.speed = BULLET_SPEED
		self.speed_x = math.cos(self.angle) * self.speed
		self.speed_y = math.sin(self.angle) * self.speed
		self.player = player
		self.display = display
		self.mask = pygame.mask.from_surface(self.image)
	
	# Renderizando as sprites, e checando se houve colisão
	def update(self, explosion_sprite):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
			self.kill()
		self.collision(explosion_sprite)

	# Função que realiza a checagem da colisão e cria a animação de explosão para caso haja uma colisão
	def collision(self, explosion_sprite):
		relative_position = (self.rect.x - self.player.rect.x, self.rect.y - self.player.rect.y) # Posição relativa entre o projétil e o player
		collision_point = self.player.mask.overlap(self.mask, relative_position)
		if collision_point:
			self.kill()
			explosion = Explosion(self.player.rect.centerx, self.player.rect.centery)
			explosion_sprite.add(explosion)
			PROJECTILE_COLLISION_SOUND.play()
			self.player.gears = max(0, self.player.gears - BULLET_DAMAGE)