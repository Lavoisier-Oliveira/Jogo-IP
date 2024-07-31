import pygame


class Tiro():
    def __init__(self, posicao_do_tanque, tamanho: tuple, posicao_do_tanque_atual=[]):
        self.posicao_do_tanque = list(posicao_do_tanque)
        self.imagem = pygame.image.load('assets\Effects\Medium_Shell.png')
        self.tamanho = tamanho
        self.velocidade = 1
        self.dano = 5
        self.posicao_do_tanque_atual = [0, 0]
        self.rect = self.imagem.get_rect(center=(posicao_do_tanque[0], posicao_do_tanque[1]))

    # Função que renderiza o tiro na tela
    def render(self, display):
        display.blit(self.imagem, self.rect)

    def update(self, anglo):
        if anglo == 0 or anglo == 180 or anglo == 360:
            self.rect.x += self.velocidade
        elif anglo == 90 or anglo == 270:
            self.rect.y += self.velocidade
        else:
            self.rect.x += self.velocidade
            self.rect.y += self.velocidade