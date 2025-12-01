import sys, os
def getRule(num):
    if num == 0:
        return [1]
    elif(len(str(num)) % 2 == 0):
        return [int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])]
    else:
        return [num * 2024]

def calcRules(nums):
    nums = nums.split(" ")
    rules = []
    for num in nums:
        rules.append(getRule(int(num)))
    return " ".join([str(num) for rule in rules for num in rule])

if(__name__ == "__main__"):
    current = "8069 87014 98 809367 525 0 9494914 5"
    for i in range(25):
        print("on iteration: ", i)
        current = calcRules(current)
        os.system("cls")
    print(current)
    print(len(current.split(" ")))
    