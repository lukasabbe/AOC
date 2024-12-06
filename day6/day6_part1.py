from util import readData , readTestData

def findPlayer(map):
    arrow = ["^", "V", "<", ">"]
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in arrow:
                return x, y

def turnRight(char):
    if(char == "^"):
        char = ">"
    elif(char == "V"):
        char = "<"
    elif(char == "<"):
        char = "^"
    elif(char == ">"):
        char = "V"
    return char

def runMapScript(map):
    x, y = findPlayer(map)
    vissitedSet = set()

    while True:
        copyX, copyY = x, y
        direction = map[y][x]
        if(direction == "^"):
            y -= 1
        elif(direction == "V"):
            y += 1
        elif(direction == "<"):
            x -= 1
        elif(direction == ">"):
            x += 1

        if(x < 0 or x >= len(map[0]) or y < 0 or y >= len(map)):
            vissitedSet.add((x, y))
            map[copyY][copyX] = "X"
            break

        if(map[y][x] == "#"):
            map[copyY][copyX] = turnRight(map[copyY][copyX])
            x, y = copyX, copyY
        else:
            map[copyY][copyX] = "X"
            map[y][x] = direction
        vissitedSet.add((x, y))
if __name__ == "__main__":
    map = readData()
    runMapScript(map)