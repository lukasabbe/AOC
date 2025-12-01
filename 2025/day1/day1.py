def part1():
    txtLines = open("day1/input.txt").read().splitlines()
    zeros = 0
    dial = 50
    for line in txtLines:
        dir = line[0]
        steps = int(line[1:]) % 100
        if dir == "L":
            if dial - steps < 0:
                dial = 100 + (dial - steps)
            else:
                dial -= steps
        elif dir == "R":
            if dial + steps >= 100:
                dial = (dial + steps) - 100
            else:
                dial += steps
        if dial == 0:
            zeros += 1
    print(zeros)

def part2():
    txtLines = open("day1/input.txt").read().splitlines()
    zeros = 0
    dial = 50
    for line in txtLines:
        dir = line[0]
        steps = int(line[1:])
        for _step in range(steps):
            if dir == "L":
                if dial - 1 < 0:
                    dial = 99
                else:
                    dial -= 1
            elif dir == "R":
                if dial + 1 >= 100:
                    dial = 0
                else:
                    dial += 1
            if dial == 0:
                zeros += 1
    print(zeros)

if __name__ == "__main__":
    part1()
    part2()