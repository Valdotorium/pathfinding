import pygame

#basic pygame scriipt

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("First Game")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)
