# 請注意：程式碼中所提供的檔案路徑，不可進行變動，write.txt檔案需為UTF-8編碼格式
# 將使用者輸入的五筆資料寫入到write.txt（若不存在，則讓程式建立它）
# 每一筆資料為一行，包含學生名字和期末總分，以空白隔開。
# 檔案寫入完成後要關閉。
file = open("write.txt",mode="w")
times = 5

for i in range(times):
    in1 = input()
    file.write("{}\n".format(in1))

file.close()