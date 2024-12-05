def readData():
    rules = []
    order = []
    with open("./day5/day5_values.txt", "r") as file:
        flip = False
        for line in file:
            if(line == "\n"):
                flip = True
                continue
            if(not flip):
                rules.append(line.strip().split("|")) 
            else:
                order.append(line.strip().split(","))
    return rules, order

def readTestData():    
    rules = []
    order = []
    with open("./day5/test_data.txt", "r") as file:
        flip = False
        for line in file:
            if(line == "\n"):
                flip = True
                continue
            if(not flip):
                rules.append(line.strip().split("|")) 
            else:
                order.append(line.strip().split(","))
    return rules, order