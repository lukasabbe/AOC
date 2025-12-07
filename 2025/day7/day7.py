import functools

def find_start(map: list[list[str]]):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                return x, y
    return -1, -1

def go_down(map: list[list[str]], x: int, y: int, total=0):
    if y + 1 >= len(map):
        return total
    if map[y][x] == ".":
        map[y][x] = "|"
        total += go_down(map, x, y + 1)
    if map[y][x] == "^":
        total += 1
    if map[y][x] == "^" and x - 1 >= 0 and map[y][x - 1] == ".":
        map[y][x - 1] = "|"
        total += go_down(map, x - 1, y + 1)
    if map[y][x] == "^" and x + 1 < len(map[y]) and map[y][x + 1] == ".":
        map[y][x + 1] = "|"
        total += go_down(map, x + 1, y + 1)
    return total

def go_down_timelines(map: list[list[str]], x: int, y: int):
    @functools.cache
    def dfs(px: int, py: int) -> int:
        if py + 1 >= len(map):
            return 1
        total = 0
        if map[py][px] == ".":
            total += dfs(px, py + 1)
        
        if map[py][px] == "^" and px - 1 >= 0 and map[py][px - 1] == ".":
            total += dfs(px - 1, py + 1)
        if map[py][px] == "^" and px + 1 < len(map[py]) and map[py][px + 1] == ".":
            total += dfs(px + 1, py + 1)

        return total

    return dfs(x, y)
        


def part1(map: list[list[str]]):
    start_x, start_y = find_start(map)
    total = go_down(map, start_x, start_y + 1)
    print(total)

def part2(map: list[list[str]]):
    start_x, start_y = find_start(map)
    total = go_down_timelines(map, start_x, start_y + 1)
    print(total)


if __name__ == "__main__":
    map = [[char for char in line] for line in open("day7/input.txt").read().splitlines()]
    part1(map)
    map = [[char for char in line] for line in open("day7/input.txt").read().splitlines()]
    part2(map)