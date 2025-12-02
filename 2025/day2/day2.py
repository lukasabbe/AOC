def isVaildId(id: str):
    for check in range(1, len(id) // 2 + 1):
        pattern = id[0:check]
        vaild = False
        for i in range(check, len(id), check):
            if id[i : i + check] != pattern:
                vaild = True
                break
        if not vaild:
            return False
    return True


def isVaildIdOne(id: str):

    if len(id) % 2 != 0:
        return True

    if id[len(id) // 2 :] == id[0:len(id) // 2]:
        return False
    return True

def part1():
    ids = open("day2/input.txt").read().split(",")
    total = 0
    for id in ids:
        numOne = int(id.split("-")[0].strip())
        numTwo = int(id.split("-")[1].strip())
        for i in range(numOne, numTwo + 1):
            iStr = str(i)
            if not isVaildIdOne(iStr):
                total += int(iStr)
    print(total)

def part2():
    ids = open("day2/input.txt").read().split(",")
    total = 0
    for id in ids:
        numOne = int(id.split("-")[0].strip())
        numTwo = int(id.split("-")[1].strip())
        for i in range(numOne, numTwo + 1):
            iStr = str(i)
            if not isVaildId(iStr):
                total += int(iStr)
    print(total)

if __name__ == "__main__":
    part1()
    part2()