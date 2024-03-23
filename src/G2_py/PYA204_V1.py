in1=eval(input())
in2=eval(input())
op=input()
output=0

if op == "+":
    output=in1+in2
elif op == "-":
    output=in1-in2
elif op == "*":
    output=in1*in2
elif op == "/":
    output=in1/in2
elif op == "//":
    output=in1//in2
elif op == "%":
    output=in1%in2
    
print("{:}".format(output))