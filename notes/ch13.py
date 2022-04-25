def search(x, nums):
    # nums = list of numbers and x is a number
    # Returns the position in the list where x occurs or -1 if
    # x is not in the list
    try:
        return nums.index(x)
    except:
        return -1

def linear_search(search_list, target):
    # search through the list of items one by one until the target is found
    for i in range(len(search_list)):
        if search_list[i] == target:  # item found, return the index value
            return i
    return -1  # loop finished, item was not in the list

# binary search is faster and for bigger numbers
# linear search is slow, but good for smaller numbers

def binary_search(search_list, target):
    left_index = 0
    right_index = len(search_list) - 1
    while left_index <= right_index:     # there is still a range to search
        middle_index = (left_index + right_index) // 2  # position of middle item
        middle_value = search_list[middle_index]
        if middle_value == target:    # found it! Return the index
            return middle_index
        elif middle_value < target:   # target is in lower half of range
            left_index = middle_index + 1    #     move top marker down
        else:                           # target is in upper half
            right_index = middle_index - 1    #     move bottom marker up
    return -1                 # no range left to search
                              # target is not there

def rec_binary(x, nums, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if x ==  nums[middle]:
        return middle
    elif x < nums[middle]:
        return rec_binary(x, nums, left, middle - 1)
    else:
        return rec_binary(x, nums, middle + 1, right)


def print_me(s):
    print(s)
    print_me(s)  # recursion, it's going to print over and over and over again.
    # Recursion def:Looping with only using function calls

def print_repeat(s, n):
    if n == 0:
        return
    else:
        print(s)
        print_repeat(s, n - 1)  # repeat it only n times, everytime it loops through it subtracts one
        # when writing a recursive function your parameter need to decrease/approach your base case

# recursive function rules
# 1. base case
# 2. decreasing parameter
#

def sum_list(the_list):
    if len(the_list) == 0:
        return 0
    else:
        return the_list[0] + sum_list(the_list[1:])
    # starts: 3 + sum_list([7, 5]) <- 12
    # next: 7 + sum_list([5]) <- 5
    # final: 5 + sum_list([]) <-- base case, sum_list([]) returns 0
    # nothing returns until getting to the base case
    # returns total of list

    # stack overflow: forgot definition

def sum_list_tail(the_list, acc):  # more desired to use
    if len(the_list) == 0:
        return acc
    else:
        acc = the_list[0] + acc
        return sum_list_tail(the_list[1:], acc)
    # acc = 3 + 0
    # sum_list_tail([7,5],3)

    # acc = 7 + 3
    # sum_list_tail([5], 10)

    # acc = 5 + 10
    # sum_list_tail([], 15)
    # base case = 15 bc empty list []
    # return 15


# Fibonacci sequence: 1, 1, 2, 3, 5, 8,..., (n-1) + (n-2) <-- base cases are the first two numbers: 1, 1
# function returns the nth number
# Fib(3) --> 2
# Fib(6) --> 8

# loop
def fib(n):
    current_num = 1  # <- base case
    previous_num = 1  # <- base case
    for i in range(n - 2):  # -2 because we already have current and previous start
        sum = current_num + previous_num
        previous_num = current_num
        current_num = sum
    return current_num

# recursively - takes longer w bigger numbers because it has to do the math for each branch, it has a
# ton of more branches.
# examples: Fib(40) --> (Fib(39) --> (Fib(38) + Fib(37)) + Fib(38) --> (Fib(37) + Fib(36))) and so on..

def fib_rec(n):
    if n < 3:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

# sorting a list from smallest to last -- [3, 2, 1, 4] --> [1, 2, 3, 4]  big O(n^2)

# merge sort big O(nlogn) --> takes list and breaks it down into half, into half, into half, until there are single
# elements, and then it merges. Everytime it merges two list, it sorts it as it merges

def select_sort(sort_list):
    pass

def merge_sort(sort_list):
    pass


if __name__ == '__main__':
    print(select_sort([3,2,1,4]))

    # print(fib(45)) # <-- loop goes faster
    # print(fib_rec(45))

    # print(sum_list([3,7,5]))
    # print(sum_list_tail([3,7,5], 0))

    # s = sum_list([3,7,9])
    # print(s)

    # print_repeat('hi', 3)

    # print_me("hi")

    # my_list = [3,4,2,1,9,10,81,45]
    # my_list.sort()

