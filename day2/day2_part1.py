from util import readData

def isSafe(line : list):
    safe = True
    counter = 0
    for i in range(len(line)-1):
        if(abs(int(line[i]) - int(line[i+1])) > 3):
            safe = False
        if(int(line[i]) - int(line[i+1]) < 0):
            counter-=1
        elif int(line[i]) - int(line[i+1]) > 0:
            counter+=1
    if abs(counter) != len(line)-1:
        safe = False
    return safe

if __name__ == "__main__":
    #lines = ["7 6 4 2 1","1 2 7 8 9","9 7 6 2 1","1 3 2 4 5","8 6 4 4 1","1 3 6 7 9"]
    lines = readData()
    print(sum(1 for line in lines if isSafe(line.split(" "))))