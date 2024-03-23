a=eval(input())
b=eval(input())

output=0

for i in range(a,b+1):
    if(i%2 == 0):
        output+=i

print(output)
