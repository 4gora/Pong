import pygame

pygame.init()


# FUNÇÃO PARA MOSTRAR FPS


def show_fps(clock, screen):
    info_font = pygame.font.Font("font/Pixeltype.ttf", 30)
    fps_info = info_font.render(str(int(clock.get_fps())), None, "green")
    screen.blit(fps_info, (0, 0))


# FUNÇÃO PARA MOSTRAR GRID


def show_grid(screen, screen_witdth):
    for x in range(0, screen_witdth, 50):
        pygame.draw.line(screen, "RED", (1, x), (screen_witdth, x), 1)
        pygame.draw.line(screen, "RED", (x, 1), (x, screen_witdth), 1)


# FUNÇÃO PARA MOSTRAR LEGENDA DE BINDING


def show_binding_caption(screen, screen_witdth):
    caption_font = pygame.font.Font("font/Pixeltype.ttf", 20)
    caption = caption_font.render(
        "Play/ pause - P | Reset - R | Show FPS - F | Show grid - G | Exit menu - I",
        True,
        "green",
    )

    screen.blit(caption, (screen_witdth - caption.get_width() - 10, 10))


# FUNÇÃO RESET


def reset(screen_center, screen_witdth, vel):

    jogador_pos = pygame.Vector2(50, 250)
    adversario_pos = pygame.Vector2(screen_witdth - 70, 250)
    bola_pos = pygame.Vector2(screen_center)
    bola_vel = pygame.Vector2(vel, vel)

    return jogador_pos, adversario_pos, bola_pos, bola_vel
