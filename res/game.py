import pygame
import res.world as world
class Game():
    def __init__(self, screen, screenSize):
        #world data
        self.worldSize = 200
        #generate world data from world.py module
        self.world = world.createWorld(self.worldSize)

        #visuals
        self.tileSize = 50
        self.zoom = 1.0
        self.cameraPosition = [(self.worldSize / 2) * self.zoom , (self.worldSize / 2) * self.zoom]
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

        #also using Q and E to zoom
        if self.keys[pygame.K_q]:
            self.zoom -= 0.05
        if self.keys[pygame.K_e]:
            self.zoom += 0.05
        #mousewheel for zooming
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                print("Scroll")
                print(event.x, event.y)
                if event.y < 0:
                    self.zoom += 0.05
                elif event.y > 0:
                    self.zoom -= 0.05
            

    def update(self):
        self.interactions()
        world.draw(self.screen, self.world, self.zoom, self.cameraPosition, self.tileSize, self.screenSize)
        pygame.display.flip()

        #update
        
