# Projeto de Introdução à Programação: CInflito de Tanques

Projeto desenvolvido durante a disciplina de Introdução à Programação do Centro de Informática da Universidade Federal de Pernambuco. O projeto consiste na criação de um jogo 2D utilizando a linguagem de programação Python e a biblioteca PyGame como base do projeto.

A ideia principal do projeto é ser um jogo de tanques player versus player com top-view (Ambiente do jogo é observado de cima para baixo). Originalmente, todos os integrantes planejavam se inspirar em DD Tank, um jogo de batalha com diversas armas e cenário dinâmico, porém com o tempo decidimos alterar a ideia principal do jogo e seguir com a ideia de um jogo de batalha top-view. 

### Integrantes:

Julia Sovka Souza  
Lavoisier Oliveira Cândido  
Luis Eduardo Ribeiro Freitas  
Renan Santana Costa  
Renato Monteiro Correia Medeiros  
Valter Bezerra da Rocha Junior 

## Requisitos Funcionais

- Instalação do Python.
- Para ter acesso ao código fonte basta realizar o comando git clone “[https://github.com/Lavoisier-Oliveira/Jogo-IP.git](https://github.com/Lavoisier-Oliveira/Jogo-IP.git)” em qualquer diretório.
- Para realizar a instalação de maneira segura, devemos criar um ambiente virtual no diretório escolhido -

```powershell
## Comando para criar o ambiente virtual 
python -m venv <nome_do_ambiente>

## Lista de comandos para acessar o ambiente virtual com base no terminal utilizado
<nome_do_ambiente>\Scripts\activate.bat
<nome_do_ambiente>\Scripts\activate
<nome_do_ambiente>\Scripts\activate.ps1
```

- Instalação da versão mais atualizada do PyGame, utilizando o comando pip install pygame, ou utilizando o comando pip install -r requirements.txt (Esse arquivo possui as dependências a serem instaladas).
- Por fim, basta executar o arquivo [app.py](http://app.py) na raiz principal do projeto para ter a execução do jogo concluída, isso pode ser feito com o comando python app.py.

```powershell
## Lista de Comandos - 
git clone “[https://github.com/Lavoisier-Oliveira/Jogo-IP.git](https://github.com/Lavoisier-Oliveira/Jogo-IP.git)”
pip install pygame // pip install -r requirements.txt
python app.py
```

## Arquitetura do Projeto

- [app.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/app.py) - Arquivo principal do projeto, é nesse arquivo em que são reunidas as informações de todo o projeto para a execução do código. Este arquivo reúne todos os outros blocos de código e então executa o script para o funcionamento do jogo.
- [requirements.txt](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/requirements.txt) - Esse arquivo possui as dependências a serem instaladas no ambiente virtual, no nosso caso apenas realizamos a instalação da biblioteca do PyGame na versão 2.6.0.
- [parameters.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/parameters.py) - Neste arquivo são guardadas todas as constantes que podem ser acessadas em todos os arquivos, como por exemplo a variável que guarda o tamanho da tela.
- screens - Pasta que possui as telas do jogo.
    - [home_menu_screen.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/screens/home_menu_screen.py) - Tela de menu inicial para começar o jogo.
    - [tank_selection_screen.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/screens/tank_selection_screen.py) - Tela inicial na qual ambos os jogadores devem selecionar seus tanques para iniciar o jogo.
    - [gamescreen.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/screens/game_screen.py) - Arquivo que ao ser executado carrega a página principal do jogo.
- entities - Pasta que contém todas as entidades principais do jogo que foram estruturadas utilizando os conceitos de Programação Orientada a Objetos (POO), cada entidade possui suas funções como locomoção, geração de imagens, criação de animação, renderização na tela, e entre outros.
    - [tank.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/tank.py) - Este arquivo possui a principal entidade do jogo, esta classe recebe inputs do teclado no (W, A, S, D) e (↑ ↓ ← → ) para a realização do movimento de cada jogador.
    - [collectible.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/collectible.py) - Esse é o arquivo que possui todas as funções principais na geração dos coletáveis, como criação do coletável no mapa, renderização do coletável no mapa, remoção dos coletáveis, e a checagem de colisão entre o player e o coletável. Esta é a classe que vai ser herdada por todos os outros coletáveis.
    - [flag.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/flags.py) - Arquivo para a criação do coletável de bandeira, que herda a classe Collectible.
    - [municao.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/municao.py) - Arquivo para a criação do coletável de munição do tanque, que herda a classe Collectible.
    - [engrenagem.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/engrenagem.py) - Arquivo para a criação do coletável de engrenagem (vida do tanque), que herda a classe Collectible.
    - [projectile.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/projectile.py) - O arquivo [projectile.py](http://projectile.py/) possui a classe Projectile que deve guardar todos os sprites de projéteis gerados ao pressionar as teclas de espaço, ou “m”. Essa classe possui alguns dos atributos da classe tanque, para então podermos checar a colisão entre o projétil e o tanque inimigo, e realizar a checagem do ângulo no qual o projétil deve ser lançado. A classe possui duas funções principais, a função para a checagem de colisão, que instancia a classe Explosions(Classe do arquivo [animations.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/animations.py)) para guardar os sprites e assim criar a animação de explosão. Outra função, é a função de update que sempre renderiza o projétil na tela. O projétil some quando atinge um tanque, ou é lançado para fora do mapa.
    - [animations.py](https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/entities/animations.py) - Este arquivo guarda todas as animações principais do projeto, desde as animações de explosões, movimento, e entre outros. Para a geração das animações utilizamos uma sequência de imagens carregadas ao instanciar alguma das classes, e guardando essa sequência de imagens, ao passar dos frames alteramos as imagens renderizadas com a lista de imagens criada anteriormente, sempre desenhando a nova imagem de animação na tela.
- assets - Pasta que contém todos os arquivos de imagem utilizados no desenvolvimento do jogo. Essa pasta possui todas as sprites de tanques, imagens de explosão, imagens dos objetos coletáveis, projéteis e entre outros.
- audio - Pasta que contém os arquivos de áudio utilizados para o desenvolvimento do jogo. Este arquivo possui o som de background, e os sons da coleta de itens.
    
    ### Flowchart da Arquitetura do projeto -

    <p align = "center">
      <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/flow_chart.png">
    </p>

## Capturas de Tela

<p align = "center">
  <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/selection_1.jpg">
</p>
<p align = "center">
  <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/selection_2.jpg">
</p>
<p align = "center">
  <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/game_panel.jpg">
</p>
<p align = "center">
  <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/collecting.jpg">
</p>
<p align = "center">
  <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/explosion.png">
</p>
<p align = "center">
  <img width = 936 height = 724 src="https://github.com/Lavoisier-Oliveira/Jogo-IP/blob/main/assets/capturas/restart_game.png">
</p>

## Bibliotecas, Ferramentas e Frameworks utilizados

- PyGame - Como dito anteriormente, a biblioteca do PyGame foi a principal fonte para a criação do projeto como um todo. Uma vez que a biblioteca forneceu todas as ferramentas para a geração, desenho, e renderização de imagens e aplicar isso em um sistema para a criação da jogabilidade. A importância dessa ferramenta se demonstra também na sua capacidade de checar colisões entre dois objetos, processamento de imagens, criação de animações utilizando uma sequência de imagens, e entre outros.
- Math - A biblioteca foi utilizada no projeto com o objetivo de gerar movimentos que podem alternar entre o eixo x e y, assim poderíamos checar a angulação do tanque para realizar o seu movimento, também utilizamos essa biblioteca para que o projétil do tanque também seja capaz de realizar um movimento de acordo com o ângulo do tanque.
- Sys - Biblioteca utilizada para finalizar o programa.
- Random - Essa biblioteca foi utilizada com o intuito de gerar os coletáveis de maneira aleatória no mapa.

## Divisão de Trabalho

A divisão de trabalho foi feita utilizando o notion, no qual cada integrante podia observar as atividades e seu status para escolher qual tarefa escolher.

- Lavoisier - Refatoração dos códigos dos Itens Colecionáveis por meio da implementação da POO. Correção nos sons do jogo. Adição da licença MIT ao projeto. Criação da tela de escolha dos tanques. Adição dos tanques à tela do jogo, além de participação na movimentação do tanque. Adição de Imagens de fundo às telas do jogo.
- Júlia -
- Valter - Criação da tela inicial
- Renato -
- Luis -
- Renan - Realização da documentação do projeto, sons de alguns coletáveis, sons de disparo, e explosão, criação do coletável da bandeira, criação do projétil do tanque e sua animação de explosão.

## Conceitos utilizados

A utilização dos conceitos abordados durante a realização das aulas se faz presente por toda a estrutura do código. Podemos observar a utilização de estruturas condicionais (if/else), e laços de repetição para a checagem de eventos, comparação de valores, checagem de colisão entre objetos, e entre outros. O uso de lista, tuplas e dicionários também se fez presente para guardar informações durante a execução do jogo. O uso de funções foi fundamental para a organização do código, uma vez que com a criação de funções conseguimos modularizar o código e assim transformar o ambiente de desenvolvimento mais limpo e fácil de entender. 

O entendimento acerca das estruturas de dados foram imprescindíveis para a realização do projeto, uma vez que a todo momento se fazia necessário a criação e atualização da posição de algum objeto presente no jogo. Essa posição, que podia ser demonstrada em um plano cartesiano em píxeis do cenário do jogo, ou seja, a posição de cada objeto, podia ser guardada na forma (x, y) desse plano cartesiano.

Outro fator importante foram os conceitos de programação orientada a objetos (POO), que por sua vez, assim como as funções, possibilitam a modularização do código, possibilitando também a realização da subdivisão do desenvolvimento de cada componente. Com os conceitos de POO, foi possível realizar uma melhor organização na divisão de tarefas e a realização de código mais coeso, no qual cada arquivo possuía o seu script individual que podia ser executado posteriormente no arquivo [app.py](http://app.py/) na raiz do projeto.

### Exemplos de cada conceito utilizado durante o desenvolvimento -

- Estruturas Condicionais - Checagem de todos os eventos que acontecem na execução do jogo.
    
    ```python
    # Checar se algum player morreu ou pegou 8 bandeiras
    loser = None
    if player1.flags == QTD_FLAGS_TO_WIN:
    	loser = "Player 2"
    elif player2.flags == QTD_FLAGS_TO_WIN:
    	loser = "Player 1"
    if player1.gears <= 0:
    	player1.is_alive = False
    	loser = "Player 1"
    elif player2.gears <= 0:
    	player2.is_alive = False
    	loser = "Player 2"
    ```
    
- Laços de Repetição - Adicionando os frames da explosão utilizando laço de repetição para adicionar cada imagem a uma lista de imagens.
    
    ```python
    # Adicionando a lista de frames possíveis todas as imagens de explosão
    for i in range(8):
        explosion_frame = pygame.image.load(f'assets/Explosions/Explosion_{i+1}.png')
        w, h = explosion_frame.get_size()
        width = int(w * 0.5)
        height = int(h * 0.5)
        explosion_frame = pygame.transform.scale(explosion_frame, (width, height))
        self.frames_imgs.append(explosion_frame)
    ```
    
- Listas - Dicionário que possui listas para cada coletável, adição de tanques a uma lista de tanques, e criação do retângulo do tanque a partir de sua posição inicial.
    
    ```python
    #Dicionários de coletáveis
    dict_collectibles = {
    	'engrenagem': [],
    	'municao': [],
    	'bandeira': []
    }
    
    # Lista de tanques
    tanks = []
    
    angle = 0 
    vx, vy = 0, 0

    def __init__(self, color: str, model: int, initial_pos: list, size: int, speed: int, keys: tuple):
        self.keys = keys
        self.image = pygame.image.load(f"./assets/Hulls_Color_{color}/Hull_0{model}.png")
        self.size = size
        self.image = pygame.transform.scale(self.image, (self.size,
                                                         self.size)).convert_alpha()  
        self.original_image = self.image.copy()  	
        self.rect = self.image.get_rect(center=initial_pos) # Gerando o retângulo do tanque utilizando a lista da posição inicial em que o tanque foi gerado
        self.speed = speed  
        self.mask = pygame.mask.from_surface(self.image) 
        self.gears = 5
        self.ammo = 5
        self.flags = 0
        
        # Adicionando cada tanque instanciado a lista de tanques
        Tank.tanks.append(self)
    ```
    
- Funções - Função que atualiza o frame atual da animação e retorna a nova imagem.
    
    ```python
    # Função para atualizar o frame atual e gerar a imagem do frame atual
    def update(self):
        self.frame_now += 1
        if self.frame_now >= 7:
            self.index += 1
            if self.index >= self.frames:
                self.kill()
            else:
                self.image = self.frames_imgs[self.index]
                self.frame_now = 0
    ```
    
- Tuplas e Dicionários - Definição das teclas de cada jogador, e guardando informações dos coletáveis.
    
    ```python
    #Tuplas para guardar as teclas que cada jogador pode utilizar
    KEYS_PLAYER_1 = (pygame.K_a, pygame.K_w, pygame.K_s, pygame.K_d)
    KEYS_PLAYER_2 = (pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT)
    
    # Dicionários para guardar informações referentes aos coletáveis
    dict_collectibles = {
    	'engrenagem': [],
    	'municao': [],
    	'bandeira': []
    }
    last_spawn_time = {
    	'engrenagem': 0,
    	'municao': 0,
    	'bandeira': 0
    }
    collectible_generation_time = { 
    	'engrenagem': GEAR_GEN_TIME,
    	'municao': AMMO_GEN_TIME,
    	'bandeira': FLAG_GEN_TIME
    }
    ```
    

## Desafios, erros e decisões tomadas

- Utilização do Git e Github -
    
    A maioria dos desafios que a equipe teve envolveram questões de organização do trabalho. Grande parte dos membros não tinham experiência com softwares de versionamento de código, por isso a equipe decidiu primeiramente se concentrou em resolver o problema de organização do grupo. Antes de começar realmente a desenvolver, todos os membros tiveram que aprender a utilizar o Git e Github.  Os encontros com os monitores foram fundamentais para encontrar formas de resolver os problemas de organização da equipe e também solucionar dúvidas inerentes ao jogo em si. Para evitar o conflito entre códigos de cada integrante da equipe optamos por criar uma branch para cada integrante, assim cada um seria capaz de desenvolver sem afetar outro integrante.
    
- Planejamento -
    
    Na primeira semana do projeto tivemos dificuldades para articular todas as ideias e decidir qual seria o jogo de maneira rápida. Outro problema foi a divisão de tarefas, a qual só foi ser realizada no fim da primeira semana. Criação do notion da equipe para a organização de informações sobre o projeto (incluindo a divisão de tarefas), e criação de um repositório que foi fundamental para o versionamento do projeto.
    
- Modelos de Pixel Art -
    
    Tivemos dificuldades com a criação de modelos utilizando pixel art, então utilizamos alguns modelos open source encontrados no site itch.io. Nesse site encontramos as sprites dos tanques, e algumas animações que foram úteis para a realização do projeto.
