def readData():
    leftList = []
    rightList = []
    with open("./day1/day1_values.txt", "r") as file:
        for line in file:
            lineSplit = line.split()
            leftList.append(int(lineSplit[0]))
            rightList.append(int(lineSplit[-1]))
    return leftList, rightList