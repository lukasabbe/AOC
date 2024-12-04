from util import readData, readTestData
from day4_part1 import vaildPos

def findXmas(input :list):
    sum = 0
    bigXDir = {}
    for i in range(len(input)):
        for j in range(len(input[i])):
            bigXDir = checkPos(j, i, input, bigXDir)
    for key in bigXDir:
        if(bigXDir[key] > 1):
            sum+=1
    return sum


def checkPos(x, y, input, xPoses):
    if(vaildPos(x+2, y+2, input) and input[y][x] == "M" and input[y+1][x+1] == "A" and input[y+2][x+2] == "S"): #down right
        xPoses[(y+1, x+1)] = xPoses[(y+1, x+1)] + 1 if (y+1, x+1) in xPoses else 1
    if(vaildPos(x-2, y-2, input) and input[y][x] == "M" and input[y-1][x-1] == "A" and input[y-2][x-2] == "S"): #up left
        xPoses[(y-1, x-1)] = xPoses[(y-1, x-1)] + 1 if (y-1, x-1) in xPoses else 1
    if(vaildPos(x+2, y-2, input) and input[y][x] == "M" and input[y-1][x+1] == "A" and input[y-2][x+2] == "S"): #up right
        xPoses[(y-1, x+1)] = xPoses[(y-1, x+1)] + 1 if (y-1, x+1) in xPoses else 1
    if(vaildPos(x-2, y+2, input) and input[y][x] == "M" and input[y+1][x-1] == "A" and input[y+2][x-2] == "S"): #down left
        xPoses[(y+1, x-1)] = xPoses[(y+1, x-1)] + 1 if (y+1, x-1) in xPoses else 1
    return xPoses

if(__name__ == "__main__"):
    data = readData()
    print(findXmas(data))