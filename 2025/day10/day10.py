class Indicator:
    def __init__(self, id: int, state: str = "."):
        self.state: bool = False if state == "." else True
        self.id: int = id

class Button:
    def __init__(self, activates: list[Indicator], ids: list[int]):
        self.activates: list[Indicator] = activates
        self.ids: list[int] = ids

class Machine:
    def __init__(self, strIndicators: list[str], stringButtons: list[str], joltageStr: list[str]):
        self._targetIndicators = [Indicator(i, state) for i, state in enumerate(strIndicators)]
        self.indicators = [Indicator(i, '.') for i in range(len(strIndicators))]
        self.buttons: list[Button] = [Button([self.findIndicatorById(int(id)) for id in buttonStr.split(",")], [int(id) for id in buttonStr.split(",")]) for buttonStr in stringButtons]
        self._target_joltage: list[int] = [int(joltage) for joltage in joltageStr.split(",")]
        self.joltage: list[int] = [0 for _ in self._target_joltage]
    
    def findIndicatorById(self, id: int) -> Indicator:
        for indicator in self.indicators:
            if indicator.id == id:
                return indicator
        raise ValueError(f"Indicator with id {id} not found")
    
    def isCorrect(self) -> bool:
        for indicator in self._targetIndicators:
            if indicator.state != self.indicators[indicator.id].state:
                return False
        return True


def findTargetIndicators(machine: Machine) -> int:
    from collections import deque

    max_depth = 10000000000
    start_state = tuple(indicator.state for indicator in machine.indicators)
    
    for i, indicator in enumerate(machine.indicators):
        indicator.state = start_state[i]
    if machine.isCorrect():
        return 0

    button_maps = [[indicator.id for indicator in button.activates] for button in machine.buttons]
    visited = {start_state}
    queue = deque([(start_state, 0)])

    while queue:
        state, depth = queue.popleft()
        if depth == max_depth:
            continue

        for mapping in button_maps:
            new_state = list(state)
            for idx in mapping:
                new_state[idx] = not new_state[idx]
            new_state_tuple = tuple(new_state)

            for i, indicator in enumerate(machine.indicators):
                indicator.state = new_state_tuple[i]
            if machine.isCorrect():
                return depth + 1
            
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state_tuple, depth + 1))

    return float("inf")



def findTargetJoltage(machine: Machine) -> int:
    pass


if __name__ == "__main__":
    lines = open("day10/input.txt").readlines()
    machines: list[Machine] = []
    for line in lines:
        indicatorLights = list(line.split("[")[1].split("]")[0])
        line = line.split("] ")[1]
        buttonStrings = []
        while "(" in line:
            buttonStrings.append(line.split("(")[1].split(")")[0])
            line = line[line.index(")")+1:]
        joltageStr = line.split("{")[1].split("}")[0]
        machines.append(Machine(indicatorLights, buttonStrings, joltageStr))
    total_part1 = 0
    total_part2 = 0
    for machine in machines:
        print("Processing machine...")
        total_part1 += findTargetIndicators(machine)
        print("Part 1 done, starting Part 2...")
        total_part2 += findTargetJoltage(machine)
        print("Done.")
    print("Part 1:", total_part1)
    print("Part 2:", total_part2)