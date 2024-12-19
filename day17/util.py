def readData():
    with open("day17/input.txt") as f:
        registers = []
        program = []
        change = False
        for line in f:
            if line == "\n":
                change = True
                continue
            if not change:
                registers.append(line.strip().split(": ")[1])
            else:
                program.append("".join(line.strip().split(": ")[1::-2]).split(","))
    return registers, program