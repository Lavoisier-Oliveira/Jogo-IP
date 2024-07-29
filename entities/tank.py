import pygame
import math

pygame.init()
monitor = pygame.display.Info()


class Tank:
    tanks = []  # contem todos os objetos da classe

    # todo: implementar equação que, baseado na posição inicial do tanque, forneça o angulo inicial tal que este aponte para o centro da tela - seria preciso passar as dimensoes da tela para o construtor e importar uma função trigonometrica para tranformar os catetos em angulo # dessa forma o angulo seria atribuido no construtor
    vx, vy = 0, 0
    hull_angle = 0

    v_ang = 0  # rotação do weapon: +=anti-horario, -=horário
    weapon_angle = 0

    k = 100  # coeficiente de inercia - diretamente proporcional à aceleração  # valores recomendados : 10 até 200

    def __init__(self, color: str, model: int, initial_pos: list, size: int, speed: int, keys: tuple):

        # pass pygame.K_x in the order: (left, up, down, right)
        self.hull_keys = keys[0]
        self.weapon_keys = keys[1]

        self.size = size
        self.image = pygame.image.load(f"assets/Hulls_Color_{color}/Hull_0{model}.png")  # Carrega a imagem do tanque
        self.image = pygame.transform.scale(self.image, (self.size, self.size)).convert_alpha()  # Redimensiona a imagem do tanque e tranforma num formato mais versatil para o pygame operar
        self.original_image = self.image.copy()  # Guarda a imagem original para futuras rotações
        self.rect = self.image.get_rect(center=initial_pos)

        self.speed = speed  # pixels percorridos por tick
        self.aceleracao = self.k / ((self.speed * (self.size ** 2)) ** 0.5)  # formula empirica (saí testando e ficou top)
        self.desaceleracao = self.aceleracao  # isso permite configurar valores diferentes para ac. e desac., caso necessario no futuro

        Tank.tanks.append(self)

    def read_hull_input(self):

        keys = pygame.key.get_pressed()
        left_key, up_key, down_key, right_key = keys[self.hull_keys[0]], keys[self.hull_keys[1]], keys[self.hull_keys[2]], keys[self.hull_keys[3]]

        # X axis
        if left_key ^ right_key:  # acelera
            # todo: implementar caso o tank acelere para o sentido oposto ao deslocamento, sua velocidade deve diminuir 2x mais rapido do que o faria caso estivesse apenas dissipando
            if right_key:
                self.vx = self.vx + self.aceleracao if self.vx + self.aceleracao <= self.speed else self.speed
            elif left_key:
                self.vx = self.vx - self.aceleracao if self.vx - self.aceleracao >= -self.speed else -self.speed
        else:  # desacelera
            if self.vx < 0:
                self.vx = self.vx + self.desaceleracao if self.vx < -self.desaceleracao else 0
            elif self.vx > 0:
                self.vx = self.vx - self.desaceleracao if self.vx > self.desaceleracao else 0
        # Y axis
        if up_key ^ down_key:  # acelera
            if up_key:
                self.vy = self.vy - self.aceleracao if self.vy - self.aceleracao >= -self.speed else -self.speed
            elif down_key:
                self.vy = self.vy + self.aceleracao if self.vy + self.aceleracao <= self.speed else self.speed
        else:  # desacelera
            if self.vy < 0:
                self.vy = self.vy + self.desaceleracao if self.vy < -self.desaceleracao else 0
            elif self.vy > 0:
                self.vy = self.vy - self.desaceleracao if self.vy > self.desaceleracao else 0

        # calibrar vetores x e y quando o resultante ultrapassa o limite(self.speed)
        if (self.vx**2 + self.vy**2)**0.5 > self.speed:
            if self.vx >= self.speed/(2**0.5):
                self.vx -= self.desaceleracao
            elif self.vx <= -self.speed/(2**0.5):
                self.vx += self.desaceleracao
            if self.vy >= self.speed/(2**0.5):
                self.vy -= self.desaceleracao
            elif self.vy <= -self.speed / (2 ** 0.5):
                self.vy += self.desaceleracao

    def angle_hull(self):
        self.hull_angle = math.degrees(math.atan2(-self.vy, self.vx)) - 90
        # Preserve the center position while rotating
        self.image = pygame.transform.rotate(self.original_image, self.hull_angle)
        self.rect = self.image.get_rect(center=self.rect.center)  # Atualiza o retângulo da imagem com o centro preservado

    def read_weapon_input(self):

        keys = pygame.key.get_pressed()
        left_key, up_key, down_key, right_key = keys[self.weapon_keys[0]], keys[self.weapon_keys[1]], keys[self.weapon_keys[2]], keys[self.weapon_keys[3]]
        input_angle = math.degrees(math.atan2(right_key-left_key, right_key-left_key))



    def move_tank(self):

        test_rect = self.rect.copy()  # um rect de teste simulará o movimento do input, e então testaremos se houve colisão

        # check X collision
        test_rect.centerx += self.vx
        x_collision = False
        if 0 <= test_rect.left and test_rect.right <= monitor.current_w:
            for player in Tank.tanks:
                if player is not self:
                    if test_rect.colliderect(player):
                        x_collision = True
        else:
            x_collision = True

        # check Y collision
        test_rect.centerx -= self.vx
        test_rect.centery += self.vy
        y_collision = False
        if 0 <= test_rect.top and test_rect.bottom <= monitor.current_h:
            for player in Tank.tanks:
                if player is not self:
                    if test_rect.colliderect(player):
                        y_collision = True
        else:
            y_collision = True

        if not x_collision:
            self.rect.centerx += self.vx
        if not y_collision:
            self.rect.centery += self.vy

    def update(self):
        # todo: readinput() = pygame.getpressed -> readhull, readweapon
        self.read_hull_input()
        if self.vx != 0 or self.vy != 0:
            self.move_tank()
            self.angle_hull()
