in1=eval(input())

for i in range(1,in1+1):
    for j in range(1,i+1):
        print("{:4}".format(j*i),end="")
    print("")