import pygame
pygame.init()
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
screen.fill((0, 0, 0))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #pygame.display.update()
