import pygame


# FUNÇÃO PARA MOSTRAR FPS

def show_fps(clock, SCREEN):
    info_font = pygame.font.Font("font/Pixeltype.ttf", 30)
    fps_info = info_font.render(str(int(clock.get_fps())), None, "green")
    SCREEN.blit(fps_info, (0, 0))
