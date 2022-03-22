def weighted_average(in_file_name, out_file_name):
    # open file names
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w')

    # process each line of the input file
    add_w = 0
    add = 0

    for line in infile:
        # separate the names from the numbers
        name, nums = line.split(':')

        # separate each number
        sep_nums = nums.split(" ")

        # the weighted numbers
        wn = sep_nums[0::2]

        # the grades
        gn = sep_nums[1::2]

        for each_weight in wn:
            add_w = add_w + float(each_weight)
            for each_grade in gn:
                add = add + (float(each_grade) * float(each_weight))
        if add_w < 100:
            line.replace(":", "'s average: Error: The weights are less than 100.")
        elif add_w > 100:
            line.replace(":", "'s average: Error: The weights are more than 100.")
        else:
            line.replace(":", "'s average: {}".format(add))

# I honestly have no idea what I'm doing 

if __name__ == '__main__':
    weighted_average('grades.txt', 'avg.txt')

