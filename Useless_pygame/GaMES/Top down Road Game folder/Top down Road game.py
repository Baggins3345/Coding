import pygame
pygame.init()
from sys import exit



velocity = 12
x = 100
y = 100
Screen = pygame.display.set_mode((630, 750))

Road_Surface = pygame.image.load("C:\Coding\GaMES\Top down Road Game folder\Top down road.png")
road_surf_y = 0
Road_Surface2 = pygame.image.load("C:\Coding\GaMES\Top down Road Game folder\Top down road.png")
road_surf_y2 = -1000

Car = pygame.image.load("C:\Coding\GaMES\Top down Road Game folder\YellowBuggy_strip4-4.png.png")
Car_Rect = Car.get_rect(center=(540, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= velocity
            if event.key == pygame.K_RIGHT:
                x += velocity
            if event.key == pygame.K_UP:
                y -= velocity
            if event.key == pygame.K_DOWN:
                y += velocity


    road_surf_y += 3
    road_surf_y2 += 3
    if road_surf_y > 1000: road_surf_y = -1000
    if road_surf_y2 > 1000: road_surf_y2 = -1000
    Screen.blit(Road_Surface, (0, road_surf_y))
    Screen.blit(Road_Surface2, (0, road_surf_y2))
    Screen.blit(Car, (x, y))  # Update the car's position

    pygame.display.update()
