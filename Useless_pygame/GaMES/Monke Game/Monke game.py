import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1146, 640))
pygame.display.set_caption("Monke Game")
bg = pygame.image.load("C:\Coding\GaMES\Monke Game\Bg.png").convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_image = pygame.image.load("C:\Coding\GaMES\Monke Game\Monke.png").convert_alpha()
        self.image = player_image
        self.rect = self.image.get_rect(midbottom=(1070,630))

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

class People(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        people_image = pygame.image.load("C:\Coding\GaMES\Monke Game\People.png").convert_alpha()
        self.image = people_image
        self.rect = self.image.get_rect(midbottom = (1200,1000))

    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.rect.right = 1800  # Reset position to the right edge of the screen

banana_sprite = pygame.image.load("C:\Coding\GaMES\Monke Game\Banana.png").convert_alpha()
banana_rect = banana_sprite.get_rect(midbottom = (0,0))

player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(Player())

people_sprite = pygame.sprite.GroupSingle()
people_sprite.add(People())

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((64,64,64))
    player_sprite.sprite.movement()

    player_sprite.update()
    people_sprite.update()

    player_sprite.draw(screen)
    screen.blit(bg,(0, 0))
    people_sprite.draw(screen)
    
    screen.blit(banana_rect)

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS
