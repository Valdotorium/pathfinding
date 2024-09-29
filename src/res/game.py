import pygame
import res.world as world
class Game():
    def __init__(self, screen, screenSize):
        #world data
        self.worldSize = 10
        #generate world data from world.py module
        self.world = world.createWorld(self.worldSize)

        #visuals
        self.tileSize = 50
        self.zoom = 1.0
        self.cameraPosition = [(self.worldSize / 2) * self.zoom , (self.worldSize / 2) * self.zoom]
        self.screen = screen
        self.screenSize = screenSize

        #options from options.json file

        #interaction
        self.mousePos = pygame.mouse.get_pos()
        self.clickPos = pygame.mouse.get_pressed()[0]
        self.keys = pygame.key.get_pressed()
        self.clickedTicks = 0
        self.isClicked = False
        self.selectedTile = [0,0]

    def clickTile(self):
        if -1 < self.selectedTile[0] < self.world["size"] and -1 < self.selectedTile[1] < self.world["size"]:
            #check if value of selectedtile in world is 0
            if self.world["tiles"][self.selectedTile[0]][self.selectedTile[1]] == 0:
                #change to wall
                self.world["tiles"][self.selectedTile[0]][self.selectedTile[1]] = 1
            else:
                #change to air
                self.world["tiles"][self.selectedTile[0]][self.selectedTile[1]] = 0

    def interactions(self):
        #update mouse click state and position and detect key presses

        #stored for dragging
        prevMousePos = self.mousePos
        self.mousePos = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()
        wasClicked = self.isClicked

        if self.clickedTicks > 2:
            #difference between prevmousepos and mousepos
            diff = [self.mousePos[0] - prevMousePos[0], self.mousePos[1] - prevMousePos[1]]
            
            self.cameraPosition = [self.cameraPosition[0] - diff[0] / self.tileSize / self.zoom, self.cameraPosition[1] - diff[1] / self.tileSize / self.zoom]
        #interaction subfunctions

        self.isClicked = pygame.mouse.get_pressed()[0]
        if self.isClicked and not wasClicked:
            self.clickPos = pygame.mouse.get_pos()
            self.clickTile()
        
        if self.isClicked:
            self.clickedTicks += 1
        else:
            self.clickedTicks = 0

        
        #using WASD to move camera position
        if self.keys[pygame.K_w]:
            self.cameraPosition[1] -= .1
        if self.keys[pygame.K_s]:
            self.cameraPosition[1] += .1
        if self.keys[pygame.K_a]:
            self.cameraPosition[0] -= .1
        if self.keys[pygame.K_d]:
            self.cameraPosition[0] += .1

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
        world.draw(self)
        pygame.display.flip()

        #update
        
