from math import pi,tan,pow

s=eval(input())
n=5

tanN= tan(pi/n)
area = n*(pow(s,2))/(4*tanN)

print("Area = {:.4f}".format(area))
