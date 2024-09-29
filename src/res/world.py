import pygame
import math
def generateMatrix(worldsize):
    #generate a square matrix with size worldsize
    tiles = [[0]*worldsize for _ in range(worldsize)]
    return {"size": worldsize, "tiles": tiles}

def createWorld(worldsize):
    world = generateMatrix(worldsize)
    
    return world


def draw(obj):
    world = obj.world
    tileSize = obj.tileSize
    screen = obj.screen
    cameraPos = obj.cameraPosition
    zoom = obj.zoom

    #finding coordinates of the curent hovered tile
    zoomedTileSize = tileSize / zoom 
    mx, my = pygame.mouse.get_pos()
    #add camerapos to mx my
    mx += cameraPos[0] * zoomedTileSize
    my += cameraPos[1] * zoomedTileSize
    selectedTile = (math.floor(mx / zoomedTileSize), math.floor(my / zoomedTileSize))
    obj.selectedTile = selectedTile
    #draw the matrix of tiles on the screen

    for x in range(world["size"]):
        for y in range(world["size"]):
            tileX = (x - cameraPos[0]) * zoomedTileSize
            tileY = (y - cameraPos[1]) * zoomedTileSize
            if world["tiles"][x][y] == 0:
                pygame.draw.rect(screen, (255,255,255), (tileX, tileY, zoomedTileSize, zoomedTileSize), 5)
            if world["tiles"][x][y] == 1:
                pygame.draw.rect(screen, (100,100,100), (tileX, tileY, zoomedTileSize, zoomedTileSize))
            #if x and y mathe selectedTile, fill the rect red
            if selectedTile == (x, y):
                pygame.draw.rect(screen, (255,0,0), (tileX, tileY, zoomedTileSize, zoomedTileSize), 5)





