from util import readData

def mulCalc(input):
    inputs = []
    correctChars =[",","(",")"]
    i = 0
    while(True):
        if(len(input)-1 == i):
            break
        if(input[i:i+4] == "mul("):
            start = i + 3
            end = 0
            for j in range(i+3,len(input)):
                if(input[j] not in correctChars and not input[j].isnumeric()):
                    end = -1
                    break
                if(input[j] == ")"):
                    end = j
                    break
            if(end == -1):
                i+=1
                continue
            num = findNum(input[start:end+1])
            if(num != None):
                inputs.append(num)
            input = input[:i] + input[end:]
        i+=1

    return sum(inputs)


def findNum(input):
    input = input.split(",")
    if(input[0][0] != "(" and input[1][-1] != ")"):
        return None
    
    for i in range(1,len(input[0])):
        if(not input[0][i].isnumeric()):
            return None

    for i in range(len(input[1])-1):
        if(not input[1][i].isnumeric()):
            return None

    return int(input[0][1:]) * int(input[1][:-1])
    
#print(mulCalc("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))

if(__name__ == "__main__"):

    data = readData()

    print(mulCalc(data))