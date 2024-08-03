import pygame
import sys
from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint
from screens.tank_selection_screen import TankSelectionScreen
from screens.game_screen import GameScreen
from entities.engrenagem import Engrenagem
from entities.municao import Municao
from entities.projectile import Projectile, main, instance_sprites

pygame.font.init()

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

tank_selection_screen = TankSelectionScreen()
game_screen = GameScreen()

dict_collectibles = {
	'engrenagem': [],
	'municao': [],
	'bandeira': []
}
last_spawn_time = {
	'engrenagem': 0,
	'municao': 0,
	'bandeira': 0
}
collectible_generation_time = { 
	'engrenagem': GEAR_GEN_TIME,
	'municao': AMMO_GEN_TIME,
	'bandeira': FLAG_GEN_TIME
}

current_screen = tank_selection_screen
game_is_running = True

while game_is_running:
	game_time = pygame.time.get_ticks()
	
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			game_is_running = False
		elif event.type == pygame.KEYDOWN and current_screen == game_screen and (event.key == pygame.K_SPACE or event.key == pygame.K_m):
			main(player1, player2, screen, event.key) # Adicionando os projéteis
		else:
			current_screen.handle_event(event)

	current_screen.draw(screen)

	if tank_selection_screen.start_game:
		# Inicializa os tanques
		player1 = Tank(tank_selection_screen.tank_player1[0],
					   tank_selection_screen.tank_player1[1],
					   [100, 100], 50, 15, KEYS_PLAYER_1)
		player2 = Tank(tank_selection_screen.tank_player2[0],
					   tank_selection_screen.tank_player2[1],
					   [400, 400], 50, 15, KEYS_PLAYER_2)

		current_screen = game_screen
		tank_selection_screen.start_game = False

	if current_screen == game_screen:

		for collectible_type, last_time in last_spawn_time.items():
			if game_time - last_time >= collectible_generation_time[collectible_type]:
				if collectible_type == 'engrenagem':
					collectible = Engrenagem()
				elif collectible_type == 'municao':
					collectible = Municao()
				elif collectible_type == 'bandeira':
					collectible = Flag()
				collectible.add_collectible_to_dict(dict_collectibles)
				last_spawn_time[collectible_type] = game_time

		for collectible_list in dict_collectibles.values():
			for collectible in collectible_list.copy():  # Iterate over a copy of the list
				collectible.main(screen, player1, player2, game_time, dict_collectibles)

		# Renderizar tanques
		for player in Tank.tanks:
			screen.blit(player.image, player.rect.topleft)

		# Mostrar na tela a quantidade de engrenagens coletadas por jogador
		screen.blit(FONT_GEAR.render(f"PLAYER 1 : {player1.gears}", 1, WHITE_COLOR), (50, 50))
		screen.blit(FONT_GEAR.render(f"PLAYER 2 : {player2.gears}", 1, WHITE_COLOR), (SCREEN_WIDTH - 230, 50))

		# Mostrar na tela as imagens das bandeiras
		screen.blit(RED_FLAG_IMAGE, (SCREEN_WIDTH * 0.01, SCREEN_HEIGHT * 0.9))
		screen.blit(BLUE_FLAG_IMAGE, (SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.9))

		# Mostrar na tela a quantidade de bandeiras coletadas por jogador
		screen.blit(AMMO_IMAGE, (SCREEN_WIDTH*0.07, SCREEN_HEIGHT*0.9))
		screen.blit(AMMO_IMAGE, (SCREEN_WIDTH*0.82, SCREEN_HEIGHT*0.9))

		# Mostrar na tela a quantidade de bandeiras coletadas de cada jogador
		screen.blit(FONT_48.render(f': {player1.flags}', True, BLACK_COLOR), (SCREEN_WIDTH * 0.036, SCREEN_HEIGHT * 0.93))
		screen.blit(FONT_48.render(f': {player2.flags}', True, BLACK_COLOR), (SCREEN_WIDTH * 0.93, SCREEN_HEIGHT * 0.93))

		# Mostrar na tela a quantidade de munição de cada jogador
		screen.blit(FONT_48.render(f': {player1.ammo}', True, BLACK_COLOR), (SCREEN_WIDTH*0.1, SCREEN_HEIGHT*0.93))
		screen.blit(FONT_48.render(f': {player2.ammo}', True, BLACK_COLOR), (SCREEN_WIDTH*0.85, SCREEN_HEIGHT*0.93))

		# Gerando as animações de todos os projéteis e explosões
		instance_sprites(screen)

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()