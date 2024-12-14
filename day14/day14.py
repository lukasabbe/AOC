from util import readData
from PIL import Image, ImageDraw

mapSize = (101, 103)

def moveOneSec(points):
    new_points = []
    for (x, y), (vx, vy) in points:
        new_x = (x + vx) % mapSize[0]
        new_y = (y + vy) % mapSize[1]
        new_points.append(((new_x, new_y), (vx, vy)))
    return new_points

def printMap(points):
    strMap = ""
    map = [["." for i in range(mapSize[0])] for j in range(mapSize[1])]
    for i in points:
        map[int(i[0][1])][int(i[0][0])] = "#"
    for i in map:
        strMap += ("".join(i)) + "\n"
    return strMap

def renderToImage(points, filename):
    img = Image.new('RGB', (mapSize[0], mapSize[1]), color='white')
    draw = ImageDraw.Draw(img)
    for (x, y), _ in points:
        draw.point((x, y), fill='black')
    
    for (x, y), _ in points:
        if img.getpixel((x, y)) == (0, 0, 0):
            ImageDraw.floodfill(img, (x, y), (0, 0, 0))

    img.save(filename)


def splitQuads(data):
    middleX = mapSize[0] // 2
    middleY = mapSize[1] // 2
    quad1 = []
    quad2 = []
    quad3 = []
    quad4 = []
    for i in data:
        if(i[0][0] == middleX or i[0][1] == middleY):
            continue
        if(i[0][0] < middleX and i[0][1] < middleY):
            quad1.append(i)
        elif(i[0][0] >= middleX and i[0][1] < middleY):
            quad2.append(i)
        elif(i[0][0] < middleX and i[0][1] >= middleY):
            quad3.append(i)
        else:
            quad4.append(i)
    return quad1, quad2, quad3, quad4


if __name__ == "__main__":
    data = readData()
    maps = ""
    for i in range(10000):
        data = moveOneSec(data)
        renderToImage(data, f"./day14/outputs/output{i+1}.png")
    total = 1
    open("./day14/output.txt", "w").write(maps)
    for i in splitQuads(data):
        total *= len(i)
    print(total)