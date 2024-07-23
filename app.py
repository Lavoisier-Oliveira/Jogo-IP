import pygame
import sys
from settings import *
from entities.tank import Tank

# PyGame Setup
pygame.init()
monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()


p1 = Tank('A', 2, [100, 100], 50, 10, (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d))
p2 = Tank('B', 2, [200, 200], 50, 10, (pygame.K_g, pygame.K_y, pygame.K_h, pygame.K_j))
p3 = Tank('C', 2, [300, 300], 50, 10, (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT))
p4 = Tank('D', 2, [400, 400], 50, 10, (pygame.K_KP4, pygame.K_KP8, pygame.K_KP5, pygame.K_KP6))

while True:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # para sair, pressione o X da janela ou ESC
			pygame.quit()
			sys.exit()

	# Atualizar o estado do tanque
	for player in Tank.tanks:
		player.update()

	# Renderizar o jogo
	screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

