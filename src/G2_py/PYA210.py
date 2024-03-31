in1=eval(input())
in2=eval(input())
in3=eval(input())

# 檢查方法 = 任意兩個邊長之總和大於第三邊長
point1 = (in1+in2) > in3
point2 = (in1+in3) > in2
point3 = (in2+in3) > in1
sum = in1+in2+in3

if point1 & point2 & point3:
    print("{:}".format(sum))
else:
    print("Invalid")