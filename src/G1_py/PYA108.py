from math import pow,sqrt

x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())

x_pow=pow(x1-x2,2)
y_pow=pow(y1-y2,2)
sum1=x_pow+y_pow
sqrt1=sqrt(sum1)

print("( {:} , {:} )".format(x1,y1))
print("( {:} , {:} )".format(x2,y2))
print("Distance = {:.4f}".format(sqrt1))
