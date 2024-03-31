# (1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份
# 然後判斷它是否為閏年（leap year）或平年
# (2) 假設此不定數迴圈輸入-9999則會結束此迴圈
# 其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏

breakend=-9999
while(1):
    year=eval(input())
    if(year==breakend):
        break
    elif(year%4==0) & (year%100!=0) | (year%400==0):
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))
