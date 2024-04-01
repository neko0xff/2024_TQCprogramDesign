# 呼叫函式compute()
# 該函式功能為讓使用者輸入系別（Department）、學號（Student ID）和姓名（Name）並顯示這些訊息。

def compute(Department,stuID,Name):
    print("Department: {}".format(Department))
    print("Student ID: {}".format(stuID))
    print("Name: {}".format(Name))

in1=str(input())
in2=str(input())
in3=str(input())

compute(in1,in2,in3)