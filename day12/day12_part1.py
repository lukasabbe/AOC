from util import readTestData

visited = set()

def serchArea(map, x , y, char):
    if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]) or map[x][y] != char:
        return set()
    if((x,y) in visited):
        return set()
    visited.add((x,y))
    result = set({(x,y)})
    result.update(serchArea(map, x-1, y, char))
    result.update(serchArea(map, x+1, y, char))
    result.update(serchArea(map, x, y-1, char))
    result.update(serchArea(map, x, y+1, char))
    return result

def findArea(map):
    area = {}
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
    return area

def printMap(map, char = None):
    if(None == char):
        for row in map:
            print("".join(row))
        return
    for row in map:
        print("".join(row).replace(char, "*"))

def outOfBounds(map, pos):
    return pos[0] < 0 or pos[0] >= len(map) or pos[1] < 0 or pos[1] >= len(map[0])

def getfenceAmount(map, area, char):
    char = char[0]
    totalFence = 0
    for pos in area:
        x = pos[0]
        y = pos[1]
        if ((not outOfBounds(map, (x-1, y)) and map[x-1][y] != char) or outOfBounds(map, (x-1,y))):
            totalFence += 1
        if ((not outOfBounds(map, (x+1, y)) and map[x+1][y] != char) or outOfBounds(map, (x+1, y))):
            totalFence += 1
        if ((not outOfBounds(map, (x, y-1)) and map[x][y-1] != char) or outOfBounds(map, (x, y-1))):
            totalFence += 1
        if ((not outOfBounds(map, (x, y+1)) and map[x][y+1] != char) or outOfBounds(map, (x,y+1))):
            totalFence += 1
    return totalFence

if __name__ == "__main__":
    map = readTestData()
    area = findArea(map)
    total = 0
    for char in area:
        total += getfenceAmount(map, area[char], char) * len(area[char])
    print(total)