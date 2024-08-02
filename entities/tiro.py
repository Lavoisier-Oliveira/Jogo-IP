import pygame
from parameters import *




class Tiro():
    def __init__(self, posicao_do_tanque_atual=[]):
        self.posicao = SCREEN_SIZE
        self.imagem = pygame.image.load('assets/Effects/Medium_Shell.png')
        self.size = (SCREEN_WIDTH//25, SCREEN_HEIGHT//12)
        self.imagem = pygame.transform.scale(self.imagem,(self.size[0], self.size[1]))
        self.velocidade = 1
        self.dano = 5
        self.rect = self.imagem.get_rect(center=(0, 0))
        self.currente_position = [0, 0]

    # Função que renderiza o tiro na tela
    def render(self, display, tanque_rect):
        self.rect = self.imagem.get_rect(center=tanque_rect)
        display.blit(self.imagem, self.rect)

    # Função que guarda a posição atual da munição, e continua renderizando ela na tela, para que ela saia no sentido certo é necessário que a base de atualização dos eixos seja o anglo do tanque na hr do tiro
    def update(self, anglo):
        #colisao da pra ser feita no update: só colocar na função a condição para gerar os updates ser da bala não estar colidindo com o tanque e se estiver colidindo, deletar a bala atirada
        if anglo == 0 or anglo == 180 or anglo == 360:
            self.rect.x += self.velocidade
        elif anglo == 90 or anglo == 270:
            self.rect.y += self.velocidade
        else:
            self.rect.x += self.velocidade
            self.rect.y += self.velocidade

    def atirar(municao): #função para alterar o valor da munição do tanque quando a tecla de atirar for pressionada
        if municao > 0 and municao <= 20:
            municao -= 1
        return municao



