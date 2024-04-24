# 依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。
# 接著回答：set2是否為set1的子集合（subset）？
# set3是否為set1的超集合（superset）？

set1 = set()
set2 = set()
set3 = set()

print("Input to set1:")
for i in range(0,5):
    in1 = int(input())
    set1.add(in1)
print("Input to set2:")
for i in range(0,3):
    in1 = int(input())
    set2.add(in1)
print("Input to set3:")
for i in range(0,9):
    in1 = int(input())
    set3.add(in1)

print("set2 is subset of set1: {}".format(set2.issubset(set1)))
print("set3 is superset of set1: {}".format(set3.issuperset(set1)))