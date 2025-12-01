def readData():
    with open("./day7/day7_values.txt","r") as file:
        data = []
        for line in file:
            data.append(line.strip().split(": "))

    return data

def readTestData():
    with open("./day7/test_data.txt","r") as file:
        data = []
        for line in file:
            data.append(line.strip().split(": "))

    return data