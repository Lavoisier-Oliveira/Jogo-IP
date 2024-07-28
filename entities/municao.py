from random import uniform
import pygame

class Municao:
    def __init__(self, position, image, size: tuple, current_position=[]):
        self.position = list(position)
        self.image = image
        self.size = size
        self.current_position = [0, 0]

    # Função que renderiza a imagem da munição em um local aleatório do display
    def render(self, display):
        self.current_position[0], self.current_position[1] = uniform(80, self.position[0] - 80), uniform(80, self.position[1] - 80)
        display.blit(self.image, (self.current_position[0], self.current_position[1]))

    # Função que guarda a posição atual da munição, e continua renderizando ela na tela
    def update(self, display):
        display.blit(self.image, (self.current_position[0], self.current_position[1]))

    def interacao(self, rect_tanque):
        self.area_municao = pygame.rect(self.current_position[0], self.current_position[1], self.size[0], self.size[1])
        return self.area_municao.colliderect(rect_tanque)

