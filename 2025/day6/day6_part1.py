def get_num_total(line: list[str], opperation: str):
    total = 0
    for num in line:
        if opperation == "+":
            total += int(num)
        elif opperation == "*":
            if total == 0:
                total = 1
            total *= int(num)
    return total


if __name__ == "__main__":
    lines = [line.split() for line in open("day6/input.txt").read().splitlines()]
    part1_total = 0
    for x in range(len(lines[0])):
        opperation = lines[-1][x]
        temp = []
        for y in range(len(lines) - 1):
            temp.append(lines[y][x])
        part1_total += get_num_total(temp, opperation.strip())
    print(part1_total)