import threading
from time import time
def part1(data: list[list[str]]):
    total = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != "@": continue
            dir = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]
            amount = 0
            for d in dir:
                dx, dy = d
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(data[y]) and 0 <= ny < len(data) and data[ny][nx] == "@":
                    amount += 1
            if amount < 4:
                total += 1
    print(total)


def part2(data: list[list[str]]):
    total = 0
    while True:
        temp = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] != "@": continue
                dir = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]]
                amount = 0
                for d in dir:
                    dx, dy = d
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(data[y]) and 0 <= ny < len(data) and data[ny][nx] == "@":
                        amount += 1
                if amount < 4:
                    data[y][x] = "."
                    temp += 1
                    total += 1
        if temp == 0:
            break
    print(total)

if __name__ == "__main__":
    map = [[x for x in y] for y in open("day4/input.txt").read().splitlines()]
    start = time()
    t1 = threading.Thread(target=part1, args=(map,))
    t2 = threading.Thread(target=part2, args=(map,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Took {time() - start} seconds")