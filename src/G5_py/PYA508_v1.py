# 讓使用者輸入兩個正整數x、y
# 並將x與y傳遞給名為compute()的函式
# 此函式回傳x和y的最大公因數。

# 最大公因數（英語：highest common factor，hcf）也稱最大公約數（英語：greatest common divisor，gcd）是數學詞彙，
# 指能夠整除多個整數的最大正整數。而多個整數不能都為零。

from math import gcd

# 輾轉相除法(維基百科)
# 運用遞迴讓x,y兩數持續相除取餘數，直到y餘數為0，則x為最大公因數。
def compute(x,y):
    if(y==0):
        return 0
    else:
        return gcd(y,x)
    
in1,in2=eval(input())
num=compute(in1,in2)
print(num)
