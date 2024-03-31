# 讓使用者輸入兩個正整數a、b（a<=b）
# 輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）
# 以及倍數之個數、總和

a=eval(input())
b=eval(input())
count=0
total=0

for i in range(a,b+1):
    if(i%4==0) | (i%9==0):
        count+=1
        total+=i
        print("{:<4d}".format(i),end="")
        if(count%10==0):
            print()

print()
print(count)
print(total)