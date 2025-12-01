def readData():
    with open("day16/input.txt") as f:
        map = []
        for line in f:
            map.append([char for char in line.strip()])
    return map