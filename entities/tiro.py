import pygame


class Tiro():
    def __init__(self, posicao_do_tanque, imagem, tamanho: tuple, posicao_do_tanque_atual=[]):
        self.posicao_do_tanque = list(posicao_do_tanque)
        self.imagem = imagem
        self.tamanho = tamanho
        self.velocidade = 1
        self.dano = 5
        self.posicao_do_tanque_atual = [0, 0]
        self.rect = self.imagem.get_rect(center=posicao_do_tanque)

    # Função que renderiza a imagem da munição a partir da posição em que o tanque está
    def render(self, display):
        self.posicao_do_tanque_atual[0], self.posicao_do_tanque_atual[1] = (80, self.posicao_do_tanque[0] - 80), (80, self.posicao_do_tanque[1] - 80)
        display.blit(self.imagem, (self.posicao_do_tanque_atual[0], self.posicao_do_tanque_atual[1]))

    # Função que guarda a posição atual da munição, e continua renderizando ela na tela
    def update(self, display):
        display.blit(self.imagem, (self.posicao_do_tanque_atual[0], self.posicao_do_tanque_atual[1]))

    def rect_municao(self):
        return pygame.Rect(self.posicao_do_tanque_atual[0], self.posicao_do_tanque_atual[1], self.tamanho[0], self.tamanho[1])