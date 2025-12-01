from util import readTestData
from day12_part1 import findArea, outOfBounds

def getSidesPoses(map, char, area):
    char = char[0]
    poses = set()
    for pos in area:
        x = pos[0]
        y = pos[1]
        leftUpCornar = 0
        leftDownCornar = 0
        rightUpCornar = 0
        rightDownCornar = 0
        if ((not outOfBounds(map, (x-1, y)) and map[x-1][y] != char) or outOfBounds(map, (x-1,y)) and (x-1,y) not in poses):
            leftUpCornar += 1
            leftDownCornar += 1
            poses.add((x-1,y))
        if ((not outOfBounds(map, (x+1, y)) and map[x+1][y] != char) or outOfBounds(map, (x+1, y)) and (x+1,y) not in poses):
            rightUpCornar += 1
            rightDownCornar += 1
            poses.add((x+1,y))
        if ((not outOfBounds(map, (x, y-1)) and map[x][y-1] != char) or outOfBounds(map, (x, y-1)) and (x,y-1) not in poses):
            leftDownCornar +=1
            rightDownCornar += 1
            poses.add((x,y-1))
        if ((not outOfBounds(map, (x, y+1)) and map[x][y+1] != char) or outOfBounds(map, (x,y+1))) and (x,y+1) not in poses:
            leftUpCornar += 1
            rightUpCornar += 1
            poses.add((x,y+1))
        if ((not outOfBounds(map, (x-1, y-1)) and map[x-1][y-1] != char) or outOfBounds(map, (x-1,y-1)) and (x-1,y-1) not in poses and leftDownCornar == 2):
            poses.add((x-1,y-1))
        if ((not outOfBounds(map, (x+1, y-1)) and map[x+1][y-1] != char) or outOfBounds(map, (x+1, y-1)) and (x+1,y-1) not in poses and rightDownCornar == 2):
            poses.add((x+1,y-1))
        if ((not outOfBounds(map, (x-1, y+1)) and map[x-1][y+1] != char) or outOfBounds(map, (x-1, y+1)) and (x-1,y+1) not in poses and leftUpCornar == 2):
            poses.add((x-1,y+1))
        if ((not outOfBounds(map, (x+1, y+1)) and map[x+1][y+1] != char) or outOfBounds(map, (x+1,y+1))) and (x+1,y+1) not in poses and rightUpCornar == 2:
            poses.add((x+1,y+1))
    return poses

def goRight(poses, x, y):
    while((x, y) in poses):
        x += 1
        if((x, y) == poses[0] and (x+1,y) in poses):
            return (x,y), True
    return (x-1,y), False
def goLeft(poses, x, y):
    while((x, y) in poses):
        x -= 1
        if((x, y) == poses[0] and (x-1,y) in poses):
            return (x,y), True
    return (x+1,y), False
def goUp(poses, x, y):
    while((x, y) in poses):
        y -= 1
        if((x, y) == poses[0] and (x,y-1) in poses):
            return (x,y), True
    return (x,y+1), False
def goDown(poses, x, y):
    while((x, y) in poses):
        y += 1
        if((x, y) == poses[0] and (x,y+1) in poses):
            return (x,y), True
    return (x,y-1), False

def countSides(map, char, area):
    poses = list(getSidesPoses(map, char, area))
    currentPos = poses[0]
    counter = 0
    axis = True
    while(True):
        #print(currentPos)
        if(axis):
            leftPos, remove = goLeft(poses, currentPos[0], currentPos[1])
            rightPos, remove2 = goRight(poses, currentPos[0], currentPos[1])
            if(remove):
                currentPos = leftPos
            elif(remove2):
                currentPos = rightPos
            elif(leftPos != currentPos):
                currentPos = leftPos
                counter += 1
            elif(rightPos != currentPos):
                currentPos = rightPos
                counter += 1
            else:
                axis = not axis
                continue
        else:
            downPos, remove = goDown(poses, currentPos[0], currentPos[1])
            upPos, remove2 = goUp(poses, currentPos[0], currentPos[1])
            if(remove):
                currentPos = downPos
            elif(remove2):
                currentPos = upPos
            elif(downPos != currentPos):
                currentPos = downPos
                counter += 1
            elif(upPos != currentPos):
                currentPos = upPos
                counter += 1
            else:
                axis = not axis
                continue
        axis = not axis
        if(currentPos == poses[0]):
            break
    return counter



def printAround(poses, map, char):
    print(poses)
    for i in range(-10,10):
        for j in range(-10,10):
            if((i,j) in poses):
                print("X", end="")
            #elif(map[i][j] == char):
            #    print(".", end="")
            else:
                print(" ", end="")
        print()

if(__name__ == "__main__"):
    map = readTestData()
    area = findArea(map)
    total = 0
    for char in area:
        print(len(area[char]),countSides(map, char, area[char]), char)
        printAround(getSidesPoses(map, char, area[char]), map, char)
        total += countSides(map, char, area[char]) * len(area[char])
    print(total)