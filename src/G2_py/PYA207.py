in1=eval(input())
total=0

if(in1>=38000):
    total=in1*0.7
elif(in1>=28000):
    total=in1*0.8
elif(in1>=18000):
    total=in1*0.9
elif(in1>=8000):
    total=in1*0.95

print("{:}".format(total))