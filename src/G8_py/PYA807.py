# 要求使用者輸入一字串
# 該字串為五個數字
# 以空白隔開
# 請將此五個數字
# 加總（Total）並
# 計算平均（Average）: 輸出浮點數到小數點後第一位

in1 = input()
num_str1 = in1.split(" ")
total = 0
avg = 0
runtime = 5

for i in range(runtime):
    total+=int(num_str1[i])
    
avg=total/5

print("Total = {}".format(total))
print("Average = {:.1f}".format(avg))