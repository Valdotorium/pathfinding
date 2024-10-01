import pygame
import math
import random
def generateMatrix(worldsize):
    #generate a square matrix with size worldsize
    tiles = [[0]*worldsize for _ in range(worldsize)]
    #make some random tile the start
    tiles[random.randint(0,worldsize-1)][random.randint(0,worldsize-1)] = 2
    #make some random tiles the end
    tiles[random.randint(0,worldsize-1)][random.randint(0,worldsize-1)] = 3
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

            #empty
            if world["tiles"][x][y] == 0:
                pygame.draw.rect(screen, (255,255,255), (tileX, tileY, zoomedTileSize, zoomedTileSize), 5)

            #walls
            if world["tiles"][x][y] == 1:
                pygame.draw.rect(screen, (100,100,100), (tileX, tileY, zoomedTileSize, zoomedTileSize))

            #start
            if world["tiles"][x][y] == 2:
                pygame.draw.rect(screen, (0,0,255), (tileX, tileY, zoomedTileSize, zoomedTileSize), 5)

            #end
            if world["tiles"][x][y] == 3:
                pygame.draw.rect(screen, (0,255,0), (tileX, tileY, zoomedTileSize, zoomedTileSize), 5)
            #if x and y mathe selectedTile, fill the rect red
            if selectedTile == (x, y):
                pygame.draw.rect(screen, (255,0,0), (tileX, tileY, zoomedTileSize, zoomedTileSize), 5)





