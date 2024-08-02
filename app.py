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
from entities.municao import Municao

pygame.font.init()
vidap1=0
vidap2=0

lista_engrenagem=[]
engrenagem_vezes,engrenagem_tela,engrenagem_colisao=1, False, False
momento_aparicao_engrenagem = 0
cooldown=5000
flag_cycle, del_flag_time, flag_in_map, flag_taken = 1, 1, False, False
municao_aparecer, municao_desaparecer, municao_na_tela = 1, 1, False

start_time=0

pygame.mixer.music.set_volume(0.2)
musica_de_fundo=pygame.mixer.music.load(R"audio\fundo.mp3")
pygame.mixer.music.play(-1)
barulho_colisao_engrenagem=pygame.mixer.Sound(R"audio\colisao_engrenagem,.wav")
barulho_colisao_flag=pygame.mixer.Sound(R"audio\smb_coin.wav")
barulho_colisao_municao=pygame.mixer.Sound(R"audio\smb_powerup.wav")
barulho_colisao_engrenagem.set_volume(1)
barulho_colisao_flag.set_volume(0.2)
barulho_colisao_municao.set_volume(0.2)

# PyGame Setup
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

score_p1, score_p2 = 0, 0
municao_p1, municao_p2 = 20, 20

tank_selection_screen = TankSelectionScreen()
game_screen = GameScreen()
current_screen = tank_selection_screen
flag = Flag()
municao = Municao()

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
		flag_res = flag.flag_instance(screen, game_time, flag_cycle, del_flag_time, flag_in_map, flag_taken, p1, p2, score_p1, score_p2, barulho_colisao_flag)
		score_p1, score_p2, flag_cycle, del_flag_time, flag_in_map, flag_taken = flag_res[0], flag_res[1], flag_res[2], flag_res[3], flag_res[4], flag_res[5]
		municao_res = municao.collisao_municao(screen, game_time, municao_aparecer, municao_desaparecer, municao_na_tela, p1, p2, municao_p1, municao_p2, barulho_colisao_municao)
		municao_p1, municao_p2, municao_aparecer, municao_desaparecer, municao_na_tela = municao_res[0], municao_res[1], municao_res[2], municao_res[3], municao_res[4]
		if len(lista_engrenagem)!=0 and lista_engrenagem[0].vivo==False:
				lista_engrenagem.pop()

		if len(lista_engrenagem)==0:
			lista_engrenagem.append(Engrenagem())

		info_engrenagem=lista_engrenagem[0].colisao_engrenagem(screen,game_time,engrenagem_vezes,engrenagem_tela, engrenagem_colisao,p1,p2,vidap1,vidap2,momento_aparicao_engrenagem,barulho_colisao_engrenagem)
		engrenagem_vezes,engrenagem_tela,engrenagem_colisao,vidap1, vidap2, momento_aparicao_engrenagem=info_engrenagem[0],info_engrenagem[1], info_engrenagem[2], info_engrenagem[3], info_engrenagem[4], info_engrenagem[5]

		
	for player in Tank.tanks:
		screen.blit(player.image, player.rect.topleft)

		tank_selection_screen.start_game = False
		start_time= pygame.time.get_ticks()
		
	
	pygame.display.flip()
	clock.tick(FPS)
pygame.quit()
sys.exit()
