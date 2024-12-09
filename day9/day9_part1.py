from util import readData

def buildNum(strDataNum:str):
    currentNum = 0
    num = []
    for i in range(len(strDataNum)):
        if(i % 2 == 0):
            for j in range(int(strDataNum[i])):
                num.append(str(currentNum))
            currentNum += 1
        else:
            for j in range(int(strDataNum[i])):
                num.append(".")
    return num

def swapNumData(numData:list, pos1:int, pos2:int):
    temp = numData[pos1]
    numData[pos1] = numData[pos2]
    numData[pos2] = temp
    return numData

def compressNumData(numData:list):
    counterFromLastNum = len(numData) - 1
    for i in range(len(numData)):
        if(i == counterFromLastNum):
            break
        if(numData[i] == "."):
            while(numData[counterFromLastNum] == "."):
                counterFromLastNum -= 1
            numData = swapNumData(numData, i, counterFromLastNum)
            counterFromLastNum -= 1
    return numData

def sumUpData(data:str):
    total = 0
    for i in range(len(data)):
        if(data[i] != "."):
            total += int(data[i]) * i
    return total

if(__name__ == "__main__"):
    print(sumUpData(compressNumData(buildNum(readData()))))