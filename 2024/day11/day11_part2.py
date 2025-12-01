import functools

@functools.lru_cache(maxsize=None)
def getRule(num, loop):
    if loop == 0:
        return 1

    if num == 0:
        return getRule(1, loop-1)
    elif(len(str(num)) % 2 == 0):
        return getRule(int(str(num)[:len(str(num))//2]),loop-1) + getRule(int(str(num)[len(str(num))//2:]), loop-1)
    else:
        return getRule(num * 2024, loop-1)

if(__name__ == "__main__"):
    current = "8069 87014 98 809367 525 0 9494914 5"
    print(sum([getRule(int(num), 75) for num in current.split(" ")]))
    