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

def findAmountOf(num, rightlist):
    amount = 0
    for i in range(len(rightlist)):
        if rightlist[i] == num:
            amount += 1
    return amount


def getTotal(leftList, rightList):
    total = 0
    for i in range(len(leftList)):
        amount = findAmountOf(leftList[i], rightList)
        total += amount * leftList[i]
    return total


if __name__ == "__main__":
    leftList, rightList = readData()
    print(getTotal(leftList, rightList))