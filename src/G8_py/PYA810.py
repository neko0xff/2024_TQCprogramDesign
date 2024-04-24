# 首先要求使用者輸入正整數k（1 <= k <= 100）
# 代表有k筆測試資料
# 每一筆測試資料是一串數字，每個數字之間以一空白區隔
# 請找出此串列數字中最大值和最小值之間的差
# 提示：差值輸出到小數點後第二位

k = int(input())
out = 0

while(k):
    in1 = input()
    num1 = []
    str1 = in1.split(" ")
    str1_len = len(str1)
    for i in range(str1_len):
        num1.append(eval(str1[i]))
    out = max(num1)-min(num1)
    print("{:.2f}".format(out))