from util import readData, readTestData
from day5_part1 import isBefore, followRules

def swap(a, b, order):
    temp = order[a]
    order[a] = order[b]
    order[b] = temp
    return order

def remakeOrder(rules, order):
    for i in range(len(order)):
        for j in range(len(rules)):
            if(order[i] == rules[j][0] and rules[j][1] in order):
                if(not isBefore(rules[j][0], rules[j][1], order)):
                    order = swap(i, order.index(rules[j][1]), order)
            elif(order[i] == rules[j][1] and rules[j][0] in order):
                if(isBefore(rules[j][1], rules[j][0], order)):
                    order = swap(i, order.index(rules[j][0]), order)
    if(not followRules(rules, order)):
        order = remakeOrder(rules, order)
    return order

if(__name__ == "__main__"):
    rules, orders = readData()
    amount = 0
    for i in range(len(orders)):
        if(not followRules(rules, orders[i])):
            order = remakeOrder(rules, orders[i])
            amount += int(order[int((len(order)-1)/2)])

    print(amount)