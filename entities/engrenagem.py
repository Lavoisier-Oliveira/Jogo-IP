import pygame
import random
from parameters import *

class Engrenagem:
    def __init__(self ):
        monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
        self.image = pygame.image.load(R".\assets\Collectibles\engrenagem.png")
        self.size = (monitor.current_w//30, monitor.current_h//10)
        self.image = pygame.transform.scale(self.image, (self.size[0],self.size[1]))  # Redimensiona a imagem
        self.rect = self.image.get_rect()
        self.centro_x= random.randint(0, monitor.current_w)
        self.centro_y= random.randint(0, monitor.current_h)
        self.cooldown=5000
        self.momento_aparicao_engrenagem = 0
        self.vivo=True

    def render(self,display):
        display.blit(self.image,(self.centro_x,self.centro_y))
   
    def death(self):
        self.vivo=False
       
        
    def cria(self):
        return  pygame.Rect(self.centro_x, self.centro_y,self.size[0], self.size[1])

    def update(self, display): 
        display.blit(self.image, (self.centro_x, self.centro_y))

    def colisao_engrenagem(self,screen,start_time,engrenagem_vezes,engrenagem_tela, engrenagem_colisao,p1,p2,vidap1,vidap2,momento_aparicao_engrenagem,baruluho_colisao_engrenagem):
        monitor = pygame.display.Info()  # allow to get current widht and height in any monitor
        font_padrao=pygame.font.get_default_font()
        fonte_vida=pygame.font.SysFont(font_padrao,35)
        vida1=fonte_vida.render(f"PLAYER 1 : {vidap1}",1,(255,255,255))
        vida2=fonte_vida.render(f"PLAYER 2 : {vidap2}",1,(255,255,255))
        screen.blit(vida1,(50,50))
        screen.blit(vida2,(monitor.current_w-230,50))


        if start_time > 5000*engrenagem_vezes:
            self.render(screen)
            engrenagem_tela =True
            engrenagem_colisao=False
            engrenagem_vezes+=1
            self.momento_aparicao_engrenagem = pygame.time.get_ticks()
            
            

        if engrenagem_tela:
            self.update(screen)### continuar mostrando

        ###se tiver colisão entre os players e a engrenagem=vida e se vida palyer for menor que 20( lembra de tirar imagem da engrenagemm e  alterar engrenagem tela)
        if p1.rect.colliderect(self.cria()):
            if vidap1<20:
                vidap1 += 5
            engrenagem_colisao=True
            self.death()
            engrenagem_tela=False
            baruluho_colisao_engrenagem.play()
            

        elif p2.rect.colliderect(self.cria()):
            if vidap2<20:
                vidap2 += 5
            engrenagem_colisao=True
            self.death()
            print("aaaaaaaaaa")
            print(self.vivo)
            engrenagem_tela+False
            baruluho_colisao_engrenagem.play()

        #se passar 5 segundos e ninguem pegar a engrenagem
        if ((pygame.time.get_ticks() - self.momento_aparicao_engrenagem >=self.cooldown)and (engrenagem_colisao==False)) :
            self.death()
            
        return(engrenagem_vezes,engrenagem_tela, engrenagem_colisao,vidap1,vidap2,self.momento_aparicao_engrenagem)
            
        

        if len(lista_engrenagem)==0:
            lista_engrenagem.append(engrenagem = Engrenagem())
           
