import pygame
pygame.init()

FPS = 60
KEYS_PLAYER_1 = (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)
KEYS_PLAYER_2 = (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT)

PROJECTILE_SPRITES = pygame.sprite.Group()
EXPLOSION_SPRITES = pygame.sprite.Group()

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_LIGHT_COLOR = (0, 100, 0)

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.mixer.music.set_volume(0.2)
BACKGROUND_MUSIC = pygame.mixer.music.load(R"audio/fundo.mp3")
pygame.mixer.music.play(-1)

GEAR_COLLISION_SOUND = pygame.mixer.Sound(R"audio/colisao_engrenagem.wav")
GEAR_COLLISION_SOUND.set_volume(1)
FLAG_COLLISION_SOUND = pygame.mixer.Sound(R"audio/smb_coin.wav")
FLAG_COLLISION_SOUND.set_volume(0.2)
AMMO_COLLISION_SOUND = pygame.mixer.Sound(R"audio/smb_powerup.wav")
AMMO_COLLISION_SOUND.set_volume(0.2)

PROJECTILE_SOUND = pygame.mixer.Sound(R"audio/pew.mp3")
PROJECTILE_SOUND.set_volume(0.2)
PROJECTILE_COLLISION_SOUND = pygame.mixer.Sound(R"audio/kaboom_baby.mp3")
PROJECTILE_COLLISION_SOUND.set_volume(0.1)

FONT_GEAR = pygame.font.SysFont(pygame.font.get_default_font(), 35)
FONT_48 = pygame.font.Font(None, 48)

COLLECTIBLE_REMOVE_TIME = 6000
GEAR_GEN_TIME = 6000
AMMO_GEN_TIME = 5000
FLAG_GEN_TIME = 8000

BLUE_FLAG_IMAGE = pygame.image.load(R"assets/Collectibles/bandeira_azul.png")
BLUE_FLAG_IMAGE = pygame.transform.scale(BLUE_FLAG_IMAGE, (SCREEN_WIDTH // 37, SCREEN_HEIGHT // 12))

RED_FLAG_IMAGE = pygame.image.load(R"assets/Collectibles/bandeira_vermelha.png")
RED_FLAG_IMAGE = pygame.transform.scale(RED_FLAG_IMAGE, (SCREEN_WIDTH // 37, SCREEN_HEIGHT // 12))

AMMO_IMAGE = pygame.image.load(R"assets/Effects/Medium_Shell.png")
AMMO_IMAGE = pygame.transform.scale(AMMO_IMAGE, (SCREEN_WIDTH//25, SCREEN_HEIGHT//10))

GEAR_IMAGE = pygame.image.load(R"assets/Collectibles/engrenagem.png")
GEAR_IMAGE = pygame.transform.scale(GEAR_IMAGE, (SCREEN_WIDTH//25, SCREEN_HEIGHT//10))