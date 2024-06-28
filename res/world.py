import pygame
def generateMatrix(worldsize):
    #generate a square matrix with size worldsize
    tiles = [[0]*worldsize for _ in range(worldsize)]
    return {"size": worldsize, "tiles": tiles}

def createWorld(worldsize):
    world = generateMatrix(worldsize)
    
    return world
def draw(screen, world, zoom, cameraPos, tileSize, screenSize):
    #draw the matrix of tiles on the screen

    for x in range(world["size"]):
        for y in range(world["size"]):
            tileX = (x - cameraPos[0]) / zoom
            tileY = (y - cameraPos[1]) / zoom

            if tileX >= 0 and tileX < screenSize[0] and tileY >= 0 and tileY < screenSize[1]:
                tileColor = (255, 255, 255) if world["tiles"][x][y] == 0 else (0, 0, 0)
                pygame.draw.rect(screen, tileColor, (tileX * tileSize, tileY * tileSize, tileSize / zoom, tileSize / zoom), 3)


