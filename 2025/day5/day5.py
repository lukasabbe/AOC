def part1(ranges: list[tuple[int, int]], ingredients: list[int]):
    total = 0
    for ingredient in ingredients:
        for numRange in ranges:
            if numRange[0] <= ingredient <= numRange[1]:
                total += 1
                break

    print(total)

def part2(ranges: list[tuple[int, int]]):
    mergedRanges = []
    for r in sorted(ranges):
        if not mergedRanges or mergedRanges[-1][1] < r[0]:
            mergedRanges.append(r)
        else:
            mergedRanges[-1] = (mergedRanges[-1][0], max(mergedRanges[-1][1], r[1]))

    totalCovered = sum(r[1] - r[0] + 1 for r in mergedRanges)
    print(totalCovered)

if __name__ == "__main__":
    lines = open("day5/input.txt").read().splitlines()
    ranges = []
    ingredients = []
    space = False
    for line in lines:
        if not space:
            if line == "":
                space = True
                continue
            # Process ranges here
            a, b = line.split("-")
            ranges.append((int(a), int(b)))
        else:
            # Process ingredients here
            ingredients.append(int(line))
    part1(ranges, ingredients)
    part2(ranges)