import graphics
from face import Face

def fibonacci(n):

    # first numbers of the sequence
    n = int(n)
    n1 = 0
    n2 = 1
    count = 0

    if n < 1:
        return None
    else:
        while count < n:
            add = n1 + n2
            n1 = n2
            n2 = add
            count += 1
        print(n2)

def double_investment(principle, rate):
    p, r = float(principle), float(rate)
    years = 0
    double = 2 * p
    while p <= double:
        total = p * (1+r)
        p = total
        years += 1
    print(years)

def syracuse(n):
    n = int(n)
    syracuse_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
            syracuse_list.append(int(n))
        else:
            n = (3*n)+1
            syracuse_list.append(int(n))
    print(syracuse_list)

def is_prime(n):
    n = int(n)
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    if primes_list.index(n):
        return True
    else:
        return False

def gen_primes(n):
    n = int(n)
    primes = []
    for i in range(3, n):
        if is_prime(i):
            primes.append(i)
    return primes

def goldbach(n):
    n = int(n)
    two_primes = []
    j = 0

def Face_maker():
    win = graphics.GraphWin("Face")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    Face(win, Point(5.0, 5.0), 8)






if __name__ == '__main__':
    fibonacci('6')
    double_investment('100', '0.05')
    syracuse('5')
    face_maker()
