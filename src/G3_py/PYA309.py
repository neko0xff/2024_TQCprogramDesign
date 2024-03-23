import math
n=eval(input())
output=0

for i in range(2,n+1):
    output += 1 / (math.sqrt(i-1) + math.sqrt(i))

print("{:.4f}".format(output))
