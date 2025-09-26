import pygame

from pygame.locals import *

pygame.init()

screen_w = 1000
screen_h = 1000

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Platformer")

bg_img = pygame.image.load("C:/Users/baggi/Downloads/kenney_platformer-art-deluxe/Base pack/bg.png")

run = True
while run: 

    screen.blit(bg_img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
