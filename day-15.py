# This is a Python program that simulates a DVD screensaver

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 540
ball_radius = 25

x = random.randint(ball_radius, SCREEN_WIDTH - ball_radius)
y = random.randint(ball_radius, SCREEN_HEIGHT - ball_radius)
dx = 5
dy = 5


def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


color = random_color()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x += dx
    y += dy

    if x - ball_radius <= 0 or x + ball_radius >= SCREEN_WIDTH:
        dx *= -1
        color = random_color()
    if y - ball_radius <= 0 or y + ball_radius >= SCREEN_HEIGHT:
        dy *= -1
        color = random_color()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (x, y), ball_radius)
    pygame.display.flip()
