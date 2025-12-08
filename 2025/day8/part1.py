import numpy as np
class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def equludian_distance(self, other):
        return ((self.x - other.x) ** 2 + 
                (self.y - other.y) ** 2 + 
                (self.z - other.z) ** 2) ** 0.5
    
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y and self.z == value.z
    
class Circuit:
    def __init__(self, coordinates: list[Coordinate]):
        self.coordinates: list[Coordinate] = coordinates
    
    def add(self, *coordinates: Coordinate):
        self.coordinates.extend(coordinates)
    

if __name__ == "__main__":


    lines = [list(map(int, line.split(","))) for line in open("day8/input.txt").readlines()]
    coordinates = [Coordinate(x, y, z) for x, y, z in lines]

    distances : list[tuple[float, Coordinate, Coordinate]] = []
    for i, coord in enumerate(coordinates):
        for j, other in enumerate(coordinates):
            if i < j:
                distance = coord.equludian_distance(other)
                distances.append((distance, coord, other))

    distances.sort(key=lambda x: x[0])

    coord_to_circuit = {}
    circuits : list[Circuit] = []

    for idx, (dist, coord1, coord2) in enumerate(distances):
        if idx >= 1000:
            break
            
        coord1_id = id(coord1)
        coord2_id = id(coord2)
        
        circuit1 = coord_to_circuit.get(coord1_id, -1)
        circuit2 = coord_to_circuit.get(coord2_id, -1)
        
        # Both coordinates are already in the same circuit
        if circuit1 != -1 and circuit1 == circuit2:
            continue
        
        if circuit1 != -1 and circuit2 != -1:
            for coord in circuits[circuit2].coordinates:
                circuits[circuit1].add(coord)
                coord_to_circuit[id(coord)] = circuit1
            circuits[circuit2].coordinates = [] 
            continue
        
        if circuit1 != -1 and circuit2 == -1:
            circuits[circuit1].add(coord2)
            coord_to_circuit[coord2_id] = circuit1
            continue
        
        if circuit1 == -1 and circuit2 != -1:
            circuits[circuit2].add(coord1)
            coord_to_circuit[coord1_id] = circuit2
            continue
        
        if circuit1 == -1 and circuit2 == -1:
            circuit_idx = len(circuits)
            circuits.append(Circuit([coord1, coord2]))
            coord_to_circuit[coord1_id] = circuit_idx
            coord_to_circuit[coord2_id] = circuit_idx
    
    # Add remaining coordinates as individual circuits
    for coord in coordinates:
        if id(coord) not in coord_to_circuit:
            circuits.append(Circuit([coord]))

    circuits.sort(key=lambda c: len(c.coordinates), reverse=True)
    print(np.prod([len(circuit.coordinates) for circuit in circuits[:3]]))