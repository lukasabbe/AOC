def readData():
    with open("day14/data.txt") as f:
        points = []
        for line in f:
            pos = (int(line.split("=")[1].strip().split(",")[0]), int(line.split("=")[1].strip().split(",")[1].split("v")[0].strip()))
            vel = (int(line.split("=")[2].split(",")[0].strip()), int(line.split("=")[2].split(",")[1].strip()))
            points.append((pos, vel))
        return points