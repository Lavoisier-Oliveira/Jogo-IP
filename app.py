import pygame
import sys
from parameters import *
from entities.tank import Tank
from random import randint
from tank_selection_screen import TankSelectionScreen
from game_screen import GameScreen

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

tank_selection_screen = TankSelectionScreen()
game_screen = GameScreen()
current_screen = tank_selection_screen

game_is_running = True
while game_is_running:
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
		p1 = Tank('A', randint(1, 8), [100, 100], 40, 15, KEYS_PLAYER_1)
		p2 = Tank('B', randint(1, 8), [200, 200], 50, 11, KEYS_PLAYER_2)
		p3 = Tank('C', randint(1, 8), [300, 300], 60, 10, KEYS_PLAYER_3)
		p4 = Tank(tank_selection_screen.color, tank_selection_screen.model, [400, 400], 90,  7, KEYS_PLAYER_4)
		current_screen = game_screen

		tank_selection_screen.start_game = False
	
	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()
