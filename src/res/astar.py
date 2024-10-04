class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gCost = None
        self.hCost = None
        self.fCost = None
        self.parent = None  


def calculateHCost(startNode, endNode):
    coordinatesDifference = [abs(startNode.x - endNode.x), abs(startNode.y - endNode.y)]
    savedCoordinatesDifference = coordinatesDifference.copy()
    cost = 0

    while coordinatesDifference[0] >0 and coordinatesDifference[1]>0:
        coordinatesDifference[0] -= 1
        coordinatesDifference[1] -= 1
        cost += 14
    while coordinatesDifference[0] > 0:
        coordinatesDifference[0] -= 1
        cost += 10
    while coordinatesDifference[1] > 0:
        coordinatesDifference[1] -= 1
        cost += 10

    print(savedCoordinatesDifference, cost)

    startNode.hCost = cost

    return startNode, endNode
def astar(map):
    
    openList = []
    closedList = []

    #find the coordinates of the start tile in the world
    startX, startY = next((i, j) for i, row in enumerate(map["tiles"]) for j, cell in enumerate(row) if cell == 2)

    #find the coordinates of the end tile in the world
    endX, endY = next((i, j) for i, row in enumerate(map["tiles"]) for j, cell in enumerate(row) if cell == 3)

    #initialize start node with gCost = 0, hCost = distance between start and end
    #for going to a node vertically or horizontally, add 10 to g or h costs, for going diagonally, add 14

    startNode = Node(startX, startY)
    endNode = Node(endX, endY)
    startNode.gCost = 0
    endNode.hCost = 0
    startNode, endNode = calculateHCost(startNode, endNode)
    openList.append(startNode)



    
