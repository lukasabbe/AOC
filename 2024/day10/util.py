def readData():
    with open("./day10/day10_value.txt","r") as file:
        data = []
        for line in file:
            data.append([i for i in line.strip()])
    return data



def readTestData():
    with open("./day10/test_data.txt","r") as file:
        data = []
        for line in file:
            data.append([i for i in line.strip()])

    return data