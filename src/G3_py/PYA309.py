from math import sqrt 
n=eval(input())
output=0

for i in range(2,n+1):
    output += 1 / (sqrt(i-1) + sqrt(i))

print("{:.4f}".format(output))
