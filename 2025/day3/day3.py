def part1():
    txtLines = open("day3/input.txt").read().splitlines()
    total = 0
    for line in txtLines:
        biggestNum = 0
        for i in range(len(line)):
            for y in line[i + 1 :]:
                biggestNum = max(biggestNum, int(line[i]+y))
        total += biggestNum
    print(total)

def part2():
    txtLines = open("day3/input.txt").read().splitlines()
    total = 0
    for line in txtLines:
        total += int(find_biggest(line))
    print(total)


def find_biggest(line, target_len=12):
    length = len(line)
    stack = []
    for i in range(len(line)):
        while stack and line[i] > stack[-1] and (length - i) > (target_len - len(stack)):
            stack.pop()
        if len(stack) < target_len:
            stack.append(line[i])
    return ''.join(stack[:target_len])


if __name__ == "__main__":
    part1()
    part2()