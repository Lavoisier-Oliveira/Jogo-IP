import pygame
import sys
from parameters import *
from entities.tank import Tank
from random import randint
from entities.vida import Engrenagem

# PyGame Setup
pygame.init()
monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
screen = pygame.display.set_mode((monitor.current_w, monitor.current_h))
pygame.display.set_caption(CAPTION)
background_image = pygame.image.load(R'assets\backgrounds\back2.jpg')  # Load the background image
background_image = pygame.transform.scale(background_image, (monitor.current_w, monitor.current_h))  # Resize the background image to fit the screen
clock = pygame.time.Clock()

pygame.font.init()
font_padrao=pygame.font.get_default_font()
fonte_vida=pygame.font.SysFont(font_padrao,35)
vidap1=20
vidap2=20


engrenagem = Engrenagem(monitor.current_w, monitor.current_h)
engrenagem_vezes=1

p1 = Tank('A', randint(1, 10), [100, 100], 40, 15, KEYS_PLAYER_1)
p2 = Tank('B', randint(1, 10), [200, 200], 50, 11, KEYS_PLAYER_2)
p3 = Tank('C', randint(1, 10), [300, 300], 60, 10, KEYS_PLAYER_3)
p4 = Tank('D', randint(1, 10), [400, 400], 90, 7, KEYS_PLAYER_4)

game_is_running = True
while game_is_running:
	game_time = pygame.time.get_ticks()
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # para sair, pressione o X da janela ou ESC
			game_is_running = False
	
	screen.blit(background_image, (0, 0))  # Desenhar o background

	vida1=fonte_vida.render(f"PLAYER 1 : {vidap1}",1,(255,255,255))
	vida2=fonte_vida.render(f"PLAYER 2 : {vidap2}",1,(255,255,255))
	screen.blit(vida1,(50,50))
	screen.blit(vida2,(monitor.current_w-230,50))

	# Atualizar o estado do tanque
	for player in Tank.tanks:
		player.update()


	if game_time > 10000*engrenagem_vezes:
		engrenagem.render(screen)
		engrenagem_vezes += 1
		engrenagem_colisao=False
		aparicao_engrenagem = pygame.time.get_ticks()
		cooldown=5000
		
	###se tiver colisão entre os players e a engrenagem=vida e se vida palyer for menor que 20
	

	#se passar 5 segundos e ninguem pegar a engrenagem
	if ((pygame.time.get_ticks() - aparicao_engrenagem >=cooldown)and engrenagem_colisao==False):
		engrenagem.death(self)
	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
