# 將使用者輸入的三個整數（代表一元二次方程式 的三個係數a、b、c）
# 作為參數傳遞給一個名為compute()的函式，
# 該函式回傳方程式的解，如無解則輸出【Your equation has no root.】
# cal: (a*x^2)+(b*x)+c=0
# 1. -b+sqrt(b^2-4ac)/2a
# 2. -b-sqrt(b^2-4ac)/2a

# 提示：
# 輸出有順序性
# 回傳方程式的解，無須考慮小數點位數

from math import pow,sqrt

def compute(a, b, c):
    pow1 = pow(b, 2) - 4 * a * c
    sqrt1 = sqrt(pow1)
    ans1 = -b + sqrt1 / (2 * a)
    ans2 = -b - sqrt1 / (2 * a)
    if (pow1 > 0):
        return str(ans1) + ", " + str(ans2)
    elif (pow1 == 0):
        ans3 = -b / (2 * a)
        return ans3
    else:
        str1 = "Your equation has no root."
        return str1

in1 = eval(input())
in2 = eval(input())
in3 = eval(input())
num = compute(in1, in2, in3)

print(num)