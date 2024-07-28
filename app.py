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
pygame.display.set_caption(CAPTION)
background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
background_image = pygame.transform.scale(background_image, (monitor.current_w, monitor.current_h))  # Resize the background image to fit the screen
clock = pygame.time.Clock()

p1 = Tank('A', 2, [100, 100], 40, 15, KEYS_PLAYER_1)
p2 = Tank('B', 2, [200, 200], 50, 11, KEYS_PLAYER_2)
p3 = Tank('C', 2, [300, 300], 60, 10, KEYS_PLAYER_3)
p4 = Tank('D', 2, [400, 400], 90, 7, KEYS_PLAYER_4)

imagem_municao = pygame.image.load('assets\Effects\Granade_Shell.png')
municao = Municao((monitor.current_w, monitor.current_h), (60, 60), imagem_municao)
ciclo_aparecer, ciclo_desaparecer, aparicao_municao = 1, 1, False

game_is_running = True
while game_is_running:
	game_time = pygame.time.get_ticks()
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # para sair, pressione o X da janela ou ESC
			game_is_running = False
	
	screen.blit(background_image, (0, 0))  # Desenhar o background

	# Atualizar o estado do tanque
	for player in Tank.tanks:
		player.update()

	#lógica da munição
	if game_time > 5000*ciclo_aparecer and game_time < 8000*ciclo_aparecer:
		municao.render(screen)
		aparicao_municao = True
		ciclo_aparecer += 1

	if game_time > 8000*ciclo_desaparecer:
		aparicao_municao = False
		ciclo_desaparecer += 1
		print('a')

	if aparicao_municao:
		municao.update(screen)
		if municao.interacao(p1.rect) or municao.interacao(p2.rect): #caso os tanques entreme em contato com a munição então ela desaparece
			aparicao_municao = False

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
