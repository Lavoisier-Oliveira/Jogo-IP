import pygame
from parameters import *


class Tiro():
    def __init__(self, posicao_do_tanque, posicao_do_tanque_atual=[]):
        self.posicao = SCREEN_SIZE
        self.imagem = pygame.image.load('assets/Effects/Mediu_Shell.png')
        self.size = (SCREEN_WIDTH//37, SCREEN_HEIGHT//12)
        self.imagem[0], self.imagem[1] = pygame.transform.scale(self.imagem[0],(self.size[0], self.size[1])), pygame.transform.scale(self.iamgem[1], (self.size[0], self.size[1]))
        self.currente_position = [0, 0]

    # Função que renderiza o tiro na tela
    def render(self, display):
        display.blit(self.imagem, self.rect)

    # Função que guarda a posição atual da munição, e continua renderizando ela na tela
    def update(self, display):
        display.blit(self.imagem, (self.posicao_do_tanque_atual[0], self.posicao_do_tanque_atual[1]))

    def colisao_Tiro

    def rect_municao(self):
        return pygame.Rect(self.posicao_do_tanque_atual[0], self.posicao_do_tanque_atual[1], self.tamanho[0], self.tamanho[1])
