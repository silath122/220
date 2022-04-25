def is_in_linear(search_val, values):
    i = 0
    while i < len(search_val) and search_val != values:
        i += 1
    return i < len(search_val)

def read_data(filename):
    infile = open(filename, 'r')
    txt = infile.read()
    txt = txt.replace("\n", " ")
    txt = txt.split(" ")
    i = 0
    while i < len(txt):
        txt[i] = eval(txt[i])
        i += 1
    return txt

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

def selection_sort(values):
    n = len(values)
    for low in range(n-1):
        mp = low
        for i in range(low+1, n):
            if values[i] < values[mp]:
                mp = i
        values[low], values[mp] = values[mp], values[low]

def calc_area(rect):
    x1, y1, x2, y2 = rect.getPoints()
    length = y2 - y1
    width = x2 - x1
    area = length * width
    return area

def rect_sort(rectangles):
    rect_list = []
    for each_rect in rectangles:
        rect_list = rect_list + calc_area(each_rect)
    selection_sort(rect_list)