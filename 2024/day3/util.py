def readData():
    str = ""
    with open("./day3/day3_values.txt", "r") as file:
        str = file.read()
    return str