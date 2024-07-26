import pygame
import sys

from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint

# PyGame Setup
pygame.init()
monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h))
pygame.display.set_caption(CAPTION)
background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
background_image = pygame.transform.scale(background_image, (monitor.current_w, monitor.current_h))  # Resize the background image to fit the screen
clock = pygame.time.Clock()

p1 = Tank('A', randint(1, 8), [100, 100], 40, 15, KEYS_PLAYER_1)
p2 = Tank('B', randint(1, 8), [200, 200], 50, 11, KEYS_PLAYER_2)
p3 = Tank('C', randint(1, 8), [300, 300], 60, 10, KEYS_PLAYER_3)
p4 = Tank('D', randint(1, 8), [400, 400], 90, 7, KEYS_PLAYER_4)

# Instanciando a classe Flag 
flag_img = pygame.image.load('assets/Collectibles/bandeira.png') # Imagem da bandeira
flag_img = pygame.transform.scale(flag_img, (monitor.current_w//37, monitor.current_h//12)) # Transformando o tamanho da imagem da bandeira
flag = Flag((monitor.current_w, monitor.current_h), flag_img) # Classe Flag instanciada 
flag_cycle, del_flag_time, flag_p = 1, 1, False # Variavéis para fazer a checagem das condições da bandeira na tela

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
	
	# Gerando uma bandeira em um local aleatório no intervalo de 7 segundos
	if game_time > 7000*flag_cycle and game_time < 10000*flag_cycle:
		flag.render(screen) # Função da classe Flag para renderizar a flag em um local aleatório
		flag_cycle += 1
		flag_p = True
	# Após 3 segundos que a bandeira foi gerada, ela não deve mais aparecer na tela
	if game_time > 10000*del_flag_time: 
		flag_p = False
		del_flag_time += 1
	if flag_p:
		flag.update(screen)	# Função para sempre renderizar a bandeira na tela

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
