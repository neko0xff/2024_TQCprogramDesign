# 以不定數迴圈的方式輸入一個正整數（代表分數）
# 之後根據以下分數與GPA的對照表，印出其所對應的GPA。
# 分　數 	GPA
# 90 ~ 100 	A
# 80 ~ 89 	B
# 70 ~ 79 	C
# 60 ~ 69 	D
# 0 ~ 59 	E
# 假設此不定數迴圈輸入-9999則會結束此迴圈。

breakend=-9999

while(1):
    n=eval(input())
    if(n==breakend):
        break
    elif(n>=90):
        print("A")
    elif(n>=80):
        print("B")
    elif(n>=70):
        print("C")
    elif(n>=60):
        print("D")
    else:
        print("E")