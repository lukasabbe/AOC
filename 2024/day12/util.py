def readTestData():
    map = []
    with open("./day12/test_input.txt") as f:
        for line in f:
            map.append([i for i in line.strip()])
    return map