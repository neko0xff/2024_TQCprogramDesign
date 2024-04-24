# 讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
# 提示：平均分數輸出到小數點後第二位

stu1 = []
stu2 = []
stu3 = []
runtime=5
people=3

print("The 1st student:")
for i in range(1,runtime+1):
    in1 = eval(input())
    stu1.append(in1)

print("The 2nd student:")
for i in range(1,runtime+1):
    in1 = eval(input())
    stu2.append(in1)

print("The 3rd student:")
for i in range(1,runtime+1):
    in1 = eval(input())
    stu3.append(in1)


sum1 = sum(stu1)
sum2 = sum(stu2)
sum3 = sum(stu3)

print("Student {}".format(1))
print("#Sum {}".format(sum1))
print("#Average {:.2f}".format(sum1/runtime))
print("Student {}".format(2))
print("#Sum {}".format(sum2))
print("#Average {:.2f}".format(sum2/runtime))
print("Student {}".format(3))
print("#Sum {}".format(sum3))
print("#Average {:.2f}".format(sum3/runtime))