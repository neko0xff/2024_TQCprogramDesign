# 請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。
# 要求使用者輸入五個人的名字並加入到data.txt的尾端。
# 之後再顯示此檔案的內容。

file = open("data.txt",mode="a+")
times = 5

for i in range(times):
    in1 = input()
    file.write("\n{}".format(in1))

print("Append completed!")
print('Content of "data.txt":')
file.seek(0)
print(file.read())