import pygame
import sys

from parameters import *
from entities.tank import Tank
from entities.flags import Flag
from random import randint
from screens.tank_selection_screen import TankSelectionScreen
from screens.game_screen import GameScreen
from entities.engrenagem import Engrenagem
from screens.tank_selection_screen import TankSelectionScreen
from screens.game_screen import GameScreen

pygame.font.init()
vidap1=0
vidap2=0

lista_engrenagem=[]
engrenagem_vezes,engrenagem_tela,engrenagem_colisao=1,False, False
momento_aparicao_engrenagem = 0
cooldown=5000

start_time=0

pygame.mixer.music.set_volume(0.2)
musica_de_fundo=pygame.mixer.music.load(R"audio\fundo.mp3")
pygame.mixer.music.play(-1)
baruluho_colisao_engrenagem=pygame.mixer.Sound(R"audio\colisao_engrenagem,.wav")
baruluho_colisao_engrenagem.set_volume(1)

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
	
		tank_selection_screen.start_game = False
		
	if current_screen == game_screen:
		flag_res = flag.flag_instance(screen, game_time, flag_cycle, del_flag_time, flag_p, flag_taken, p1, p2, score_p1, score_p2)
		score_p1, score_p2, flag_cycle, del_flag_time, flag_p, flag_taken = flag_res[0], flag_res[1], flag_res[2], flag_res[3], flag_res[4], flag_res[5]
		if len(lista_engrenagem)!=0 and lista_engrenagem[0].vivo==False:
				lista_engrenagem.pop()

		if len(lista_engrenagem)==0:
			lista_engrenagem.append(Engrenagem())

		info_engrenagem=lista_engrenagem[0].colisao_engrenagem(screen,game_time,engrenagem_vezes,engrenagem_tela, engrenagem_colisao,p1,p2,vidap1,vidap2,momento_aparicao_engrenagem,baruluho_colisao_engrenagem)
		engrenagem_vezes,engrenagem_tela,engrenagem_colisao,vidap1, vidap2, momento_aparicao_engrenagem=info_engrenagem[0],info_engrenagem[1], info_engrenagem[2], info_engrenagem[3], info_engrenagem[4], info_engrenagem[5]

		
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)

		tank_selection_screen.start_game = False
		start_time= pygame.time.get_ticks()
		
	
	pygame.display.flip()
	clock.tick(FPS)
pygame.quit()
sys.exit()
