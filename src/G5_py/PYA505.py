# 將使用者輸入的三個參數
# 變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數）
# 作為參數傳遞給一個名為compute()的函式
# 該函式功能為：一列印出x個a字元，總共印出y列。

def compute(a,x,y):
    for i in range(0,y):
        for j in range(0,x):
            print("{}".format(a),end=" ")
        print()

in1=str(input())
in2=eval(input())
in3=eval(input())

compute(in1,in2,in3)