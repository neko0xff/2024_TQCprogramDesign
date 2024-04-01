# 讓使用者輸入兩個整數
# 接著呼叫函式compute()
# 此函式接收兩個參數a、b，並回傳從a連加到b的和。

def compute(a,b):
    out=0
    for i in range(a,b+1):
        out+=i
    return out

in1=eval(input())
in2=eval(input())
num=compute(in1,in2)
print(num)