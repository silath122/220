from math import sqrt
def getNumbers():
    # empty list
    nums = []

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr !="":
        x = eval(xStr)
        nums.append(x) # add value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    sum = 0.0
    for num in nums:
        sum = sum + num
    return sum / len(nums)

def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = xbar - num
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq/(len(nums)-1))

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos-1]) / 2
    else:
        median = nums [midPos]
    return median

def main():
    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    print('\nThe mean is', xbar)
    print("The standard deviation is", std)
    print("The median is", med)
def color():
    colors = ['sky', 'blue', 'rose red', 'sunny yellow']
    col_split = []
    for color in colors:
        col_split.append(list(color.split(' ')))
        print(col_split[])
    print(col_split)


if __name__ == '__main__':
    color()
