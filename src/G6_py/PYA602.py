# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和
# 提示：J、Q、K以及A分別代表11、12、13以及1

num=[]
runtime=5

for i in range(1,runtime+1):
    in1=input()
    if(in1 == "J"): num.append(11)
    elif(in1 == "Q"): num.append(12)
    elif(in1 == "K"): num.append(13)
    elif(in1 == "A"): num.append(1)
    else: num.append(int(in1))

print(sum(num))