import pygame
import sys
from settings import *
from entities.tank import Tank

# PyGame Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

tank = Tank('B', 2)

while True:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Atualizar o estado do tanque
	tank.update() 

	# Renderizar o jogo
	screen.fill((0, 0, 0))  # Preencher a tela com uma cor (preto)
	screen.blit(tank.image, tank.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

###	screen.pygame.image.load(f"assets/backgrounds/back1.jpg")  # Preencher a tela com uma cor (preto)