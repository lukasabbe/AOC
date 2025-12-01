from util import readData, readTestData
from day10_part1 import outsideBounds, findAllStarts, findAmountOfPaths, findTrail

if(__name__ == "__main__"):
    print(findTrail(readData(), False))