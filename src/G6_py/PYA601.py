# 利用一維串列存放使用者輸入的12個正整數（範圍1~99）。
# 顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。
# 提示：輸出每一個數字欄寬設定為3，每3個一列，靠右對齊。

runtime=12
total=0
num=[]

for i in range(1,runtime+1):
    in1=eval(input())
    num.append(in1)

for j in range(1,runtime+1):
    if(j%3==0):
        print("{:3d}".format(num[j-1]))
    else:
        print("{:3d}".format(num[j-1]),end='')
    if (j-1)%2==0:
        total+=num[j-1]
print(total)