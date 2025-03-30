import pygame
from sys import exit

def mostrar_menu(tela, largura_tela, altura_tela):
    pygame.init()
    fonte_menu = pygame.font.Font("./font/Pixeltype.ttf", 50)
    modo_jogo = None

    while modo_jogo is None:
        tela.fill("BLACK")

        # Texto do menu
        titulo = fonte_menu.render("Escolha o modo de jogo:", True, "WHITE")
        opcao_1 = fonte_menu.render("1. Contra o Computador", True, "WHITE")
        opcao_2 = fonte_menu.render("2. 1x1 (Dois Jogadores)", True, "WHITE")

        # Posicionamento do texto
        tela.blit(titulo, (largura_tela // 2 - titulo.get_width() // 2, altura_tela // 3))
        tela.blit(opcao_1, (largura_tela // 2 - opcao_1.get_width() // 2, altura_tela // 2))
        tela.blit(opcao_2, (largura_tela // 2 - opcao_2.get_width() // 2, altura_tela // 2 + 60))

        pygame.display.update()

        # Eventos para capturar a escolha do jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Jogar contra o computador
                    modo_jogo = "computador"
                elif event.key == pygame.K_2:  # Jogar 1x1
                    modo_jogo = "1x1"
                elif event.key == pygame.K_ESCAPE:  # Sair do jogo
                    pygame.quit()
                    exit()

    return modo_jogo