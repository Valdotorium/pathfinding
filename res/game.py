import pygame
import res.world as world
class Game():
    def __init__(self, screen, screenSize):
        #world data
        self.worldSize = 100
        #generate world data from world.py module
        self.world = world.createWorld(self.worldSize)

        #visuals
        self.tileSize = 50
        self.zoom = 1.0
        self.cameraPosition = ((self.worldSize / 2) * self.zoom , (self.worldSize / 2) * self.zoom)
        self.screen = screen
        self.screenSize = screenSize

        #options from options.json file

        #others
        self.mousePos = pygame.mouse.get_pos()
        self.clickPos = pygame.mouse.get_pressed()[0]
        self.keys = pygame.key.get_pressed()
    def interactions(self):
        #update mouse click state and position and detect key presses
        self.mousePos = pygame.mouse.get_pos()
        self.clickPos = pygame.mouse.get_pressed()[0]
        self.keys = pygame.key.get_pressed()

        #using WASD to move camera position
        if self.keys[pygame.K_w]:
            self.cameraPosition[1] -= 1
        if self.keys[pygame.K_s]:
            self.cameraPosition[1] += 1
        if self.keys[pygame.K_a]:
            self.cameraPosition[0] -= 1
        if self.keys[pygame.K_d]:
            self.cameraPosition[0] += 1

        #using mouse scroll to zoom in and out
        scroll = pygame.mouse.get_pressed()[1]
        if scroll > 0:
            self.zoom *= 1.1
        if scroll < 0:
            self.zoom /= 1.1

    def update(self):
        self.interactions()
        world.draw(self.screen, self.world, self.zoom, self.cameraPosition, self.tileSize, self.screenSize)
        pygame.display.flip()

        #update
        
