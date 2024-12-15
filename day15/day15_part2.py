from util import readDataPart2
from day15_part1 import printMap, findRobot

def checkIfMoveable(house, instruction, x, y):
    deltaPos = {"v":(1,0),">":(0,1),"<":(0,-1),"^":(-1,0)}
    deltaX = deltaPos[instruction][1]
    deltaY = deltaPos[instruction][0]
    dir = "",0

    if(house[y + deltaY][x + deltaX] == "."):
        return True
    if(house[y + deltaY][x+deltaX] == "#"):
        return False

    if(house[y + deltaY][x] == "["):
        dir = "[]",1
    else:
        dir = "][",-1
    if(house[y + deltaY][x + deltaX] == dir[0][0]):
        isMovebale = checkIfMoveable(house, instruction, deltaX + x, deltaY + y)
        isMovebale2 = checkIfMoveable(house, instruction, deltaX + x + dir[1], deltaY + y)
        if(isMovebale and isMovebale2):
            return True
    return False
    

def move(house, instruction,x ,y, char = "@"):
    box = "[]"
    deltaPos = {"v":(1,0),">":(0,1),"<":(0,-1),"^":(-1,0)}
    deltaX = deltaPos[instruction][1]
    deltaY = deltaPos[instruction][0]

    if(house[y + deltaY][x + deltaX] == "."):
        house[y][x] = "."
        house[y + deltaY][x + deltaX] = char
        return house, (x + deltaX, y + deltaY)

    if(instruction == "v" or instruction == "^"):
        if(checkIfMoveable(house, instruction, x, y)):
            dir = "",0
            if(house[y + deltaY][x] == "["):
                dir = "[]",1
            else:
                dir = "][",-1
            if(house[y + deltaY][x + deltaX] == dir[0][0]):
                moveData = move(house, instruction, deltaX + x, deltaY + y, dir[0][0])
                moveData2 = move(moveData[0], instruction, deltaX + x + dir[1], deltaY + y, dir[0][1])
                if(moveData[1] != (x + deltaX, y + deltaY) and moveData2[1] != (x + deltaX + dir[1], y + deltaY)):
                    house = moveData2[0]
                    robotMove = move(house, instruction, x, y, char)
                    return robotMove
    elif(house[y + deltaY][x+deltaX] in box):
        data1 = move(house, instruction, x + deltaX, y + deltaY, house[y + deltaY][x+deltaX])
        house = data1[0]
        if(data1[1] != (x + deltaX, y + deltaY)):
            data = move(house, instruction, x, y, char)
            house = data[0]
            x = data[1][0]
            y = data[1][1]
    return house, (x,y)





if(__name__ == "__main__"):
    house, instructions = readDataPart2()
    y,x = findRobot(house)
    for instruction in instructions:
        data = move(house, instruction, x, y)
        house = data[0]
        x = data[1][0]
        y = data[1][1]
    total = 0
    for row in range(len(house)):
        for col in range(len(house[row])):
            if(house[row][col] == "["):
                total += 100 * row + col
    printMap(house)
    print(total)