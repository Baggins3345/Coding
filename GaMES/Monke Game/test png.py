import pygame, sys
try:
    player_image = pygame.image.load("C:\Coding\GaMES\Monke Game\Monke.png").convert_alpha()
    people_image = pygame.image.load("C:\Coding\GaMES\Monke Game\People.png").convert_alpha()
except pygame.error as e:
    print("Error loading image:", e)
    pygame.quit()
    sys.exit()