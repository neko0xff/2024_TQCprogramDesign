n=eval(input())

# 判斷它是3或5的倍數
if (n%3 == 0) & (n%5 == 0):
    print("{:} is a multiple of 3 and 5.".format(n))
elif(n%5 == 0):
    print("{:} is a multiple of 5.".format(n))
elif(n%3 == 0):
    print("{:} is a multiple of 3.".format(n))
else:
    print("{:} is not a multiple of 3 or 5.".format(n))