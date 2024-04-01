# 讓使用者輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數）
# 計算這兩個分數的和為p/q，接著將p和q傳遞給名為compute()函式
# 此函式回傳p和q的最大公因數（Greatest Common Divisor, GCD）
# 再將p和q各除以其最大公因數
# 最後輸出的結果必須以最簡分數表示。

from math import gcd

def compute(p,q):
    return gcd(p,q)

x,y=eval(input())
m,n=eval(input())
# 計算兩個分數的和
p = x * n + m * y
q = y * n

# 計算p和q的最大公因數
cal1 = compute(p, q)

# 將p和q各除以其最大公因數
p //= cal1
q //= cal1

print("{}/{} + {}/{} = {}/{}".format(x,y,m,n,p,q))