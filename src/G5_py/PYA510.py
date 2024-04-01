# 計算費氏數列（Fibonacci numbers）
# 使用者輸入一正整數num (num>=2)
# 並將它傳遞給名為compute()的函式
# 此函式將輸出費氏數列前num個的數值。
# 提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
# F0=0,F1=1,Fn=Fn-1+Fn-2
# 輸出格式部分: 每個數值後方為一個半形空格

def compute(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        a,b=0,1
        for i in range(2, num + 1):
            a,b = b,(a + b)
        return b

num=eval(input())

for i in range(0,num):
    print("{}".format(compute(i)),end=" ")



