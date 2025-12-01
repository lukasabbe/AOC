from util import readData, readTestData
from day8_part1 import printSky, outsideBounds, makeAntenaMap


def getAntenaAntiNodes(antenas, sky):
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

        counter = 1
        while True:
            isIn = False
            downRight = ((minAnten[0] + (maxAnten[0] - minAnten[0]) * counter), (minAnten[1] + (maxAnten[1] - minAnten[1]) * counter))
            downLeft = ((minAnten[0] - (maxAnten[0] - minAnten[0]) * counter), (minAnten[1] - (maxAnten[1] - minAnten[1])  * counter))
            upRight = ((maxAnten[0] + (minAnten[0] - maxAnten[0]) * counter), (maxAnten[1] + (minAnten[1] - maxAnten[1]) * counter))
            upLeft = ((maxAnten[0] - (minAnten[0] - maxAnten[0]) * counter), (maxAnten[1] - (minAnten[1] - maxAnten[1]) * counter))
            
            if(not outsideBounds(sky, upLeft[0], upLeft[1]) and upLeft != maxAnten):
                isIn = True
                antiNoides.append(upLeft)
            if(not outsideBounds(sky, upRight[0], upRight[1]) and upRight != maxAnten ):
                isIn = True
                antiNoides.append(upRight)
            if(not outsideBounds(sky, downRight[0], downRight[1]) and downRight != minAnten):
                isIn = True
                antiNoides.append(downRight)
            if(not outsideBounds(sky, downLeft[0], downLeft[1]) and downLeft != minAnten):
                isIn = True
                antiNoides.append(downLeft)
            if(not isIn):
                break
            counter += 1
    return antiNoides

def placeAntiNodes(sky):
    antenaMap = makeAntenaMap(sky)
    total = 0
    countedPostion = set()
    for antena in antenaMap:
        if(len(antenaMap[antena]) == 1):
            continue
        for (i,j) in getAntenaAntiNodes(antenaMap[antena],sky):
            if(sky[i][j] == "."):
                sky[i][j] = "#"
            if((i,j) not in countedPostion):
                total += 1
            countedPostion.add((i,j))
    printSky(sky)
    print(total)

if(__name__ == "__main__"):
    sky = readData()
    placeAntiNodes(sky)