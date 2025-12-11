import functools

def find_paths(devices: dict[str, list[str]], start: str, end: str, must_pass: list[str] | None = None) -> int:
    visited: set[str] = set()

    @functools.cache
    def dfs(current: str, has_first: bool, has_second: bool) -> int:
        if current == end and has_first and has_second:
            return 1

        visited.add(current)

        count = 0

        for neighbor in devices.get(current, []):
            if neighbor not in visited:
                count += dfs(neighbor, has_first or neighbor == must_pass[0], has_second or neighbor == must_pass[1])

        visited.remove(current) # backtrack
        return count

    if not must_pass:
        return dfs(start, True, True)
    return dfs(start, False, False) 
    

if __name__ == "__main__":
    lines = open("day11/input.txt").readlines()
    
    devices: dict[str, list[str]] = {}

    for line in lines:
        id = line.split(":")[0]
        ids = line.split(":")[1].strip().split(" ")

        devices[id] = ids

    print(find_paths(devices, "you", "out"))
    print(find_paths(devices, "svr", "out", must_pass=["dac", "fft"]))