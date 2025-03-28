import pygame

pygame.init()


# FUNÇÃO PARA MOSTRAR FPS


def mostrar_fps(relogio, tela):
    fonte_info = pygame.font.Font("font/Pixeltype.ttf", 30)
    fps_info = fonte_info.render(str(int(relogio.get_fps())), None, "green")
    tela.blit(fps_info, (0, 0))


# FUNÇÃO PARA MOSTRAR GRID


def mostrar_grid(screen, screen_witdth):
    for x in range(0, screen_witdth, 50):
        pygame.draw.line(screen, "RED", (1, x), (screen_witdth, x), 1)
        pygame.draw.line(screen, "RED", (x, 1), (x, screen_witdth), 1)


# FUNÇÃO PARA MOSTRAR LEGENDA DOS ATALHOS


def mostrar_legenda(tela, largura_tela):
    fonte_legenda = pygame.font.Font("font/Pixeltype.ttf", 20)
    legenda_txt = fonte_legenda.render(
        "Pausar - P | Reiniciar - R | FPS - F | Mostrar grid - G | Sair do menu - I",
        True,
        "green",
    )

    tela.blit(legenda_txt, (largura_tela - legenda_txt.get_width() - 10, 10))


# FUNÇÃO RESET


def reset(centro_tela, largura_tela, vel):

    jogador_pos = pygame.Vector2(50, 250)
    adversario_pos = pygame.Vector2(largura_tela - 70, 250)
    bola_pos = pygame.Vector2(centro_tela)
    bola_vel = pygame.Vector2(vel, vel)

    return jogador_pos, adversario_pos, bola_pos, bola_vel
