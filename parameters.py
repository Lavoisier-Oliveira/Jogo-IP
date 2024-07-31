import pygame
pygame.init()

FPS = 60
KEYS_PLAYER_1 = (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT)
KEYS_PLAYER_2 = (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)
KEYS_PLAYER_3 = (pygame.K_g, pygame.K_y, pygame.K_h, pygame.K_j)
KEYS_PLAYER_4 = (pygame.K_KP4, pygame.K_KP8, pygame.K_KP5, pygame.K_KP6)

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREEN_LIGHT_COLOR = (0, 100, 0)

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)