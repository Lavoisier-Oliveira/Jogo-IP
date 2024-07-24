import pygame
import sys
import random

from parameters import *
from entities.tank import Tank
from entities.flags import Flag

# PyGame Setup
pygame.init()
monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h))
pygame.display.set_caption(CAPTION)
background_image = pygame.image.load(R'assets\backgrounds\back2.jpg') # Load the background image
background_image = pygame.transform.scale(background_image, (monitor.current_w, monitor.current_h)) # Resize the background image to fit the screen
clock = pygame.time.Clock()

flag_img = pygame.image.load('assets/Effects/Exhaust_Fire.png')
flag = Flag((monitor.current_w, monitor.current_h), flag_img)
flag_cycle, flag_p = 1, False

p1 = Tank('A', 2, [100, 100], 50, 10, KEYS_PLAYER_1)
p2 = Tank('B', 2, [200, 200], 50, 10, KEYS_PLAYER_2)
p3 = Tank('C', 2, [300, 300], 50, 10, KEYS_PLAYER_3)
p4 = Tank('D', 2, [400, 400], 50, 10, KEYS_PLAYER_4)

game_is_running = True
while game_is_running:
	game_time = pygame.time.get_ticks()
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # para sair, pressione o X da janela ou ESC
			game_is_running = False
	
	screen.blit(background_image, (0,0))  # Desenhar o background

	# Atualizar o estado do tanque
	for player in Tank.tanks:
		player.update()
	
	if game_time > 5000*flag_cycle:
		flag.render(screen)
		flag_cycle += 1
		flag_p = True

	if flag_p:
		flag.update(screen)	

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()