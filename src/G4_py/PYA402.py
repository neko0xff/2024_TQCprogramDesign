# 讓使用者輸入數字，
# 輸入的動作直到輸入值為9999才結束
# 然後找出其最小值
# 並輸出最小值

breakend=9999
list01=[]

while(1):
    n=eval(input())
    if(n==breakend):
        break
    else:
        list01.append(n)

print(min(list01))