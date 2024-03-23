in1=eval(input())
output=0

for i in range(1,in1+1):
    if i % 5 == 0:
        output+=i

print(output)