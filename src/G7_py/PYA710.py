# 為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"）
# 再輸入一鍵值並檢視此鍵值是否存在於該詞典中

break_str = "end"
dict01 = {}

while(1):
    #Key: (後方有一空白格)
    key = input("Key: ")
    if(key == break_str):
        break
    else:
        #Value: (後方有一空白格)
        value = input("Value: ")
        dict01[key]=value

search = input("Search key: ")
print(search in dict01)