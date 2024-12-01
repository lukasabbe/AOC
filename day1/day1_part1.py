def getTotal(leftList, rightList):
    leftList.sort()
    rightList.sort()
    total = 0
    for i in range(len(leftList)):
        total += abs(leftList[i] - rightList[i])
    return total

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

if __name__ == "__main__":
    leftList, rightList = readData()
    print(getTotal(leftList, rightList))
