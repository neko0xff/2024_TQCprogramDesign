# 讓使用者輸入十個整數作為樣本數
# 輸出眾數（樣本中出現最多次的數字）及其出現的次數
# 提示：假設樣本中只有一個眾數。

from math import pow
runtime = 10
count = [0]*int(pow(runtime,2))

for i in range(1,runtime+1):
    in1=int(input())
    count[in1]+=1

num_max=max(count)
print(count.index(num_max))
print(num_max)