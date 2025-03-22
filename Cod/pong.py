import pygame
from sys import exit
import pygame.locals
import utils


pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
centro_tela = (largura_tela // 2, altura_tela // 2)
relogio = pygame.time.Clock()


# TEXTO E TÍTULO DO ARQUIVO
pygame.display.set_caption("Pong")


fonte = pygame.font.Font("./font/Pixeltype.ttf", 100)
local_titulo = fonte.render("Pong", None, "WHITE")
rect_titulo = local_titulo.get_rect(center=(centro_tela[0], 100))


fps_ligado = False # tecla F para mostrar o FPS
grid_ligado = False # tecla G para mostrar o grid
jogo_rodando = False # tecla P o ESPAÇO para pausar o jogo
legenda_ligada = True # tecla I para mostrar as legendas

# ---------------------------------------------------------------------------------

vel = 8

# DEFININDO TAMANHO DOS RETÂNGULOS (JOGADORES)
jogador_rect_largura, jogador_rect_altura = 20, 150

# DEFININDO JOGADOR
jogador_pos = pygame.Vector2(50, 250)
jogador_vel = vel
jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, jogador_rect_largura, jogador_rect_altura)

# DEFININDO ADVERSÁRIO
adversario_pos = pygame.Vector2(largura_tela - 70, 250)
adversario_vel = vel
adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, jogador_rect_largura, jogador_rect_altura)

# DEFININDO BOLA
bola_pos = pygame.Vector2(centro_tela)
bola_vel = pygame.Vector2(vel, vel)
bola_r = 15


#  LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f: # tecla F para mostrar o FPS
                fps_ligado = not fps_ligado
            elif event.key == pygame.K_g: # tecla G para mostrar o grid
                grid_ligado = not grid_ligado
            elif event.key == pygame.K_p or event.key == pygame.K_SPACE: # tecla P ou ESPAÇO para pausar o jogo
                jogo_rodando = not jogo_rodando
            elif event.key == pygame.K_r: # tecla R para resetar o jogo
                jogo_rodando = False
                jogador_pos, adversario_pos, bola_pos, bola_vel = utils.reset(
                    centro_tela, largura_tela, vel
                )
            elif event.key == pygame.K_i:
                legenda_ligada = not legenda_ligada

    tela.fill("BLACK")
    tela.blit(local_titulo, rect_titulo)

    # MOSTRANDO JOGADORES
    adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, jogador_rect_largura, jogador_rect_altura)
    jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, jogador_rect_largura, jogador_rect_altura)
    pygame.draw.rect(tela, "WHITE", jogador)
    pygame.draw.rect(tela, "WHITE", adversario)

    # BOLA
    pygame.draw.circle(tela, "white", bola_pos, bola_r)

    # PLAY / PAUSE
    if jogo_rodando:
        # DEFININDO MOVIMENTO DO ADVERSÁRIO
        adversario_pos.y += adversario_vel
        if adversario.bottom >= altura_tela:
            adversario_vel = -abs(adversario_vel)
        elif adversario.top <= 0:
            adversario_vel = abs(adversario_vel)

        # DEFININDO MOVIMENTO DA BOLA
        bola_pos += bola_vel

        if bola_pos.x - bola_r <= 0 or bola_pos.x + bola_r >= largura_tela:
            bola_vel.x = -bola_vel.x
        if bola_pos.y - bola_r <= 0 or bola_pos.y + bola_r >= altura_tela:
            bola_vel.y = -bola_vel.y

        # MOVIMENTO DO JOGADOR
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            jogador_pos.y -= jogador_vel  # movimenta o jogador para cima
            jogador_pos.y = max(
                jogador_pos.y, 0
            )  # limita o movimento para cima por meio da função max()
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            jogador_pos.y += jogador_vel  # movimenta o jogador para baixo
            jogador_pos.y = min(
                jogador_pos.y, altura_tela - jogador.height
            )  # limita o movimento para baixo com a função min()

    # TOGGLE BINDS
    if fps_ligado:
        utils.mostrar_fps(relogio, tela)
    if grid_ligado:
        utils.mostrar_grid(tela, largura_tela)
    if legenda_ligada:
        utils.mostrar_legenda(tela, largura_tela)

    pygame.display.update()
    relogio.tick(60)
