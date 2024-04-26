# 請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。
# 讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。
## 檔案讀取完成後要關閉

file = open("read.txt",mode="r")
total = 0
data01 = []

for i in file:
    data01 = i.split(" ")
    for j in range(len(data01)):
        num = int(data01[j])
        total+=num

print(total)