import math

x1,y1=eval(input()),eval(input())
x2,y2=5,6

x_pow=math.pow(x1-x2,2)
y_pow=math.pow(y1-y2,2)
sqrt1=math.sqrt(x_pow+y_pow)

if sqrt1<=15:
    print("Inside")
else:
    print("Outside")
