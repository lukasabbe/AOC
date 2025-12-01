def readData():
    lines = []
    with open("./day4/day4_values.txt", "r") as file:
        for line in file:
            lines.append([char for char in line.strip()])
    return lines

def readTestData():
    lines = []
    with open("./day4/test_data.txt", "r") as file:
        for line in file:
            lines.append([char for char in line.strip()])
    return lines