def findMinPair(leftList, rightList):
    leftMinValue = min(leftList)
    rightMinValue = min(rightList)
    return abs(leftMinValue - rightMinValue), leftMinValue, rightMinValue

def getTotal(leftList, rightList):
    total = 0
    for i in range(len(leftList)):
        pair = findMinPair(leftList, rightList)
        total += pair[0]
        leftList.remove(pair[1])
        rightList.remove(pair[2])
    return total

def readData():
    leftList = []
    rightList = []
    with open("day1_values.txt", "r") as file:
        for line in file:
            left = line.split()[0]
            right = line.split()[-1]
            leftList.append(int(left))
            rightList.append(int(right))
    return leftList, rightList

if __name__ == "__main__":
    leftList, rightList = readData()
    print(getTotal(leftList, rightList))
