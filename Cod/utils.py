import pygame

pygame.init()


# FUNÇÃO PARA MOSTRAR FPS
def mostrar_fps(relogio, tela):
    fonte_info = pygame.font.Font(None, 30)
    fps_info = fonte_info.render(str(int(relogio.get_fps())), None, "green")
    tela.blit(fps_info, (0, 0))


# FUNÇÃO PARA MOSTRAR LEGENDA DOS ATALHOS
def mostrar_legenda(tela, legenda_ligada):
    fonte_legenda = pygame.font.Font(None, 20)
    if legenda_ligada:
        legenda_txt = fonte_legenda.render(
            "Pausar - P ou ESPAÇO | Reiniciar - R | FPS - F | Fechar legenda - I | Sair - ESC",
            True,
            "green",
        )
    else:
        legenda_txt = fonte_legenda.render("Mostrar legenda - I", True, "green")

    tela.blit(legenda_txt, (tela.get_width() - legenda_txt.get_width() - 10, 10))


# TOGGLE BINDS
def toggle_binds(relogio, tela, fps_ligado, legenda_ligada):
    if fps_ligado:
        mostrar_fps(relogio, tela)
    mostrar_legenda(tela, legenda_ligada)


# FUNÇÃO PARA REINICIAR O JOGO
def reset(
    centro_tela,
    largura_tela,
    bola_velocidade,
    placar_jogador,
    placar_adversario,
    placar_fonte,
):

    jogador_pos = pygame.Vector2(50, 250)
    adversario_pos = pygame.Vector2(largura_tela - 70, 250)
    bola_pos = pygame.Vector2(centro_tela)
    bola_vel = pygame.Vector2(bola_velocidade, bola_velocidade)

    placar_jogador = 0
    placar_adversario = 0

    placar_jogador_texto = placar_fonte.render(str(placar_jogador), True, "WHITE")
    placar_adversario_texto = placar_fonte.render(str(placar_adversario), True, "WHITE")

    return (
        jogador_pos,
        adversario_pos,
        bola_pos,
        bola_vel,
        placar_jogador,
        placar_adversario,
        placar_jogador_texto,
        placar_adversario_texto,
    )


# FUNÇÃO QUE DEFINE O MOVIMENTO DA BOLA
def movimento_bola(
    bola_pos, bola_vel, bola_r, largura_tela, altura_tela, jogador, adversario
):
    # Atualiza a posição da bola
    bola_pos += bola_vel

    # Colisão com as bordas da tela
    if bola_pos.x - bola_r <= 0 or bola_pos.x + bola_r >= largura_tela:
        bola_vel.x = -bola_vel.x
    if bola_pos.y - bola_r <= 0 or bola_pos.y + bola_r >= altura_tela:
        bola_vel.y = -bola_vel.y

    # COLISÃO DA BOLA COM OS JOGADORES
    if jogador.colliderect(
        pygame.Rect(bola_pos.x - bola_r, bola_pos.y - bola_r, bola_r * 2, bola_r * 2)
    ):
        bola_vel.x = abs(bola_vel.x)
    if adversario.colliderect(
        pygame.Rect(bola_pos.x - bola_r, bola_pos.y - bola_r, bola_r * 2, bola_r * 2)
    ):
        bola_vel.x = -abs(bola_vel.x)

    return bola_pos, bola_vel


# FUNÇÃO QUE DEFINE O MOVIMENTO DOS JOGADORES
def movimento_jogadores(
    keys,
    modo_jogo,
    jogador_pos,
    adversario_pos,
    jogador_vel,
    adversario_vel,
    altura_tela,
    jogador_rect_altura,
):
    if modo_jogo == "computador":
        # Jogador 1 pode usar W/S ou as setas para se movimentar
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            jogador_pos.y -= jogador_vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            jogador_pos.y += jogador_vel
        jogador_pos.y = max(0, min(jogador_pos.y, altura_tela - jogador_rect_altura))

        # Movimento automático do computador
        adversario_pos.y += adversario_vel
        if (
            adversario_pos.y + jogador_rect_altura >= altura_tela
            or adversario_pos.y <= 0
        ):
            adversario_vel *= -1

    elif modo_jogo == "1x1":
        # Jogador 1 usa W/S
        if keys[pygame.K_w]:
            jogador_pos.y -= jogador_vel
        if keys[pygame.K_s]:
            jogador_pos.y += jogador_vel
        jogador_pos.y = max(0, min(jogador_pos.y, altura_tela - jogador_rect_altura))

        # Jogador 2 usa as setas
        if keys[pygame.K_UP]:
            adversario_pos.y -= jogador_vel
        if keys[pygame.K_DOWN]:
            adversario_pos.y += jogador_vel
        adversario_pos.y = max(
            0, min(adversario_pos.y, altura_tela - jogador_rect_altura)
        )

    return jogador_pos, adversario_pos, adversario_vel
