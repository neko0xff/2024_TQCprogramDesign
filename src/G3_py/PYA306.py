# 輸出n!的值
# 5! = 5*4*3*2*1

n=eval(input())
output=1

for i in range(2,n+1):
    output*=i

print(output)