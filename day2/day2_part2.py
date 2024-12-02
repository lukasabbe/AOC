from util import readData


def isSafe(splitLine:list):
    safeCount = True
    incrising = False
    decrising = False
    for i in range(len(splitLine)):
        if(len(splitLine) - 1 != i):
            if(abs(int(splitLine[i]) - int(splitLine[i+1])) > 3):
                safeCount = False
            if(int(splitLine[i]) - int(splitLine[i+1]) < 0):
                decrising = True
            elif(int(splitLine[i]) - int(splitLine[i+1]) == 0):
                safeCount = False
            else:
                incrising = True
    if(incrising and decrising):
        safeCount = False
    if(not incrising and not decrising):
        safeCount = False
    if safeCount:
        print(splitLine)
    return safeCount

if __name__ == "__main__":
    #lines = ["7 6 4 2 1","1 2 7 8 9","9 7 6 2 1","1 3 2 4 5","8 6 4 4 1","1 3 6 7 9"]
    lines = readData()

    safeList = []
    for line in lines:
        line = line.split(" ")
        if(isSafe(line)):
            safeList.append(1)
        else:
            for i in range(len(line)):
                copyOfList = line.copy()
                copyOfList.pop(i)
                if(isSafe(copyOfList)):
                    safeList.append(1)
                    break
        
    print(sum(1 for line in safeList))