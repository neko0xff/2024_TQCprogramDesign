from math import pi,pow

radius=float(input())

perimeter = 2*pi*radius
area = pi*pow(radius,2)


print("Radius = {:.2f}".format(radius))
print("Perimeter = {:.2f}".format(perimeter))
print("Area = {:.2f}".format(area))
