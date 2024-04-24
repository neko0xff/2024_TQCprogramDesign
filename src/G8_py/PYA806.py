# 讓使用者輸入一字串和一字元
# 並將此字串及字元作為參數傳遞給名為compute()的函式
# 此函式將回傳該字串中指定字元出現的次數
# 接著再輸出結果

def compute(str1,char1):
    count_time = str1.count(char1)
    print("{} occurs {} time(s)".format(char1,count_time))

in1 = input()
in2 = input()
compute(in1,in2)