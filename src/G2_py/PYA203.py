year=eval(input())

# 判斷規則：每四年一閏，每百年不閏，但每四百年也一閏
if (year%4 == 0) & (year%100 != 0) | (year%400 == 0):
    print("{:} is a leap year.".format(year))
else: 
    print("{:} is not a leap year.".format(year))