from util import readData

def getTotal(leftList, rightList):
    leftList.sort()
    rightList.sort()
    return sum([abs(leftList[i] - rightList[i]) for i in range(len(leftList))])

if __name__ == "__main__":
    leftList, rightList = readData()
    print(getTotal(leftList, rightList))
