import pygame
from sys import exit


def ball_animation():

    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pong 2")

# PLAYERS AND BALL
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 7
            if event.key == pygame.K_s:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 7
            if event.key == pygame.K_s:
                player_speed -= 7

    ball_animation()

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    screen.fill("grey12")
    pygame.draw.rect(screen, "WHITE", player)
    pygame.draw.rect(screen, "WHITE", opponent)
    pygame.draw.ellipse(screen, "WHITE", ball)
    pygame.draw.aaline(
        screen, "WHITE", (screen_width / 2, 0), (screen_width / 2, screen_height)
    )

    pygame.display.flip()
    clock.tick(60)