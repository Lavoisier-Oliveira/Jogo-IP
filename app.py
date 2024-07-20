import pygame, sys
from settings import *
from entities.tank import Tank

# PyGame Setup
pygame.init()
screen = pygame.display.set_mode(TAM)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

tank = Tank('D', 3)

while True:
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Renderizar o jogo
	screen.fill((0, 0, 0))  # Preencher a tela com uma cor (preto)
	screen.blit(tank.image, tank.pos)  # Desenhar o tanque na nova posição

	# Flip() the display to put your work on screen
	pygame.display.flip()
	pygame.display.update()
	tank.update()