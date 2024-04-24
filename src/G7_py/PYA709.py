# 輸入一顏色詞典color_dict
#（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"）
# 再根據key值的字母由小到大排序並輸出。

break_str = "end"
color_dict = {}

while(1):
    key = input("Key: ")
    if(key == break_str): break
    color_dict[key] = input("Value: ")

for i in sorted(color_dict.keys()):
    print("{}: {}".format(i,color_dict[i]))
