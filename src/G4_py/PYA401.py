# 由使用者輸入十個數字
# 然後找出其最小值
# 最後輸出最小值

runtime=10
list01=[]

for i in range(1,runtime+1):
    n=eval(input())
    list01.append(n)

print(min(list01))