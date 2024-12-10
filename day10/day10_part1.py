from util import readData, readTestData

def findAllStarts(map):
    startPoints = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if(map[i][j] == "0"):
                startPoints.append((i,j))
    return startPoints

def outsideBounds(map, i, j):
    return i < 0 or i >= len(map) or j < 0 or j >= len(map[0])

ninePoses = []
def findAmountOfPaths(map, startPoint, nextNum, useNinePoses = True):

    if(nextNum == 10 and map[startPoint[0]][startPoint[1]] == "9"):
        if(useNinePoses):
            ninePoses.append(startPoint)
        return 1

    total = 0
    
    if(not outsideBounds(map, startPoint[0] + 1, startPoint[1]) and map[startPoint[0] + 1][startPoint[1]] == str(nextNum) and (startPoint[0] + 1, startPoint[1]) not in ninePoses):
        total += findAmountOfPaths(map, (startPoint[0] + 1, startPoint[1]), nextNum + 1, useNinePoses)
    if(not outsideBounds(map, startPoint[0] - 1, startPoint[1]) and map[startPoint[0] - 1][startPoint[1]] == str(nextNum) and (startPoint[0] - 1, startPoint[1]) not in ninePoses):
        total +=findAmountOfPaths(map, (startPoint[0] - 1, startPoint[1]), nextNum + 1, useNinePoses)
    if(not outsideBounds(map, startPoint[0], startPoint[1] + 1) and map[startPoint[0]][startPoint[1] + 1] == str(nextNum) and (startPoint[0], startPoint[1] + 1) not in ninePoses):
        total += findAmountOfPaths(map, (startPoint[0], startPoint[1] + 1), nextNum + 1, useNinePoses)
    if(not outsideBounds(map, startPoint[0], startPoint[1] - 1) and map[startPoint[0]][startPoint[1] - 1] == str(nextNum) and (startPoint[0], startPoint[1] - 1) not in ninePoses):
        total += findAmountOfPaths(map, (startPoint[0], startPoint[1] - 1), nextNum + 1, useNinePoses)
    
    return total

def findTrail(map, useNinePoses = True):
    startPoints = findAllStarts(map)
    total = 0
    for startPoint in startPoints:
        total += findAmountOfPaths(map, startPoint, 1, useNinePoses)
        ninePoses.clear()
    return total

if(__name__ == "__main__"):
    print(findTrail(readData()))