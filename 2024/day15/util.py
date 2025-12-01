def readData():
    with open("day15/data.txt") as f:
        house = []
        instructions = []
        flip = False
        for line in f:
            if(line == "\n"):
                flip = True
            if(not flip):
                house.append([char for char in line.strip()])
            else:
                instructions.extend([char for char in line.strip()])
        return house, instructions
    
def readDataPart2():
    with open("day15/data.txt") as f:
        house = []
        instructions = []
        flip = False
        for line in f:
            if(line == "\n"):
                flip = True
            if(not flip):
                row = []
                for char in line.strip():
                    if(char == "#"):
                        row.append("#")	
                        row.append("#")
                    elif(char == "O"):
                        row.append("[")
                        row.append("]")
                    elif(char == "."):
                        row.append(".")
                        row.append(".")
                    else:
                        row.append(char)
                        row.append(".")
                house.append(row)
            else:
                instructions.extend([char for char in line.strip()])
        return house, instructions