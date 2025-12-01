def readData():
    lines = []
    with open("./day2/day2_values.txt", "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines