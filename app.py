import pygame
import sys
from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint
from screens.tank_selection_screen import TankSelectionScreen
from screens.game_screen import GameScreen
from screens.home_menu_screen import HomeMenuScreen
from entities.engrenagem import Engrenagem
from entities.municao import Municao
from entities.projectile import Projectile, main, instance_sprites

pygame.font.init()

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

home_menu_screen = HomeMenuScreen()
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

current_screen = home_menu_screen
game_is_running = True

while game_is_running:
	game_time = pygame.time.get_ticks()
	
	# Poll for events
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			game_is_running = False
		elif event.type == pygame.KEYDOWN and current_screen == game_screen and (event.key == PLAYER_1_SHOT_BUTTON or event.key == PLAYER_2_SHOT_BUTTON):
			main(player1, player2, screen, event.key) # Adicionando os projéteis
		else:
			current_screen.handle_event(event)

	current_screen.draw(screen)

	# verifica a transição de telas
	if current_screen == home_menu_screen and home_menu_screen.start_game:
		current_screen = tank_selection_screen

	elif current_screen == tank_selection_screen and tank_selection_screen.start_game:
		# Inicializa os tanques
		player1 = Tank(tank_selection_screen.tank_player1[0],
					   tank_selection_screen.tank_player1[1],
					   [100, 100], 60, 10, KEYS_PLAYER_1)
		player2 = Tank(tank_selection_screen.tank_player2[0],
					   tank_selection_screen.tank_player2[1],
					   [400, 400], 60, 10, KEYS_PLAYER_2)

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
			screen.blit(player.cannon_image, player.rect.topleft)

		# Mostrar na tela a quantidade de engrenagens coletadas por jogador
		screen.blit(FONT_GEAR.render(f"PLAYER 1 : {player1.gears}", 1, BLACK_COLOR), (50, 50))
		screen.blit(FONT_GEAR.render(f"PLAYER 2 : {player2.gears}", 1, BLACK_COLOR), (SCREEN_WIDTH - 230, 50))

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

		# Checar se algum player morreu ou pegou 8 bandeiras
		loser = None
		if player1.flags == QTD_FLAGS_TO_WIN:
			loser = "Player 2"
		elif player2.flags == QTD_FLAGS_TO_WIN:
			loser = "Player 1"
		if player1.gears <= 0:
			player1.is_alive = False
			loser = "Player 1"
		elif player2.gears <= 0:
			player2.is_alive = False
			loser = "Player 2"

		if loser is not None:
			end_font = pygame.font.Font(None, 74)
			end_text = end_font.render(f"Fim de jogo para o(a) {loser}", True, BLACK_COLOR)
			title_rect = end_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
			screen.blit(end_text, title_rect)

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
sys.exit()