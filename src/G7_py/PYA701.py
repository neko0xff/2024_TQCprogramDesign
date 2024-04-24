# 輸入數個整數並儲存至串列中
# 以輸入-9999為結束點（串列中不包含-9999）
# 再將此串列轉換成數組
# 最後顯示該數組以及其長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）

list01 = []
break_num = -9999

while(1):
    in1=int(input())
    if(in1 == break_num): break
    else: list01.append(in1)

tuple01 = tuple(list01)
print(tuple01)
print("Length: {}".format(len(tuple01)))
print("Max: {}".format(max(tuple01)))
print("Min: {}".format(min(tuple01)))
print("Sum: {}".format(sum(tuple01)))