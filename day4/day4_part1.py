from util import readData, readTestData

def findXmas(input :list):
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            sum += checkPos(j, i, input)
    return sum


def checkPos(x, y, input):
    sum = 0
    if(input[y][x] != "X"):
        return sum
    if(vaildPos(x+3, y, input) and input[y][x+1] == "M" and input[y][x+2] == "A" and input[y][x+3] == "S"): #right
        sum+=1
    if(vaildPos(x-3, y, input) and input[y][x-1] == "M" and input[y][x-2] == "A" and input[y][x-3] == "S"): #left
        sum+=1
    if(vaildPos(x, y+3, input) and input[y+1][x] == "M" and input[y+2][x] == "A" and input[y+3][x] == "S"): #down
        sum+=1
    if(vaildPos(x, y-3, input) and input[y-1][x] == "M" and input[y-2][x] == "A" and input[y-3][x] == "S"): #up
        sum+=1
    if(vaildPos(x+3, y+3, input) and input[y+1][x+1] == "M" and input[y+2][x+2] == "A" and input[y+3][x+3] == "S"): #down right
        sum+=1
    if(vaildPos(x-3, y-3, input) and input[y-1][x-1] == "M" and input[y-2][x-2] == "A" and input[y-3][x-3] == "S"): #up left
        sum+=1
    if(vaildPos(x+3, y-3, input) and input[y-1][x+1] == "M" and input[y-2][x+2] == "A" and input[y-3][x+3] == "S"): #up right
        sum+=1
    if(vaildPos(x-3, y+3, input) and input[y+1][x-1] == "M" and input[y+2][x-2] == "A" and input[y+3][x-3] == "S"): #down left
        sum+=1
    return sum
    
def vaildPos(x, y, input):
    if(x < 0 or y < 0 or x >= len(input[0]) or y >= len(input)):
        return False
    return True

if(__name__ == "__main__"):
    data = readData()
    print(findXmas(data))