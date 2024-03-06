import pygame
from sys import exit
import pygame.locals
import utils

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
clock = pygame.time.Clock()


# TEXTO E TÍTULO DO ARQUIVO
pygame.display.set_caption("Pong")
font = pygame.font.Font("font/Pixeltype.ttf", 100)
title_surface = font.render("Pong", None, "WHITE")
rect_title = title_surface.get_rect(center=(SCREEN_CENTER[0], 100))


fps_toggle = False
grid_toggle = False

# ---------------------------------------------------------------------------------

# DEFININDO TAMANHO DOS RETÂNGULOS (JOGADORES)
ret_width, ret_height = 20, 150

# DEFININDO JOGADOR
jogador_pos = pygame.Vector2(50, 250)
jogador_vel = 4
jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, ret_width, ret_height)

# DEFININDO ADVERSÁRIO
adversario_pos = pygame.Vector2(700, 250)
adversario_vel = 4
adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, ret_width, ret_height)

# DEFININDO BOLA
bola_pos = pygame.Vector2(SCREEN_CENTER)
bola_vel = pygame.Vector2(4, 4)
bola_r = 20


#  LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fps_toggle = not fps_toggle
            elif event.key == pygame.K_g:
                grid_toggle = not grid_toggle

    SCREEN.fill("BLACK")
    SCREEN.blit(title_surface, rect_title)

    # MOSTRANDO JOGADORES
    adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, ret_width, ret_height)
    jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, ret_width, ret_height)
    pygame.draw.rect(SCREEN, "WHITE", jogador)
    pygame.draw.rect(SCREEN, "WHITE", adversario)

    # BOLA
    pygame.draw.circle(SCREEN, "white", bola_pos, bola_r)

    # DEFININDO MOVIMENTO DO ADVERSÁRIO
    adversario_pos.y += adversario_vel
    if adversario.bottom >= SCREEN_HEIGHT:
        adversario_vel = -abs(adversario_vel)
    elif adversario.top <= 0:
        adversario_vel = abs(adversario_vel)

    # DEFININDO MOVIMENTO DA BOLA
    bola_pos.x += bola_vel.x
    bola_pos.y += bola_vel.y

    if bola_pos.x - bola_r <= 0 or bola_pos.x + bola_r >= SCREEN_WIDTH:
        bola_vel.x = -bola_vel.x
    if bola_pos.y - bola_r <= 0 or bola_pos.y + bola_r >= SCREEN_HEIGHT:
        bola_vel.y = -bola_vel.y

    # MOVIMENTO DO JOGADOR
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jogador_pos.y -= jogador_vel  # movimenta o jogador para cima
        jogador_pos.y = max(
            jogador_pos.y, 0
        )  # limita o movimento para cima por meio da função max()
    elif keys[pygame.K_s]:
        jogador_pos.y += jogador_vel  # movimenta o jogador para baixo
        jogador_pos.y = min(
            jogador_pos.y, SCREEN_HEIGHT - jogador.height
        )  # limita o movimento para baixo com a função min()

    # TOGGLE BINDS
    if fps_toggle:
        utils.show_fps(clock, SCREEN)
    if grid_toggle:
        utils.show_grid(SCREEN, SCREEN_WIDTH)

    pygame.display.update()
    clock.tick(60)
