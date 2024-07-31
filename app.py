import pygame
import sys

from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint
from tank_selection_screen import TankSelectionScreen
from game_screen import GameScreen

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

score_p1, score_p2 = 0, 0

# Instanciando a classe Flag 
flag_img = [pygame.image.load('assets/Collectibles/bandeira.png'), pygame.image.load('assets/Collectibles/bandeira_azul.png')] # Imagem da bandeira
size_img = (SCREEN_WIDTH//37, SCREEN_HEIGHT//12)
# Transformando o tamanho da imagem da bandeira
flag_img[0], flag_img[1] = pygame.transform.scale(flag_img[0], (size_img[0], size_img[1])), pygame.transform.scale(flag_img[1], (size_img[0], size_img[1])) 
flag = Flag((SCREEN_WIDTH, SCREEN_HEIGHT), flag_img[0], size_img) # Classe Flag instanciada 
flag_cycle, del_flag_time, flag_p, flag_taken = 1, 1, False, False # Variavéis para fazer a checagem das condições da bandeira na tela

tank_selection_screen = TankSelectionScreen()
game_screen = GameScreen()
current_screen = tank_selection_screen

game_is_running = True
while game_is_running:
	font = pygame.font.Font(None, 48)
	game_time = pygame.time.get_ticks()
	# Poll for events
	for event in pygame.event.get():
		# para sair, pressione o X da janela ou ESC
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			game_is_running = False
		else:
			current_screen.handle_event(event)
	
	current_screen.draw(screen)

	if tank_selection_screen.start_game:
		
		# Inicializa os tanques
		p1 = Tank(tank_selection_screen.color, tank_selection_screen.model, [100, 100], 90,  7, KEYS_PLAYER_1)
		p2 = Tank('B', randint(1, 8), [200, 200], 50, 11, KEYS_PLAYER_2)
		current_screen = game_screen

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
		tank_selection_screen.start_game = False
		
		score_tab1 = font.render(f': {score_p1}', True, (0, 0, 0))
		screen.blit(flag_img[0], (SCREEN_WIDTH*0.01, SCREEN_HEIGHT*0.9))
		screen.blit(score_tab1, (SCREEN_WIDTH*0.036, SCREEN_HEIGHT*0.93))
		score_tab2 = font.render(f': {score_p2}', True, (0, 0, 0))
		screen.blit(flag_img[1], (SCREEN_WIDTH*0.904, SCREEN_HEIGHT*0.9))
		screen.blit(score_tab2, (SCREEN_WIDTH*0.93, SCREEN_HEIGHT*0.93))

		# Gerando uma bandeira em um local aleatório no intervalo de 7 segundos
		if game_time > 7000*flag_cycle and game_time < 10000*flag_cycle:
			flag.render(screen) # Função da classe Flag para renderizar a flag em um local aleatório
			flag_cycle += 1
			flag_p, flag_taken = True, False
		# Após 3 segundos que a bandeira foi gerada, ela não deve mais aparecer na tela
		if game_time > 10000*del_flag_time: 
			flag_p = False
			del_flag_time += 1
		if flag_p:
			flag.update(screen)	# Função para sempre renderizar a bandeira na tela
		
		if p1.rect.colliderect(flag.rect_self(flag_p)):
			if not flag_taken:
				score_p1 += 1
			flag_p, flag_taken = False, True
		elif p2.rect.colliderect(flag.rect_self(flag_p)):
			if not flag_taken:
				score_p2 += 1
			flag_p, flag_taken = False, True

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
