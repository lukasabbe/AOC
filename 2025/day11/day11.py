def find_paths(devices: dict[str, list[str]], start: str, end: str, must_pass: list[str] | None = None) -> int:
    if must_pass is None: must_pass = set()
    else: must_pass = set(must_pass)

    visited: set[str] = set()

    def dfs(current: str, remaining: set[str]) -> int:
        if current == end and not remaining:
            return 1

        visited.add(current)

        new_remaining = remaining - {current}

        count = 0

        for neighbor in devices.get(current, []):
            if neighbor not in visited:
                count += dfs(neighbor, new_remaining)

        visited.remove(current) # backtrack
        return count


    return dfs(start, must_pass) 
    

if __name__ == "__main__":
    lines = open("day11/input.txt").readlines()
    
    devices: dict[str, list[str]] = {}

    for line in lines:
        id = line.split(":")[0]
        ids = line.split(":")[1].strip().split(" ")

        devices[id] = ids

    print(find_paths(devices, "you", "out"))
    print(find_paths(devices, "svr", "out", must_pass=["dac", "fft"]))