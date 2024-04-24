# 輸入數個整數並儲存至集合
# 以輸入-9999為結束點（集合中不包含-9999)
# 最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）

set1 = set()
break_num=-9999
while(1):
    in1=int(input())
    if(in1 == break_num): break
    else: set1.add(in1)

print("Length: {}".format(len(set1)))
print("Max: {}".format(max(set1)))
print("Min: {}".format(min(set1)))
print("Sum: {}".format(sum(set1)))