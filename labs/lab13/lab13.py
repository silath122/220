from lab12.algorithms import *

def trade_alert(filename):
    num_list = read_data(filename)
    for each_num in num_list:
        if each_num > 830:
            print('Warning! The trading volume', each_num, ' exceeds 830 at',
                  num_list.index(each_num), 'seconds.')
        elif each_num == 500:
            print('Pay attention! The trading volume', each_num, 'is equal to 500 at',
                  num_list.index(each_num), 'seconds.')

if __name__ == '__main__':
    trade_alert('trades.txt')

