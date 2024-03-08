import pygame
from sys import exit
import pygame.locals
import utils

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_center = (screen_width // 2, screen_height // 2)
clock = pygame.time.Clock()


# TEXTO E TÍTULO DO ARQUIVO
pygame.display.set_caption("Pong")
font = pygame.font.Font("font/Pixeltype.ttf", 100)
title_surface = font.render("Pong", None, "WHITE")
rect_title = title_surface.get_rect(center=(screen_center[0], 100))


fps_toggle = False
grid_toggle = False
game_running = False
caption_toggle = False

# ---------------------------------------------------------------------------------

vel = 8

# DEFININDO TAMANHO DOS RETÂNGULOS (JOGADORES)
ret_width, ret_height = 20, 150

# DEFININDO JOGADOR
jogador_pos = pygame.Vector2(50, 250)
jogador_vel = vel
jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, ret_width, ret_height)

# DEFININDO ADVERSÁRIO
adversario_pos = pygame.Vector2(screen_width - 70, 250)
adversario_vel = vel
adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, ret_width, ret_height)

# DEFININDO BOLA
bola_pos = pygame.Vector2(screen_center)
bola_vel = pygame.Vector2(vel, vel)
bola_r = 15


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
            elif event.key == pygame.K_p:
                game_running = not game_running
            elif event.key == pygame.K_r:
                game_running = False
                jogador_pos, adversario_pos, bola_pos, bola_vel = utils.reset(
                    screen_center, screen_width, vel
                )
            elif event.key == pygame.K_i:
                caption_toggle = not caption_toggle

    screen.fill("BLACK")
    screen.blit(title_surface, rect_title)

    # MOSTRANDO JOGADORES
    adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, ret_width, ret_height)
    jogador = pygame.Rect(jogador_pos.x, jogador_pos.y, ret_width, ret_height)
    pygame.draw.rect(screen, "WHITE", jogador)
    pygame.draw.rect(screen, "WHITE", adversario)

    # BOLA
    pygame.draw.circle(screen, "white", bola_pos, bola_r)

    # PLAY / PAUSE
    if game_running:
        # DEFININDO MOVIMENTO DO ADVERSÁRIO
        adversario_pos.y += adversario_vel
        if adversario.bottom >= screen_height:
            adversario_vel = -abs(adversario_vel)
        elif adversario.top <= 0:
            adversario_vel = abs(adversario_vel)

        # DEFININDO MOVIMENTO DA BOLA
        bola_pos += bola_vel

        if bola_pos.x - bola_r <= 0 or bola_pos.x + bola_r >= screen_width:
            bola_vel.x = -bola_vel.x
        if bola_pos.y - bola_r <= 0 or bola_pos.y + bola_r >= screen_height:
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
                jogador_pos.y, screen_height - jogador.height
            )  # limita o movimento para baixo com a função min()

    # TOGGLE BINDS
    if fps_toggle:
        utils.show_fps(clock, screen)
    if grid_toggle:
        utils.show_grid(screen, screen_width)
    if caption_toggle:
        utils.show_binding_caption(screen, screen_width)

    pygame.display.update()
    clock.tick(75)
