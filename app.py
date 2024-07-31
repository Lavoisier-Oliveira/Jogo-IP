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

p1 = Tank('A', 2, [100, 100], 40, 15, KEYS_PLAYER_1, 20)
p2 = Tank('B', 2, [200, 200], 50, 11, KEYS_PLAYER_2, 20)

imagem_municao = pygame.image.load('assets\Effects\Medium_Shell.png')
tamanho_imagem = (monitor.current_w//25, monitor.current_h//12)
imagem_municao = pygame.transform.scale(imagem_municao, (tamanho_imagem[0], tamanho_imagem[1]))
municao = Municao((monitor.current_w, monitor.current_h), imagem_municao, tamanho_imagem)
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

	qnt_municao1 = font.render(f'Munição: {p1.municao}', True, (0, 0, 0))
	screen.blit(qnt_municao1, (10, background_image.get_height() - 40))
	qnt_municao2 = font.render(f'Munição: {p2.municao}', True, (0, 0, 0))
	screen.blit(qnt_municao2, (background_image.get_width() -100, background_image.get_height() - 40))


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

	if p1.rect.colliderect(municao.rect_municao()):
		if(aparicao_municao):
			p1.municao += 3
		aparicao_municao = False
	elif p2.rect.colliderect(municao.rect_municao()):
		if aparicao_municao:
			p2.municao += 3
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
