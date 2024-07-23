import pygame

pygame.init()
monitor = pygame.display.Info()

class Tank:

    tanks = []

    angle = 0  # Armazena o ângulo atual # talvez seja possível armar uma equação que, baseado na posição inicial do tanque, forneça o angulo inicial tal que este aponte para o centro da tela - seria preciso passar as dimensoes da tela para o construtor e importar uma função trigonometrica para tranformar os catetos em angulo # dessa forma o angulo seria atribuido no construtor
    vx, vy = 0, 0

    def __init__(self, color: str, model: int, initial_pos: list, size: int, speed: int, keys: tuple):
        self.keys = keys  # pass pygame.K_x in the order: left, up, down, right
        self.image = pygame.image.load(f"assets/Hulls_Color_{color}/Hull_0{model}.png")  # Carrega a imagem do tanque
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size, self.size)).convert_alpha()  # Redimensiona a imagem do tanque e tranforma num formato mais versatil para o pygame operar
        self.current_pos = initial_pos  # Posição do tanque
        self.original_image = self.image.copy()  # Guarda a imagem original para futuras rotações
        self.rect = self.image.get_rect(center=self.current_pos)
        self.speed = speed  # pixels percorridos por tick
        Tank.tanks.append(self)

    def read_input(self):

        self.vx = self.vy = 0  # current vx and vy are still holding the values from previous read

        keys = pygame.key.get_pressed()
        left_key, up_key, down_key, right_key = keys[self.keys[0]], keys[self.keys[1]], keys[self.keys[2]], keys[self.keys[3]]

        # x axis
        if left_key and not right_key:
            self.vx = -self.speed
        elif right_key and not left_key:
            self.vx = self.speed
        # y axis
        if up_key and not down_key:
            self.vy = -self.speed
        elif down_key and not up_key:
            self.vy = self.speed

        if (left_key ^ right_key) and (up_key ^ down_key) != 0:  # se estiver movendo na diagonal
            self.vx /= (2 ** 0.5)
            self.vy /= (2 ** 0.5)

    def angle_image(self):
        if self.vx > 0:
            if self.vy > 0:
                self.angle = -135
            elif self.vy < 0:
                self.angle = -45
            else:  # self.vy == 0
                self.angle = -90
        elif self.vx < 0:
            if self.vy > 0:
                self.angle = +135
            elif self.vy < 0:
                self.angle = +45
            else:  # self.vy == 0
                self.angle = +90
        else:  # self.vx == 0
            if self.vy > 0:
                self.angle = +180
            elif self.vy < 0:
                self.angle = 0
            else:  # self.vy == 0
                pass

        # Preserve the center position while rotating
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(
            center=self.rect.center)  # Atualiza o retângulo da imagem com o centro preservado

    def move(self):

        if 0 <= self.current_pos[0]-self.size/2+self.vx and self.current_pos[0]+self.size/2+self.vx <= monitor.current_w:  # (movimento x não atravessa esquerda) e (movimento x não atravessa direita)
            self.current_pos[0] += self.vx
        if 0 <= self.current_pos[1]-self.size/2+self.vy and self.current_pos[1]+self.size/2+self.vy <= monitor.current_h:  # (movimento y não atravessa teto) e (movimento y não atravessa chão)
            self.current_pos[1] += self.vy
        self.rect.center = self.current_pos  # Atualiza a posição do retângulo com a nova posição

    def update(self):
        self.read_input()
        self.move()
        self.angle_image()