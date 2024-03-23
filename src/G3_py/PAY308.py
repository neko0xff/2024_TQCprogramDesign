n=eval(input())

for i in range(n):
    tmp=num=eval(input())
    ans=0
    while(tmp!=0):
        ans+=tmp%10
        tmp//=10
    print("Sum of all digits of {:} is {:}".format(num,ans))