# want to sort by frequency of words, not 0 (word), 1 (number)
def word_sort(tup):
    return tup[1]


def count(file_name):
    # open the file
    # read all the lines
    text = open(file_name, 'r').read()

    # make all lowercase
    text = text.lower()

    # replace all punctuation
    for ch in "~!@#$%^&*()_:\"><?{}|`-[]\\;\',./":
        text = text.replace(ch, ' ')
    print(text)

    # split into list of words -> list[str]
    words = text.split()

    # count all words - use a dictionary
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        if word in counts:
            counts[word] = counts[word] +  1
        else:
            counts[word] = 1
    print(counts)

    # sort word counts - convert dictionary to a list
    # interested in keys and values
    counts_list = list(counts.items())
    print(counts_list)
    counts_list.sort(key=word_sort,reverse=True)

    # display/print
    for i in range(5):
        print(counts_list[i][0], counts_list[i][1])

if __name__ == '__main__':
    count('alice.txt')


# {}
# key: word -> str
# value: frequency ->
# counts = {"the':54, "a": 29, "she": 408
