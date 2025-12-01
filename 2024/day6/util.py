def readData():
    with open("./day6/day6_values.txt", "r") as file:
        map = []
        for line in file:
            map.append([char for char in line.strip()])
        return map
def readTestData():
    with open("./day6/test_data.txt", "r") as file:
        map = []
        for line in file:
            map.append([char for char in line.strip()])
        return map