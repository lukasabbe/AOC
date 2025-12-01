from util import readData

def move(house, instruction,x ,y, char = "@"):
    deltaPos = {"v":(1,0),">":(0,1),"<":(0,-1),"^":(-1,0)}
    deltaX = deltaPos[instruction][1]
    deltaY = deltaPos[instruction][0]
    moved = False
    if(house[y + deltaY][x + deltaX] == "."):
        house[y][x] = "."
        house[y + deltaY][x + deltaX] = char
        moved = True
    elif(house[y + deltaY][x+deltaX] == "O"):
        data1 = move(house, instruction, x + deltaX, y + deltaY, "O")
        house = data1[0]
        if(data1[1] != (x + deltaX, y + deltaY)):
            data = move(house, instruction, x, y, char)
            house = data[0]
            x = data[1][0]
            y = data[1][1]
    
    if(moved):
        return house, (x + deltaX, y + deltaY)
    else:
        return house, (x,y)

def findRobot(house):
    for i in range(len(house)):
        for j in range(len(house[i])):
            if(house[i][j] == "@"):
                return (i,j)
            
def printMap(house):
    for row in house:
        print("".join(row))

if(__name__ == "__main__"):
    house, instructions = readData()
    x,y = findRobot(house)
    for instruction in instructions:
        data = move(house, instruction, x, y)
        house = data[0]
        x = data[1][0]
        y = data[1][1]
    printMap(house)

    total = 0
    for row in range(len(house)):
        for col in range(len(house[row])):
            if(house[row][col] == "O"):
                total += 100 * row + col
    print(total)
    

