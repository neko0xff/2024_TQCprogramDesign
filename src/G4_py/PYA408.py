# 讓使用者輸入十個整數
# 計算並輸出偶數和奇數的個數

runtime=10
odd=0
even=0

for i in range(1,runtime+1):
    n=eval(input())
    if(n%2 == 0):
        even+=1
    else:
        odd+=1
    
print("Even numbers: {}".format(even))
print("Odd numbers: {}".format(odd))