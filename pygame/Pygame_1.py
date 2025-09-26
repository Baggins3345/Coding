import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Variable for the screen size 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("First Game!")
WHITE = (255,255,255)
FPS = 60

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
player = pygame.Rect((300,250,50,50))

obsticles = []
for _ in range(16):
    obsticle_rect = pygame.Rect(random.randint(0,700), random.randint(0,500),25,25)
    obsticles.append(obsticle_rect)

def draw_window():
    col = RED
    if player.collidelist(obsticles) >=0:
        col = GREEN
    screen.fill(WHITE)
    pos = pygame.mouse.get_pos()
    player.center = pos
    pygame.draw.rect(screen,col, player)
    for obsticle in obsticles:
        pygame.draw.rect(screen,BLUE,obsticle)
    pygame.display.update()
    

def main():
    clock = pygame.time.Clock()
    run = True
    pygame.mouse.set_visible(False)
    
    # Game play loop
    while run:
        
        clock.tick(FPS)
        # key = pygame.key.get_pressed()
        # if key[pygame.K_a] == True:
        #     player.move_ip(-5,0)

        # elif key[pygame.K_d] == True:
        #     player.move_ip(5,0)

        # elif key[pygame.K_w] == True:
        #     player.move_ip(0,-5)

        # elif key[pygame.K_s] == True:
        #     player.move_ip(0,5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        
    pygame.quit()

if __name__ == "__main__":
    main()

