import pygame
from parameters import *
from entities.tank import Tank

class GameScreen:
	def __init__(self):
		self.background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
		self.background_image = pygame.transform.scale(self.background_image, SCREEN_SIZE)  # Resize the background image to fit the screen

	def handle_event(self, event):
		pass

	def update(self):
		pass

	def draw(self, screen):
		screen.blit(self.background_image, (0, 0))  # Desenhar o background

		# Atualizar o estado do tanque
		for player in Tank.tanks:
			player.update()

		for player in Tank.tanks:
			screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	def end_surface(self, loser, screen, event):
		if loser is not None:
			end_font = pygame.font.Font(None, 74)
			end_text = end_font.render(f"Fim de jogo para o(a) {loser}", True, BLACK_COLOR)
			title_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
			screen.blit(end_text, title_rect)
			transparent_surface = pygame.Surface(SCREEN_SIZE)
			transparent_surface.fill(BLACK_COLOR)
			transparent_surface.set_alpha(100)
			screen.blit(transparent_surface, (0, 0))
			# Restart
			restart = pygame.Rect((SCREEN_WIDTH // 2 - 125), SCREEN_HEIGHT // 1.3, 250, 80)
			pygame.draw.rect(screen, GREEN_LIGHT_COLOR, restart) # cria o botão de início
			font = pygame.font.Font(None, 55)
			button = font.render("RESTART",True, WHITE_COLOR)
			text = button.get_rect(center=restart.center)
			screen.blit(button, text)
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				if restart.collidepoint(x, y):
					Tank.tanks = []
					return True
				