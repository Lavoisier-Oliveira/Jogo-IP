import pygame
pygame.init()

FPS = 60
KEYS_PLAYER_1 = (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d, pygame.KMOD_CTRL)
KEYS_PLAYER_2 = (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE)

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_LIGHT_COLOR = (0, 100, 0)

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)