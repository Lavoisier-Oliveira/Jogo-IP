import pygame
import sys

from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint
from screens.tank_selection_screen import TankSelectionScreen
from screens.game_screen import GameScreen

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

score_p1, score_p2 = 0, 0

tank_selection_screen = TankSelectionScreen()
game_screen = GameScreen()
current_screen = tank_selection_screen
flag = Flag()
flag_cycle, del_flag_time, flag_p, flag_taken = 1, 1, False, False # Variavéis para fazer a checagem das condições da bandeira na tela

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
		p1 = Tank(tank_selection_screen.tank_player1[0], tank_selection_screen.tank_player1[1], [100, 100], 50, 15, KEYS_PLAYER_1)
		p2 = Tank(tank_selection_screen.tank_player2[0], tank_selection_screen.tank_player2[1], [400, 400], 50, 15, KEYS_PLAYER_2)
		current_screen = game_screen

	# Renderizar o jogo
	# screen.fill("black")  # Preencher a tela com uma cor (preto)
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)  # Desenhar o tanque na nova posição

	# Flip the display to put your work on screen
		tank_selection_screen.start_game = False
		
		flag_res = flag.flag_instance(screen, game_time, flag_cycle, del_flag_time, flag_p, flag_taken, p1, p2, score_p1, score_p2)
		score_p1, score_p2, flag_cycle, del_flag_time, flag_p, flag_taken = flag_res[0], flag_res[1], flag_res[2], flag_res[3], flag_res[4], flag_res[5]
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
