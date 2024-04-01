# 讓使用者輸入兩個整數
# 接著呼叫函式compute()
# 此函式接收兩個參數a、b，並回傳a^b的值。

from math import pow

def compute(a,b):
    out=int(pow(a,b))
    return out

in1=eval(input())
in2=eval(input())
num=compute(in1,in2)
print(num)