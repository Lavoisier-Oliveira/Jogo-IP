import pygame
import sys
from parameters import *
from entities.tank import Tank
from random import randint
from screens.tank_selection_screen import TankSelectionScreen
from screens.game_screen import GameScreen

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE) # Cria a janela do jogo com o tamanho da tela do monitor
clock = pygame.time.Clock() # Cria um objeto para ajudar a controlar o tempo

tank_selection_screen = TankSelectionScreen() # Cria a tela de seleção de tanques
game_screen = GameScreen() # Cria a tela do jogo
current_screen = tank_selection_screen # Define a tela atual como a tela de seleção de tanques

game_is_running = True
while game_is_running:
	# Poll for events
	for event in pygame.event.get():
		# para sair, pressione o X da janela ou ESC
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # Verifica se o evento é de fechar a janela
			game_is_running = False
		else:
			current_screen.handle_event(event) # Trata os eventos da tela atual
	
	current_screen.draw(screen) # Desenha a tela atual

	if tank_selection_screen.start_game:
		
		# Inicializa os tanques
		p1 = Tank(tank_selection_screen.tank_player1[0], tank_selection_screen.tank_player1[1], [100, 100], 50, 15, KEYS_PLAYER_1)
		p2 = Tank(tank_selection_screen.tank_player2[0], tank_selection_screen.tank_player2[1], [400, 400], 50, 15, KEYS_PLAYER_2)
		current_screen = game_screen

		tank_selection_screen.start_game = False
	
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
