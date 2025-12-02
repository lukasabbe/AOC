def part1(id: str):
    if len(id) % 2 != 0:
        return True
    if id[len(id) // 2 :] == id[0:len(id) // 2]:
        return False
    return True

def part2(id: str):
    for check in range(1, len(id) // 2 + 1):
        pattern = id[0:check]
        valid = False
        for i in range(check, len(id), check):
            if id[i : i + check] != pattern:
                valid = True
                break
        if not valid:
            return False
    return True

def checkValid(func):
    ids = open("day2/input.txt").read().split(",")
    total = 0
    for id in ids:
        numOne = int(id.split("-")[0].strip())
        numTwo = int(id.split("-")[1].strip())
        for i in range(numOne, numTwo + 1):
            iStr = str(i)
            if not func(iStr):
                total += int(iStr)
    print(total)

if __name__ == "__main__":
    #part 1
    checkValid(part1)
    #part 2
    checkValid(part2)