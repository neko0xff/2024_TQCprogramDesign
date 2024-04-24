# 自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"）
# 將此兩詞典合併
# 並根據key值字母由小到大排序輸出
# 如有重複key值，後輸入的key值將覆蓋前一key值

break_str = "end"
dict1 = {}
dict2 = {}

print("Create dict1:")
while(1):
    key = input("Key: ")
    if(key == break_str): break
    dict1[key] = input("Value: ")

print("Create dict2:")
while(1):
    key = input("Key: ")
    if(key == break_str): break
    dict2[key] = input("Value: ")

dict1.update(dict2)
for i in sorted(dict1.keys()):
    print("{}: {}".format(i,dict1[i]))