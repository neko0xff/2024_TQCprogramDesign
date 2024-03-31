# 以不定數迴圈的方式輸入身高與體重
# 計算出BMI之後再根據以下對照表
# 印出BMI及相對應的BMI代表意義(State)
# BMI值 	代表意義
# BMI < 18.5 	under weight
# 18.5 <= BMI < 25 	normal
# 25.0 <= BMI < 30 	over weight
# 30 <= BMI 	fat
# 假設此不定數迴圈輸入-9999則會結束此迴圈
# 輸出浮點數到小數點後第二位。
# cal: BMI = H(kg)/W^2(cm)

from math import pow

breakend=-9999
while(1):
    h=eval(input())
    if (h==breakend):
        break
    else:
        w=eval(input())
        if(w==breakend):
            break
        else:
            BMI=w/pow(h/100,2)
            print("BMI: {:.2f}".format(BMI))
            if(BMI <= 18.5):
                print("State: under weight")
            elif(18.5 <= BMI < 25):
                print("State: normal")
            elif(25.0 <= BMI < 30):
                print("State: over weight")
            elif(30 <= BMI):
                print("State: fat")