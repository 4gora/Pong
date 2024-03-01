import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pong")

# TEXTO ESCRITO NO JOGO -- PONG
font = pygame.font.Font("font/Pixeltype.ttf", 100)
title_surface = font.render("Pong", None, "WHITE")

clock = pygame.time.Clock()

# DEFININDO TAMANHO DOS RETÂNGULOS (JOGADORES)
ret_width, ret_height = 20, 150

jogador = pygame.Rect(50, 250, ret_width, ret_height)

# DEFININDO ADVERSÁRIO
adversario_pos = pygame.Vector2(700, 250)
adversario_vel = 4
adversario = pygame.Rect(
    adversario_pos.x, adversario_pos.y, ret_width, ret_height)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    adversario_pos.y += adversario_vel
    if adversario_pos.y + adversario.height >= SCREEN_HEIGHT:
        adversario_vel = -adversario_vel
    elif adversario_pos.y <= 0:
        adversario_vel = abs(adversario_vel)

    adversario = pygame.Rect(adversario_pos.x, adversario_pos.y, 20, 150)

    SCREEN.fill("BLACK")
    SCREEN.blit(title_surface, (350, 100))

    pygame.draw.rect(SCREEN, "WHITE", jogador)
    pygame.draw.rect(SCREEN, "WHITE", adversario)

    pygame.display.update()
    clock.tick(60)
