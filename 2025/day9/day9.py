def part1(red_tiles: list[tuple[int, int]]):
    total = 0
    for x, y in red_tiles:
        for px, py in red_tiles:
            total = max(total, (abs(x - px)+1) * (abs(y - py)+1))
    
    print("Part 1:", total)

def part2(red_tiles: list[tuple[int, int]]):
    edges = []
    for i in range(len(red_tiles)):
        tile1 = red_tiles[i]
        tile2 = red_tiles[(i+1) % len(red_tiles)]

        if tile1[0] == tile2[0]:
            edges.append((tile1[0], tile1[0], min(tile1[1], tile2[1]), max(tile1[1], tile2[1]), True))
        else:
            edges.append((min(tile1[0], tile2[0]), max(tile1[0], tile2[0]), tile1[1], tile1[1], False))
    
    max_area = 0

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            tile1 = red_tiles[i]
            tile2 = red_tiles[j]

            min_x, max_x = min(tile1[0], tile2[0]), max(tile1[0], tile2[0])
            min_y, max_y = min(tile1[1], tile2[1]), max(tile1[1], tile2[1])

            area = (max_x - min_x) + 1 * (max_y - min_y) + 1

            if area <= max_area:
                continue

            intersects = False
            for ex_min, ex_max, ey_min, ey_max, is_vertical in edges:
                if is_vertical:
                    if  min_x < ex_min < max_x:
                        if not (ey_max <= min_y or ey_min >= max_y):
                            intersects = True
                            break
                else:
                    if  min_y < ey_min < max_y:
                        if not (ex_max <= min_x or ex_min >= max_x):
                            intersects = True
                            break
            
            if intersects:
                continue
                
            mid_x = (min_x + max_x) / 2
            mid_y = (min_y + max_y) / 2

            crossings = 0
            for ex_min, ex_max, ey_min, ey_max, is_vertical in edges:
                if is_vertical:
                    if ey_min <= mid_y < ey_max:
                        if ex_min > mid_x:
                            crossings += 1
            
            if crossings % 2 != 0:
                max_area = area
    print("Part 2:", max_area)

if __name__ == "__main__":
    red_tiles = [tuple(map(int, line.split(","))) for line in open("day9/input.txt").readlines()]
    part1(red_tiles)
    part2(red_tiles)