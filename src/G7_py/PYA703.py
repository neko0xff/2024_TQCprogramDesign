# 輸入一些字串至數組（至少輸入五個字串）
# 以字串"end"為結束點（數組中不包含字串"end")
# 接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。

tuple01 = ()
break_str = "end"

while(1):
    in1 = input()
    if(in1 == break_str): break
    else: tuple01 += (in1,)

print("{}".format(tuple01))
print("{}".format(tuple01[:3]))
print("{}".format(tuple01[-3:]))