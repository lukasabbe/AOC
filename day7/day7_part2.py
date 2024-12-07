from util import readData, readTestData

def getAllResults(nums:list):
    if(len(nums) == 1):
        return [int(nums[0])]
    num = nums.pop()
    results = getAllResults(nums)
    result = [int(num) * result for result in results]
    result2 = [int(num) + result for result in results]
    result3 = [int(str(result)+num) for result in results]
    result.extend(result2)
    result.extend(result3)
    return result

def calcOperators(data):
    if(int(data[0]) in getAllResults(data[1].split(" "))):
            return True
    return False

if(__name__ == "__main__"):
    print(sum([int(i[0]) for i in readData() if(calcOperators(i))]))