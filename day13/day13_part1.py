from util import readTestData
from functools import cache
from sympy import symbols, Eq, solve, Integer

@cache
def findPriceSum(x, xInc, x2, x2Inc, sum):
    if(x > sum):
        return None
    elif(x2 > sum):
        return None
    elif x == sum:
        return [0,0]
    elif x2 == sum:
        return [0,0]
    
    total = findPriceSum(x + xInc, xInc, x2 + x2Inc, x2Inc, sum)
    if(total != None):
        return total[0] + 1, total[1]
    total2 = findPriceSum(x + x2Inc, xInc, x2 + xInc, x2Inc, sum)
    if(total2 != None):
        return total2[0], total2[1] + 1
    return None

def calc(xInc,xInc2,yInc,yInc2,sum,sum2):
    x,y = symbols('x y')
    eq1 = Eq(xInc*x + y*xInc2, sum)
    eq2 = Eq(x*yInc + y*yInc2, sum2)
    return solve((eq1,eq2), (x,y))

if __name__ == "__main__":

    data = readTestData()
    prices = []
    prices_part2 = []
    current = -1
    for i in data:
        if(len(i) == 0):
            continue
        if(i[0] == "B"):
            plutSplit = i.split("+")
            if(current == -1):
                prices.append((plutSplit[1].split(",")[0], plutSplit[2].strip()))
                prices_part2.append((plutSplit[1].split(",")[0], plutSplit[2].strip()))
                current = 1
            else:
                prices[len(prices)-1] = (prices[len(prices)-1][0], prices[len(prices)-1][1], plutSplit[1].split(",")[0], plutSplit[2].strip())
                prices_part2[len(prices_part2)-1] = (prices_part2[len(prices_part2)-1][0], prices_part2[len(prices_part2)-1][1], plutSplit[1].split(",")[0], plutSplit[2].strip())
                current = -1
        else:
            equSplit = i.split("=")
            prices[len(prices)-1] = (prices[len(prices)-1][0], prices[len(prices)-1][1], prices[len(prices)-1][2], prices[len(prices)-1][3], equSplit[1].split(",")[0], equSplit[2].strip())
            prices_part2[len(prices_part2)-1] = (prices_part2[len(prices_part2)-1][0], prices_part2[len(prices_part2)-1][1], prices_part2[len(prices_part2)-1][2], prices_part2[len(prices_part2)-1][3], str(int(equSplit[1].split(",")[0]) + 10000000000000), str(int(equSplit[2].strip()) + 10000000000000))

    tokens = 0
    for i in prices:
        values = calc(int(i[0]), int(i[2]), int(i[1]), int(i[3]), int(i[4]), int(i[5]))
        valuesList = [values[x] for x in values]
        if(not isinstance(valuesList[0], Integer) or not isinstance(valuesList[1], Integer)):
            continue
        tokens += valuesList[0] *3 + valuesList[1]

    print("Part 2")
    tokens_part2 = 0
    for i in prices_part2:
        values = calc(int(i[0]), int(i[2]), int(i[1]), int(i[3]), int(i[4]), int(i[5]))
        valuesList = [values[x] for x in values]
        if(not isinstance(valuesList[0], Integer) or not isinstance(valuesList[1], Integer)):
            continue
        tokens_part2 += valuesList[0] *3 + valuesList[1]

    print(tokens)
    print(tokens_part2)