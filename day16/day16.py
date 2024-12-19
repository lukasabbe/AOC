from util import readData
from collections import deque, defaultdict
import heapq

def findChar(map, char):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if(map[i][j] == char):
                return (j, i)

def toGraph(map):
    graph = {}
    for i in range(len(map)):
        for j in range(len(map[i])):
            if(map[i][j] == "."):
                graph[(j, i)] = []
                if(i > 0 and map[i-1][j] == "."):
                    graph[(j, i)].append((j, i-1))
                if(i < len(map) - 1 and map[i+1][j] == "."):
                    graph[(j, i)].append((j, i+1))
                if(j > 0 and map[i][j-1] == "."):
                    graph[(j, i)].append((j-1, i))
                if(j < len(map[i]) - 1 and map[i][j+1] == "."):
                    graph[(j, i)].append((j+1, i))
    return graph

def findCheapestPath(graph, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, start, 1)]
    costs = defaultdict(lambda: float('inf'))
    costs[(start, None)] = 0
    vissited = set()

    while pq:
        current_cost, current_pos, prev_dir = heapq.heappop(pq)
        if(prev_dir == 0 or prev_dir == 1):
            vissited.add(current_pos)
        if current_pos == end:
            return current_cost, vissited

        for i, direction in enumerate(directions):
            next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if next_pos in graph:
                move_cost = 1
                turn_cost = 0 if prev_dir is None or prev_dir == i else 1000
                new_cost = current_cost + move_cost + turn_cost

                if new_cost < costs[(next_pos, i)]:
                    costs[(next_pos, i)] = new_cost
                    heapq.heappush(pq, (new_cost, next_pos, i))

    return float('inf')

if __name__ == "__main__":
    map = readData()
    start = findChar(map, "S")
    end = findChar(map, "E")
    map[start[1]][start[0]] = "."
    map[end[1]][end[0]] = "."
    graph = toGraph(map)
    cheapest_cost, vissited = findCheapestPath(graph, start, end)
    print(f"The cheapest cost from start to end is: {cheapest_cost}")
    print(f"Vissited nodes: {len(vissited)}")
