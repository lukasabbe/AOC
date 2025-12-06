if __name__ == "__main__":
    lines_part2 = [line[::-1] for line in open("day6/input.txt").read().splitlines()]
    opperations = lines_part2.pop().split()
    part2_total = 0
    opperationCount = 0
    temp = 0
    for x in range(len(lines_part2[0])):
        num = ""
        for y in range(len(lines_part2)):
            if lines_part2[y][x] != " ":
                num += lines_part2[y][x]
        if num == "":
            opperationCount += 1
            part2_total += temp
            temp = 0
            continue
        if opperations[opperationCount] == "+":
            temp += int(num)
        elif opperations[opperationCount] == "*":
            if temp == 0:
                temp = 1
            temp *= int(num)
    part2_total += temp
    print(part2_total)