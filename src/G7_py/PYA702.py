# 輸入並建立兩組數組
# 各以-9999為結束點（數組中不包含-9999）。
# 將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列

tuple01 = ()
tuple02 = ()
break_num=-9999

print("Create tuple1:")
while(1):
    in1 = int(input())
    if(in1 == break_num): break
    else: tuple01 += (in1,)
print("Create tuple2:")
while(1):
    in1 = int(input())
    if(in1 == break_num): break
    else: tuple02 += (in1,)

tuple01 += tuple02
list01 = list(tuple01)
list01.sort()

print("Combined tuple before sorting: {}".format(tuple01))
print("Combined list after sorting: {}".format(list01))