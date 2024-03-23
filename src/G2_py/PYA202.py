in1=int(input())

# 判斷它是3或5的倍數
if (in1%3 == 0) & (in1%5 == 0):
    print("{:} is a multiple of 3 and 5.".format(in1))
elif in1%5 == 0:
    print("{:} is a multiple of 5.".format(in1))
elif in1%3 == 0:
    print("{:} is a multiple of 3.".format(in1))
else:
    print("{:} is not a multiple of 3 or 5.".format(in1))