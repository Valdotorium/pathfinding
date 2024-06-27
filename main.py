import pygame
import asyncio
async def main():
    #basic pygame scriipt

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("project phoenix")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        screen.fill((0,0,0))
        clock.tick(60)

if __name__ == "__main__":
    asyncio.run(main())
