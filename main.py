import pygame
import asyncio
import res.game as game
async def main():
    #basic pygame scriipt

    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    Phoenix = game.Game(screen, (1200, 800))
    pygame.display.set_caption("project phoenix")
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        Phoenix.update()
        screen.fill((0,0,0))
        clock.tick(60)


if __name__ == "__main__":
    asyncio.run(main())
