import pygame
import sys
from parameters import *
from entities.tank import Tank
from random import randint
from entities.municao import Municao

# PyGame Setup
pygame.init()
monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h))
background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
background_image = pygame.transform.scale(background_image, (monitor.current_w, monitor.current_h))  # Resize the background image to fit the screen
clock = pygame.time.Clock()

p1 = Tank('A', 2, [100, 100], 40, 15, KEYS_PLAYER_1, 20)
p2 = Tank('B', 2, [200, 200], 50, 11, KEYS_PLAYER_2, 20)

municao = Municao()
ciclo_aparecer, ciclo_desaparecer, aparicao_municao = 1, 1, False

game_is_running = True
while game_is_running:
	font = pygame.font.Font(None, 48)
	game_time = pygame.time.get_ticks()
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # para sair, pressione o X da janela ou ESC
			game_is_running = False
	
	screen.blit(background_image, (0, 0))  # Desenhar o background

	# Atualizar o estado do tanque
	for player in Tank.tanks:
		player.update()

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição
		
	municao_interacao = municao.collisao_municao(screen, game_time, ciclo_aparecer, ciclo_desaparecer, aparicao_municao, p1, p2, p1.municao, p2.municao)
	p1.municao, p2.municao, ciclo_aparecer, ciclo_desaparecer, aparicao_municao = municao_interacao[0], municao_interacao[1], municao_interacao[2], municao_interacao[3], municao_interacao[4]
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
