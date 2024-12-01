def readData():
    leftList = []
    rightList = []
    with open("./day1/day1_values.txt", "r") as file:
        for line in file:
            left = line.split()[0]
            right = line.split()[-1]
            leftList.append(int(left))
            rightList.append(int(right))
    return leftList, rightList