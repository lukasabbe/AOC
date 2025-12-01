from util import readData, readTestData


def makeAntenaMap(sky):
    antenaMap = {}
    for i in range(len(sky)):
        for j in range(len(sky[i])):
            if(sky[i][j] == "." or sky[i][j] == "#"):
                continue
            if(sky[i][j] not in antenaMap):
                antenaMap[sky[i][j]] = [(i,j)]
            else:
                antenaMap[sky[i][j]].append((i,j))
    return antenaMap


def getAntenaAntiNodes(antenas):
    antiNoides = []
    par = set()
    for antena in antenas:
        for antena2 in antenas:
            if(antena == antena2):
                continue
            if((antena, antena2) in par or (antena2, antena) in par):
                continue
            par.add((antena, antena2))
    for (a, b) in par:
        minAnten = min(a, b)
        maxAnten = max(a, b)
        antiNoides.extend(
            [
                (minAnten[0] + (maxAnten[0] - minAnten[0]), minAnten[1] + (maxAnten[1] - minAnten[1])),
                (minAnten[0] - (maxAnten[0] - minAnten[0]), minAnten[1] - (maxAnten[1] - minAnten[1])),
                (maxAnten[0] + (minAnten[0] - maxAnten[0]), maxAnten[1] + (minAnten[1] - maxAnten[1])),
                (maxAnten[0] - (minAnten[0] - maxAnten[0]), maxAnten[1] - (minAnten[1] - maxAnten[1]))
            ]
        )
        if(minAnten in antiNoides):
            antiNoides.remove(minAnten)
        if(maxAnten in antiNoides):
            antiNoides.remove(maxAnten)
    return antiNoides

def printSky(sky):
    for i in range(len(sky)):
        print("".join(sky[i]))

def outsideBounds(sky, i, j):
    return i < 0 or i >= len(sky) or j < 0 or j >= len(sky[0])

def placeAntiNodes(sky):
    antenaMap = makeAntenaMap(sky)
    total = 0
    countedPostion = set()
    for antena in antenaMap:
        if(len(antenaMap[antena]) == 1):
            continue
        for (i,j) in getAntenaAntiNodes(antenaMap[antena]):
            if(not outsideBounds(sky, i, j) and sky[i][j] == "." and (i,j) not in countedPostion):
                total += 1
                sky[i][j] = "#"
            elif not outsideBounds(sky, i, j) and sky[i][j] != "#" and (i,j) not in countedPostion:
                total += 1
            countedPostion.add((i,j))
    printSky(sky)
    print(total)

if(__name__ == "__main__"):
    sky = readData()
    placeAntiNodes(sky)