import pygame
from sys import exit

class Player1():
    def __init__(self):
        super().__init__()
        self.P1 = pygame.draw.rect(screen, (255,0,0), (10,100,10,100))


    def movment(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.P1.y < 600:
            self.P1.y -= 10
        if keys[pygame.K_DOWN] and self.P1.y > 0:
            self.P1.y += 10

    def update(self):
        self.movment()

       


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

player1 = pygame.sprite.GroupSingle()
player1.add(Player1())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player1.draw(screen)
    player1.update()



    pygame.display.flip()
    clock.tick(60)