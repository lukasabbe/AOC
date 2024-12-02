from util import readData
from day2_part1 import isSafe

def checkLine(line:list):
    if(isSafe(line)):
        return True
    else:
        for i in range(len(line)):
            copyOfList = line.copy()
            copyOfList.pop(i)
            if(isSafe(copyOfList)):
                return True
    return False

if __name__ == "__main__":
    #lines = ["7 6 4 2 1","1 2 7 8 9","9 7 6 2 1","1 3 2 4 5","8 6 4 4 1","1 3 6 7 9"]
    lines = readData()
        
    print(sum(1 for line in lines if checkLine(line.split(" "))))