# 讓使用者輸入十個成績
# 接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績
# 作加總及平均
# 並輸出結果。
# 提示：平均值輸出到小數點後第二位。

num = []
runtime = 10

for i in range(1,runtime+1):
    in1=eval(input())
    num.append(in1)

ans = sum(num)-min(num)-max(num)
avg = ans/8
print("{:}".format(ans))
print("{:.2f}".format(avg))
