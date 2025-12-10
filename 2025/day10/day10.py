import copy
class Indicator:
    def __init__(self, id: int, state: str = "."):
        self.state: bool = False if state == "." else True
        self.id: int = id
    
    def toggle(self):
        self.state = not self.state

class Button:
    def __init__(self, activates: list[Indicator]):
        self.activates: list[Indicator] = activates
    
    def activate(self):
        for indicator in self.activates:
            indicator.toggle()

class Machine:
    def __init__(self, strIndicators: list[str], stringButtons: list[str]):
        self._targetIndicators = [Indicator(i, state) for i, state in enumerate(strIndicators)]
        self.indicators = [Indicator(i, '.') for i in range(len(strIndicators))]
        self.buttons : list[Button] = [Button([self.findIndicatorById(int(id)) for id in buttonStr.split(",")]) for buttonStr in stringButtons]
    
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


def turnOffAllIndicators(machine: Machine) -> int:
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
        machines.append(Machine(indicatorLights, buttonStrings))
    total = 0
    for machine in machines:
        total += turnOffAllIndicators(machine)
    print("Part 1:", total)