from day3_part1 import findNum
from util import readData

def mulCalc(input):
    inputs = []
    i = 0

    doNext = True

    while(True):
        if(len(input)-1 == i):
            break
        if(input[i:i+4] == "do()"):
            doNext = True
        elif(input[i:i+7] == "don't()"):
            doNext = False

        if(input[i] == "m" and input[i+1] == "u" and input[i+2] == "l" and input[i+3] == "("):
            start = i + 3
            end = 0
            for j in range(i+3,len(input)):
                if(input[j] != ")" and input[j] != "(" and input[j] != "," and not input[j].isnumeric()):
                    end = -1
                    break
                if(input[j] == ")"):
                    end = j
                    break
            if(end == -1):
                i+=1
                continue
            num = findNum(input[start:end+1])
            if(num != None and doNext):
                inputs.append(num)
            input = input[:i] + input[end:]
        i+=1

    return sum(inputs)

if(__name__ == "__main__"):
    data = readData()
    print(mulCalc(data))