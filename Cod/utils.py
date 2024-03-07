import pygame

pygame.init()


# FUNÇÃO PARA MOSTRAR FPS


def show_fps(clock, SCREEN):
    info_font = pygame.font.Font("font/Pixeltype.ttf", 30)
    fps_info = info_font.render(str(int(clock.get_fps())), None, "green")
    SCREEN.blit(fps_info, (0, 0))


# FUNÇÃO PARA MOSTRAR GRID


def show_grid(SCREEN, SCREEN_WIDTH):
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(SCREEN, "RED", (1, x), (SCREEN_WIDTH, x), 1)
        pygame.draw.line(SCREEN, "RED", (x, 1), (x, SCREEN_WIDTH), 1)


# FUNÇÃO PARA MOSTRAR LEGENDA DE BINDING


def show_binding_caption(SCREEN, SCREEN_WIDTH):
    caption_font = pygame.font.Font("font/Pixeltype.ttf", 20)
    caption = caption_font.render(
        "Play/ pause - P | Reset - R | Show FPS - F | Show grid - G | Exit menu - I",
        True,
        "green",
    )

    SCREEN.blit(caption, (SCREEN_WIDTH - caption.get_width() - 10, 10))


# FUNÇÃO RESET


def reset(SCREEN_CENTER, SCREEN_WIDTH, vel):

    jogador_pos = pygame.Vector2(50, 250)
    adversario_pos = pygame.Vector2(SCREEN_WIDTH - 70, 250)
    bola_pos = pygame.Vector2(SCREEN_CENTER)
    bola_vel = pygame.Vector2(vel, vel)

    return jogador_pos, adversario_pos, bola_pos, bola_vel
