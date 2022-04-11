from Die import Die
from Student import Student
import math
def cannon():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))

    # convert angle to radians
    theta = math.radians(angle)

    # set the initial position and velocities in x and y directions
    xpos = h0
    ypos = 0.0
    xvel = vel * math.cos(theta)
    yvel = vel * math.sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0.0:
        # calculate the position and velocity in time seconds
        xpos = xpos + time * xvel
        yvell = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvell)/2.0
        yvel = yvell
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))





def main():
    d = Die(6)
    d2 = Die(12)
    d.roll()
    d2.roll()
    print(d.get_value(), d2.get_value())

# classes can be used to store data

# student
# we want it to have instant variable: name, hours, quality_points
# we want methods: getters/setters, get_gpa

# GPA = quality_points/hours
def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def student():
    # open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    # set best to the record for the first student in the file
    best = Student(infile.readline())

    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    # print information about the best student
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
    student()