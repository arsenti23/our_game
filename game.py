import pygame
import os
import sys

COLOR1 = (0, 0, 0)
COLOR2 = (255, 255, 255)
COLORR = (255, 0, 0)
COLORG = (0, 255, 0)
COLORB = (0, 0, 255)

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
FPS = 30


def terminate(self):
    pygame.quit()
    sys.exit()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.fill(COLOR1)
    pygame.display.flip()
