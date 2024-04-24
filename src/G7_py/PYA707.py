# 輸入X組和Y組各自的科目至集合中
# 以字串"end"作為結束點（集合中不包含字串"end"）
# 請依序分行顯示
# (1) X組和Y組的所有科目
# (2) X組和Y組的共同科目
# (3) Y組有但X組沒有的科目
# (4) X組和Y組彼此沒有的科目（不包含相同科目)
# 提示：科目須參考範例輸出樣本，依字母由小至大進行排序

break_str = "end"
x_set = set()
y_set = set()

print("Enter group X's subjects:")
while(1):
    in1 = input()
    if(in1 == break_str): break
    x_set.add(in1)
print("Enter group Y's subjects:")
while(1):
    in1 = input()
    if(in1 == break_str): break
    y_set.add(in1)


print(sorted(x_set|y_set))
print(sorted(x_set&y_set))
print(sorted(y_set-x_set))
print(sorted(x_set^y_set))