from util import readData

def findAmountOf(num, rightlist):
    return sum(1 for x in rightlist if x == num)

def getTotal(leftList, rightList):
    return sum([findAmountOf(num, rightList) * num for num in leftList])

if __name__ == "__main__":
    leftList, rightList = readData()
    print(getTotal(leftList, rightList))