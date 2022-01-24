
def calc_balance():
    balance = eval(input("Enter your net balance here: "))
    cycle = eval(input("Enter number of days in the billing cycle here: "))
    payment = eval(input("Enter amount payment amount here: "))
    day = eval(input("Enter day payment was made here: "))
    annual = eval(input("Enter annual interest rate: "))
    interest = (((balance * cycle) - (payment * (cycle-day))) / cycle) * ((annual/12) * .01)
    print("The monthly interest charge is: "+"$"+str(interest))

calc_balance()