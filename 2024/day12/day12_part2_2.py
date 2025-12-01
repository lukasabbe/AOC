from util import readTestData
from day12_part1 import outOfBounds, printMap, serchArea

def findArea(map):
    area = {}
    perimitor = {}
    for row in range(len(map)):
        for cell in range(len(map[row])):
            value = map[row][cell]
            setArea = serchArea(map, row, cell, value)
            visited = set()
            add = True
            for k,v in area.items():
                if(v == setArea):
                    add = False
                    break
            if add and len(setArea) > 0:
                if(area.get(value) == None):
                    area[value] = setArea
                else:
                    i = 0
                    while(area.get(value+str(i)) != None):
                        i+=1
                    area[value+str(i)] = setArea
    for k,v in area.items():
        perim = []
        for pos in v:
            if((pos[0] + 1, pos[1]) not in v):
                perim.append((pos[0], pos[1]))
            elif((pos[0] - 1, pos[1]) not in v):
                perim.append((pos[0], pos[1]))
            elif((pos[0], pos[1] + 1) not in v):
                perim.append((pos[0], pos[1]))
            elif((pos[0], pos[1] - 1) not in v):
                perim.append((pos[0], pos[1]))
        perimitor[k] = set(perim)
    return area, perimitor


def findLine(edgeSet, edgePos, char, direction) -> list:
    if((edgePos[0],edgePos[1]) not in edgeSet):
        return [], 1
    if(direction == "both"):
        right, num = findLine(edgeSet, (edgePos[0]+1, edgePos[1]), char, "right")
        left, num = findLine(edgeSet, (edgePos[0]-1, edgePos[1]), char, "left")
        down, num = findLine(edgeSet, (edgePos[0], edgePos[1]+1), char, "down")
        up, num = findLine(edgeSet, (edgePos[0], edgePos[1]-1), char, "up")
        if(len(right) + len(left) > len(down) + len(up)):
            right.extend(left)
            right.append((edgePos[0], edgePos[1]))
            if(edgeSet[(edgePos[0], edgePos[1])] == 2):
                return right, 2
            else:
                return right,num 
        else:
            down.extend(up)
            down.append((edgePos[0], edgePos[1]))
            if(edgeSet[(edgePos[0], edgePos[1])] == 2):
                return down, 2
            else:
                return down,num 
            
    if(direction == "right"):
        lines, num= findLine(edgeSet, (edgePos[0]+1, edgePos[1]), char, "right")
        lines.append((edgePos[0], edgePos[1]))
        if(edgeSet[(edgePos[0], edgePos[1])] == 2):
            return lines, 2
        else:
            return lines,num 
    if(direction == "left"):
        lines, num = findLine(edgeSet, (edgePos[0]-1, edgePos[1]), char, "left")
        lines.append((edgePos[0], edgePos[1]))
        if(edgeSet[(edgePos[0], edgePos[1])] == 2):
            return lines, 2
        else:
            return lines,num 
    if(direction == "down"):
        lines, num = findLine(edgeSet, (edgePos[0], edgePos[1]+1), char, "down")
        lines.append((edgePos[0], edgePos[1]))
        if(edgeSet[(edgePos[0], edgePos[1])] == 2):
            return lines, 2
        else:
            return lines,num 
    if(direction == "up"):
        lines, num = findLine(edgeSet, (edgePos[0], edgePos[1]-1), char, "up")
        lines.append((edgePos[0], edgePos[1]))
        if(edgeSet[(edgePos[0], edgePos[1])] == 2):
            return lines, 2
        else:
            return lines,num 
    

def countEdges(map, edgeSet, char):
    lines = []
    printPrem(edgeSet)
    for edgePos in edgeSet:
        line, num = findLine(edgeSet, edgePos, char, "both")
        line.sort() 
        if(line not in lines):
            for i in range(num):
                lines.append(line)
    return len(lines)


def insideBounds(area, pos, char):
    return pos in area[char]

def printPrem(preSet):
    for i in range(-10, 10):
        for j in range(-10, 10):
            if((i,j) in preSet):
                print("#", end="")
            else:
                print(" ", end="")
        print()

def pointsAround(edge,area):
    pointsAround = {}
    for k,v in edge.items():
        amountDict = {}
        for(i,j) in v:
            if(not insideBounds(area,(i+1, j), k)):
                if((i+1, j) in amountDict):
                    amountDict[(i+1, j)] += 1
                else:
                    amountDict[(i+1, j)] = 1
            if(not insideBounds(area,(i-1, j), k)):
                if((i-1, j) in amountDict):
                    amountDict[(i-1, j)] += 1
                else:
                    amountDict[(i-1, j)] = 1
            if(not insideBounds(area,(i, j+1), k)):
                if((i, j+1) in amountDict):
                    amountDict[(i, j+1)] += 1
                else:
                    amountDict[(i, j+1)] = 1
            if(not insideBounds(area,(i, j-1), k)):
                if((i, j-1) in amountDict):
                    amountDict[(i, j-1)] += 1
                else:
                    amountDict[(i, j-1)] = 1
        pointsAround[k] = amountDict
    return pointsAround

if(__name__ == "__main__"):
    map = readTestData()
    area, pre = findArea(map)
    total = 0
    pre = pointsAround(pre, area)
    for k,v in pre.items():
        print(countEdges(map, v, k), k)
    