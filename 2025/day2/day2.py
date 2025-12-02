def part1(id: str):
    if len(id) % 2 != 0:
        return True
    if id[len(id) // 2 :] == id[0:len(id) // 2]:
        return False
    return True

def part2(id: str):
    for pattern_length in range(1, len(id) // 2 + 1):
        pattern = id[0:pattern_length]
        valid = False
        for i in range(pattern_length, len(id), pattern_length):
            if id[i : i + pattern_length] != pattern:
                valid = True
                break
        if not valid:
            return False
    return True

def checkValid(isValidScript):
    intervals = open("day2/input.txt").read().split(",")
    total = 0
    for interval in intervals:
        startId = int(interval.split("-")[0].strip())
        endId = int(interval.split("-")[1].strip())
        for i in range(startId, endId + 1):
            iStr = str(i)
            if not isValidScript(iStr):
                total += int(iStr)
    print(total)

if __name__ == "__main__":
    #part 1
    checkValid(part1)
    #part 2
    checkValid(part2)