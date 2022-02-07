""" Siah Thomas """
def traffic_tracker():
    roads = eval(input("How many roads were surveyed? "))
    total = 0
    for i in range(1, roads + 1):
        print("How many days was road", i, "surveyed?", end=' ')
        days = eval(input(" "))
        rs = 0
        for j in range(1, days + 1):
            print("How many cars traveled on day", j, end='?')
            cars = eval(input(" "))
            rs = rs + cars
            total = total + cars
        avg_for_day = rs / days
        print("Road", i, "average vehicles per day:", round(avg_for_day, 1))
    print("The total number of vehicles traveled on all roads: ", total)
    avg_roads = total / roads
    print("Average number of vehicles per road: ", round(avg_roads, 1))

