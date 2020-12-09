import pygame
pygame.init()
white = 255,255,255
black = 0,0,0
screen = pygame.display.set_mode((600,600))
ball = pygame.draw.circle(screen, white, [450,200], 30, width=0)
top = pygame.draw.rect(screen,white,[0,0,600,10])
left = pygame.draw.rect(screen,white,[0,0,10,600])
right = pygame.draw.rect(screen,white,[590,0,10,600])
player = pygame.draw.rect(screen,white,[300,450,100,10])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    pygame.display.flip()