import pygame


# FUNÇÃO PARA MOSTRAR FPS

def show_fps(clock, SCREEN):
    info_font = pygame.font.Font("font/Pixeltype.ttf", 30)
    fps_info = info_font.render(str(int(clock.get_fps())), None, "green")
    SCREEN.blit(fps_info, (0, 0))


# FUNÇÃO PARA MOSTRAR GRID

def show_grid(SCREEN, SCREEN_WIDTH):
    for x in range(0, SCREEN_WIDTH, 50):
        pygame.draw.line(SCREEN, 'RED', (1, x), (SCREEN_WIDTH, x), 1)
        pygame.draw.line(SCREEN, 'RED', (x, 1), (x, SCREEN_WIDTH), 1)
