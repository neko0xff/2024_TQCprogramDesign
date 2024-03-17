
import math

x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())

x_pow=(x1-x2)**2
y_pow=(y1-y2)**2
sum=x_pow+y_pow
sqrt=math.sqrt(sum)

print("({:.4f} , {:.4f})".format(x1,y1))
print("({:.4f} , {:.4f})".format(x2,y2))
print("Distance = {:.4f}".format(sqrt))
