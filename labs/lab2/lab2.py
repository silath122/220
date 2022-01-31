import math

def types_of_me():
    n = eval(input("Enter the values to be entered: "))
    rm = 0
    har = 0
    ge = 1
    for i in range(n):
        temp = eval(input("Enter a value: "))
        rm = rm + (temp * temp)
        rms = math.sqrt(rm / n)
        har = har + (1 / temp)
        harm = n / har
        ge = ge * temp
        geo = ge ** (1 / n)
    print(round(rms, 3))
    print(round(harm, 3))
    print(round(geo, 3))

types_of_me()

