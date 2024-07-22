import pygame


class Tank:

    angle = 0  # Armazena o ângulo atual # talvez seja possível armar uma equação que, baseado na posição inicial do tanque, forneça o angulo inicial tal que este aponte para o centro da tela - seria preciso passar as dimensoes da tela para o construtor e importar uma função trigonometrica para tranformar os catetos em angulo # dessa forma o angulo seria atribuido no construtor
    vx, vy = 0, 0

    def __init__(self, color: str, model: int, initial_pos: list, size: int, speed: int):
        self.image = pygame.image.load(f"assets/Hulls_Color_{color}/Hull_0{model}.png")  # Carrega a imagem do tanque
        self.image = pygame.transform.scale(self.image, (size, size)).convert_alpha()  # Redimensiona a imagem do tanque e tranforma num formato mais versatil para o pygame operar
        self.current_pos = initial_pos  # Posição do tanque
        self.original_image = self.image.copy()  # Guarda a imagem original para futuras rotações
        self.rect = self.image.get_rect(center=self.current_pos)
        self.speed = speed  # pixels percorridos por tick

    def read_input(self):

        self.vx = self.vy = 0  # current vx and vy are still holding the values from previous read

        keys = pygame.key.get_pressed()
        a, w, s, d = keys[pygame.K_a], keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_d]

        # x axis
        if a and not d:
            self.vx = -self.speed
        elif d and not a:
            self.vx = self.speed
        # y axis
        if w and not s:
            self.vy = -self.speed
        elif s and not w:
            self.vy = self.speed

        if (a or d) and (w or s) != 0:  # se estiver movendo na diagonal
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
        self.current_pos[0] += self.vx
        self.current_pos[1] += self.vy
        self.rect.center = self.current_pos  # Atualiza a posição do retângulo com a nova posição

    def update(self):
        self.read_input()
        self.move()
        self.angle_image()
