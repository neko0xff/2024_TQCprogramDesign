in1=input()

if ('A' <= in1 <= 'Z') | ('a' <= in1 <= 'z'):
    print("{:} is an alphabet.".format(in1))
elif ('0' <= in1 <= '9'):
    print("{:} is a number.".format(in1))
else:
    print("{:} is a symbol.".format(in1))