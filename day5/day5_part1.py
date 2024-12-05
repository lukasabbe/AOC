from util import readData, readTestData

def isBefore(before, after, order):
    for i in range(len(order)):
        if(order[i] == before):
            return True
        elif(order[i] == after):
            return False
    return True

def followRules(rules, order):
    for i in range(len(order)):
        for j in range(len(rules)):
            if(order[i] == rules[j][0] and rules[j][1] in order):
                if(not isBefore(rules[j][0], rules[j][1], order)):
                    return False
            elif(order[i] == rules[j][1] and rules[j][0] in order):
                if(isBefore(rules[j][1], rules[j][0], order)):
                    return False
    return True

if(__name__ == "__main__"):
    rules, orders = readData()
    print(sum([ int(orders[i][int((len(orders[i])-1)/2)]) for i in range(len(orders)) if(followRules(rules, orders[i]))]))