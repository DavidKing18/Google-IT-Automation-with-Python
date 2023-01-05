import math

def triangle(base, height):
    return "Area of triangle: {}".format(base*height/2)

def rectangle(length, breadth):
    return "Area of rectangle: {}".format(length*breadth)

def circle(radius):
    return "Area of circle: {}".format(math.pi*(radius**2))
