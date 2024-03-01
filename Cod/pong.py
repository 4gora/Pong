import pygame
from sys import exit
import pygame.locals
import utils

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


# TEXTO E TÍTULO DO ARQUIVO
pygame.display.set_caption("Pong")
font = pygame.font.Font("font/Pixeltype.ttf", 100)
title_surface = font.render("Pong", None, "WHITE")

fps_toggle = False

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


#  LOOP PRINCIPAL
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fps_toggle = not fps_toggle

    SCREEN.fill("BLACK")
    SCREEN.blit(title_surface, (350, 100))

    # DEFININDO MOVIMENTO DO ADVERSÁRIO
    adversario_pos.y += adversario_vel
    if adversario.bottom >= SCREEN_HEIGHT:
        adversario_vel = -abs(adversario_vel)
    elif adversario.top <= 0:
        adversario_vel = abs(adversario_vel)

    # MOSTRANDO JOGADORES
    adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, ret_width, ret_height)
    jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, ret_width, ret_height)
    pygame.draw.rect(SCREEN, "WHITE", jogador)
    pygame.draw.rect(SCREEN, "WHITE", adversario)

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

    if fps_toggle:
        utils.show_fps(clock, SCREEN)

    pygame.display.update()
    clock.tick(60)
