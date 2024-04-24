# 要求使用者輸入一字串
# 顯示該字串每個字元的索引

in1  = input()
in1_index = 0

for i in in1:
    print("Index of '{}': {}".format(i,in1_index))
    in1_index+=1