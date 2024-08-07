import pygame

# Animação de Explosão
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y, frames=8):
		super(Explosion, self).__init__()
		self.frames_imgs = []
		# Adicionando a lista de frames possíveis todas as imagens de explosão
		for i in range(8):
			explosion_frame = pygame.image.load(f'Assets/Explosions/Explosion_{i+1}.png')
			w, h = explosion_frame.get_size()
			width = int(w * 0.5)
			height = int(h * 0.5)
			explosion_frame = pygame.transform.scale(explosion_frame, (width, height))
			self.frames_imgs.append(explosion_frame)
		self.frames = frames
		self.index = 0
		self.image = self.frames_imgs[self.index]
		self.rect = self.image.get_rect(center=(x, y))

		self.frame_now = 0

	# Função para atualizar o frame atual e gerar a imagem do frame atual
	def update(self):
		self.frame_now += 1
		if self.frame_now >= 7:
			self.index += 1
			if self.index >= self.frames:
				self.kill()
			else:
				self.image = self.frames_imgs[self.index]
				self.frame_now = 0
