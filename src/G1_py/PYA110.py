
import math

n=eval(input())
s=eval(input())

pi=math.pi
tanN=math.tan(pi/n)
area=n*(s**2)/4*tanN

print("Area = {:.4f}".format(area))
