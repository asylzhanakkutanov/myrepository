import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

clock = pygame.time.Clock()

ball = Ball(300, 200, screen_size=(WIDTH, HEIGHT))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ball.move(-20, 0)

    if keys[pygame.K_RIGHT]:
        ball.move(20, 0)

    if keys[pygame.K_UP]:
        ball.move(0, -20)

    if keys[pygame.K_DOWN]:
        ball.move(0, 20)

    screen.fill((64, 64, 64))

    ball.draw(screen, pygame)

    pygame.display.update()

pygame.quit()