def readData():
    with open("./day8/day8_values.txt","r") as file:
        data = []
        for line in file:
            data.append([i for i in line.strip()])

    return data

def readTestData():
    with open("./day8/test_data.txt","r") as file:
        data = []
        for line in file:
            data.append([i for i in line.strip()])

    return data