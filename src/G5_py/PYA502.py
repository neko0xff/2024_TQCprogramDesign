# 使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式
# 此函式將回傳x和y的乘積

def compute(x,y):
    out=x*y
    return out

in1=eval(input())
in2=eval(input())
cal=compute(in1,in2)
print(cal)