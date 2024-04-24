# 要求使用者輸入十個數字並存放在串列中。
# 接著由大到小的順序顯示最大的3個數字

num = []
runtime=10
for i in range(1,runtime+1):
    in1=eval(input())
    num.append(in1)

num.sort()
print("{} {} {}".format(num[-1],num[-2],num[-3]))
