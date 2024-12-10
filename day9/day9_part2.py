from util import readData
from day9_part1 import sumUpData, buildNum, swapNumData

def findBiggestChunk(numData:list, findChunk:str):
    indexStart = 0
    indexStop = 0
    foundStart = False
    for i in range(len(numData)):
        if(numData[i] == findChunk and not foundStart):
            indexStart = i
            foundStart = True
        if(numData[i] != findChunk and foundStart):
            indexStop = i
            break
        if(i == len(numData) - 1):
            indexStop = len(numData)
    return (indexStart, indexStop)

def getBiggestChunk(numData:list):
    biggest = 0
    for i in range(len(numData)):
        if(numData[i] == "."):
            continue
        elif(int(numData[i]) > biggest):
            biggest = int(numData[i])
    return biggest

def findDotAreaAtLeftOf(numData:list, leftIndex:int ,length:int):
    startIndex = -1
    currentLenght = 0
    for i in range(len(numData)):
        if(i == leftIndex):
            break
        if(numData[i] == "."):
            currentLenght += 1
            if(startIndex == -1):
                startIndex = i
            if(currentLenght == length):
                return (startIndex, i)
        else:
            currentLenght = 0
            startIndex = -1
    return None

def compressNumData(numData:list):
    biggestChunk = getBiggestChunk(numData)

    while(biggestChunk > 0):
        (indexStart, indexStop) = findBiggestChunk(numData, str(biggestChunk))
        dotData = findDotAreaAtLeftOf(numData,indexStart,indexStop - indexStart)
        if(dotData != None):
            (dotStartIndex, dotEndIndex) = dotData
            while(indexStart != indexStop +1 and dotStartIndex != dotEndIndex+1):
                numData = swapNumData(numData, indexStart, dotStartIndex)
                indexStart += 1
                dotStartIndex += 1
        biggestChunk -= 1

    return numData


if(__name__ == "__main__"):
    print(sumUpData(compressNumData(buildNum(readData()))))