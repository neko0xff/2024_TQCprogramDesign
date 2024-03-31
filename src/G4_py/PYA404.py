# 輸入一個正整數
# 將此正整數以反轉的順序輸出
# 並判斷如輸入0，則輸出為0

n=str(input())

out="".join(reversed(n))
print(out)