import pygame
from sys import exit
import pygame.locals
import utils
import random
from menu import mostrar_menu


pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
centro_tela = (largura_tela // 2, altura_tela // 2)
relogio = pygame.time.Clock()


# TEXTO E TÍTULO DO ARQUIVO
pygame.display.set_caption("Pong")


fonte = pygame.font.Font(None, 100)
local_titulo = fonte.render("Pong", None, "WHITE")
rect_titulo = local_titulo.get_rect(center=(centro_tela[0], 100))


# PLACAR DOS JOGADORES
placar_fonte = pygame.font.Font(None, 50)
placar_jogador = 0
placar_adversario = 0

placar_jogador_texto = placar_fonte.render(str(placar_jogador), True, "WHITE")
placar_adversario_texto = placar_fonte.render(str(placar_adversario), True, "WHITE")

placar_jogador_rect = placar_jogador_texto.get_rect(center=(30, 50))
placar_adversario_rect = placar_adversario_texto.get_rect(
    center=(largura_tela - 30, 50)
)


fps_ligado = False  # tecla F para mostrar o FPS
grid_ligado = False  # tecla G para mostrar o grid
jogo_rodando = False  # tecla P o ESPAÇO para pausar o jogo
legenda_ligada = False  # tecla I para mostrar as legendas

# ---------------------------------------------------------------------------------

jogador_vel = 8
bola_velocidade = 6

# DEFININDO TAMANHO DOS RETÂNGULOS (JOGADORES)
jogador_rect_largura, jogador_rect_altura = 20, 150

# DEFININDO JOGADOR
jogador_pos = pygame.Vector2(50, 250)
jogador_vel = jogador_vel
jogador = pygame.Rect(
    jogador_pos.x, jogador_pos.y, jogador_rect_largura, jogador_rect_altura
)

# DEFININDO ADVERSÁRIO
adversario_pos = pygame.Vector2(largura_tela - 70, 250)
adversario_vel = jogador_vel
adversario = pygame.Rect(
    adversario_pos.x, adversario_pos.y, jogador_rect_largura, jogador_rect_altura
)

# DEFININDO BOLA
bola_pos = pygame.Vector2(centro_tela)
bola_vel = pygame.Vector2(bola_velocidade, bola_velocidade)
bola_r = 15


modo_jogo = mostrar_menu(tela, largura_tela, altura_tela)

#  LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # tecla F para mostrar o FPS
                fps_ligado = not fps_ligado
            elif event.key == pygame.K_g:  # tecla G para mostrar o grid
                grid_ligado = not grid_ligado
            elif (
                event.key == pygame.K_p or event.key == pygame.K_SPACE
            ):  # tecla P ou ESPAÇO para pausar o jogo
                jogo_rodando = not jogo_rodando
            elif event.key == pygame.K_r:  # tecla R para resetar o jogo
                jogo_rodando = False
                jogo_rodando = False
                (
                    jogador_pos,
                    adversario_pos,
                    bola_pos,
                    bola_vel,
                    placar_jogador,
                    placar_adversario,
                    placar_jogador_texto,
                    placar_adversario_texto,
                ) = utils.reset(
                    centro_tela,
                    largura_tela,
                    bola_velocidade,
                    placar_jogador,
                    placar_adversario,
                    placar_fonte,
                )

            elif event.key == pygame.K_i:
                legenda_ligada = not legenda_ligada
            elif event.key == pygame.K_ESCAPE:  # tecla ESC para sair do jogo
                pygame.quit()
                exit()

    tela.fill("BLACK")
    tela.blit(local_titulo, rect_titulo)

    # MOSTRANDO PLACAR

    tela.blit(placar_jogador_texto, placar_jogador_rect)
    tela.blit(placar_adversario_texto, placar_adversario_rect)

    # MOSTRANDO JOGADORES
    adversario = pygame.Rect(
        adversario_pos.x, adversario_pos.y, jogador_rect_largura, jogador_rect_altura
    )
    jogador = pygame.Rect(
        jogador_pos.x, jogador_pos.y, jogador_rect_largura, jogador_rect_altura
    )
    pygame.draw.rect(tela, "WHITE", jogador)
    pygame.draw.rect(tela, "WHITE", adversario)

    # BOLA
    pygame.draw.circle(tela, "white", bola_pos, bola_r)

    # PLAY / PAUSE
    if jogo_rodando:

        # DEFININDO MOVIMENTO DA BOLA
        bola_pos += bola_vel

        # COLISÃO DA BOLA COM AS BORDAS DA TELA
        if bola_pos.x - bola_r <= 0 or bola_pos.x + bola_r >= largura_tela:
            bola_vel.x = -bola_vel.x
        if bola_pos.y - bola_r <= 0 or bola_pos.y + bola_r >= altura_tela:
            bola_vel.y = -bola_vel.y

        # COLISÃO DA BOLA COM OS JOGADORES
        if jogador.colliderect(
            pygame.Rect(
                bola_pos.x - bola_r, bola_pos.y - bola_r, bola_r * 2, bola_r * 2
            )
        ):
            bola_vel.x = abs(bola_vel.x)
        if adversario.colliderect(
            pygame.Rect(
                bola_pos.x - bola_r, bola_pos.y - bola_r, bola_r * 2, bola_r * 2
            )
        ):
            bola_vel.x = -abs(bola_vel.x)

        # PONTUAÇÃO
        if bola_pos.x - bola_r <= 0:
            placar_adversario += 1
            placar_adversario_texto = placar_fonte.render(
                str(placar_adversario), True, "WHITE"
            )
            placar_adversario_rect = placar_adversario_texto.get_rect(
                center=(largura_tela - 30, 50)
            )
            bola_pos = pygame.Vector2(centro_tela)
            bola_vel = pygame.Vector2(
                bola_velocidade * random.choice([-1, 1]),
                bola_velocidade * random.choice([-1, 1]),
            )
        elif bola_pos.x + bola_r >= largura_tela:
            placar_jogador += 1
            placar_jogador_texto = placar_fonte.render(
                str(placar_jogador), True, "WHITE"
            )
            placar_jogador_rect = placar_jogador_texto.get_rect(center=(30, 50))
            bola_pos = pygame.Vector2(centro_tela)
            bola_vel = pygame.Vector2(
                bola_velocidade * random.choice([-1, 1]),
                bola_velocidade * random.choice([-1, 1]),
            )

        # MOVIMENTOS DOS JOGADORES
        keys = pygame.key.get_pressed()
        if modo_jogo == "computador":
            # Jogador 1 pode usar W/S ou as setas para se movimentar
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                jogador_pos.y -= jogador_vel
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                jogador_pos.y += jogador_vel
            jogador_pos.y = max(
                0, min(jogador_pos.y, altura_tela - jogador_rect_altura)
            )
            # MOVIMENTO DO COMPUTADOR MODO AUTOMÁTICO
            adversario_pos.y += adversario_vel
            if adversario.bottom >= altura_tela:
                adversario_vel = -abs(adversario_vel)
            elif adversario.top <= 0:
                adversario_vel = abs(adversario_vel)
        elif modo_jogo == "1x1":
            # Jogador 1 usa W/S
            if keys[pygame.K_w]:
                jogador_pos.y -= jogador_vel
            if keys[pygame.K_s]:
                jogador_pos.y += jogador_vel
            jogador_pos.y = max(
                0, min(jogador_pos.y, altura_tela - jogador_rect_altura)
            )

            # Jogador 2 usa as setas
            if keys[pygame.K_UP]:
                adversario_pos.y -= jogador_vel
            if keys[pygame.K_DOWN]:
                adversario_pos.y += jogador_vel
            adversario_pos.y = max(
                0, min(adversario_pos.y, altura_tela - jogador_rect_altura)
            )

    # TOGGLE BINDS
    if fps_ligado:
        utils.mostrar_fps(relogio, tela)
    if grid_ligado:
        utils.mostrar_grid(tela, largura_tela)

    utils.mostrar_legenda(tela, largura_tela, legenda_ligada)

    pygame.display.update()
    relogio.tick(60)
