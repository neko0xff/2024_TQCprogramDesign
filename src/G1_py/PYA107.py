
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
num5 = eval(input())

sum = num1+num2+num3+num4+num5
avg = sum/5

print("{:} {:} {:} {:} {:}".format(num1,num2,num3,num4,num5))
print("Sum = {:.1f}".format(sum))
print("Average = {:.1f}".format(avg))