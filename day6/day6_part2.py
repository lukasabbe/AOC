from util import readData , readTestData
from day6_part1 import findPlayer, turnRight
import copy

def runMapScript(map, loopX, loopY):
    x, y = findPlayer(map)
    vissitedSet = set()
    isLooping = False
    loopCounter = 0
    loopDict = {}
    vissitedSet.add((x, y))

    while True:
        copyX, copyY = x, y
        direction = map[y][x]

        if((x, y) not in loopDict):
            loopDict[(x, y)] = 1
        else:
            loopDict[(x, y)] += 1
        
        if(loopDict[(x, y)] > 10):
            isLooping = True
            break

        if(direction == "^"):
            y -= 1
        elif(direction == "V"):
            y += 1
        elif(direction == "<"):
            x -= 1
        elif(direction == ">"):
            x += 1

        if(x < 0 or x >= len(map[0]) or y < 0 or y >= len(map) or loopCounter > 10):
            vissitedSet.add((x, y))
            if(loopCounter > 10):
                isLooping = True
            break

        if(map[y][x] == "#" or map[y][x] == "O"):
            if(x == loopX and y == loopY):
                loopCounter += 1
            map[copyY][copyX] = turnRight(map[copyY][copyX])
            x, y = copyX, copyY
        else:
            map[y][x] = direction
            map[copyY][copyX] = "."
        vissitedSet.add((x, y))
    return vissitedSet, isLooping

def checkWithObstical(map, x, y):
    map = copy.deepcopy(map)
    arrow = ["^", "V", "<", ">"]
    if(map[y][x] not in arrow):
        map[y][x] = "O"
    visitedPlaces, isLooping = runMapScript(map, x, y)
    if(isLooping):
        return True
    else:
        return False

def checkBounds(map, x, y):
    if(x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)):
        return True
    return False

def printMap(map):
    for row in map:
        print("".join(row))

if __name__ == "__main__":
    map = readData()
    visitedPlaces, isLooping = runMapScript(copy.deepcopy(map), -1, -1)
    obstiaclSet = set()
    obsticals = 0
    for place in visitedPlaces:
        obsticalX = place[0] + 1
        obsticalY = place[1]
        if((obsticalX, obsticalY) not in obstiaclSet):
            obstiaclSet.add((obsticalX, obsticalY))
            if(not checkBounds(map,obsticalX, obsticalY) and checkWithObstical(map, obsticalX, obsticalY)):
                obsticals += 1
        obsticalX = place[0] - 1
        obsticalY = place[1]
        if((obsticalX, obsticalY) not in obstiaclSet):
            obstiaclSet.add((obsticalX, obsticalY))
            if(not checkBounds(map,obsticalX, obsticalY) and checkWithObstical(map, obsticalX, obsticalY)):
                obsticals += 1
        obsticalX = place[0]
        obsticalY = place[1] + 1
        if((obsticalX, obsticalY) not in obstiaclSet):
            obstiaclSet.add((obsticalX, obsticalY))
            if(not checkBounds(map,obsticalX, obsticalY) and checkWithObstical(map, obsticalX, obsticalY)):
                obsticals += 1
        obsticalX = place[0]
        obsticalY = place[1] - 1
        if((obsticalX, obsticalY) not in obstiaclSet):
            obstiaclSet.add((obsticalX, obsticalY))
            if(not checkBounds(map,obsticalX, obsticalY) and checkWithObstical(map, obsticalX, obsticalY)):
                obsticals += 1
    print(obsticals)