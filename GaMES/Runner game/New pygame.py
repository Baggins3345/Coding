#this is like the body of the car
import pygame
from sys import exit

#this is like turing the key to start the car
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')

#draw all our elemets and update eveything, and close
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #this is the opposite to 'pygame.init()'
            exit() #this is from the module 'sys' to exit the game

    screen.blit(test_surface,(200,100))#blit means put on another surface
    
    pygame.display.update()
    clock.tick(60)




