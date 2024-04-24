# 讓使用者建立一個3*3的矩陣
# 其內容為從鍵盤輸入的整數（不重複）
# 接著輸出矩陣最大值與最小值的索引
# input: 九個整數

num = []
runtime = 9

for n in range(runtime):
    in1 = eval(input())
    num.append(in1)

num_max=max(num)
max_x=num.index(num_max)//3
max_y=num.index(num_max)%3
num_min=min(num)
min_x=num.index(num_min)//3
min_y=num.index(num_min)%3

print("Index of the largest number {} is: ({}, {})".format(num_max,max_x,max_y))
print("Index of the smallest number {} is: ({}, {})".format(num_min,min_x,min_y))
